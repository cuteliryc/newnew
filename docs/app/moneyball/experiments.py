"""Слой 6. Эксперименты и очередь гипотез.

Правила из исследований: выигрывает меньшинство тестов (8–33%), подглядывание завышает
ложные победы, поэтому решение принимается только при запланированном объёме выборки.
Очередь гипотез ранжируется не по субъективному ICE, а по нашей же истории побед в слое.
"""

from .io import num
from .stats import false_win_rate, prob_better


def evaluate(rows, cfg):
    e = cfg["experiments"]
    thr = e["decision_threshold"]
    results = []
    for r in rows:
        if not (num(r, "n_a") and num(r, "n_b")):
            continue
        pb = prob_better(num(r, "conv_a"), num(r, "n_a"), num(r, "conv_b"), num(r, "n_b"),
                         prior_events=cfg["prior_events"])
        planned = num(r, "planned_n_per_variant")
        reached = not planned or min(num(r, "n_a"), num(r, "n_b")) >= planned
        if not reached:
            verdict = "ждать: объём не набран (не подглядываем)"
        elif pb["p_b_better"] >= thr:
            verdict = "B лучше — внедрять"
        elif pb["p_b_better"] <= 1 - thr:
            verdict = "A лучше — оставить A"
        else:
            verdict = "разницы не видно — выбрать проще/дешевле и записать вывод"
        recorded = str(r.get("result") or "").lower()
        if recorded == "win" and pb["p_b_better"] < thr and reached:
            verdict += " ⚠ в таблице записано «win», но расчёт победу не подтверждает"
        results.append({
            "id": r.get("id"), "layer": r.get("layer"), "hypothesis": r.get("hypothesis"),
            "variable": r.get("variable"), "p_b_better": pb["p_b_better"],
            "lift": pb["lift_mean"], "lift_90": [pb["lift_low"], pb["lift_high"]],
            "reached_planned_n": reached, "verdict": verdict,
            "recorded_result": r.get("result"),
        })
    return results


def win_rates(rows, cfg):
    """Доля побед по слоям с априором на уровне отрасли."""
    base = cfg["experiments"]["base_win_rate"]
    k = 5
    layers = {}
    for r in rows:
        result = str(r.get("result") or "").lower()
        if result not in ("win", "loss", "flat"):
            continue
        layer = str(r.get("layer") or "other")
        w, n = layers.get(layer, (0, 0))
        layers[layer] = (w + (result == "win"), n + 1)
    out = {}
    for layer, (w, n) in layers.items():
        rate = (w + base * k) / (n + k)
        out[layer] = {"wins": w, "finished": n, "win_rate": rate,
                      "false_win_share": false_win_rate(rate)}
    return out


def prioritize(hypotheses, rates, cfg):
    """Ожидаемая ценность гипотезы в деньгах на час работы."""
    e = cfg["experiments"]
    weights = e["evidence_weight"]
    ranked = []
    for h in hypotheses:
        if str(h.get("status") or "new").lower() not in ("new", "queued"):
            continue
        layer = str(h.get("layer") or "other")
        p_win = rates.get(layer, {}).get("win_rate", e["base_win_rate"])
        evidence = str(h.get("evidence") or "none").lower()
        value = num(h, "expected_lift") * num(h, "value_at_stake")
        cost = max(num(h, "cost_hours", 1.0), 0.5)
        score = p_win * weights.get(evidence, 0.5) * value / cost
        ranked.append({**h, "p_win": p_win, "expected_value": p_win * value, "score": score})
    ranked.sort(key=lambda h: h["score"], reverse=True)
    return ranked


def analyze(experiments, hypotheses, cfg):
    rates = win_rates(experiments, cfg)
    return {
        "status": "ok",
        "running_and_finished": evaluate(experiments, cfg),
        "win_rates": rates,
        "queue": prioritize(hypotheses, rates, cfg)[:15],
        "note": "Главный актив системы — история тестов: чем она длиннее, тем точнее приоритеты.",
    }
