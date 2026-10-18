"""Слой 10. Клиенты: повторные продажи, LTV по когортам и RFM-сегменты.

Привлечение дорогое, поэтому прибыль с клиента = первая сделка + повторные.
Здесь простая версия; для точного прогноза покупок есть BG/NBD (Fader, Hardie & Lee 2005).
"""

from datetime import date

from .io import num


def _d(v):
    try:
        return date.fromisoformat(str(v)[:10])
    except (TypeError, ValueError):
        return None


def _bucket(value, edges):
    for i, e in enumerate(edges):
        if value <= e:
            return i + 1
    return len(edges) + 1


def analyze(orders, cfg, today=None):
    """orders: строки заказов customer_id, date, revenue."""
    rows = [r for r in orders if r.get("customer_id") and _d(r.get("date"))]
    if not rows:
        return {"status": "no_data", "hint": "заполните data/orders.csv (customer_id, date, revenue)"}
    today = today or max(_d(r["date"]) for r in rows)
    margin = cfg["gross_margin"]

    customers = {}
    for r in rows:
        c = customers.setdefault(r["customer_id"], {"first": _d(r["date"]), "last": _d(r["date"]),
                                                    "orders": 0, "revenue": 0.0})
        d = _d(r["date"])
        c["first"], c["last"] = min(c["first"], d), max(c["last"], d)
        c["orders"] += 1
        c["revenue"] += num(r, "revenue")

    n = len(customers)
    repeaters = sum(1 for c in customers.values() if c["orders"] > 1)

    cohorts = {}
    for c in customers.values():
        key = c["first"].strftime("%Y-%m")
        co = cohorts.setdefault(key, {"customers": 0, "revenue": 0.0, "repeat": 0})
        co["customers"] += 1
        co["revenue"] += c["revenue"]
        co["repeat"] += c["orders"] > 1
    for co in cohorts.values():
        co["profit_per_customer"] = co["revenue"] * margin / co["customers"]
        co["repeat_rate"] = co["repeat"] / co["customers"]

    # RFM: давность (меньше — лучше), частота, деньги — по тертилям базы.
    rec = sorted((today - c["last"]).days for c in customers.values())
    freq = sorted(c["orders"] for c in customers.values())
    mon = sorted(c["revenue"] for c in customers.values())

    def edges(xs):
        return [xs[len(xs) // 3], xs[2 * len(xs) // 3]] if len(xs) >= 3 else [xs[0], xs[-1]]

    er, ef, em = edges(rec), edges(freq), edges(mon)
    segments = {}
    for cid, c in customers.items():
        r = 4 - _bucket((today - c["last"]).days, er)
        f = _bucket(c["orders"], ef)
        m = _bucket(c["revenue"], em)
        if r == 3 and f >= 2:
            seg = "ядро: удерживать и просить рекомендации"
        elif r == 3:
            seg = "новые: довести до второй покупки"
        elif r == 2 and f >= 2:
            seg = "остывают: напомнить с поводом"
        elif f >= 2 or m == 3:
            seg = "ценные, но ушли: вернуть персональным оффером"
        else:
            seg = "разовые: не тратить много"
        s = segments.setdefault(seg, {"customers": 0, "revenue": 0.0, "ids": []})
        s["customers"] += 1
        s["revenue"] += c["revenue"]
        if len(s["ids"]) < 20:
            s["ids"].append(cid)

    return {
        "status": "ok",
        "customers": n,
        "repeat_rate": repeaters / n,
        "avg_orders": sum(c["orders"] for c in customers.values()) / n,
        "profit_per_customer": sum(c["revenue"] for c in customers.values()) * margin / n,
        "cohorts": dict(sorted(cohorts.items())),
        "segments": segments,
        "note": "repeat_purchases для планировщика = avg_orders. Действия по сегментам — с контрольной группой.",
    }
