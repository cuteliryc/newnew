"""ИИ-агенты — необязательное дополнение к движку.

Агент — это файл agents/<имя>.md: шапка с настройками и текст инструкции.
Движок сам собирает для агента контекст (свежие расчёты, базу знаний, бриф),
вызывает GPT (по умолчанию через Codex CLI и подписку ChatGPT), сохраняет ответ
и забирает из него гипотезы в data/hypotheses.csv.

Новый агент = новый .md-файл по образцу templates/agent.md. Код менять не нужно.
"""

import json
import re
from datetime import date, datetime
from pathlib import Path

from .io import append_csv
from .llm import complete

HYPOTHESIS_FIELDS = ["id", "created", "source_agent", "layer", "hypothesis", "variable", "source",
                     "evidence", "expected_lift", "value_at_stake", "cost_hours", "status"]

PREAMBLE = """Ты — агент аналитической системы маркетинга. Пиши по-русски, коротко и конкретно.
Жёсткие правила:
1. Опирайся только на данные из контекста. Не выдумывай цифры, кейсы и источники.
2. Помечай тип каждого утверждения: [ФАКТ] — есть в данных; [ВЫВОД] — следует из данных;
   [ДОПУЩЕНИЕ] — предположение; [ИССЛЕДОВАНИЕ] — из базы знаний (с меткой силы); [РЕКОМЕНДАЦИЯ].
3. Если данных мало для вывода — так и скажи и предложи, какой тест или данные это решат.
4. Решения о деньгах — через предельную прибыль, а не CTR или средний ROAS.
5. В конце ответа дай блок ```json {"hypotheses": [...]} ``` (можно пустой список). Поля гипотезы:
   layer (budget|creative|copy|offer|channel|audience|landing|funnel|pr|other), hypothesis,
   variable, evidence (strong|medium|weak|none), expected_lift (доля, напр. 0.15),
   value_at_stake (деньги в месяц, которые затрагивает), cost_hours.
"""


def parse_agent(path):
    text = Path(path).read_text(encoding="utf-8")
    meta, body = {}, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.S)
    if m:
        body = m.group(2)
        for line in m.group(1).splitlines():
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            value = value.strip()
            if value.startswith("[") and value.endswith("]"):
                value = [v.strip().strip("'\"") for v in value[1:-1].split(",") if v.strip()]
            elif value.lower() in ("true", "false"):
                value = value.lower() == "true"
            meta[key.strip()] = value
    meta.setdefault("name", Path(path).stem)
    meta.setdefault("inputs", [])
    return meta, body.strip()


def list_agents(agents_dir):
    return [parse_agent(p)[0] for p in sorted(Path(agents_dir).glob("*.md"))]


def _trim(text, limit):
    return text if len(text) <= limit else text[:limit] + "\n…[обрезано]"


def build_context(meta, engine_dir, knowledge_dir, extra=None, limit=60000):
    """inputs агента: имена разделов engine.json (funnel, budget, …) или файлов knowledge/*."""
    parts = []
    engine_file = Path(engine_dir) / "engine.json"
    engine = json.loads(engine_file.read_text(encoding="utf-8")) if engine_file.exists() else {}
    per_input = max(limit // max(len(meta["inputs"]) + 1, 1), 2000)
    for name in meta["inputs"]:
        if name in engine:
            parts.append(f"## Расчёт движка: {name}\n```json\n"
                         f"{_trim(json.dumps(engine[name], ensure_ascii=False, indent=1, default=str), per_input)}\n```")
            continue
        kp = Path(knowledge_dir) / name
        if kp.is_file():
            parts.append(f"## База знаний: {name}\n{_trim(kp.read_text(encoding='utf-8'), per_input)}")
        elif kp.is_dir():
            for f in sorted(kp.glob("*.json"))[:3]:
                parts.append(f"## База знаний: {name}/{f.name}\n{_trim(f.read_text(encoding='utf-8'), per_input // 3)}")
        else:
            parts.append(f"## {name}\n(нет данных)")
    if extra:
        parts.append(f"## Задание пользователя\n{extra}")
    return _trim("\n\n".join(parts), limit)


def extract_hypotheses(answer):
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", answer, re.S)
    for block in reversed(blocks):
        try:
            data = json.loads(block)
        except json.JSONDecodeError:
            continue
        if isinstance(data.get("hypotheses"), list):
            return data["hypotheses"]
    return []


def run_agent(name, cfg, agents_dir="agents", engine_dir=None, knowledge_dir="knowledge",
              out_dir="outputs", hypotheses_csv="data/hypotheses.csv", extra=None, images=(),
              dry_run=False):
    path = Path(agents_dir) / f"{name}.md"
    if not path.exists():
        raise FileNotFoundError(f"нет агента {path}")
    meta, body = parse_agent(path)
    engine_dir = engine_dir or latest_engine_dir(out_dir)
    context = build_context(meta, engine_dir, knowledge_dir, extra, cfg["llm"]["max_context_chars"])
    prompt = f"{PREAMBLE}\n# Твоя роль\n{body}\n\n# Контекст\n{context}\n"
    day = date.today().isoformat()
    target = Path(out_dir) / day / "agents"
    target.mkdir(parents=True, exist_ok=True)
    if dry_run:
        (target / f"{name}.prompt.md").write_text(prompt, encoding="utf-8")
        return {"agent": name, "prompt_file": str(target / f"{name}.prompt.md"), "dry_run": True}

    answer = complete(prompt, cfg["llm"], images=images,
                      backend=meta.get("backend"), model=meta.get("model"))
    out_file = target / f"{name}.md"
    out_file.write_text(answer, encoding="utf-8")

    hyps = extract_hypotheses(answer)
    stamp = datetime.now().strftime("%y%m%d%H%M")
    rows = []
    for i, h in enumerate(hyps):
        if not isinstance(h, dict) or not h.get("hypothesis"):
            continue
        rows.append({**h, "id": f"H{stamp}-{name[:6]}-{i + 1}", "created": day,
                     "source_agent": name, "status": "new"})
    if rows:
        append_csv(hypotheses_csv, rows, HYPOTHESIS_FIELDS)
    return {"agent": name, "output": str(out_file), "hypotheses_added": len(rows)}


def latest_engine_dir(out_dir="outputs"):
    days = sorted(p for p in Path(out_dir).glob("20*") if (p / "engine.json").exists())
    return days[-1] if days else Path(out_dir)
