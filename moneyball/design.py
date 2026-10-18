"""Слой 7. Дизайн: сборка баннеров по правилам компоновки и обучение на результатах.

Что подтверждено исследованиями и поэтому проверяется автоматически:
  - доля площади текста и элементов (Pieters & Wedel 2004: площадь текста двигает внимание);
  - визуальная «пиксельная» сложность вредит, продуманная композиция помогает (Pieters, Wedel & Batra 2010);
  - читаемость: контраст текста (обоснование — беглость восприятия, прямых тестов на CTR нет).
Золотое сечение и правило третей как законы НЕ подтверждаются — поэтому это просто варианты
компоновки, а какая работает у вас, решает бандит по вашим результатам.
"""

import io
import math
from datetime import date
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

from .io import append_csv, num, write_csv
from .stats import thompson_pick

PHI = (1 + 5 ** 0.5) / 2

_BOLD = [
    "/usr/share/fonts/opentype/inter/Inter-Bold.otf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]
_REGULAR = [
    "/usr/share/fonts/opentype/inter/Inter-Regular.otf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/Library/Fonts/Arial.ttf",
    "C:/Windows/Fonts/arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]

MANIFEST_FIELDS = [
    "creative_id", "channel", "status", "launched", "format", "persona", "offer", "angle", "hook",
    "cta", "layout", "text_density", "size", "headline", "sub", "file",
    "text_area_share", "image_area_share", "headline_size_ratio", "contrast_headline",
    "contrast_cta", "edge_density", "jpeg_bpp", "colorfulness", "warnings",
    "spend", "impressions", "clicks", "leads", "deals", "revenue",
]


# ---------- цвет и контраст ----------

def hex_rgb(value):
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def _linear(c):
    c = np.asarray(c, dtype=float) / 255
    return np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def luminance(rgb):
    r, g, b = _linear(rgb)
    return float(0.2126 * r + 0.7152 * g + 0.0722 * b)


def contrast_lum(l1, l2):
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def region_luminance_range(img, box):
    x, y, w, h = [int(v) for v in box]
    crop = np.asarray(img.convert("RGB").crop((x, y, x + max(w, 1), y + max(h, 1))), dtype=float)
    lin = _linear(crop)
    lum = 0.2126 * lin[..., 0] + 0.7152 * lin[..., 1] + 0.0722 * lin[..., 2]
    return float(np.percentile(lum, 5)), float(np.percentile(lum, 95))


def worst_contrast(rgb, lum_range):
    l = luminance(rgb)
    return min(contrast_lum(l, lum_range[0]), contrast_lum(l, lum_range[1]))


def pick_text_color(preferred, lum_range, min_contrast):
    """Свой цвет, если читается; иначе белый/чёрный; если и они не читаются — нужна подложка."""
    options = [preferred, (255, 255, 255), (17, 17, 17)]
    scored = [(worst_contrast(c, lum_range), c) for c in options]
    if scored[0][0] >= min_contrast:
        return preferred, scored[0][0], False
    best = max(scored)
    return best[1], best[0], best[0] < min_contrast


# ---------- шрифты и текст ----------

def _font_path(cfg_path, candidates):
    for p in [cfg_path] + candidates:
        if p and Path(p).exists():
            return p
    return None


def _font(path, size):
    return ImageFont.truetype(path, size) if path else ImageFont.load_default()


def wrap(draw, text, font, width):
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=font) <= width or not line:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def fit_text(draw, text, font_path, box, max_size, min_size, spacing=1.15):
    """Подбирает максимальный кегль, при котором текст помещается в блок."""
    _, _, w, h = box
    size = max_size
    while size >= min_size:
        font = _font(font_path, size)
        lines = wrap(draw, text, font, w)
        line_h = size * spacing
        widest = max((draw.textlength(l, font=font) for l in lines), default=0)
        if len(lines) * line_h <= h and widest <= w:
            return lines, font, size
        size -= 2
    font = _font(font_path, min_size)
    return wrap(draw, text, font, w), font, min_size


# ---------- компоновки ----------

def _stack(x, top, w, bottom, H, land, align="left", cta_w=None):
    """Колонка текста: заголовок → подзаголовок → кнопка снизу, без наложений."""
    cta_h = round(H * (0.12 if land else 0.07))
    gap = round(H * (0.03 if land else 0.02))
    cta_y = bottom - cta_h
    room = max(cta_y - gap - top, 1)
    head_h = round(room * 0.64)
    cta_w = cta_w or round(w * (0.9 if land else 0.6))
    cta_x = x if align == "left" else x + (w - cta_w) // 2
    return {"headline": (x, top, w, head_h),
            "sub": (x, top + head_h + gap // 2, w, room - head_h - gap // 2),
            "cta": (cta_x, cta_y, cta_w, cta_h), "align": align}


def layout_boxes(name, W, H):
    """Блоки (x, y, w, h) для изображения и текстов + целевая точка фокуса продукта."""
    m = round(0.06 * min(W, H))
    land = W > H * 1.2
    logo_h = round((0.08 if land else 0.04) * H)
    cw = W - 2 * m

    if name in ("thirds", "golden", "grid") and land:
        # Горизонтальный формат: картинка справа, колонка текста слева.
        if name == "thirds":
            text_w, focal = W // 3, (W * 2 / 3, H / 3)
        elif name == "golden":
            text_w = W - round(W / PHI)
            focal = (text_w + (W - text_w) / PHI ** 2, H / PHI ** 2)
        else:
            g = round(0.02 * W)
            col = (cw - 11 * g) / 12
            text_w = round(m + 6 * col + 5 * g + g)
            focal = (text_w + (W - text_w) / 2, H / 2)
        image = (text_w, 0, W - text_w, H) if name != "grid" else (text_w, m, W - text_w - m, H - 2 * m)
        return {"image": image, "image_mode": "cover", "focal": focal,
                "logo": (m, m, text_w - 2 * m, logo_h),
                **_stack(m, m + logo_h + m // 2, text_w - 2 * m, H - m, H, land)}

    if name in ("thirds", "golden"):
        img_h = round(H * 2 / 3) if name == "thirds" else round(H / PHI)
        focal = (W * 2 / 3, H / 3) if name == "thirds" else (W / PHI, img_h / PHI)
        return {"image": (0, 0, W, img_h), "image_mode": "cover", "focal": focal,
                "logo": (m, m, cw // 2, logo_h),
                **_stack(m, img_h + m // 2, cw, H - m, H, land)}

    if name == "grid":
        g = round(0.02 * W)
        col = (cw - 11 * g) / 12
        img_h = round((H - 2 * m) * (7 if H / W > 1.2 else 6) / 12)
        text_w = round(10 * col + 9 * g)
        return {"image": (m, m, cw, img_h), "image_mode": "cover", "focal": (W / 2, m + img_h / 2),
                "logo": (round(m + 8 * (col + g)), m + g, round(4 * col + 3 * g), logo_h),
                **_stack(m, m + img_h + 2 * g, text_w, H - m, H, land, cta_w=round(5 * col + 4 * g))}

    if name == "center":
        y_img = m + logo_h + m // 2
        img_h = round(H * (0.32 if land else 0.48))
        boxes = _stack(m, y_img + img_h + m // 2, cw, H - m, H, land, align="center",
                       cta_w=round(W * (0.3 if land else 0.55)))
        return {"image": (m, y_img, cw, img_h), "image_mode": "contain", "focal": (W / 2, y_img + img_h / 2),
                "logo": (m, m, cw, logo_h), **boxes}

    if name == "zpattern":
        # Z-путь взгляда: бренд ↖ → заголовок вверху → продукт по диагонали → кнопка ↘.
        head_top = m + logo_h + m // 3
        head_h = round(H * (0.26 if land else 0.18))
        y_img = head_top + head_h + m // 3
        cta_h = round(H * (0.12 if land else 0.075))
        img_h = H - m - cta_h - m // 2 - y_img
        return {"image": (m, y_img, cw, img_h), "image_mode": "contain", "focal": (W / 2, y_img + img_h / 2),
                "logo": (m, m, cw // 2, logo_h),
                "headline": (m, head_top, cw, head_h),
                "sub": (m, H - m - cta_h, round(cw * 0.55), cta_h),
                "cta": (m + round(cw * 0.6), H - m - cta_h, round(cw * 0.4), cta_h),
                "align": "left"}

    raise ValueError(f"неизвестная компоновка: {name}")


# ---------- изображение ----------

def _placeholder(size, accent):
    w, h = size
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    r = min(w, h) * 0.32
    cx, cy = w / 2, h / 2
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=accent + (255,))
    return img


def place_image(canvas, src, box, mode, focal_target, focal_src=(0.5, 0.5)):
    bx, by, bw, bh = [int(v) for v in box]
    iw, ih = src.size
    if mode == "cover":
        scale = max(bw / iw, bh / ih)
    else:
        scale = min(bw / iw, bh / ih)
    nw, nh = max(1, math.ceil(iw * scale)), max(1, math.ceil(ih * scale))
    im = src.resize((nw, nh), Image.LANCZOS)
    tx, ty = focal_target
    if mode == "cover":
        left = min(max(focal_src[0] * nw - (tx - bx), 0), nw - bw)
        top = min(max(focal_src[1] * nh - (ty - by), 0), nh - bh)
        im = im.crop((int(left), int(top), int(left) + bw, int(top) + bh))
        pos = (bx, by)
    else:
        x = int(min(max(tx - nw / 2, bx), bx + bw - nw))
        y = int(min(max(ty - nh / 2, by), by + bh - nh))
        pos = (x, y)
    canvas.alpha_composite(im, dest=pos)
    return (pos[0], pos[1], im.size[0], im.size[1])


# ---------- метрики готового баннера ----------

def edge_density(img):
    g = np.asarray(img.convert("L"), dtype=float)
    gx = np.abs(np.diff(g, axis=1))[:-1, :]
    gy = np.abs(np.diff(g, axis=0))[:, :-1]
    return float(((gx + gy) > 40).mean())


def jpeg_bpp(img):
    buf = io.BytesIO()
    img.convert("RGB").save(buf, "JPEG", quality=75)
    return buf.tell() * 8 / (img.size[0] * img.size[1])


def colorfulness(img):
    """Hasler & Süsstrunk (2003)."""
    a = np.asarray(img.convert("RGB"), dtype=float)
    rg = a[..., 0] - a[..., 1]
    yb = 0.5 * (a[..., 0] + a[..., 1]) - a[..., 2]
    return float(np.hypot(rg.std(), yb.std()) + 0.3 * np.hypot(rg.mean(), yb.mean()))


def text_density(share):
    return "low" if share < 0.12 else "mid" if share < 0.25 else "high"


# ---------- рендер ----------

def render(spec, cfg, image=None):
    d = cfg["design"]
    W, H = d["sizes"][spec["size"]]
    colors = spec.get("colors", {})
    bg = hex_rgb(colors.get("bg", "#111111"))
    text_rgb = hex_rgb(colors.get("text", "#FFFFFF"))
    accent = hex_rgb(colors.get("accent", "#C8FF00"))
    bold = _font_path(d.get("font_bold"), _BOLD)
    regular = _font_path(d.get("font_regular"), _REGULAR)
    min_c = d["min_contrast"]

    canvas = Image.new("RGBA", (W, H), bg + (255,))
    boxes = layout_boxes(spec["layout"], W, H)
    src = image if image is not None else _placeholder((800, 800), accent)
    mode = spec.get("image_fit") or boxes["image_mode"]
    img_rect = place_image(canvas, src.convert("RGBA"), boxes["image"], mode,
                           boxes["focal"], tuple(spec.get("focal_src", (0.5, 0.5))))
    draw = ImageDraw.Draw(canvas)

    text_area = 0.0
    measures = {}
    warnings = []

    def put_text(key, text, font_path, max_ratio, min_ratio, color=None):
        nonlocal text_area
        if not text:
            return
        box = boxes[key]
        lines, font, size = fit_text(draw, text, font_path, box, round(H * max_ratio), round(H * min_ratio))
        line_h = size * 1.15
        block_h = len(lines) * line_h
        widths = [draw.textlength(l, font=font) for l in lines]
        bw = max(widths) if widths else 0
        x0 = box[0] if boxes["align"] == "left" else box[0] + (box[2] - bw) / 2
        rect = (x0, box[1], bw, block_h)
        lum = region_luminance_range(canvas, rect)
        rgb, c, need_scrim = pick_text_color(color or text_rgb, lum, min_c)
        if need_scrim:
            pad = size * 0.4
            scrim = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
            ImageDraw.Draw(scrim).rounded_rectangle(
                (x0 - pad, box[1] - pad, x0 + bw + pad, box[1] + block_h + pad),
                radius=int(pad), fill=bg + (225,))
            canvas.alpha_composite(scrim)
            lum = region_luminance_range(canvas, rect)
            rgb, c, _ = pick_text_color(color or text_rgb, lum, min_c)
            warnings.append(f"{key}: добавлена подложка для читаемости")
        for i, line in enumerate(lines):
            lx = box[0] if boxes["align"] == "left" else box[0] + (box[2] - widths[i]) / 2
            draw.text((lx, box[1] + i * line_h), line, font=font, fill=rgb)
        text_area += bw * block_h
        measures[key] = {"size": size, "contrast": c}

    k = 1.35 if W > H * 1.2 else 1.0  # в горизонтальном формате высота мала — кегль крупнее
    put_text("logo", spec.get("logo_text"), bold, 0.035 * k, 0.022 * k)
    put_text("headline", spec["headline"], bold, 0.085 * k, 0.035 * k)
    put_text("sub", spec.get("sub"), regular, 0.036 * k, 0.026 * k)

    # Кнопка CTA: акцентный цвет, текст чёрный/белый по контрасту.
    cta = spec.get("cta")
    if cta:
        bx, by, bw_, bh_ = boxes["cta"]
        font_size = round(bh_ * 0.46)
        font = _font(bold, font_size)
        tw = draw.textlength(cta, font=font)
        while tw > bw_ * 0.86 and font_size > 12:
            font_size -= 2
            font = _font(bold, font_size)
            tw = draw.textlength(cta, font=font)
        btn_w = min(bw_, tw + bh_ * 0.9)
        x0 = bx if boxes["align"] == "left" else bx + (bw_ - btn_w) / 2
        draw.rounded_rectangle((x0, by, x0 + btn_w, by + bh_), radius=int(bh_ / 2), fill=accent)
        al = luminance(accent)
        label = (17, 17, 17) if contrast_lum(al, luminance((17, 17, 17))) >= contrast_lum(al, 1.0) else (255, 255, 255)
        c = contrast_lum(al, luminance(label))
        draw.text((x0 + btn_w / 2, by + bh_ / 2), cta, font=font, fill=label, anchor="mm")
        text_area += btn_w * bh_
        measures["cta"] = {"size": font_size, "contrast": c}

    canvas_rgb = canvas.convert("RGB")
    share = text_area / (W * H)
    image_share = img_rect[2] * img_rect[3] / (W * H)
    head = measures.get("headline", {})
    head_ratio = head.get("size", 0) / H
    if head_ratio < 0.04:
        warnings.append("заголовок мелкий для мобильного экрана (<4% высоты)")
    if share > 0.3:
        warnings.append("текст занимает >30% площади — проверьте, не перегружен ли баннер")
    if head.get("contrast", 99) < min_c:
        warnings.append(f"контраст заголовка {head.get('contrast', 0):.1f} < {min_c}")
    features = {
        "text_area_share": round(share, 3),
        "image_area_share": round(image_share, 3),
        "headline_size_ratio": round(head_ratio, 3),
        "contrast_headline": round(head.get("contrast", 0), 2),
        "contrast_cta": round(measures.get("cta", {}).get("contrast", 0), 2),
        "edge_density": round(edge_density(canvas_rgb), 3),
        "jpeg_bpp": round(jpeg_bpp(canvas_rgb), 3),
        "colorfulness": round(colorfulness(canvas_rgb), 1),
        "text_density": text_density(share),
        "warnings": "; ".join(warnings),
    }
    return canvas_rgb, features


# ---------- тексты без ИИ ----------

_TEMPLATES = [
    ("speed", "{benefit} — за {time}"),
    ("benefit", "{benefit}"),
    ("pain", "{pain}? {solution}"),
    ("audience", "{audience}: {benefit}"),
    ("proof", "{proof}"),
    ("offer", "{offer}"),
    ("contrast", "{alternative} → {benefit}"),
]


def copy_variants(brief):
    """Заголовки по шаблонам из полей брифа. Угол (angle) записывается для обучения."""
    out = [{"headline": h["text"], "angle": h.get("angle", "custom")} if isinstance(h, dict)
           else {"headline": h, "angle": "custom"} for h in brief.get("headlines", [])]
    if out:
        return out
    for angle, tpl in _TEMPLATES:
        try:
            text = tpl.format(**{k: v for k, v in brief.items() if isinstance(v, str)})
        except KeyError:
            continue
        out.append({"headline": text[0].upper() + text[1:], "angle": angle})
    if not out:
        raise ValueError("в брифе нет ни headlines, ни полей benefit/pain/offer/… для шаблонов")
    return out


# ---------- выбор вариантов по прошлым результатам ----------

def _arms(creatives, tag, values, result):
    arms = {v: (0.0, 0.0) for v in values}
    for r in creatives:
        v = r.get(tag)
        if v is None or (values and str(v) not in arms):
            continue
        s, n = arms.get(str(v), (0.0, 0.0))
        arms[str(v)] = (s + num(r, result), n + num(r, "impressions"))
    return arms


def plan_banners(brief, creatives, cfg, n=None, seed_sizes=None):
    """Какие баннеры собрать: компоновки и углы выбирает бандит по вашей истории."""
    d = cfg["design"]
    res = cfg["creatives"]["result"]
    n = n or brief.get("n", 6)
    sizes = seed_sizes or brief.get("sizes", ["square"])
    layouts = brief.get("layouts") or d["layouts"]
    variants = copy_variants(brief)
    angles = sorted({v["angle"] for v in variants})

    tot_imp = sum(num(r, "impressions") for r in creatives)
    base = sum(num(r, res) for r in creatives) / tot_imp if tot_imp else 0.01
    layout_arms = _arms(creatives, "layout", layouts, res)
    angle_arms = _arms(creatives, "angle", angles, res)

    specs = []
    used = set()
    for i in range(n):
        layout = thompson_pick(layout_arms, base, cfg["prior_events"])[0]
        angle = thompson_pick(angle_arms, base, cfg["prior_events"])[0]
        options = [v for v in variants if v["angle"] == angle] or variants
        variant = options[i % len(options)]
        key = (layout, variant["headline"])
        if key in used:  # не дублировать одинаковые пары
            layout = layouts[i % len(layouts)]
        used.add((layout, variant["headline"]))
        for size in sizes:
            specs.append({
                "layout": layout, "size": size, "angle": variant["angle"],
                "headline": variant["headline"], "sub": brief.get("sub"),
                "cta": brief.get("cta"), "logo_text": brief.get("logo_text"),
                "colors": brief.get("colors", {}), "focal_src": brief.get("focal", [0.5, 0.5]),
                "offer": brief.get("offer_tag") or brief.get("offer"),
                "persona": brief.get("persona"), "hook": brief.get("hook"),
                "image_fit": brief.get("image_fit"),
            })
    return specs


def contact_sheet(paths, out_path, thumb=360):
    imgs = [Image.open(p) for p in paths]
    if not imgs:
        return None
    cols = min(4, len(imgs))
    rows = math.ceil(len(imgs) / cols)
    cell_h = max(round(thumb * im.size[1] / im.size[0]) for im in imgs)
    sheet = Image.new("RGB", (cols * (thumb + 16) + 16, rows * (cell_h + 16) + 16), (240, 240, 240))
    for i, im in enumerate(imgs):
        t = im.copy()
        t.thumbnail((thumb, cell_h))
        sheet.paste(t, (16 + (i % cols) * (thumb + 16), 16 + (i // cols) * (cell_h + 16)))
    sheet.save(out_path)
    return out_path


def build(brief, creatives, cfg, out_dir, base_dir=".", register_to=None):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    image = None
    if brief.get("image"):
        p = Path(base_dir) / brief["image"]
        if p.exists():
            image = Image.open(p)
    specs = plan_banners(brief, creatives, cfg)
    stamp = date.today().strftime("%y%m%d")
    rows, files = [], []
    for i, spec in enumerate(specs):
        img, feats = render(spec, cfg, image)
        cid = f"B{stamp}-{i + 1:02d}-{spec['layout']}-{spec['size']}"
        path = out / f"{cid}.png"
        img.save(path)
        files.append(path)
        rows.append({"creative_id": cid, "status": "planned", "format": "static",
                     "file": str(path), "channel": brief.get("channel"), **spec, **feats})
    write_csv(out / "manifest.csv", rows, MANIFEST_FIELDS)
    contact_sheet(files, out / "overview.png")
    if register_to:
        append_csv(register_to, rows, MANIFEST_FIELDS)
    return rows
