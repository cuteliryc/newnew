"""Слой 4. Слова и формулировки.

Два источника правды разной силы:
  1) тесты текста из experiments.csv (layer=copy) — причинный вывод;
  2) слова и приёмы в заголовках креативов — корреляция, только как подсказка для теста.
Исследования показывают: эффект отдельного слова — проценты, интуиция часто ошибается в знаке,
поэтому слова проверяются тестом, а сначала тестируются крупные углы подачи.
"""

import re

from .io import num
from .stats import prob_better, sample_size_per_variant

_WORD = re.compile(r"[a-zа-яё0-9]+", re.IGNORECASE)
_STOP = set("""
и в во не что он на я с со как а то все она так его но да ты к у же вы за бы по только ее мне
было вот от меня еще нет о из ему когда даже ну ли если уже или ни быть был него до вас опять
уж вам ведь там потом себя ничего ей может они тут где есть надо ней для мы тебя их чем была
сам без будет тогда кто этот того потому этого какой совсем ним здесь этом один почти мой тем
чтобы нее сейчас были куда зачем всех можно при об после над больше тот через эти нас про всего
них какая много три эту моя свою этой перед лучше чуть том такой им более всегда между
the a an and or of to in for on with is are you your it this that be at by from
""".split())

# Структурные приёмы заголовка, которые можно проверить тестом.
_PATTERNS = {
    "есть_число": lambda t: bool(re.search(r"\d", t)),
    "вопрос": lambda t: "?" in t,
    "восклицание": lambda t: "!" in t,
    "обращение_на_ты_вы": lambda t: bool(re.search(r"\b(ты|тебе|твой|вы|вам|ваш)\b", t, re.I)),
    "цена_или_выгода": lambda t: bool(re.search(r"(₽|руб|\$|€|%|скидк|бесплатн|дешевл)", t, re.I)),
    "срок": lambda t: bool(re.search(r"(\bза \d+|\bдн|недел|час|минут|сегодня|быстр)", t, re.I)),
}


def stem(word):
    w = word.lower().replace("ё", "е")
    return w[:6] if len(w) > 6 else w


def tokens(text):
    return {stem(w) for w in _WORD.findall(text or "") if w.lower() not in _STOP and len(w) > 2}


def _length_bucket(text):
    n = len(_WORD.findall(text or ""))
    return "коротко_до_5" if n <= 5 else "средне_6_10" if n <= 10 else "длинно_11+"


def _feature_stats(rows, has_feature, res, base, k, tot_imp, tot_res):
    with_f = [r for r in rows if has_feature(r)]
    if not with_f or len(with_f) == len(rows):
        return None
    imp = sum(num(r, "impressions") for r in with_f)
    x = sum(num(r, res) for r in with_f)
    pb = prob_better(tot_res - x, tot_imp - imp, x, imp, prior_mean=base, prior_events=k)
    return {"creatives": len(with_f), "impressions": imp, "results": x,
            "lift_vs_rest": pb["lift_mean"], "lift_90": [pb["lift_low"], pb["lift_high"]],
            "p_better_than_rest": pb["p_b_better"]}


def analyze(creatives, experiments, cfg):
    c = cfg["creatives"]
    res, col, k = c["result"], c["text_column"], cfg["prior_events"]
    rows = [r for r in creatives if num(r, "impressions") > 0 and r.get(col)]
    out = {"status": "ok", "tested": [], "words": [], "patterns": {}, "length": []}

    for e in experiments:
        if str(e.get("layer", "")).lower() != "copy":
            continue
        if not (num(e, "n_a") and num(e, "n_b")):
            continue
        pb = prob_better(num(e, "conv_a"), num(e, "n_a"), num(e, "conv_b"), num(e, "n_b"),
                         prior_events=k)
        out["tested"].append({
            "id": e.get("id"), "variable": e.get("variable"),
            "a": e.get("variant_a"), "b": e.get("variant_b"),
            "p_b_better": pb["p_b_better"], "lift": pb["lift_mean"],
            "lift_90": [pb["lift_low"], pb["lift_high"]],
            "status": e.get("status"), "learning": e.get("learning"),
        })

    if not rows:
        out["hint"] = "нет креативов с текстом и показами — анализ слов пропущен"
        return out

    tot_imp = sum(num(r, "impressions") for r in rows)
    tot_res = sum(num(r, res) for r in rows)
    base = tot_res / tot_imp if tot_imp else 0.0

    vocab = {}
    for r in rows:
        for t in tokens(r[col]):
            vocab.setdefault(t, 0)
            vocab[t] += 1
    for word, count in vocab.items():
        if count < c["min_creatives"]:
            continue
        s = _feature_stats(rows, lambda r, w=word: w in tokens(r[col]), res, base, k, tot_imp, tot_res)
        if s:
            out["words"].append({"word": word, **s})
    out["words"].sort(key=lambda s: s["lift_vs_rest"], reverse=True)

    for name, fn in _PATTERNS.items():
        s = _feature_stats(rows, lambda r, f=fn: f(r[col]), res, base, k, tot_imp, tot_res)
        if s:
            out["patterns"][name] = s
    for bucket in ("коротко_до_5", "средне_6_10", "длинно_11+"):
        s = _feature_stats(rows, lambda r, b=bucket: _length_bucket(r[col]) == b, res, base, k, tot_imp, tot_res)
        if s:
            out["length"].append({"bucket": bucket, **s})

    if base > 0:
        out["sample_size_hint"] = {
            f"+{int(m * 100)}%": sample_size_per_variant(base, m) for m in (0.1, 0.2, 0.5)
            if base * (1 + m) < 1
        }
    out["caveat"] = ("Слова из креативов — корреляция: подсказка, что тестировать. "
                     "Решение «это слово работает» — только по тесту в tested.")
    return out
