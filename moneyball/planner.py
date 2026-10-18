"""Планировщик без ИИ: запрос (задача, аудитория, кабинеты, бюджет) → план.

1. Юнит-экономика: сколько можно платить за клиента и за заявку.
2. Каналы: оценка доступных кабинетов по каталогу и по вашим данным.
3. Бюджет: ядро / тесты / разведка, причём на тест — столько, чтобы успеть сделать вывод.
4. Кейсы: похожие успешные истории → проверяемые гипотезы.
"""

import json
from pathlib import Path

from . import offer as offer_mod
from . import pr as pr_mod
from .io import num

EVIDENCE_W = {"strong": 1.5, "medium": 1.2, "weak": 0.8, "vendor": 0.7}
LEVER_TO_LAYER = {
    "creative": "creative", "design": "creative", "copy": "copy", "offer": "offer",
    "targeting": "audience", "budget": "budget", "measurement": "budget",
    "landing": "landing", "channel": "channel", "retention": "retention",
    "positioning": "offer", "process": "funnel",
}

# Стартовые конверсии, если своих данных ещё нет. Это ДОПУЩЕНИЯ — замените своими.
DEFAULT_LEAD_TO_DEAL = {"b2b_services": 0.1, "creative_services": 0.1, "agency": 0.1, "saas": 0.05,
                        "b2c_ecom": 1.0, "marketplace_seller": 1.0, "local_services": 0.2}
MIN_LEADS_FOR_DECISION = 30


def load_cases(cases_dir):
    cases = []
    for p in sorted(Path(cases_dir).glob("*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        items = data if isinstance(data, list) else data.get("cases", [])
        for c in items:
            c.setdefault("_file", p.name)
            cases.append(c)
    return cases


def load_catalog(path):
    p = Path(path)
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8")).get("channels", {})


def unit_economics(req, funnel_stats=None):
    check = num(req, "avg_check")
    margin = req.get("margin") or 0.7
    repeat = req.get("repeat_purchases") or 1.0
    model = req.get("business_model", "")
    l2d = req.get("lead_to_deal")
    source = "запрос"
    if l2d is None and funnel_stats and funnel_stats.get("status") == "ok":
        rates = funnel_stats["total"]["rates_shrunk"]
        stages = funnel_stats["stages"]
        if "leads" in stages:
            i = stages.index("leads")
            l2d = 1.0
            for r in rates[i:]:
                l2d *= r
            source = "ваши данные (funnel.csv)"
    if l2d is None:
        l2d = DEFAULT_LEAD_TO_DEAL.get(model, 0.1)
        source = "допущение — замените своими данными"
    ltv_profit = check * margin * repeat
    max_cac = ltv_profit
    # Целевой CAC — треть от предельного: остаётся прибыль и запас на ошибку модели.
    target_cac = ltv_profit / 3
    return {
        "avg_check": check, "margin": margin, "repeat_purchases": repeat,
        "profit_per_customer": ltv_profit,
        "max_cac_breakeven": max_cac, "target_cac": target_cac,
        "lead_to_deal": l2d, "lead_to_deal_source": source,
        "max_cpl_breakeven": max_cac * l2d, "target_cpl": target_cac * l2d,
        "note": "Целевой CAC = 1/3 прибыли с клиента — запас на ошибки (правило, не закон).",
    }


def score_channels(req, catalog, funnel_stats=None):
    task = req.get("task", "leads")
    model = req.get("business_model", "")
    market = req.get("market", "RU")
    budget = num(req, "budget_month")
    own = {}
    if funnel_stats and funnel_stats.get("status") == "ok":
        for g in funnel_stats["groups"].get("channel", []):
            own[g["group"]["channel"]] = g
    scored = []
    for key in req.get("channels_available", []):
        info = catalog.get(key, {})
        score, why = 0.0, []
        if not info:
            why.append("нет в каталоге — оценка только по вашим данным")
        else:
            avail = info.get("available_from_ru")
            if market == "RU" and avail is False:
                scored.append({"channel": key, "score": -99, "role": "skip",
                               "why": ["недоступен для рекламодателей из РФ по каталогу"], "info": info})
                continue
            if task in info.get("best_for", []):
                score += 3
                why.append(f"подходит под задачу «{task}»")
            if model and model in info.get("business_models", []):
                score += 2
                why.append(f"подходит модели «{model}»")
            if market in info.get("markets", []) or "Global" in info.get("markets", []):
                score += 1
            if avail == "partial":
                score -= 1
                why.append("доступ частичный")
            min_b = info.get("min_budget")
            if min_b and budget and budget < min_b:
                score -= 3
                why.append(f"бюджет ниже минимального порога канала (~{min_b:,.0f})".replace(",", " "))
            if info.get("legal_flag"):
                why.append(f"⚖ {info['legal_flag']}")
            if task == "leads" and info.get("intent") == "search":
                score += 1
                why.append("поисковый спрос — люди уже ищут решение")
        if key in own:
            g = own[key]
            if g["profit_per_1000"] > 0:
                score += 4
                why.append(f"ваши данные: прибыль {g['profit_per_1000']:.0f} на 1000 входов")
            else:
                score -= 2
                why.append("ваши данные: пока убыточен")
            hours = (g["cost"] - g.get("spend", 0)) / (req.get("hourly_rate") or 1500)
            if hours > 0 and g.get("spend", 0) == 0:
                profit_hour = (g["realized_profit"] + g["cost"]) / hours
                why.append(f"маржа на час работы ≈{profit_hour:,.0f}".replace(",", " "))
        cost_type = info.get("cost_type")
        if not cost_type and key in own:
            g = own[key]
            cost_type = "time" if g["cost"] > 0 and g.get("spend", 0) == 0 else "money"
        if not cost_type:
            cost_type = "time" if key.startswith(("cold_", "organic_")) or key.endswith("_organic") else "money"
        scored.append({"channel": key, "score": score, "why": why, "info": info,
                       "own": own.get(key), "cost_type": cost_type})
    # Внутри своих данных — бонус за место по прибыли на 1000 (самые «недооценённые» наверх).
    ranked_own = sorted((c for c in scored if c.get("own") and c["own"]["profit_per_1000"] > 0),
                        key=lambda c: c["own"]["profit_per_1000"], reverse=True)
    for i, c in enumerate(ranked_own[:3]):
        c["score"] += 3 - i
    scored.sort(key=lambda c: c["score"], reverse=True)
    # Роли раздаются отдельно: платные каналы делят деньги, «часовые» — ваше время.
    for cost_type, n_core in (("money", 2), ("time", 1)):
        group = [c for c in scored if c.get("cost_type") == cost_type and c.get("role") != "skip"]
        for i, c in enumerate(group):
            c["role"] = "core" if i < n_core and c["score"] >= 3 else "test" if c["score"] > 0 else "skip"
    return scored


def split_budget(req, channels, econ, exploration_share=0.1):
    budget = num(req, "budget_month")
    if not budget:
        return {"note": "бюджет не указан — распределение не считаю"}
    explore = budget * exploration_share
    test_need = MIN_LEADS_FOR_DECISION * econ["target_cpl"] if econ["target_cpl"] else 0
    paid = [c for c in channels if c.get("cost_type") != "time"]
    core = [c for c in paid if c.get("role") == "core"]
    tests = [c for c in paid if c.get("role") == "test"]
    available = budget - explore
    plan, notes = {}, []
    for c in channels:
        if c.get("cost_type") == "time" and c.get("role") in ("core", "test"):
            plan[c["channel"]] = {"role": "ядро" if c["role"] == "core" else "тест", "budget": 0,
                                  "hours_week": 5 if c["role"] == "core" else 3,
                                  "note": "канал стоит времени, а не денег"}
    # Тестов берём столько, сколько бюджет реально позволяет довести до вывода.
    affordable = int(available * 0.4 // test_need) if test_need else len(tests)
    if tests and affordable < len(tests):
        notes.append(f"бюджета хватит довести до вывода {affordable} тест(а) из {len(tests)}: "
                     f"на один нужно ≈{test_need:,.0f} ({MIN_LEADS_FOR_DECISION} заявок × целевой CPL)".replace(",", " "))
        tests = tests[:max(affordable, 0)]
    test_total = min(available * 0.4, test_need * len(tests)) if tests else 0
    core_total = available - test_total
    for c in core:
        plan[c["channel"]] = {"role": "ядро", "budget": core_total / len(core)}
    for c in tests:
        plan[c["channel"]] = {"role": "тест", "budget": test_total / len(tests)}
    if not core and tests:
        notes.append("каналов-ядра нет: весь бюджет идёт в тесты до появления победителя")
        for c in tests:
            plan[c["channel"]]["budget"] = available / len(tests)
    return {"plan": plan, "exploration": explore, "test_budget_needed_each": test_need, "notes": notes,
            "rule": "≈10% — разведка новых идей, тестам — сколько нужно для вывода, остальное — ядру. "
                    "Пропорции — стартовое допущение; после 12+ недель данных их заменяет budget-модель."}


def match_cases(req, cases, top=8):
    chans = set(req.get("channels_available", []))
    model, industry = req.get("business_model"), req.get("industry")
    market, task = req.get("market"), req.get("task")
    ranked = []
    for c in cases:
        if "what_they_did" not in c:
            continue
        s = 0.0
        overlap = chans & set(c.get("channels", []))
        if chans and not overlap and not c.get("news_values"):
            continue
        s += 2 * len(overlap)
        s += 3 if model and c.get("business_model") == model else 0
        s += 2 if industry and c.get("industry") == industry else 0
        s += 2 if market and c.get("market") == market else (1 if c.get("market") == "Global" else 0)
        s += 2 if task and c.get("objective") == task else 0
        s *= EVIDENCE_W.get(c.get("evidence"), 0.8)
        s *= 0.85 if c.get("source_seen") == "search_snippet" else 1.0
        s *= 1.1 if (c.get("year") or 0) >= 2022 else 1.0
        if s > 0:
            ranked.append({**c, "_match": round(s, 2), "_overlap": sorted(overlap)})
    ranked.sort(key=lambda c: c["_match"], reverse=True)
    # Разнообразие: не больше трёх кейсов на один канал и на один рычаг.
    picked, per_channel, per_lever = [], {}, {}
    for c in ranked:
        ch = (c["_overlap"] or c.get("channels") or ["—"])[0]
        lever = (c.get("levers") or ["—"])[0]
        if per_channel.get(ch, 0) >= 3 or per_lever.get(lever, 0) >= 3:
            continue
        per_channel[ch] = per_channel.get(ch, 0) + 1
        per_lever[lever] = per_lever.get(lever, 0) + 1
        picked.append(c)
        if len(picked) >= top:
            break
    return picked


def hypotheses_from_cases(cases, econ, req):
    rows = []
    for c in cases:
        if not c.get("test_to_run"):
            continue
        levers = c.get("levers") or ["creative"]
        rows.append({
            "layer": LEVER_TO_LAYER.get(levers[0], "other"),
            "hypothesis": c["test_to_run"],
            "variable": ", ".join(levers),
            "source": f"кейс {c.get('id')} ({c.get('source_url')})",
            "evidence": {"strong": "strong", "medium": "medium"}.get(c.get("evidence"), "weak"),
            "expected_lift": 0.15,
            "value_at_stake": num(req, "budget_month") * 0.3,
            "cost_hours": 4,
            "status": "new",
            "source_agent": "planner",
        })
    return rows


def calendar(req, channels, has_data):
    """Первые 4 недели: что делать по порядку. Правила — практика системы [ДОПУЩЕНИЕ]."""
    core = [c["channel"] for c in channels if c.get("role") == "core"]
    tests = [c["channel"] for c in channels if c.get("role") == "test"]
    return [
        {"week": 1, "focus": "Фундамент",
         "do": ["Метки источника на каждую заявку (UTM / поле в CRM)" if not req.get("has_tracking") else
                "Проверить, что у каждой заявки есть источник и этап в CRM",
                "Заполнить оффер по чек-листу и закрыть 2 главных пробела",
                "Снимок объявлений 3–5 конкурентов в competitors.csv",
                f"Запуск ядра: {', '.join(core) or 'выбрать 1 канал'} — 3–5 креативов на разные углы"]},
        {"week": 2, "focus": "Креатив и тексты",
         "do": ["Баннеры по брифу (moneyball banners) с разными углами, не синонимами",
                "Контент: 3–4 публикации на темы, которые уже залетали (или на 3 разных темы для разведки)",
                f"Тестовые каналы: {', '.join(tests) or 'нет'} — бюджет на вывод, не меньше"]},
        {"week": 3, "focus": "Первые выводы",
         "do": ["weekly: воронка в деньгах — где самый дорогой разрыв",
                "Выключить креативы, которые с вероятностью ≥90% хуже остальных (при достаточном объёме)",
                "Запустить 1 тест оффера (снятие риска / пробник)"]},
        {"week": 4, "focus": "Масштаб и PR",
         "do": ["Перенести 10–30% бюджета в канал с лучшей отдачей последнего рубля",
                "Выбрать 1 PR-идею с оценкой ≥60 и подготовить доказательства",
                "Записать выводы в experiments.csv — это ваши будущие априорные вероятности"
                + ("" if has_data else "; без данных выводы этой недели предварительные")]},
    ]


def build_plan(req, catalog, cases, funnel_stats=None, creative_stats=None, engine=None):
    engine = engine or {}
    econ = unit_economics(req, funnel_stats)
    channels = score_channels(req, catalog, funnel_stats)
    budget = split_budget(req, channels, econ)
    matched = match_cases(req, [c for c in cases if not c.get("news_values")])
    angles = []
    if creative_stats and creative_stats.get("status") == "ok":
        angles = [w for w in creative_stats.get("winners", []) if w["tag"] in ("angle", "hook")]
    offer_check = offer_mod.check(req["offer"], engine.get("competitors")) if req.get("offer") else None
    pr_ideas = pr_mod.generate_ideas(req.get("pr", {}), cases) if req.get("pr") else []
    content = engine.get("content") if (engine.get("content") or {}).get("status") == "ok" else None
    retention = engine.get("retention") if (engine.get("retention") or {}).get("status") == "ok" else None
    return {
        "request": req,
        "unit_economics": econ,
        "offer": offer_check,
        "channels": [{k: v for k, v in c.items() if k != "info"} for c in channels],
        "budget": budget,
        "cases": [{k: c.get(k) for k in ("id", "title", "brand", "market", "channels", "what_they_did",
                                         "mechanism", "metrics", "transferable_lesson", "test_to_run",
                                         "evidence", "source_url", "_match")} for c in matched],
        "proven_angles": angles,
        "content": {"outliers": content["outliers"][:5], "tags": content["tags"]} if content else None,
        "retention": {k: retention[k] for k in ("repeat_rate", "avg_orders", "profit_per_customer", "segments")}
        if retention else None,
        "pr_ideas": [i for i in pr_ideas if i.get("idea")][:4],
        "default_tests": [
            "Сначала тестируйте крупные различия углов (боль / выгода / доказательство / скорость / цена), "
            "а не отдельные слова: эффект слова — проценты, угла — десятки процентов.",
            f"Решение по каналу — после ≈{MIN_LEADS_FOR_DECISION} заявок и хотя бы первых сделок, "
            "а не по CTR и цене клика.",
            "Каждой заявке — источник (UTM / метка в CRM), иначе связать рекламу с деньгами нельзя.",
        ],
        "calendar": calendar(req, channels, bool(funnel_stats and funnel_stats.get("status") == "ok")),
        "hypotheses": hypotheses_from_cases(matched, econ, req),
    }
