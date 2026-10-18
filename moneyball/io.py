"""Чтение CSV и конфига. Только стандартная библиотека."""

import copy
import csv
import json
import re
from pathlib import Path

DEFAULT_CONFIG = {
    "currency": "RUB",
    # Стоимость часа вашей работы: ручные касания тоже стоят денег.
    "hourly_rate": 1500,
    # Валовая маржа с выручки (0..1). Заполните своё значение.
    "gross_margin": 0.7,
    # Сила априорного сглаживания: «сколько событий» весит среднее по аккаунту.
    "prior_events": 5,
    "funnel": {
        "stages": [
            ["impressions", "Показы / касания"],
            ["clicks", "Клики / ответы"],
            ["leads", "Заявки / диалоги"],
            ["qualified", "Офферы / квалиф."],
            ["deals", "Сделки"],
        ],
        "revenue": "revenue",
        "group_by": [["channel"], ["channel", "offer"], ["segment"]],
    },
    "budget": {
        "outcome": "revenue",
        "outcome_is_revenue": True,
        # Если outcome — сделки, а не выручка: маржинальная прибыль с одной сделки.
        "value_per_outcome": None,
        "min_weeks": 12,
        "min_spend_cv": 0.15,
        "max_step": 0.3,
        "exploration_share": 0.1,
        "total_budget": None,
    },
    "creatives": {
        "tags": ["hook", "angle", "format", "persona", "offer", "cta", "layout"],
        "result": "leads",
        "text_column": "headline",
        "min_creatives": 3,
    },
    "competitors": {
        "survivor_days": 30,
        "gap_share": 0.15,
        "crowded_share": 0.7,
    },
    "experiments": {
        "decision_threshold": 0.95,
        # Доля тестов, которые обычно выигрывают (8–33% в исследованиях).
        "base_win_rate": 0.2,
        "evidence_weight": {"strong": 1.5, "medium": 1.0, "weak": 0.7, "none": 0.5},
    },
    "design": {
        "sizes": {
            "square": [1080, 1080],
            "portrait": [1080, 1350],
            "story": [1080, 1920],
            "landscape": [1200, 628],
        },
        "layouts": ["thirds", "golden", "grid", "center", "zpattern"],
        "min_contrast": 4.5,
        "font_bold": None,
        "font_regular": None,
    },
    "llm": {
        # "codex" — GPT через подписку ChatGPT (вход в браузере: `codex login`).
        # "openai_api" — платный API или любой OpenAI-совместимый сервис.
        "backend": "codex",
        # None — модель по умолчанию из настроек Codex / сервиса.
        "model": None,
        "timeout_sec": 600,
        "max_context_chars": 60000,
        "codex_bin": "codex",
        "base_url": "https://api.openai.com/v1",
        "api_key_env": "OPENAI_API_KEY",
        "temperature": 0.3,
        "max_tokens": 2500,
    },
}

_NUMERIC = re.compile(r"^-?\d+(?:[.,]\d+)?$")


def _merge(base, extra):
    for key, value in extra.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            _merge(base[key], value)
        else:
            base[key] = value
    return base


def load_config(path="config.json"):
    cfg = copy.deepcopy(DEFAULT_CONFIG)
    p = Path(path)
    if p.exists():
        _merge(cfg, json.loads(p.read_text(encoding="utf-8")))
    return cfg


def _parse(key, value):
    if value is None:
        return None
    s = value.strip()
    if s == "":
        return None
    # Идентификаторы оставляем строками, даже если они из цифр.
    if key == "id" or key.endswith("_id"):
        return s
    if _NUMERIC.match(s):
        return float(s.replace(",", "."))
    return s


def read_csv(path):
    p = Path(path)
    if not p.exists():
        return []
    with p.open(encoding="utf-8-sig", newline="") as f:
        return [
            {k.strip(): _parse(k.strip(), v) for k, v in row.items() if k}
            for row in csv.DictReader(f)
        ]


def write_csv(path, rows, fieldnames=None):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: "" if row.get(k) is None else row.get(k) for k in fieldnames})


def append_csv(path, rows, fieldnames):
    p = Path(path)
    exists = p.exists() and p.stat().st_size > 0
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        if not exists:
            w.writeheader()
        for row in rows:
            w.writerow({k: "" if row.get(k) is None else row.get(k) for k in fieldnames})


def num(row, key, default=0.0):
    value = row.get(key)
    return float(value) if isinstance(value, (int, float)) else default


def write_json(path, data):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
