"""Командная строка: python3 -m moneyball <команда>. Список команд: python3 -m moneyball -h"""

import argparse
import json
import shutil
import sys
from pathlib import Path

from . import agents, design, planner, pr, weekly
from .io import append_csv, load_config, read_csv, write_json
from .llm import LLMError, login_status
from .stats import prob_better, sample_size_per_variant

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"


def _load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def cmd_init(args):
    target = Path(args.dir)
    for sub in ("data", "briefs", "requests", "ideas", "assets", "outputs"):
        (target / sub).mkdir(parents=True, exist_ok=True)
    copied = []
    for src in (TEMPLATES / "data").glob("*.csv"):
        dst = target / "data" / src.name
        if not dst.exists():
            shutil.copy(src, dst)
            copied.append(str(dst))
    for name, sub in (("brief.json", "briefs"), ("request.json", "requests"), ("pr_idea.json", "ideas")):
        dst = target / sub / f"example_{name}"
        if not dst.exists():
            shutil.copy(TEMPLATES / name, dst)
            copied.append(str(dst))
    cfg_dst = target / "config.json"
    if not cfg_dst.exists():
        shutil.copy(TEMPLATES / "config.json", cfg_dst)
        copied.append(str(cfg_dst))
    print("Создано:\n  " + "\n  ".join(copied) if copied else "Всё уже на месте.")


def cmd_weekly(args, cfg):
    target, _ = weekly.run(cfg, args.data, args.out)
    print(f"Отчёт: {target / 'report.md'}\nРасчёты для агентов: {target / 'engine.json'}")
    if args.agents:
        for meta in agents.list_agents(args.agents_dir):
            if not meta.get("weekly"):
                continue
            try:
                res = agents.run_agent(meta["name"], cfg, args.agents_dir, target, args.knowledge,
                                       args.out, Path(args.data) / "hypotheses.csv")
                print(f"  агент {meta['name']}: {res['output']} (+{res['hypotheses_added']} гипотез)")
            except LLMError as exc:
                print(f"  агент {meta['name']}: не запущен — {exc}")


def cmd_plan(args, cfg):
    req = _load_json(args.request)
    funnel_stats = creative_stats = None
    engine_dir = agents.latest_engine_dir(args.out)
    if (Path(engine_dir) / "engine.json").exists():
        engine = _load_json(Path(engine_dir) / "engine.json")
        funnel_stats, creative_stats = engine.get("funnel"), engine.get("creatives")
    cases = []
    for d in (Path(args.knowledge) / "cases",):
        cases += planner.load_cases(d)
    catalog = planner.load_catalog(Path(args.knowledge) / "channels.json")
    plan = planner.build_plan(req, catalog, cases, funnel_stats, creative_stats)
    out = Path(args.out) / "plans" / f"{Path(args.request).stem}"
    write_json(out / "plan.json", plan)
    (out / "plan.md").write_text(render_plan(plan, cfg), encoding="utf-8")
    if args.save_hypotheses and plan["hypotheses"]:
        rows = [{**h, "id": f"P-{Path(args.request).stem}-{i + 1}"} for i, h in enumerate(plan["hypotheses"])]
        append_csv(Path(args.data) / "hypotheses.csv", rows, agents.HYPOTHESIS_FIELDS)
        print(f"Гипотез добавлено в data/hypotheses.csv: {len(rows)}")
    print(f"План: {out / 'plan.md'}")


def render_plan(p, cfg):
    cur = p["request"].get("currency", cfg["currency"])

    def m(x):
        return "—" if x is None else f"{x:,.0f} {cur}".replace(",", " ")

    e = p["unit_economics"]
    r = p["request"]
    L = [f"# План: {r.get('task', 'задача')} — {r.get('audience', '')}", "",
         "## Сколько можно платить",
         f"- Прибыль с клиента: {m(e['profit_per_customer'])} (чек {m(e['avg_check'])} × маржа {e['margin']:.0%} × покупок {e['repeat_purchases']})",
         f"- Предельный CAC (в ноль): {m(e['max_cac_breakeven'])}; целевой CAC: {m(e['target_cac'])}",
         f"- Конверсия заявка → сделка: {e['lead_to_deal']:.0%} ({e['lead_to_deal_source']})",
         f"- **Целевая цена заявки: {m(e['target_cpl'])}**, в ноль — {m(e['max_cpl_breakeven'])}",
         f"- _{e['note']}_", "", "## Каналы", ""]
    roles = {"core": "ядро", "test": "тест", "skip": "не сейчас"}
    for c in p["channels"]:
        L.append(f"- **{c['channel']}** — {roles.get(c.get('role'), c.get('role'))} (балл {c['score']:.0f}): "
                 + ("; ".join(c["why"]) or "нет данных для оценки"))
    b = p["budget"]
    L += ["", "## Бюджет на месяц"]
    if "plan" in b:
        for ch, row in b["plan"].items():
            L.append(f"- {ch}: {m(row['budget'])} ({row['role']})")
        L.append(f"- разведка новых идей: {m(b['exploration'])}")
        for n in b["notes"]:
            L.append(f"- ⚠ {n}")
        L.append(f"\n_{b['rule']}_")
    else:
        L.append(b.get("note", ""))
    L += ["", "## Что тестировать в первую очередь"] + [f"- {t}" for t in p["default_tests"]]
    if p["proven_angles"]:
        L.append("\nПо вашим данным сильнее работают: " + ", ".join(
            f"{a['tag']}=«{a['value']}» ({a['lift_vs_rest'] * 100:+.0f}%)" for a in p["proven_angles"]))
    L += ["", "## Похожие кейсы и что из них проверить", ""]
    if not p["cases"]:
        L.append("Подходящих кейсов в базе нет (knowledge/cases).")
    for c in p["cases"]:
        L += [f"**{c.get('title')}** — {c.get('brand')}, {c.get('market')} [{c.get('evidence')}]",
              f"- Сделали: {c.get('what_they_did')}",
              f"- Почему сработало: {c.get('mechanism')}",
              f"- Тест для вас: {c.get('test_to_run')}",
              f"- Источник: {c.get('source_url')}", ""]
    return "\n".join(L)


def cmd_banners(args, cfg):
    brief = _load_json(args.brief)
    creatives = read_csv(Path(args.data) / "creatives.csv")
    out = Path(args.out) / "banners" / Path(args.brief).stem
    register = Path(args.data) / "creatives.csv" if args.register else None
    rows = design.build(brief, creatives, cfg, out, base_dir=Path(args.brief).parent, register_to=register)
    print(f"Баннеров: {len(rows)} → {out}\nОбзор: {out / 'overview.png'}\nРазметка: {out / 'manifest.csv'}")
    for r in rows:
        if r["warnings"]:
            print(f"  ⚠ {r['creative_id']}: {r['warnings']}")
    if args.review:
        try:
            res = agents.run_agent("art-director", cfg, args.agents_dir, None, args.knowledge, args.out,
                                   Path(args.data) / "hypotheses.csv",
                                   extra="Проверь баннеры на картинке-обзоре и разметку:\n"
                                         + (out / "manifest.csv").read_text(encoding="utf-8")[:8000],
                                   images=[out / "overview.png"])
            print(f"Ревью арт-директора: {res['output']}")
        except LLMError as exc:
            print(f"Ревью не выполнено: {exc}")


def cmd_pr(args, cfg):
    cases = planner.load_cases(Path(args.knowledge) / "cases")
    if args.action == "score":
        idea = _load_json(args.file)
        res = pr.score_idea(idea)
        out = Path(args.out) / "pr" / f"{Path(args.file).stem}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(pr.render_score(idea, res, pr.similar_cases(idea, cases)), encoding="utf-8")
        print(f"Оценка: {res['score']}/100 — {res['verdict']}\nПодробно: {out}")
    else:
        brief = _load_json(args.file)
        ideas = pr.generate_ideas(brief, cases)
        out = Path(args.out) / "pr" / f"{Path(args.file).stem}_ideas.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(pr.render_ideas(brief, ideas), encoding="utf-8")
        print(f"Идей: {len(ideas)} → {out}")


def cmd_agent(args, cfg):
    if args.action == "list":
        for meta in agents.list_agents(args.agents_dir):
            flag = " [еженедельно]" if meta.get("weekly") else ""
            print(f"{meta['name']}{flag}: {meta.get('description', '')}")
        return
    try:
        res = agents.run_agent(args.name, cfg, args.agents_dir, None, args.knowledge, args.out,
                               Path(args.data) / "hypotheses.csv", extra=args.task,
                               images=args.image or (), dry_run=args.dry_run)
    except LLMError as exc:
        sys.exit(f"Ошибка: {exc}")
    print(json.dumps(res, ensure_ascii=False, indent=1))


def cmd_abtest(args, cfg):
    res = prob_better(args.conv_a, args.n_a, args.conv_b, args.n_b, prior_events=cfg["prior_events"])
    print(f"P(B лучше A) = {res['p_b_better']:.3f}\nПрирост B к A: {res['lift_mean'] * 100:+.1f}% "
          f"(90%: {res['lift_low'] * 100:+.1f}% … {res['lift_high'] * 100:+.1f}%)")


def cmd_sample(args, cfg):
    n = sample_size_per_variant(args.base_rate, args.mde)
    print(f"Нужно ≈{n:,} попыток на вариант".replace(",", " "))


def cmd_demo(args, cfg):
    demo = ROOT / "examples" / "demo"
    out = Path(args.out) / "demo"
    cfg = load_config(demo / "config.json")
    target, _ = weekly.run(cfg, demo, out)
    print(f"Демо-отчёт: {target / 'report.md'}")
    rows = design.build(_load_json(demo / "brief.json"), read_csv(demo / "creatives.csv"), cfg,
                        out / "banners", base_dir=demo)
    print(f"Демо-баннеры: {len(rows)} → {out / 'banners'}")
    plan = planner.build_plan(_load_json(demo / "request.json"),
                              planner.load_catalog(ROOT / "knowledge" / "channels.json"),
                              planner.load_cases(ROOT / "knowledge" / "cases"),
                              _load_json(target / "engine.json")["funnel"])
    write_json(out / "plan.json", plan)
    (out / "plan.md").write_text(render_plan(plan, cfg), encoding="utf-8")
    print(f"Демо-план: {out / 'plan.md'}")


def main(argv=None):
    p = argparse.ArgumentParser(prog="moneyball", description="Аналитическая система маркетинга")
    p.add_argument("--config", default="config.json")
    p.add_argument("--data", default="data")
    p.add_argument("--out", default="outputs")
    p.add_argument("--knowledge", default=str(ROOT / "knowledge"))
    p.add_argument("--agents-dir", default=str(ROOT / "agents"))
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("init", help="создать папки, шаблоны данных и config.json")
    s.add_argument("--dir", default=".")
    s = sub.add_parser("weekly", help="еженедельный расчёт и отчёт")
    s.add_argument("--agents", action="store_true", help="после расчёта запустить GPT-агентов (weekly: true)")
    s = sub.add_parser("plan", help="план под запрос: аудитория, кабинеты, бюджет")
    s.add_argument("request")
    s.add_argument("--save-hypotheses", action="store_true")
    s = sub.add_parser("banners", help="собрать баннеры по брифу")
    s.add_argument("brief")
    s.add_argument("--register", action="store_true", help="добавить баннеры в data/creatives.csv")
    s.add_argument("--review", action="store_true", help="ревью GPT-арт-директора по картинке")
    s = sub.add_parser("pr", help="идеи для СМИ и оценка идеи")
    s.add_argument("action", choices=["ideas", "score"])
    s.add_argument("file")
    s = sub.add_parser("agent", help="GPT-агенты")
    s.add_argument("action", choices=["list", "run"])
    s.add_argument("name", nargs="?")
    s.add_argument("--task", help="задание агенту своими словами")
    s.add_argument("--image", action="append", help="картинка для агента (можно несколько)")
    s.add_argument("--dry-run", action="store_true", help="только собрать промпт, не вызывать GPT")
    s = sub.add_parser("abtest", help="сравнить два варианта")
    for name in ("conv_a", "n_a", "conv_b", "n_b"):
        s.add_argument(name, type=float)
    s = sub.add_parser("sample-size", help="сколько нужно показов на вариант")
    s.add_argument("base_rate", type=float)
    s.add_argument("mde", type=float, help="относительный прирост, напр. 0.2")
    sub.add_parser("login", help="проверить вход в ChatGPT через Codex")
    sub.add_parser("demo", help="прогнать всё на демо-данных")

    args = p.parse_args(argv)
    if args.cmd == "init":
        return cmd_init(args)
    cfg = load_config(args.config)
    handlers = {"weekly": cmd_weekly, "plan": cmd_plan, "banners": cmd_banners, "pr": cmd_pr,
                "agent": cmd_agent, "abtest": cmd_abtest, "sample-size": cmd_sample, "demo": cmd_demo}
    if args.cmd == "login":
        print(login_status(cfg["llm"]))
        print("Если не вошли: выполните `codex login` — откроется браузер для входа в ChatGPT.")
        return
    if args.cmd == "agent" and args.action == "run" and not args.name:
        sys.exit("укажите имя агента: moneyball agent run <имя>")
    handlers[args.cmd](args, cfg)


if __name__ == "__main__":
    main()
