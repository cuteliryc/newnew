"""Мост для онлайн-версии (docs/): страница вызывает эти функции через Pyodide.

Все входы и выходы — строки (JSON, CSV, Markdown, base64), чтобы их было просто передавать из JavaScript.
Данные пользователя живут только в памяти браузера.
"""

import base64
import io
import json
import tempfile
from pathlib import Path

from . import design, planner, pr, weekly
from .io import load_config, read_csv
from .stats import prob_better, sample_size_per_variant

DATA_FILES = ["funnel.csv", "channel_weeks.csv", "creatives.csv", "competitors.csv", "experiments.csv",
              "hypotheses.csv", "content.csv", "orders.csv"]

_state = {"root": Path("."), "engine": None}


def setup(root, fonts_dir=None):
    _state["root"] = Path(root)
    _state["fonts"] = Path(fonts_dir) if fonts_dir else None
    return "ok"


def _cfg(config_json=None):
    cfg = load_config("__none__")
    if config_json:
        extra = json.loads(config_json)
        for k, v in extra.items():
            if isinstance(v, dict) and isinstance(cfg.get(k), dict):
                cfg[k].update(v)
            else:
                cfg[k] = v
    fonts = _state.get("fonts")
    if fonts:
        cfg["design"]["font_bold"] = str(fonts / "Inter-Bold.otf")
        cfg["design"]["font_regular"] = str(fonts / "Inter-Regular.otf")
    return cfg


def _knowledge():
    k = _state["root"] / "knowledge"
    return planner.load_catalog(k / "channels.json"), planner.load_cases(k / "cases")


def run_weekly(files_json, config_json=None):
    """files_json: {"funnel.csv": "<текст csv>", …}. Возвращает {"report": md, "engine": json}."""
    files = json.loads(files_json)
    cfg = _cfg(config_json)
    with tempfile.TemporaryDirectory() as tmp:
        data = Path(tmp) / "data"
        data.mkdir()
        for name, text in files.items():
            if name in DATA_FILES and text:
                (data / name).write_text(text, encoding="utf-8")
        target, result = weekly.run(cfg, data, Path(tmp) / "out")
        report = (target / "report.md").read_text(encoding="utf-8")
    _state["engine"] = result
    _state["creatives"] = files.get("creatives.csv", "")
    return json.dumps({"report": report, "engine": result}, ensure_ascii=False, default=str)


def run_plan(request_json, config_json=None):
    req = json.loads(request_json)
    cfg = _cfg(config_json)
    catalog, cases = _knowledge()
    engine = _state.get("engine") or {}
    plan = planner.build_plan(req, catalog, cases, engine.get("funnel"), engine.get("creatives"), engine)
    return json.dumps({"markdown": planner.render_plan(plan, cfg), "plan": plan}, ensure_ascii=False, default=str)


def run_banners(brief_json, image_b64=None, config_json=None):
    brief = json.loads(brief_json)
    cfg = _cfg(config_json)
    creatives = []
    if _state.get("creatives"):
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8") as f:
            f.write(_state["creatives"])
        creatives = read_csv(f.name)
    image = None
    if image_b64:
        from PIL import Image
        image = Image.open(io.BytesIO(base64.b64decode(image_b64.split(",")[-1])))
    specs = design.plan_banners(brief, creatives, cfg)
    out = []
    for i, spec in enumerate(specs):
        img, feats = design.render(spec, cfg, image)
        buf = io.BytesIO()
        img.save(buf, "PNG")
        cid = f"B-{i + 1:02d}-{spec['layout']}-{spec['size']}"
        out.append({"creative_id": cid, "png": base64.b64encode(buf.getvalue()).decode("ascii"),
                    "row": {"creative_id": cid, "status": "planned", "format": "static",
                            "channel": brief.get("channel"), **spec, **feats}})
    fields = design.MANIFEST_FIELDS
    lines = [",".join(fields)]
    for b in out:
        r = b["row"]
        lines.append(",".join('"' + str(r.get(k, "") if r.get(k) is not None else "").replace('"', '""') + '"'
                              for k in fields))
    return json.dumps({"banners": out, "manifest": "\n".join(lines)}, ensure_ascii=False, default=str)


def run_pr_score(idea_json):
    idea = json.loads(idea_json)
    _, cases = _knowledge()
    res = pr.score_idea(idea)
    md = pr.render_score(idea, res, pr.similar_cases(idea, cases), pr.similar_cases(idea, cases, top=3, anti=True))
    return json.dumps({"result": res, "markdown": md}, ensure_ascii=False)


def run_pr_ideas(brief_json):
    brief = json.loads(brief_json)
    _, cases = _knowledge()
    return pr.render_ideas(brief, pr.generate_ideas(brief, cases), cases)


def pr_form():
    return json.dumps({"blocks": {b: {k: {"q": q, "w": w} for k, (q, w) in c.items()} for b, c in pr.BLOCKS.items()},
                       "flags": pr.STOP_FLAGS, "patterns": [{"name": p["name"], "needs": p["needs"]} for p in pr.PATTERNS]},
                      ensure_ascii=False)


def run_abtest(conv_a, n_a, conv_b, n_b):
    return json.dumps(prob_better(conv_a, n_a, conv_b, n_b))


def run_sample_size(base_rate, mde):
    return sample_size_per_variant(base_rate, mde)


def catalog_json():
    catalog, cases = _knowledge()
    slim = [{k: c.get(k) for k in ("id", "title", "brand", "market", "industry", "channels", "objective",
                                   "what_they_did", "mechanism", "transferable_lesson", "test_to_run",
                                   "evidence", "source_url", "year", "pattern", "news_values",
                                   "why_media_covered", "risks_or_backlash", "_file")} for c in cases]
    return json.dumps({"channels": catalog, "cases": slim}, ensure_ascii=False)


def offer_checks():
    from .offer import CHECKS
    return json.dumps([{"key": k, "q": q} for k, q, _ in CHECKS], ensure_ascii=False)
