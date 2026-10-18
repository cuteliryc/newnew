import json
import math
from pathlib import Path

import numpy as np
import pytest

from moneyball import agents, budget, creative, design, experiments, funnel, planner, pr, stats
from moneyball.io import load_config, read_csv

ROOT = Path(__file__).resolve().parent.parent
DEMO = ROOT / "examples" / "demo"


@pytest.fixture(scope="module")
def cfg():
    return load_config(DEMO / "config.json")


def test_shrink_pulls_small_samples_to_mean():
    # 3 из 20 — это не 15%, если среднее 2%: оценка должна быть ближе к среднему
    est = stats.shrink_rate(3, 20, 0.02, prior_events=5)
    assert 0.02 < est < 0.05
    # на большом объёме сглаживание почти не влияет
    assert abs(stats.shrink_rate(1500, 10000, 0.02) - 0.15) < 0.01


def test_sample_size_matches_textbook():
    # 2% базовая конверсия, +10% относительно → ≈80 тыс. на вариант
    n = stats.sample_size_per_variant(0.02, 0.10)
    assert 75000 < n < 85000


def test_false_win_rate_low_base_rate():
    # при 8% выигрышных тестов заметная доля «побед» ложная
    assert 0.2 < stats.false_win_rate(0.08) < 0.35


def test_prob_better_direction():
    res = stats.prob_better(100, 10000, 150, 10000)
    assert res["p_b_better"] > 0.99 and res["lift_mean"] > 0.3


def test_budget_recovers_saturation_and_equalizes():
    rng = np.random.default_rng(1)
    spend = 10000 * (1 + 0.5 * np.sin(np.arange(30) / 2.5))
    p_true = {"theta": 0.3, "alpha": 1.5, "half": 12000.0, "base": 20000.0, "beta": 160000.0}
    a = budget.adstock(spend, 0.3)
    y = 20000 + 160000 * budget.hill(a, 1.5, 12000) + rng.normal(0, 2000, 30)
    fit = budget.fit_channel(spend, y)
    assert fit["r2"] > 0.9
    # предельная отдача падает с ростом расхода — насыщение найдено
    assert budget.marginal(5000, fit) > budget.marginal(20000, fit)


def test_funnel_finds_bottleneck(cfg):
    rows = read_csv(DEMO / "funnel.csv")
    res = funnel.analyze(rows, cfg)
    assert res["status"] == "ok"
    channels = {g["group"]["channel"]: g for g in res["groups"]["channel"]}
    assert channels["cold_telegram"]["profit_per_1000"] > channels["vk_ads"]["profit_per_1000"]


def test_creative_detects_planted_winner(cfg):
    res = creative.analyze(read_csv(DEMO / "creatives.csv"), cfg)
    winners = {(w["tag"], w["value"]) for w in res["winners"]}
    assert ("hook", "before_after") in winners


def test_experiments_no_peeking(cfg):
    rows = read_csv(DEMO / "experiments.csv")
    res = {r["id"]: r for r in experiments.evaluate(rows, cfg)}
    assert res["E3"]["verdict"].startswith("ждать")


def test_banner_render_and_features(cfg, tmp_path):
    brief = json.loads((DEMO / "brief.json").read_text(encoding="utf-8"))
    for layout in cfg["design"]["layouts"]:
        for size in ("square", "story", "landscape"):
            spec = {"layout": layout, "size": size, "headline": "Контент к дропу за 3 дня",
                    "sub": brief["sub"], "cta": brief["cta"], "logo_text": "BRAND",
                    "colors": brief["colors"]}
            img, feats = design.render(spec, cfg)
            assert img.size == tuple(cfg["design"]["sizes"][size])
            assert feats["contrast_headline"] >= cfg["design"]["min_contrast"]
            assert 0 < feats["text_area_share"] < 0.6


def test_contrast_rule_switches_unreadable_color():
    color, c, scrim = design.pick_text_color((240, 240, 240), (0.9, 0.95), 4.5)
    assert c >= 4.5 or scrim


def test_copy_variants_from_brief_fields():
    out = design.copy_variants({"benefit": "контент без съёмки", "time": "3 дня", "offer": "Первый визуал бесплатно"})
    angles = {v["angle"] for v in out}
    assert {"speed", "benefit", "offer"} <= angles


def test_planner_unit_economics():
    econ = planner.unit_economics({"avg_check": 38000, "margin": 0.7, "repeat_purchases": 2,
                                   "lead_to_deal": 0.1})
    assert math.isclose(econ["profit_per_customer"], 53200)
    assert math.isclose(econ["target_cpl"], 53200 / 3 * 0.1)


def test_pr_score_flags_and_brand_link():
    weak = pr.score_idea({"answers": {"surprise": 2, "conflict": 2, "brand_link": 0}})
    assert "не о вас" in weak["verdict"]
    flagged = pr.score_idea({"answers": {k: 2 for k in pr.CRITERIA}, "red_flags": {"misleading": True}})
    assert flagged["red_flags"]


def test_agent_parsing(tmp_path):
    f = tmp_path / "x.md"
    f.write_text("---\nname: x\ninputs: [funnel, cases]\nweekly: true\n---\nРоль", encoding="utf-8")
    meta, body = agents.parse_agent(f)
    assert meta["inputs"] == ["funnel", "cases"] and meta["weekly"] is True and body == "Роль"
    hyps = agents.extract_hypotheses('текст\n```json\n{"hypotheses": [{"hypothesis": "h"}]}\n```')
    assert hyps == [{"hypothesis": "h"}]


def test_content_outliers_found(cfg):
    from moneyball import content
    res = content.analyze(read_csv(DEMO / "content.csv"), cfg)
    assert res["status"] == "ok" and res["outliers"]
    assert res["tags"]["topic"][0]["value"] == "до/после"


def test_retention_segments(cfg):
    from moneyball import retention
    res = retention.analyze(read_csv(DEMO / "orders.csv"), cfg)
    assert res["status"] == "ok"
    assert sum(s["customers"] for s in res["segments"].values()) == res["customers"]


def test_offer_check_lists_missing():
    from moneyball import offer
    res = offer.check({"checks": {"outcome": True}})
    assert res["passed"] == 1 and len(res["fix_first"]) == 4


def test_time_channels_get_hours_not_money():
    funnel_stats = None
    req = {"task": "leads", "channels_available": ["cold_telegram", "telegram_ads"], "budget_month": 50000,
           "avg_check": 38000, "margin": 0.7, "lead_to_deal": 0.1}
    econ = planner.unit_economics(req)
    channels = planner.score_channels(req, {"telegram_ads": {"best_for": ["leads"], "markets": ["RU"]}}, funnel_stats)
    plan = planner.split_budget(req, channels, econ)["plan"]
    assert plan.get("cold_telegram", {}).get("budget", 0) == 0 or "cold_telegram" not in plan
