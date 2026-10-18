"""Слой 8. Попадание в СМИ (earned media): форма оценки идеи, шаблоны идей, журнал прогнозов.

Основа формы:
  - новостные ценности: чем больше факторов, тем выше шанс стать новостью (Galtung & Ruge 1965;
    Harcup & O'Neill 2016/2017: эксклюзив, конфликт, сюрприз, аудиовизуальность, шерабельность) [СИЛЬНО];
  - шеринг: эмоции высокой активации и польза (Berger & Milkman 2012: гнев +34%, awe +30%,
    польза +30%, интерес +25%, тревога +21%, сюрприз +14%, грусть −16% на +1 SD) [СИЛЬНО];
  - чего ждут журналисты: релевантность, доступ к спикеру, свои данные, фото (Muck Rack 2026, Cision 2025) [ВЕНДОР];
  - паттерны и анти-паттерны 45 кейсов (knowledge/cases/earned_media.json).
Веса — экспертная сборка, а не регрессия [ДОПУЩЕНИЕ]. Их калибрует журнал прогнозов (data/pr_log.csv).
"""

from .io import num

# Блоки и критерии: ключ → (вопрос, вес). Оценка критерия: 0 / 0.5 / 1.
BLOCKS = {
    "A. Новостная ценность": {
        "A1_surprise": ("Нарушает ожидание категории? Можно написать «впервые», «самый», «вопреки»?", 10),
        "A2_exclusive": ("Что журналист получит только от нас: данные, доступ, спикера, первый показ?", 8),
        "A3_visual": ("Одна картинка объясняет всё? Понятен ли кадр без подписи?", 6),
        "A4_conflict": ("Есть понятный «противник» (норма категории, лидер, несправедливость), а гнев — не на нас?", 6),
        "A5_timeliness": ("Почему именно сейчас: событие, сезон, идущая история?", 5),
        "A6_people": ("Есть лицо истории: эксперт, герой-клиент, «человек против машины», известный в нише?", 5),
    },
    "B. Шерабельность": {
        "B1_emotion": ("Вызывает эмоцию высокой активации: смех, восторг, азарт, праведное негодование против нормы?", 8),
        "B2_value": ("Полезно или «круто» переслать другу (практическая польза / социальная валюта)?", 6),
        "B3_participation": ("Может ли аудитория участвовать: найти, проголосовать, повторить?", 6),
    },
    "C. Связь с бизнесом": {
        "C1_product_hero": ("Продукт — герой истории: через неделю вспомнят, что продаём и чем лучше?", 10),
        "C2_right_to_play": ("Наша история подтверждает право на эту позицию? Готовы держать её под давлением?", 7),
        "C3_path_measure": ("Куда придёт человек после статьи и как измерим (брендовый поиск, регистрации, промокод)?", 5),
        "C4_capacity": ("Выдержим ли пик спроса ×10–×100 (сайт, производство, поддержка)?", 3),
    },
    "D. Исполнимость": {
        "D1_budget": ("Сработает ли малая версия? Есть бесплатные каналы усиления?", 5),
        "D2_control": ("Что если провалится публично или никто не заметит — есть план Б?", 5),
        "D3_second_wave": ("Какой будет следующая новость: реакция, итог, реванш, цифры через неделю?", 5),
    },
}
CRITERIA = {k: v for block in BLOCKS.values() for k, v in block.items()}

STOP_FLAGS = {
    "fabrication": "Ложь или фабрикация: фейковые данные, отзывы, документы",
    "tragedy": "Чужая трагедия, протест, война или катастрофа как фон для продукта (Pepsi)",
    "humiliation": "Унижение или сексуализация групп людей (Burger King Россия, BK UK 8 марта)",
    "polarizing": "Поляризующая тема без связи с миссией и без готовности держать позицию (Bud Light, ВкусВилл)",
    "safety": "Объект или действие можно принять за угрозу; риск для жизни и здоровья (Cartoon Network)",
    "unlimited": "Неограниченные или бессрочные обязательства, призы без лимитов (Domino's Россия)",
    "irreversible": "Механика требует необратимых действий от людей (татуировки и т.п.)",
    "customer_data": "Риск раскрыть данные клиентов, не проверен 152-ФЗ (Strava)",
    "platform_rules": "Нарушение правил площадки (Whopper Sacrifice)",
    "ru_compliance": "РФ: нет плана маркировки оплачиваемых элементов (erid, ЕРИР), не просчитан НДФЛ с призов, "
                     "сравнение с конкурентом не проверено юристом",
    "headline_number": "Ключевая цифра анонса не выдержит проверки через месяц или год",
}

PITCH_CHECKLIST = [
    "Новость в заголовке до 10 слов, питч до 200 слов (69% журналистов хотят короче 200 слов) [ВЕНДОР]",
    "5–15 конкретных авторов, писавших на тему за 3 месяца: 86% отклоняют нерелевантный питч [ВЕНДОР]",
    "Эксклюзив одному изданию или эмбарго; спикер готов к интервью в день выхода",
    "Свои данные с методикой и фото/видео высокого разрешения",
    "Индивидуальное письмо, до полудня; Q&A на неудобные вопросы и пост на случай провала",
]

MEASURE = [
    "Публикации в целевых СМИ: заголовок, упоминание продукта, ссылка (не AVE и не «охват»)",
    "Брендовый поиск (Wordstat / Google Trends), прямой трафик, регистрации — против контрольного периода",
    "Продажи по выделенному промокоду или странице",
]

PATTERNS = [
    {"key": "human_vs_machine", "nv": "human_vs_machine", "name": "Человек против машины", "small_biz": "в локальном масштабе",
     "template": "Публичное соревнование «{capability} vs {human_pro}». Задача: {task}. "
                 "Независимый судья, открытый счёт, видео.",
     "needs": ["capability", "human_pro", "task"],
     "example": "IBM Deep Blue, Watson в Jeopardy!, DeepMind AlphaGo, бот OpenAI против Dendi в Dota 2 (TI 2017)"},
    {"key": "first_or_record", "nv": "first_or_record", "name": "Первые / рекорд", "small_biz": "рекорд города или ниши",
     "template": "Первые на рынке ({market}): {feat}. С замером, датой и доказательствами.",
     "needs": ["market", "feat"], "example": "Red Bull Stratos, Tesla Roadster в космосе"},
    {"key": "spectacle_demo", "nv": "spectacle", "name": "Демо продукта как зрелище", "small_biz": "да",
     "template": "Демо на пределе ({product}): {extreme}. Одно видео без монтажа.",
     "needs": ["product", "extreme"], "example": "Blendtec «Will It Blend?», Volvo Epic Split"},
    {"key": "david_vs_goliath", "nv": "david_vs_goliath", "name": "Давид против Голиафа", "small_biz": "мягкий вызов лидеру",
     "template": "Результат: {result}. Наш бюджет: {small_budget}. У крупного игрока ({big_rival}): {big_budget}. "
                 "Сравнение рядом.",
     "needs": ["result", "small_budget", "big_rival", "big_budget"],
     "example": "Dollar Shave Club против Gillette ($4 500 → 12 000 регистраций за 48 часов)"},
    {"key": "exclusive_data", "nv": "exclusive_data", "name": "Данные, которых нет ни у кого", "small_biz": "да — лучший вариант",
     "template": "Исследование. Данные: {data_asset}. Вопрос: {finding}. Методика и выборка открыты.",
     "needs": ["data_asset", "finding"], "example": "Spotify Wrapped, исследования Airbnb, OkCupid OkTrends, СберИндекс"},
    {"key": "moral_stance", "nv": "moral_stance", "name": "Позиция против собственной выгоды", "small_biz": "если есть право на позицию",
     "template": "Отказ от нормы рынка: {industry_norm}. Причина: {reason}. Что это меняет для клиентов.",
     "needs": ["industry_norm", "reason"], "example": "Patagonia «Don't Buy This Jacket», Moldy Whopper"},
    {"key": "absurd_humor", "nv": "humor_absurd", "name": "Абсурдный юмор в скучной категории", "small_biz": "да",
     "template": "Абсурдный образ для {product}: {absurd_idea}.",
     "needs": ["product", "absurd_idea"], "example": "Liquid Death, сова Duolingo, Squatty Potty"},
    {"key": "newsjacking", "nv": "timeliness", "name": "Ньюсджекинг за 24 часа", "small_biz": "да, локально",
     "template": "Повод: {event}. Реакция за 24 часа: {response}.",
     "needs": ["event", "response"], "example": "Oreo во время блэкаута, «Ситимобил» и кот Виктор"},
    {"key": "honesty", "nv": "surprise", "name": "Честность и самоирония", "small_biz": "да",
     "template": "Публично признаём: {admission}. Что мы с этим сделали: {fix}.",
     "needs": ["admission", "fix"], "example": "KFC «FCK», Domino's Pizza Turnaround"},
    {"key": "radical_transparency", "nv": "exclusive_data", "name": "Радикальная прозрачность", "small_biz": "да",
     "template": "Публикуем то, что на рынке обычно скрывают: {secret}. С цифрами и выводами.",
     "needs": ["secret"], "example": "Открытые результаты «Додо Пиццы»"},
    {"key": "participation", "nv": "utility", "name": "Механика участия / обмен", "small_biz": "только с лимитами и налогами",
     "template": "Аудитория делает: {action}. Получает: {reward}. Лимит участников: {limit}.",
     "needs": ["action", "reward", "limit"],
     "example": "Whopper Detour; анти-пример — Domino's Россия «100 пицц за тату» без лимитов"},
]


def _val(answers, key):
    try:
        v = float(answers.get(key, 0))
    except (TypeError, ValueError):
        return 0.0
    return min(max(v, 0.0), 1.0)


def score_idea(idea):
    """idea: {"title":…, "answers": {критерий: 0|0.5|1}, "stop_flags": {флаг: true/false}}"""
    answers = idea.get("answers", {})
    blocks, total = {}, 0.0
    for name, crits in BLOCKS.items():
        got = sum(w * _val(answers, k) for k, (_, w) in crits.items())
        top = sum(w for _, w in crits.values())
        blocks[name] = {"score": round(got, 1), "max": top}
        total += got
    flags_in = idea.get("stop_flags") or idea.get("red_flags") or {}
    flags = [STOP_FLAGS[k] for k, v in flags_in.items() if v and k in STOP_FLAGS]
    news_values = sum(1 for k in BLOCKS["A. Новостная ценность"] if _val(answers, k) >= 0.5)
    score = round(total)
    if flags:
        verdict = "стоп: есть стоп-флаг — переделать или к юристу, независимо от баллов"
    elif news_values < 3:
        verdict = f"мало новостных ценностей ({news_values} из 6, нужно ≥3) — СМИ, скорее всего, не возьмут"
    elif _val(answers, "C1_product_hero") == 0:
        verdict = "напишут о событии, но не о вас: продукт не герой истории"
    elif score >= 70:
        verdict = "делать: готовить питч и доказательства"
    elif score >= 50:
        verdict = "доработать слабые блоки (обычно A2, A3 или C1)"
    else:
        verdict = "не делать в таком виде"
    weakest = sorted(((w * (1 - _val(answers, k)), q) for k, (q, w) in CRITERIA.items()), reverse=True)
    return {"score": score, "verdict": verdict, "blocks": blocks, "news_values": news_values,
            "stop_flags": flags, "improve_first": [q for loss, q in weakest[:4] if loss > 0]}


# Какие теги кейсов соответствуют критериям формы.
_CRIT_TO_NV = {"A1_surprise": ["surprise", "first_or_record"], "A2_exclusive": ["exclusive_data"],
               "A3_visual": ["visual", "spectacle"], "A4_conflict": ["conflict", "david_vs_goliath"],
               "A5_timeliness": ["timeliness"], "A6_people": ["celebrity", "human_vs_machine"],
               "B1_emotion": ["humor_absurd"], "B2_value": ["utility"]}


def _is_anti(c):
    return str(c.get("pattern", "")).lower().startswith("анти-паттерн")


def similar_cases(idea, cases, top=5, anti=False):
    want = {nv for k, tags in _CRIT_TO_NV.items() if _val(idea.get("answers", {}), k) >= 1 for nv in tags}
    ranked = []
    for c in cases:
        if not c.get("news_values") or _is_anti(c) != anti:
            continue
        overlap = len(want & set(c["news_values"]))
        if overlap:
            ranked.append((overlap + {"strong": 0.5, "medium": 0.3}.get(c.get("evidence"), 0), c))
    ranked.sort(key=lambda x: x[0], reverse=True)
    return [c for _, c in ranked[:top]]


def anti_patterns(cases):
    return [c for c in cases if _is_anti(c)]


def generate_ideas(brief, cases):
    """brief: поля бренда. Шаблон заполняется, если в брифе есть нужные поля."""
    ideas = []
    for p in PATTERNS:
        missing = [n for n in p["needs"] if not brief.get(n)]
        idea = {"pattern": p["name"], "key": p["key"], "nv": p["nv"], "small_biz": p["small_biz"],
                "missing_fields": missing, "example": p["example"]}
        if not missing:
            idea["idea"] = p["template"].format(**brief)
        ideas.append(idea)
    ideas.sort(key=lambda i: len(i["missing_fields"]))
    return ideas


def calibration(log_rows):
    """Журнал: прогноз (score) до запуска и факт после. Через 10+ запусков — видно, предсказывает ли форма."""
    done = [r for r in log_rows if r.get("score") is not None and r.get("publications") is not None]
    if len(done) < 5:
        return {"runs": len(done), "note": "нужно ≥5 запусков с фактом, чтобы проверять форму"}
    xs = [num(r, "score") for r in done]
    ys = [num(r, "publications") for r in done]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    vx = sum((x - mx) ** 2 for x in xs) ** 0.5
    vy = sum((y - my) ** 2 for y in ys) ** 0.5
    r = cov / (vx * vy) if vx and vy else 0.0
    return {"runs": len(done), "corr_score_publications": round(r, 2),
            "note": "Корреляция < 0.3 на 10+ запусках — веса формы надо пересматривать."}


def render_score(idea, res, cases, risks=()):
    L = [f"# Идея для СМИ: {idea.get('title', '')}", "",
         f"**{res['score']}/100 — {res['verdict']}**", "",
         f"Новостных ценностей: {res['news_values']} из 6", ""]
    for name, b in res["blocks"].items():
        L.append(f"- {name}: {b['score']:.0f} из {b['max']}")
    if res["stop_flags"]:
        L += ["", "## Стоп-флаги"] + [f"- {f}" for f in res["stop_flags"]]
    if res["improve_first"]:
        L += ["", "## Что усилить в первую очередь"] + [f"- {q}" for q in res["improve_first"]]
    if cases:
        L += ["", "## Похожие кейсы"]
        for c in cases:
            L.append(f"- {c.get('title')} ({c.get('brand')}, {c.get('year')}) [{c.get('evidence')}]: "
                     f"{c.get('why_media_covered')} — {c.get('source_url')}")
    if risks:
        L += ["", "## Анти-примеры с похожими приёмами — проверьте, не повторяете ли ошибку"]
        for c in risks:
            L.append(f"- {c.get('brand')} ({c.get('year')}): {c.get('risks_or_backlash')} — {c.get('source_url')}")
    L += ["", "## Перед отправкой журналистам"] + [f"- {x}" for x in PITCH_CHECKLIST]
    L += ["", "## Как измерить"] + [f"- {x}" for x in MEASURE]
    L += ["", "Запишите прогноз и итог в data/pr_log.csv — так система проверит, работает ли форма."]
    return "\n".join(L)


def render_ideas(brief, ideas, cases=()):
    L = [f"# Идеи для СМИ: {brief.get('brand', '')}", ""]
    for i in ideas:
        L.append(f"## {i['pattern']} (для малого бизнеса: {i['small_biz']})")
        L.append(i["idea"] if i.get("idea") else f"Заполните в брифе: {', '.join(i['missing_fields'])}")
        L.append(f"_Примеры: {i['example']}_")
        related = sorted((c for c in cases if i["nv"] in (c.get("news_values") or [])
                          and not str(c.get("pattern", "")).lower().startswith("анти-паттерн")),
                         key=lambda c: {"strong": 0, "medium": 1}.get(c.get("evidence"), 2))[:3]
        for c in related:
            L.append(f"- кейс: {c.get('title')} ({c.get('brand')}) — {c.get('source_url')}")
        L.append("")
    bad = anti_patterns(cases)[:6]
    if bad:
        L.append("## Чего не делать (анти-примеры)")
        for c in bad:
            L.append(f"- {c.get('brand')}: {c.get('risks_or_backlash')} — {c.get('source_url')}")
        L.append("")
    L.append("Оценить идею: заполните форму (templates/pr_idea.json) и запустите `moneyball pr score <файл>`.")
    return "\n".join(L)
