"""Слой 3. «Геном» креатива: какие признаки (хук, угол, формат, компоновка…) связаны с результатом.

Для каждого значения тега: сглаженная доля результата на показ против всех остальных креативов
и вероятность, что это значение действительно лучше. Это корреляция, а не доказательство:
платформа показывает разные креативы разным людям. Сильные находки проверяются split-тестом.
"""

from .io import num
from .stats import prob_better, shrink_rate


def analyze(rows, cfg):
    c = cfg["creatives"]
    res = c["result"]
    k = cfg["prior_events"]
    rows = [r for r in rows if num(r, "impressions") > 0]
    if not rows:
        return {"status": "no_data", "hint": "заполните data/creatives.csv (показы и результаты)"}

    tot_imp = sum(num(r, "impressions") for r in rows)
    tot_res = sum(num(r, res) for r in rows)
    base = tot_res / tot_imp if tot_imp else 0.0
    margin = cfg["gross_margin"]

    board = []
    for r in rows:
        imp, x, spend = num(r, "impressions"), num(r, res), num(r, "spend")
        rate = shrink_rate(x, imp, base, k)
        item = {
            "creative_id": r.get("creative_id"),
            "results": x,
            "impressions": imp,
            "rate_raw": x / imp,
            "rate_shrunk": rate,
            "cost_per_result_shrunk": spend / (imp * rate) if rate else None,
            "tags": {t: r.get(t) for t in c["tags"] if r.get(t) is not None},
        }
        if r.get("revenue") is not None:
            item["profit"] = num(r, "revenue") * margin - spend
        board.append(item)
    board.sort(key=lambda i: i["rate_shrunk"], reverse=True)

    tags = {}
    for tag in c["tags"]:
        values = {}
        for r in rows:
            if r.get(tag) is not None:
                values.setdefault(str(r[tag]), []).append(r)
        if len(values) < 2:
            continue
        stats = []
        for value, items in values.items():
            imp = sum(num(r, "impressions") for r in items)
            x = sum(num(r, res) for r in items)
            pb = prob_better(tot_res - x, tot_imp - imp, x, imp, prior_mean=base, prior_events=k)
            stats.append({
                "value": value,
                "creatives": len(items),
                "impressions": imp,
                "results": x,
                "rate_shrunk": shrink_rate(x, imp, base, k),
                "lift_vs_rest": pb["lift_mean"],
                "lift_90": [pb["lift_low"], pb["lift_high"]],
                "p_better_than_rest": pb["p_b_better"],
                "reliable": len(items) >= c["min_creatives"] and x >= k,
            })
        stats.sort(key=lambda s: s["lift_vs_rest"], reverse=True)
        tags[tag] = stats

    winners = [
        {"tag": t, **s} for t, items in tags.items() for s in items
        if s["reliable"] and s["p_better_than_rest"] >= 0.9
    ]
    losers = [
        {"tag": t, **s} for t, items in tags.items() for s in items
        if s["reliable"] and s["p_better_than_rest"] <= 0.1
    ]
    return {
        "status": "ok",
        "result_metric": res,
        "account_rate": base,
        "creatives": len(rows),
        "leaderboard": board[:15],
        "tags": tags,
        "winners": sorted(winners, key=lambda s: s["lift_vs_rest"], reverse=True),
        "losers": sorted(losers, key=lambda s: s["lift_vs_rest"]),
        "caveat": "Связь признаков с результатом корреляционная: алгоритм площадки показывает "
                  "креативы разным аудиториям. Победителей подтверждайте split-тестом.",
    }
