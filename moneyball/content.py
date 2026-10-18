"""Слой 9. Контент и соцсети (органика): что «залетело» и какие темы/форматы стабильно сильнее.

«Залёт» считается относительно медианы последних публикаций на той же площадке —
так сравниваются посты в разное время и при разном размере аудитории.
Порог по умолчанию ×3 от медианы [ДОПУЩЕНИЕ — задайте свой в config.content.outlier_x].
"""

from statistics import median

from .io import num


def analyze(rows, cfg):
    c = cfg.get("content", {})
    metric = c.get("metric", "reach")
    window = int(c.get("window", 10))
    outlier_x = float(c.get("outlier_x", 3.0))
    tags = c.get("tags", ["format", "topic", "hook"])
    rows = [r for r in rows if r.get(metric) is not None]
    if not rows:
        return {"status": "no_data", "hint": "заполните data/content.csv (публикации и их охваты)"}

    by_platform = {}
    for r in sorted(rows, key=lambda r: str(r.get("date"))):
        by_platform.setdefault(str(r.get("platform") or "—"), []).append(r)

    scored = []
    for platform, items in by_platform.items():
        for i, r in enumerate(items):
            prev = [num(x, metric) for x in items[max(0, i - window):i]]
            base = median(prev) if prev else None
            score = num(r, metric) / base if base else None
            # Пересылки и сохранения — сигнал ценности сильнее лайков.
            engaged = num(r, "shares") + num(r, "saves")
            scored.append({**r, "x_median": score,
                           "share_save_rate": engaged / num(r, metric) if num(r, metric) else None})

    outliers = sorted([s for s in scored if s["x_median"] and s["x_median"] >= outlier_x],
                      key=lambda s: s["x_median"], reverse=True)

    tag_stats = {}
    valid = [s for s in scored if s["x_median"]]
    for tag in tags:
        values = {}
        for s in valid:
            if s.get(tag):
                values.setdefault(str(s[tag]), []).append(s["x_median"])
        if len(values) < 2:
            continue
        tag_stats[tag] = sorted(
            [{"value": v, "posts": len(xs), "median_x": median(xs), "hit_rate": sum(x >= outlier_x for x in xs) / len(xs)}
             for v, xs in values.items()],
            key=lambda t: t["median_x"], reverse=True)

    leads = [s for s in scored if num(s, "leads") > 0]
    return {
        "status": "ok",
        "metric": metric,
        "posts": len(scored),
        "outliers": [{k: o.get(k) for k in ("date", "platform", "post_id", "format", "topic", "hook",
                                            metric, "x_median", "share_save_rate", "leads", "url")}
                     for o in outliers[:15]],
        "tags": tag_stats,
        "posts_with_leads": len(leads),
        "rule": "Залетевшую тему не придумывать заново, а масштабировать: другой формат, другая площадка, "
                "продолжение. Решение «тема работает» — когда она залетает повторно, а не один раз.",
    }
