"""Статистика: сглаживание к среднему, сравнение вариантов, размер выборки, бандит."""

import math
from statistics import NormalDist

import numpy as np

_rng = np.random.default_rng(42)
_EPS = 1e-9


def _prior(prior_mean, prior_events):
    """Beta-априор, который «весит» prior_events успехов при среднем prior_mean."""
    m = min(max(prior_mean, 1e-6), 1 - 1e-6)
    strength = prior_events / m
    return m * strength, (1 - m) * strength


def shrink_rate(successes, trials, prior_mean, prior_events=5):
    """Оценка доли, сглаженная к среднему по аккаунту.

    (успехи + a) / (попытки + a + b). Защищает от выводов по 3 конверсиям из 20 кликов.
    """
    if prior_mean <= 0:
        return successes / trials if trials else 0.0
    a, b = _prior(prior_mean, prior_events)
    return (successes + a) / (trials + a + b)


def beta_samples(successes, trials, prior_mean, prior_events=5, size=20000):
    a, b = _prior(prior_mean if prior_mean > 0 else 0.01, prior_events)
    failures = max(trials - successes, 0)
    return _rng.beta(a + successes, b + failures, size)


def prob_better(s_a, n_a, s_b, n_b, prior_mean=None, prior_events=5):
    """P(доля B > доли A) и распределение относительного прироста B к A."""
    if prior_mean is None:
        total = n_a + n_b
        prior_mean = (s_a + s_b) / total if total else 0.01
    a = beta_samples(s_a, n_a, prior_mean, prior_events)
    b = beta_samples(s_b, n_b, prior_mean, prior_events)
    lift = b / np.maximum(a, _EPS) - 1
    return {
        "p_b_better": float((b > a).mean()),
        "lift_mean": float(np.median(lift)),
        "lift_low": float(np.quantile(lift, 0.05)),
        "lift_high": float(np.quantile(lift, 0.95)),
    }


def sample_size_per_variant(base_rate, mde_rel, alpha=0.05, power=0.8):
    """Сколько попыток на вариант нужно, чтобы заметить относительный прирост mde_rel."""
    p1 = base_rate
    p2 = base_rate * (1 + mde_rel)
    if not 0 < p1 < 1 or not 0 < p2 < 1:
        raise ValueError("доли должны быть между 0 и 1")
    z_a = NormalDist().inv_cdf(1 - alpha / 2)
    z_b = NormalDist().inv_cdf(power)
    pbar = (p1 + p2) / 2
    n = (z_a * math.sqrt(2 * pbar * (1 - pbar)) + z_b * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(n / (p2 - p1) ** 2)


def false_win_rate(win_rate, alpha=0.05, power=0.8):
    """Доля «побед», которые на самом деле ложные, при данной базовой доле выигрышей."""
    true_wins = win_rate * power
    false_wins = (1 - win_rate) * alpha / 2
    return false_wins / (true_wins + false_wins)


def thompson_pick(arms, prior_mean, prior_events=5, k=1):
    """Бандит: выбирает k вариантов, пропорционально вероятности быть лучшим.

    arms: {имя: (успехи, попытки)}. Новые варианты без данных тоже получают шанс.
    """
    draws = {name: beta_samples(s, n, prior_mean, prior_events, size=1)[0] for name, (s, n) in arms.items()}
    return [name for name, _ in sorted(draws.items(), key=lambda kv: kv[1], reverse=True)[:k]]


def win_probabilities(arms, prior_mean, prior_events=5, size=20000):
    """P(вариант лучший) для каждого варианта — основа распределения показов."""
    names = list(arms)
    if not names:
        return {}
    matrix = np.vstack([beta_samples(s, n, prior_mean, prior_events, size) for s, n in arms.values()])
    best = matrix.argmax(axis=0)
    return {name: float((best == i).mean()) for i, name in enumerate(names)}
