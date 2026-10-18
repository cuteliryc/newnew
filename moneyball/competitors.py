"""Слой 5. Конкуренты: что они показывают, что держат долго и где у нас разрыв.

Длительность показа — фильтр «что изучить», а не доказательство эффективности:
исследований, которые связывают срок жизни объявления с результатом, нет.
Копировать рекламный натиск конкурента обычно бесполезно (Steenkamp et al., 2005) —
наблюдаем, извлекаем гипотезы и тестируем у себя.
"""

from datetime import date

from .io import num


def _d(value):
    if not value:
        return None
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


def _share(rows, column):
    counts = {}
    for r in rows:
        v = r.get(column)
        if v:
            counts[str(v)] = counts.get(str(v), 0) + 1
    total = sum(counts.values())
    return {k: v / total for k, v in counts.items()} if total else {}


def analyze(competitor_rows, our_creatives, cfg):
    cc = cfg["competitors"]
    rows = [r for r in competitor_rows if r.get("competitor")]
    if not rows:
        return {"status": "no_data", "hint": "заполните data/competitors.csv (снимки библиотек объявлений)"}

    snapshots = sorted({_d(r.get("snapshot_date")) for r in rows if _d(r.get("snapshot_date"))})
    latest = snapshots[-1] if snapshots else None
    previous = snapshots[-2] if len(snapshots) > 1 else None

    # Одно объявление может встречаться в нескольких снимках — берём последнюю запись.
    ads = {}
    for r in sorted(rows, key=lambda r: str(r.get("snapshot_date"))):
        ads[(r["competitor"], r.get("ad_id") or r.get("text"))] = r

    enriched = []
    for (comp, _), r in ads.items():
        first, last = _d(r.get("first_seen")), _d(r.get("last_seen")) or _d(r.get("snapshot_date"))
        days = (last - first).days if first and last else None
        enriched.append({**r, "longevity_days": days,
                         "active": bool(latest and last and last >= latest),
                         "new": bool(previous and first and first > previous)})

    active = [a for a in enriched if a["active"]]
    survivors = sorted(
        [a for a in enriched if (a["longevity_days"] or 0) >= cc["survivor_days"]],
        key=lambda a: a["longevity_days"] or 0, reverse=True,
    )

    # Сколько конкурентов использует угол, какая доля их активных объявлений и есть ли он у нас.
    matrix = {}
    competitors = sorted({a["competitor"] for a in enriched})
    their_share = _share(active, "angle")
    our_share = _share(our_creatives, "angle")
    for angle in sorted(set(their_share) | set(our_share)):
        users = {a["competitor"] for a in active if a.get("angle") == angle}
        coverage = len(users) / len(competitors) if competitors else 0
        status = "ок"
        if their_share.get(angle, 0) >= cc["gap_share"] and not our_share.get(angle):
            status = "разрыв: у них держится, мы не тестировали"
        elif coverage >= cc["crowded_share"]:
            status = "паритет: у всех одинаково — здесь трудно выделиться"
        elif our_share.get(angle) and not their_share.get(angle):
            status = "наша территория: у конкурентов нет"
        matrix[angle] = {"their_share": their_share.get(angle, 0), "our_share": our_share.get(angle, 0),
                         "competitors_using": len(users), "status": status}

    per_comp = {}
    for comp in competitors:
        items = [a for a in enriched if a["competitor"] == comp]
        per_comp[comp] = {
            "active": sum(a["active"] for a in items),
            "new_since_last_snapshot": sum(a["new"] for a in items),
            "stopped": sum(1 for a in items if not a["active"]),
            "top_offers": sorted(_share([a for a in items if a["active"]], "offer").items(),
                                 key=lambda kv: kv[1], reverse=True)[:3],
        }

    fields = ("competitor", "platform", "angle", "offer", "format", "hook", "text", "url", "longevity_days")
    return {
        "status": "ok",
        "latest_snapshot": latest,
        "previous_snapshot": previous,
        "competitors": per_comp,
        "angle_matrix": matrix,
        "survivors_to_study": [{k: a.get(k) for k in fields} for a in survivors[:15]],
        "new_ads": [{k: a.get(k) for k in fields} for a in enriched if a["new"]][:20],
        "caveat": "Длительность показа — фильтр для изучения, не доказательство. "
                  "Решения — только после теста у себя.",
    }
