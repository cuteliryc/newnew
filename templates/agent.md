---
name: my-agent
description: Одна строка — что делает агент
inputs: [funnel, creatives, principles.md]
weekly: false
backend: codex
model:
---

Скопируйте этот файл в agents/<имя>.md и опишите роль.

Поля шапки:
- name — имя для запуска: `python3 -m moneyball agent run <name>`.
- inputs — что положить в контекст. Разделы расчёта: funnel, budget, creatives, copy,
  competitors, experiments. Файлы и папки базы знаний: principles.md, cases, channels.json.
- weekly: true — запускать автоматически в `weekly --agents`.
- backend — codex (подписка ChatGPT) или openai_api. model — пусто = по умолчанию.

Дальше — инструкция агенту: кто он, что проверить, в каком виде отдать результат.
Общие правила (метки ФАКТ/ВЫВОД/ДОПУЩЕНИЕ, блок гипотез в JSON) добавляются автоматически.
