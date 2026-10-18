"""Слой 2. Бюджет по предельной отдаче.

Модель канала (как в Robyn / Meridian, упрощённо):
  adstock:  A_t = x_t + θ·A_{t−1}                 — эффект рекламы переносится на следующие недели
  Хилл:     h(A) = A^α / (A^α + K^α)              — насыщение: каждый следующий рубль даёт меньше
  отклик:   y_t = база + β·h(A_t)

Правило распределения: деньги идут туда, где последний рубль приносит больше всего,
пока предельная отдача каналов не выровняется или не упадёт ниже 1 (рубль перестал окупаться).
"""

import numpy as np

from .io import num

_THETAS = np.arange(0.0, 0.85, 0.1)
_ALPHAS = np.arange(0.5, 3.01, 0.25)
_HALFS = np.arange(0.2, 1.01, 0.1)


def adstock(x, theta):
    out = np.zeros(len(x), dtype=float)
    carry = 0.0
    for i, v in enumerate(x):
        carry = v + theta * carry
        out[i] = carry
    return out


def hill(a, alpha, half):
    a = np.asarray(a, dtype=float)
    return a ** alpha / (a ** alpha + half ** alpha)


def fit_channel(spend, outcome):
    spend = np.asarray(spend, dtype=float)
    outcome = np.asarray(outcome, dtype=float)
    sst = float(((outcome - outcome.mean()) ** 2).sum())
    best = None
    for theta in _THETAS:
        a = adstock(spend, theta)
        amax = a.max()
        if amax <= 0:
            continue
        for alpha in _ALPHAS:
            for g in _HALFS:
                half = g * amax
                h = hill(a, alpha, half)
                X = np.column_stack([np.ones_like(h), h])
                (base, beta), *_ = np.linalg.lstsq(X, outcome, rcond=None)
                if base < 0:
                    base, beta = 0.0, float(h @ outcome / (h @ h)) if h @ h else 0.0
                if beta <= 0:
                    continue
                sse = float(((outcome - base - beta * h) ** 2).sum())
                if best is None or sse < best["sse"]:
                    best = {"sse": sse, "theta": float(theta), "alpha": float(alpha),
                            "half": float(half), "base": float(base), "beta": float(beta)}
    if best is None:
        return None
    best["r2"] = 1 - best["sse"] / sst if sst else 0.0
    return best


def response(weekly_spend, p):
    """Устойчивый недельный отклик при постоянном расходе."""
    a = weekly_spend / (1 - p["theta"])
    return p["base"] + p["beta"] * float(hill(a, p["alpha"], p["half"]))


def marginal(weekly_spend, p):
    d = max(1.0, 0.01 * weekly_spend)
    return (response(weekly_spend + d, p) - response(weekly_spend, p)) / d


def allocate(fits, current, value_per_outcome, total, max_step, exploration_share):
    """Жадное распределение маленькими шагами в канал с наибольшей предельной прибылью."""
    fitted = [ch for ch, f in fits.items() if f.get("status") == "ok"]
    fixed = sum(v for ch, v in current.items() if ch not in fitted)
    explore = total * exploration_share
    pool = total - explore - fixed
    lo = {ch: current[ch] * (1 - max_step) for ch in fitted}
    hi = {ch: max(current[ch] * (1 + max_step), 1.0) for ch in fitted}
    if pool < sum(lo.values()):
        scale = pool / sum(lo.values()) if sum(lo.values()) else 0
        lo = {ch: v * scale for ch, v in lo.items()}
    alloc = dict(lo)
    remaining = pool - sum(alloc.values())
    step = max(pool / 400, 1.0)
    while remaining > 1e-6:
        options = [
            (marginal(alloc[ch], fits[ch]["params"]) * value_per_outcome, ch)
            for ch in fitted if alloc[ch] < hi[ch] - 1e-9
        ]
        if not options:
            break
        best_value, best_ch = max(options)
        if best_value < 1:
            break
        inc = min(step, remaining, hi[best_ch] - alloc[best_ch])
        alloc[best_ch] += inc
        remaining -= inc
    plan = {}
    for ch, cur in current.items():
        new = alloc.get(ch, cur)
        row = {"current": cur, "recommended": new,
               "change_pct": (new / cur - 1) if cur else None}
        if ch in fitted:
            p = fits[ch]["params"]
            row["marginal_roi_now"] = marginal(cur, p) * value_per_outcome
            row["marginal_roi_after"] = marginal(new, p) * value_per_outcome
            row["outcome_change"] = response(new, p) - response(cur, p)
        else:
            row["note"] = "оставлен как есть: модель не построена"
        plan[ch] = row
    # Если даже после перераспределения добавочный рубль приносит заметно больше рубля,
    # проблема не в пропорциях, а в общем бюджете.
    underfunded = [ch for ch, row in plan.items() if row.get("marginal_roi_after", 0) > 1.5]
    return {"plan": plan, "exploration_budget": explore, "unallocated": max(remaining, 0.0),
            "underfunded": underfunded}


def analyze(rows, cfg):
    b = cfg["budget"]
    if not rows:
        return {"status": "no_data", "hint": "заполните data/channel_weeks.csv"}
    by_channel = {}
    for r in rows:
        by_channel.setdefault(str(r.get("channel")), []).append(r)

    if b["outcome_is_revenue"]:
        value_per_outcome = cfg["gross_margin"]
    else:
        value_per_outcome = b.get("value_per_outcome")
        if not value_per_outcome:
            return {"status": "config_error",
                    "hint": "outcome не выручка — задайте budget.value_per_outcome (прибыль с одного результата)"}

    fits, current = {}, {}
    for ch, items in by_channel.items():
        items.sort(key=lambda r: str(r.get("week")))
        spend = np.array([num(r, "spend") for r in items])
        outcome = np.array([num(r, b["outcome"]) for r in items])
        recent = spend[-4:]
        current[ch] = float(recent.mean()) if len(recent) else 0.0
        weeks = len(items)
        cv = float(spend.std() / spend.mean()) if spend.mean() else 0.0
        if weeks < b["min_weeks"]:
            fits[ch] = {"status": "insufficient_data", "weeks": weeks,
                        "hint": f"нужно ≥{b['min_weeks']} недель; пока решения — через тесты"}
            continue
        if cv < b["min_spend_cv"]:
            fits[ch] = {"status": "no_variation", "spend_cv": cv,
                        "hint": "расход почти не менялся — модель не отличит эффект от фона. "
                                "Меняйте бюджет волнами ±20–30% или проведите гео/holdout-тест"}
            continue
        p = fit_channel(spend, outcome)
        if p is None:
            fits[ch] = {"status": "no_effect", "hint": "связь расхода и результата не найдена"}
            continue
        fits[ch] = {"status": "ok", "weeks": weeks, "spend_cv": cv, "params": p,
                    "r2": p["r2"], "reliable": p["r2"] >= 0.5,
                    "avg_roi": float(outcome.sum() * value_per_outcome / spend.sum() - 1) if spend.sum() else None}

    total = b.get("total_budget") or sum(current.values())
    allocation = allocate(fits, current, value_per_outcome, total, b["max_step"], b["exploration_share"])
    return {
        "status": "ok",
        "value_per_outcome": value_per_outcome,
        "total_budget_weekly": total,
        "channels": fits,
        "allocation": allocation,
        "caveat": "Модель наблюдательная. Перед крупным переносом бюджета подтвердите эффект "
                  "lift- или гео-тестом и внесите его результат в experiments.csv.",
    }
