"""Еженедельный прогон: все расчёты → outputs/<дата>/engine.json + report.md."""

from datetime import date
from pathlib import Path

from . import budget, competitors, copy_words, creative, experiments, funnel
from .io import read_csv, write_json


def _money(x, cfg):
    if x is None:
        return "—"
    return f"{x:,.0f} {cfg['currency']}".replace(",", " ")


def _pct(x):
    return "—" if x is None else f"{x * 100:+.0f}%"


def run(cfg, data_dir="data", out_dir="outputs", day=None):
    d = Path(data_dir)
    creatives_rows = read_csv(d / "creatives.csv")
    experiments_rows = read_csv(d / "experiments.csv")
    result = {
        "date": day or date.today().isoformat(),
        "funnel": funnel.analyze(read_csv(d / "funnel.csv"), cfg),
        "budget": budget.analyze(read_csv(d / "channel_weeks.csv"), cfg),
        "creatives": creative.analyze(creatives_rows, cfg),
        "copy": copy_words.analyze(creatives_rows, experiments_rows, cfg),
        "competitors": competitors.analyze(read_csv(d / "competitors.csv"), creatives_rows, cfg),
        "experiments": experiments.analyze(experiments_rows, read_csv(d / "hypotheses.csv"), cfg),
    }
    target = Path(out_dir) / result["date"]
    write_json(target / "engine.json", result)
    (target / "report.md").write_text(render_report(result, cfg), encoding="utf-8")
    return target, result


def render_report(r, cfg):
    L = [f"# Неделя {r['date']}: что показывают данные", ""]

    f = r["funnel"]
    L.append("## 1. Воронка в деньгах")
    if f["status"] != "ok":
        L.append(f"Нет данных: {f.get('hint')}")
    else:
        t = f["total"]
        L += [f"Всего: прибыль {_money(t['realized_profit'], cfg)} при затратах {_money(t['cost'], cfg)}; "
              f"прибыль на 1000 входов {_money(t['profit_per_1000'], cfg)}.", ""]
        for key, groups in f["groups"].items():
            L += [f"**По {key}** (лучшие сверху):", "",
                  "| Группа | Объём | Сделки | Прибыль/1000 | ROI | Где теряем больше всего |",
                  "|---|---:|---:|---:|---:|---|"]
            for g in groups[:8]:
                name = " / ".join(str(v) for v in g["group"].values())
                b = g["bottleneck"]
                where = f"{b['stage']}: +{_money(b['gain_per_1000'], cfg)} на 1000 при среднем уровне" if b else "—"
                L.append(f"| {name} | {g['volume']:.0f} | {g['deals']:.0f} | {_money(g['profit_per_1000'], cfg)} "
                         f"| {_pct(g['roi'])} | {where} |")
            L.append("")

    b = r["budget"]
    L.append("## 2. Бюджет")
    if b["status"] != "ok":
        L.append(f"{b.get('hint', b['status'])}")
    else:
        L += ["Отдача последнего рубля — сколько маржинальной прибыли приносит следующий рубль в канале "
              "(1 = в ноль, выше — окупается).", "",
              "| Канал | Сейчас/нед | Рекомендация/нед | Изм. | Отдача последнего рубля: сейчас → после | Статус модели |",
              "|---|---:|---:|---:|---|---|"]
        for ch, row in b["allocation"]["plan"].items():
            fit = b["channels"][ch]
            status = f"R²={fit['r2']:.2f}" if fit["status"] == "ok" else fit.get("hint", fit["status"])
            mr = (f"{row['marginal_roi_now']:.2f} → {row['marginal_roi_after']:.2f}"
                  if "marginal_roi_now" in row else "—")
            L.append(f"| {ch} | {_money(row['current'], cfg)} | {_money(row['recommended'], cfg)} "
                     f"| {_pct(row['change_pct'])} | {mr} | {status} |")
        L += ["", f"На разведку новых идей: {_money(b['allocation']['exploration_budget'], cfg)} в неделю. "
              f"Не распределено (последний рубль не окупается): {_money(b['allocation']['unallocated'], cfg)}."]
        if b["allocation"].get("underfunded"):
            L.append(f"\n**Сигнал к росту:** в каналах {', '.join(b['allocation']['underfunded'])} следующий рубль "
                     "приносит заметно больше рубля — общий бюджет стоит увеличивать шагами 10–30% "
                     "и проверять, падает ли отдача.")
        L += ["", f"_{b['caveat']}_"]
    L.append("")

    c = r["creatives"]
    L.append("## 3. Креативы: какие признаки работают")
    if c["status"] != "ok":
        L.append(c.get("hint", ""))
    else:
        L.append(f"Креативов: {c['creatives']}, средний уровень {c['result_metric']}/показ: {c['account_rate']:.4f}.")
        if c["winners"]:
            L.append("\n**Сильнее остальных (надёжно):**")
            for w in c["winners"][:6]:
                L.append(f"- {w['tag']} = «{w['value']}»: {_pct(w['lift_vs_rest'])} "
                         f"(90%: {_pct(w['lift_90'][0])}…{_pct(w['lift_90'][1])}), "
                         f"P(лучше)={w['p_better_than_rest']:.2f}, креативов {w['creatives']}")
        if c["losers"]:
            L.append("\n**Слабее остальных:**")
            for w in c["losers"][:4]:
                L.append(f"- {w['tag']} = «{w['value']}»: {_pct(w['lift_vs_rest'])}, P(лучше)={w['p_better_than_rest']:.2f}")
        if not c["winners"] and not c["losers"]:
            L.append("Надёжных различий пока нет — нужны ещё креативы и результаты.")
        L.append(f"\n_{c['caveat']}_")
    L.append("")

    cp = r["copy"]
    L.append("## 4. Слова и формулировки")
    for t in cp.get("tested", []):
        L.append(f"- Тест {t['id']} ({t['variable']}): «{t['b']}» vs «{t['a']}» → P(B лучше)={t['p_b_better']:.2f}, "
                 f"прирост {_pct(t['lift'])}")
    top_words = [w for w in cp.get("words", []) if w["p_better_than_rest"] >= 0.8][:5]
    if top_words:
        L.append("Слова-кандидаты для теста (корреляция): " +
                 ", ".join(f"«{w['word']}» {_pct(w['lift_vs_rest'])}" for w in top_words))
    for name, s in cp.get("patterns", {}).items():
        if s["p_better_than_rest"] >= 0.8 or s["p_better_than_rest"] <= 0.2:
            L.append(f"- приём «{name}»: {_pct(s['lift_vs_rest'])}, P(лучше)={s['p_better_than_rest']:.2f}")
    if cp.get("sample_size_hint"):
        L.append("Чтобы проверить текст тестом, нужно показов на вариант: " +
                 ", ".join(f"{k} → {v:,}".replace(",", " ") for k, v in cp["sample_size_hint"].items()))
    L.append("")

    co = r["competitors"]
    L.append("## 5. Конкуренты")
    if co["status"] != "ok":
        L.append(co.get("hint", ""))
    else:
        for comp, s in co["competitors"].items():
            L.append(f"- {comp}: активных {s['active']}, новых {s['new_since_last_snapshot']}, остановлено {s['stopped']}")
        gaps = {a: m for a, m in co["angle_matrix"].items() if m["status"] != "ок"}
        if gaps:
            L.append("\n**Углы подачи:**")
            for a, m in gaps.items():
                L.append(f"- «{a}»: {m['status']} (у них {m['their_share']:.0%}, у нас {m['our_share']:.0%})")
        if co["survivors_to_study"]:
            L.append("\n**Долгоживущие объявления — изучить:**")
            for a in co["survivors_to_study"][:5]:
                L.append(f"- {a['competitor']}: {a['longevity_days']} дн., угол «{a.get('angle')}», "
                         f"«{(a.get('text') or '')[:80]}»")
        L.append(f"\n_{co['caveat']}_")
    L.append("")

    e = r["experiments"]
    L.append("## 6. Эксперименты и очередь гипотез")
    for x in e["running_and_finished"]:
        L.append(f"- {x['id']} «{x['hypothesis']}»: {x['verdict']} (P(B лучше)={x['p_b_better']:.2f}, {_pct(x['lift'])})")
    if e["win_rates"]:
        L.append("\nДоля побед по слоям: " + ", ".join(
            f"{k} {v['win_rate']:.0%} ({v['wins']}/{v['finished']})" for k, v in e["win_rates"].items()))
    if e["queue"]:
        L += ["", "**Следующие тесты (по ожидаемой ценности на час работы):**"]
        for h in e["queue"][:5]:
            L.append(f"- [{h.get('layer')}] {h.get('hypothesis')} — ценность {_money(h['expected_value'], cfg)}, "
                     f"P(победы) {h['p_win']:.0%}")
    L.append("")
    return "\n".join(L)
