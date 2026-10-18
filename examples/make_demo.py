"""Генератор ВЫМЫШЛЕННЫХ демо-данных: показать, как работает система, и проверить формулы.

Зависимости зашиты известные (какой хук сильнее, как насыщается канал), чтобы было видно,
что движок их находит. Это не реальные данные и не бенчмарки.
"""

import csv
import json
import math
from datetime import date, timedelta
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

OUT = Path(__file__).parent / "demo"
rng = np.random.default_rng(7)


def write(name, rows):
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / name).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def funnel():
    # Канал: (касаний/нед, CR ответа, CR диалога, CR оффера, CR сделки, часы/100 касаний, расход/нед)
    channels = {
        "cold_telegram": (60, 0.12, 0.5, 0.45, 0.25, 2.0, 0),
        "cold_instagram": (60, 0.05, 0.5, 0.4, 0.25, 2.0, 0),
        "cold_email": (80, 0.04, 0.6, 0.5, 0.2, 0.8, 0),
        "telegram_ads": (25000, 0.008, 0.08, 0.5, 0.2, 0.02, 9000),
        "vk_ads": (40000, 0.006, 0.05, 0.4, 0.15, 0.01, 7000),
    }
    offers = {"ai_content": 38000, "vibecoding": 60000, "launch": 151600}
    rows = []
    start = date(2026, 7, 6)
    for week in range(12):
        d = (start + timedelta(weeks=week)).isoformat()
        for ch, (vol, c1, c2, c3, c4, hrs, spend) in channels.items():
            for offer, check in offers.items():
                share = {"ai_content": 0.6, "vibecoding": 0.3, "launch": 0.1}[offer]
                n = int(vol * share)
                clicks = rng.binomial(n, c1)
                leads = rng.binomial(clicks, c2)
                qual = rng.binomial(leads, c3)
                deals = rng.binomial(qual, c4 * (0.6 if offer == "launch" else 1))
                rows.append({"date": d, "channel": ch, "campaign": f"{ch}_{offer}",
                             "segment": "fashion_founder" if offer != "vibecoding" else "expert_founder",
                             "offer": offer, "spend": round(spend * share), "hours": round(n * hrs / 100, 1),
                             "impressions": n, "clicks": clicks, "leads": leads, "qualified": qual,
                             "deals": deals, "revenue": deals * check})
    write("funnel.csv", rows)


def channel_weeks():
    # Истинные параметры: theta, alpha, half, beta (выручка), база
    truth = {"telegram_ads": (0.3, 1.5, 12000, 160000, 20000),
             "vk_ads": (0.2, 1.2, 6000, 50000, 10000),
             "yandex_direct": (0.4, 2.0, 15000, 180000, 30000)}
    rows = []
    start = date(2026, 4, 6)
    for ch, (theta, alpha, half, beta, base) in truth.items():
        carry = 0.0
        base_spend = {"telegram_ads": 9000, "vk_ads": 7000, "yandex_direct": 10000}[ch]
        for week in range(26):
            spend = base_spend * (1 + 0.45 * math.sin(week / 2.5)) * rng.uniform(0.85, 1.15)
            carry = spend + theta * carry
            h = carry ** alpha / (carry ** alpha + half ** alpha)
            revenue = max(base + beta * h + rng.normal(0, 6000), 0)
            rows.append({"week": (start + timedelta(weeks=week)).isoformat(), "channel": ch,
                         "spend": round(spend), "revenue": round(revenue), "deals": round(revenue / 38000, 1)})
    write("channel_weeks.csv", rows)


def creatives():
    hooks = {"before_after": 1.5, "pain": 1.2, "question": 1.0, "price": 0.8}
    angles = {"speed": 1.3, "price": 0.9, "quality": 1.1, "proof": 1.2}
    layouts = {"thirds": 1.0, "golden": 1.0, "grid": 1.1, "center": 0.9, "zpattern": 1.0}
    formats = {"static": 1.0, "video": 1.25}
    heads = {
        "speed": ["Контент к дропу за 3 дня", "Визуалы для бренда за 72 часа", "Съёмка не нужна: готово за 3 дня"],
        "price": ["В 5 раз дешевле съёмки", "Контент без бюджета на продакшн", "Студийный визуал по цене обеда"],
        "quality": ["Не отличить от студийной съёмки", "Визуал уровня большого бренда", "Кампания как у VCHASE"],
        "proof": ["12 брендов уже сняли так кампанию", "Кейс: лента без пустых недель", "Как DAYDESIGN запустил дроп"],
    }
    rows = []
    i = 0
    for hook, hm in hooks.items():
        for angle, am in angles.items():
            for _ in range(2):
                i += 1
                layout = list(layouts)[i % len(layouts)]
                fmt = "video" if i % 3 == 0 else "static"
                imp = int(rng.uniform(8000, 30000))
                p = 0.0012 * hm * am * layouts[layout] * formats[fmt]
                clicks = rng.binomial(imp, p * 8)
                leads = rng.binomial(imp, p)
                deals = rng.binomial(leads, 0.12)
                rows.append({"creative_id": f"C{i:03d}", "channel": "telegram_ads" if i % 2 else "vk_ads",
                             "status": "active", "launched": "2026-08-01", "format": fmt,
                             "persona": "fashion_founder", "offer": "free_sample", "angle": angle, "hook": hook,
                             "cta": "write_tg", "layout": layout, "text_density": "mid", "size": "square",
                             "headline": heads[angle][i % 3], "sub": "", "file": "",
                             "spend": round(imp * 0.3), "impressions": imp, "clicks": clicks, "leads": leads,
                             "deals": deals, "revenue": deals * 38000})
    write("creatives.csv", rows)


def competitors():
    comps = {"Studio A": ["price", "quality"], "AI Lab B": ["speed", "price", "price"],
             "Agency C": ["quality", "proof"], "Creator D": ["price", "speed"]}
    rows = []
    for snap in ("2026-09-20", "2026-10-11"):
        n = 0
        for comp, angles in comps.items():
            for j, angle in enumerate(angles):
                n += 1
                first = date(2026, 7, 1) + timedelta(days=int(rng.integers(0, 80)))
                if snap == "2026-10-11" and j == 0:
                    first = date(2026, 10, 1)
                last = date.fromisoformat(snap) if (n % 4) else first + timedelta(days=10)
                rows.append({"snapshot_date": snap, "competitor": comp, "platform": "vk_ads",
                             "ad_id": f"{comp[:3]}-{j}-{snap[5:7]}", "first_seen": first.isoformat(),
                             "last_seen": last.isoformat(), "angle": angle,
                             "offer": "скидка 20%" if angle == "price" else "бесплатный тест",
                             "format": "video" if j % 2 else "static", "hook": "price" if angle == "price" else "pain",
                             "text": f"{comp}: {angle} — пример текста объявления", "url": ""})
    rows.append({**rows[-1], "competitor": "AI Lab B", "angle": "guarantee", "ad_id": "AIL-g",
                 "first_seen": "2026-08-01", "last_seen": "2026-10-11", "snapshot_date": "2026-10-11",
                 "text": "Не понравится — вернём деньги", "offer": "гарантия"})
    rows.append({**rows[-1], "competitor": "Studio A", "angle": "guarantee", "ad_id": "STU-g"})
    write("competitors.csv", rows)


def experiments():
    write("experiments.csv", [
        {"id": "E1", "layer": "copy", "hypothesis": "Цифра в заголовке поднимет заявки", "variable": "headline",
         "variant_a": "Контент без съёмки", "variant_b": "Контент без съёмки за 3 дня", "metric": "leads/impr",
         "start": "2026-09-01", "end": "2026-09-21", "planned_n_per_variant": 20000, "n_a": 21000, "conv_a": 24,
         "n_b": 20500, "conv_b": 37, "status": "done", "result": "win", "learning": "конкретный срок работает"},
        {"id": "E2", "layer": "offer", "hypothesis": "Бесплатный визуал лучше скидки 20%", "variable": "offer",
         "variant_a": "скидка 20%", "variant_b": "бесплатный визуал", "metric": "deals/lead",
         "start": "2026-08-01", "end": "2026-09-01", "planned_n_per_variant": 60, "n_a": 62, "conv_a": 6,
         "n_b": 64, "conv_b": 11, "status": "done", "result": "win", "learning": "взаимность сильнее скидки"},
        {"id": "E3", "layer": "creative", "hypothesis": "Видео лучше статики", "variable": "format",
         "variant_a": "static", "variant_b": "video", "metric": "leads/impr", "start": "2026-09-10",
         "end": "", "planned_n_per_variant": 30000, "n_a": 14000, "conv_a": 17, "n_b": 13800, "conv_b": 24,
         "status": "running", "result": "", "learning": ""},
        {"id": "E4", "layer": "copy", "hypothesis": "Вопрос в заголовке лучше утверждения", "variable": "headline",
         "variant_a": "утверждение", "variant_b": "вопрос", "metric": "leads/impr", "start": "2026-08-10",
         "end": "2026-08-30", "planned_n_per_variant": 20000, "n_a": 20100, "conv_a": 26, "n_b": 20300,
         "conv_b": 24, "status": "done", "result": "flat", "learning": "разницы нет"},
    ])
    write("hypotheses.csv", [
        {"id": "H1", "created": "2026-10-01", "source_agent": "manual", "layer": "offer",
         "hypothesis": "Гарантия «не понравится — вернём деньги» поднимет конверсию в сделку",
         "variable": "offer", "source": "конкуренты держат угол guarantee", "evidence": "medium",
         "expected_lift": 0.2, "value_at_stake": 120000, "cost_hours": 2, "status": "new"},
        {"id": "H2", "created": "2026-10-01", "source_agent": "manual", "layer": "creative",
         "hypothesis": "Хук «до/после» в видео для vk_ads", "variable": "hook", "source": "creative winners",
         "evidence": "medium", "expected_lift": 0.3, "value_at_stake": 60000, "cost_hours": 6, "status": "new"},
        {"id": "H3", "created": "2026-10-02", "source_agent": "manual", "layer": "copy",
         "hypothesis": "Слово «бесплатно» в первой строке", "variable": "headline", "source": "интуиция",
         "evidence": "none", "expected_lift": 0.05, "value_at_stake": 60000, "cost_hours": 1, "status": "new"},
    ])


def product_image():
    W = H = 900
    img = Image.new("RGBA", (W, H), (205, 198, 188, 255))
    d = ImageDraw.Draw(img)
    for y in range(H):
        c = int(215 - 60 * y / H)
        d.line([(0, y), (W, y)], fill=(c, c - 6, c - 14, 255))
    d.ellipse((260, 700, 640, 760), fill=(60, 50, 45, 120))
    d.rounded_rectangle((330, 180, 570, 720), radius=60, fill=(30, 30, 34, 255))
    d.rounded_rectangle((385, 120, 515, 200), radius=20, fill=(200, 255, 0, 255))
    d.rectangle((360, 380, 540, 470), fill=(235, 235, 230, 255))
    img = img.filter(ImageFilter.GaussianBlur(0.6))
    img.save(OUT / "product.png")


def configs():
    (OUT / "config.json").write_text(json.dumps({
        "currency": "RUB", "hourly_rate": 1500, "gross_margin": 0.7,
        "budget": {"outcome": "revenue", "outcome_is_revenue": True},
        "creatives": {"result": "leads"},
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    brief = json.loads((Path(__file__).parent.parent / "templates" / "brief.json").read_text(encoding="utf-8"))
    brief["image"] = "product.png"
    brief["n"] = 5
    (OUT / "brief.json").write_text(json.dumps(brief, ensure_ascii=False, indent=2), encoding="utf-8")
    req = json.loads((Path(__file__).parent.parent / "templates" / "request.json").read_text(encoding="utf-8"))
    (OUT / "request.json").write_text(json.dumps(req, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    funnel()
    channel_weeks()
    creatives()
    competitors()
    experiments()
    product_image()
    configs()
    print(f"Демо-данные: {OUT}")
