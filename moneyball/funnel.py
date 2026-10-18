"""Слой 1. Воронка в деньгах: прибыль на 1000 показов/касаний и самое дорогое узкое место.

Прибыль на 1000 = 1000 × (CR1 × CR2 × … × выручка на сделку × маржа − затраты на единицу входа)
Затраты = рекламный расход + часы × ставка часа (ручная работа тоже стоит денег).
"""

from .io import num
from .stats import shrink_rate


def _sum(rows, fields):
    return {f: sum(num(r, f) for r in rows) for f in fields}


def _metrics(s, base_rates, base_rpd, cfg, stages, rev):
    k = cfg["prior_events"]
    margin = cfg["gross_margin"]
    rates, raw = [], []
    for i in range(len(stages) - 1):
        n, x = s[stages[i]], s[stages[i + 1]]
        raw.append(x / n if n else None)
        rates.append(shrink_rate(x, n, base_rates[i], k))
    deals = s[stages[-1]]
    rpd = (s[rev] + base_rpd * k) / (deals + k) if (deals + k) else 0.0
    top = s[stages[0]]
    cost = s["spend"] + s["hours"] * cfg["hourly_rate"]

    chain = 1.0
    for r in rates:
        chain *= r
    value_per_unit = chain * rpd * margin
    cost_per_unit = cost / top if top else 0.0

    # Сколько даст подтянуть каждый этап до среднего по аккаунту.
    gains = []
    for i, r in enumerate(rates):
        if r > 0 and base_rates[i] > r:
            gains.append({
                "stage": f"{stages[i]}→{stages[i + 1]}",
                "rate": r,
                "account_rate": base_rates[i],
                "gain_per_1000": 1000 * value_per_unit * (base_rates[i] / r - 1),
            })
    gains.sort(key=lambda g: g["gain_per_1000"], reverse=True)

    return {
        "volume": top,
        "deals": deals,
        "cost": cost,
        "revenue": s[rev],
        "realized_profit": s[rev] * margin - cost,
        "rates_raw": raw,
        "rates_shrunk": rates,
        "revenue_per_deal": rpd,
        "expected_value_per_1000": 1000 * value_per_unit,
        "cost_per_1000": 1000 * cost_per_unit,
        "profit_per_1000": 1000 * (value_per_unit - cost_per_unit),
        "roi": value_per_unit / cost_per_unit - 1 if cost_per_unit else None,
        "bottleneck": gains[0] if gains else None,
    }


def analyze(rows, cfg):
    stages = [s[0] for s in cfg["funnel"]["stages"]]
    rev = cfg["funnel"]["revenue"]
    fields = stages + [rev, "spend", "hours"]
    total = _sum(rows, fields)
    if not rows or total[stages[0]] == 0:
        return {"status": "no_data", "hint": "заполните data/funnel.csv"}

    base_rates = [
        total[stages[i + 1]] / total[stages[i]] if total[stages[i]] else 0.0
        for i in range(len(stages) - 1)
    ]
    base_rpd = total[rev] / total[stages[-1]] if total[stages[-1]] else 0.0

    out = {
        "status": "ok",
        "stages": stages,
        "total": _metrics(total, base_rates, base_rpd, cfg, stages, rev),
        "groups": {},
    }
    for dims in cfg["funnel"]["group_by"]:
        if not all(any(r.get(d) is not None for r in rows) for d in dims):
            continue
        groups = {}
        for r in rows:
            groups.setdefault(tuple(str(r.get(d) or "—") for d in dims), []).append(r)
        result = []
        for key, items in groups.items():
            m = _metrics(_sum(items, fields), base_rates, base_rpd, cfg, stages, rev)
            m["group"] = dict(zip(dims, key))
            result.append(m)
        result.sort(key=lambda m: m["profit_per_1000"], reverse=True)
        out["groups"]["+".join(dims)] = result
    return out
