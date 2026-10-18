"""Слой 8. Попадание в СМИ (earned media): форма оценки идеи и генератор идей по шаблонам.

Основа формы — «новостные ценности» (Galtung & Ruge 1965; Harcup & O'Neill 2016/2017)
и исследования распространения (Berger & Milkman 2012: контент с сильными, возбуждающими
эмоциями — восторг, гнев, тревога — расшаривают чаще). Веса — стартовые допущения:
система уточняет их по вашим результатам (охваты, публикации, заявки).
"""

# ключ: (вопрос, вес)
CRITERIA = {
    "first_or_record": ("Это впервые / рекорд / «самый» в своём классе?", 3),
    "surprise": ("Результат неожиданный, противоречит привычным ожиданиям?", 3),
    "conflict": ("Есть противостояние: человек vs машина, малый vs крупный, старое vs новое?", 2),
    "exclusive_data": ("Есть данные/факты, которых нет ни у кого (исследование, замер, выгрузка)?", 3),
    "magnitude": ("Это касается многих людей или больших денег?", 2),
    "relevance": ("Это важно аудитории конкретного СМИ прямо сейчас?", 2),
    "timeliness": ("Привязано к событию/тренду этой недели (ньюсджекинг)?", 2),
    "visual": ("Есть зрелищная картинка/видео, которое СМИ могут показать?", 2),
    "emotion": ("Вызывает сильную эмоцию: восторг, смех, возмущение, тревогу?", 2),
    "celebrity_elite": ("Вовлечены известные люди, бренды или институты?", 1),
    "practical_value": ("Читатель получит пользу (инструмент, вывод, совет)?", 1),
    "story": ("Есть герой и сюжет, который пересказывается в одном предложении?", 2),
    "brand_link": ("Без бренда история не существует (бренд — причина, а не наклейка)?", 3),
    "proof": ("Можно показать доказательство: замер, видео, независимый судья, открытые данные?", 2),
}

RED_FLAGS = {
    "legal_risk": "Есть юридический риск (реклама без маркировки, нарушение прав, персональные данные)",
    "misleading": "История держится на преувеличении или недоговорённости",
    "safety": "Есть риск для здоровья/безопасности людей",
    "offends_group": "Может задеть группу людей так, что история станет о скандале",
    "cannot_deliver": "Нет уверенности, что получится выполнить обещанное публично",
}

PATTERNS = [
    {"key": "human_vs_machine", "name": "Человек против машины",
     "template": "Публичное соревнование: {capability} против {human_pro} в задаче «{task}». "
                 "Независимый судья, открытый счёт, видео.",
     "needs": ["capability", "human_pro", "task"],
     "values": ["conflict", "surprise", "visual", "story", "proof"],
     "example": "OpenAI: бот обыграл профи Dendi в Dota 2 на The International 2017"},
    {"key": "first_or_record", "name": "Первые / рекорд",
     "template": "Первыми на рынке «{market}» сделали {feat} — с замером и датой.",
     "needs": ["market", "feat"],
     "values": ["first_or_record", "surprise", "proof"]},
    {"key": "exclusive_data", "name": "Данные, которых нет ни у кого",
     "template": "Исследование: проанализировали {data_asset} и выяснили {finding}. Методика и выборка открыты.",
     "needs": ["data_asset", "finding"],
     "values": ["exclusive_data", "magnitude", "practical_value", "relevance"]},
    {"key": "david_vs_goliath", "name": "Малый против крупного",
     "template": "Сделали {result} за {small_budget} — то, на что {big_rival} тратит {big_budget}. Сравнение рядом.",
     "needs": ["result", "small_budget", "big_rival", "big_budget"],
     "values": ["conflict", "surprise", "story", "magnitude"]},
    {"key": "radical_transparency", "name": "Радикальная прозрачность",
     "template": "Публикуем то, что обычно скрывают: {secret}. С цифрами и выводами.",
     "needs": ["secret"],
     "values": ["exclusive_data", "surprise", "practical_value"]},
    {"key": "open_challenge", "name": "Открытый вызов",
     "template": "Принимаем вызов: {challenge}. Если не справимся — {stake}.",
     "needs": ["challenge", "stake"],
     "values": ["conflict", "story", "emotion", "proof"]},
    {"key": "newsjacking", "name": "Ньюсджекинг за 24 часа",
     "template": "Реакция на «{event}»: за сутки сделали {response} — в тему и с пользой.",
     "needs": ["event", "response"],
     "values": ["timeliness", "relevance", "emotion"]},
    {"key": "spectacle_demo", "name": "Зрелищное демо продукта",
     "template": "Показываем {product} в экстремальных условиях: {extreme}. Одно видео без монтажа.",
     "needs": ["product", "extreme"],
     "values": ["visual", "surprise", "proof", "emotion"],
     "example": "Blendtec «Will It Blend?»"},
    {"key": "moral_stance", "name": "Позиция против нормы рынка",
     "template": "Отказываемся от {industry_norm}, потому что {reason}. Что это меняет для клиентов.",
     "needs": ["industry_norm", "reason"],
     "values": ["conflict", "surprise", "emotion", "story"],
     "example": "Patagonia «Don't Buy This Jacket»"},
]


def score_idea(idea):
    """idea: {"title":…, "answers": {критерий: 0|1|2}, "red_flags": {флаг: true/false}}"""
    answers = idea.get("answers", {})
    total = sum(w * 2 for _, w in CRITERIA.values())
    got = sum(w * min(max(int(answers.get(k, 0)), 0), 2) for k, (_, w) in CRITERIA.items())
    score = round(100 * got / total)
    flags = [RED_FLAGS[k] for k, v in idea.get("red_flags", {}).items() if v and k in RED_FLAGS]
    weak = [CRITERIA[k][0] for k in ("brand_link", "proof", "story") if int(answers.get(k, 0)) == 0]
    if flags:
        verdict = "не запускать без переделки: есть красные флаги"
    elif int(answers.get("brand_link", 0)) == 0:
        verdict = "СМИ могут написать, но не о вас: усильте связь с брендом"
    elif score >= 60:
        verdict = "сильная идея — готовить питч и доказательства"
    elif score >= 40:
        verdict = "средняя — усилить 1–2 критерия с наибольшим весом"
    else:
        verdict = "слабая для СМИ — годится для своих каналов"
    gaps = sorted(((w, q) for k, (q, w) in CRITERIA.items() if int(answers.get(k, 0)) < 2), reverse=True)[:4]
    return {"score": score, "verdict": verdict, "red_flags": flags, "weak_core": weak,
            "improve_first": [q for _, q in gaps]}


def similar_cases(idea, cases, top=5):
    values = {k for k, v in idea.get("answers", {}).items() if int(v) >= 2}
    ranked = []
    for c in cases:
        nv = set(c.get("news_values", []))
        if not nv:
            continue
        overlap = len(values & nv)
        if overlap:
            ranked.append((overlap, c))
    ranked.sort(key=lambda x: x[0], reverse=True)
    return [c for _, c in ranked[:top]]


def generate_ideas(brief, cases):
    """brief: поля бренда (capability, market, data_asset, …). Шаблон срабатывает, если поля есть."""
    ideas = []
    for p in PATTERNS:
        missing = [n for n in p["needs"] if not brief.get(n)]
        examples = [c for c in cases if c.get("pattern") and p["key"] in (c.get("news_values") or [])
                    or (c.get("pattern") or "").lower() == p["name"].lower()][:3]
        idea = {"pattern": p["name"], "values": p["values"], "missing_fields": missing,
                "example": p.get("example"), "cases": [
                    {"title": c.get("title"), "brand": c.get("brand"), "source_url": c.get("source_url")}
                    for c in examples]}
        if not missing:
            idea["idea"] = p["template"].format(**brief)
            idea["prefilled_answers"] = {v: 2 for v in p["values"]}
        ideas.append(idea)
    ideas.sort(key=lambda i: (len(i["missing_fields"]), -len(i["values"])))
    return ideas


def render_score(idea, res, cases):
    L = [f"# Идея для СМИ: {idea.get('title', '')}", "", f"**Оценка: {res['score']}/100 — {res['verdict']}**", ""]
    if res["red_flags"]:
        L += ["## Красные флаги"] + [f"- {f}" for f in res["red_flags"]] + [""]
    if res["weak_core"]:
        L += ["## Слабое ядро"] + [f"- {q}" for q in res["weak_core"]] + [""]
    L += ["## Что усилить в первую очередь"] + [f"- {q}" for q in res["improve_first"]] + [""]
    if cases:
        L += ["## Похожие кейсы"] + [f"- {c.get('title')} ({c.get('brand')}, {c.get('year')}): "
                                      f"{c.get('why_media_covered')} — {c.get('source_url')}" for c in cases]
    return "\n".join(L)


def render_ideas(brief, ideas):
    L = [f"# Идеи для СМИ: {brief.get('brand', '')}", ""]
    for i in ideas:
        L.append(f"## {i['pattern']}")
        if i.get("idea"):
            L.append(i["idea"])
        else:
            L.append(f"Заполните в брифе: {', '.join(i['missing_fields'])}")
        if i.get("example"):
            L.append(f"_Пример: {i['example']}_")
        for c in i["cases"]:
            L.append(f"- кейс: {c['title']} ({c['brand']}) — {c['source_url']}")
        L.append("")
    L.append("Оценить идею: заполните форму (templates/pr_idea.json) и запустите `moneyball pr score <файл>`.")
    return "\n".join(L)
