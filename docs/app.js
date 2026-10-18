/* Онлайн-версия Moneyball: Python-движок работает в браузере через Pyodide. */
const $ = (s, el = document) => el.querySelector(s);
const $$ = (s, el = document) => [...el.querySelectorAll(s)];

let py = null;
let web = null;
const state = { files: {}, planMd: "", manifest: "", pr: { answers: {}, flags: {} }, catalog: null };

const DATA = [
  ["funnel.csv", "Воронка", "По неделям и каналам: расход, часы, показы/касания → клики/ответы → заявки → офферы → сделки, выручка"],
  ["creatives.csv", "Креативы", "Каждый креатив с тегами (хук, угол, формат, компоновка) и результатами"],
  ["channel_weeks.csv", "Бюджет по неделям", "Недельный расход и выручка по платным каналам — для модели бюджета (12+ недель)"],
  ["competitors.csv", "Конкуренты", "Снимки библиотек объявлений: угол, оффер, первый и последний день показа"],
  ["experiments.csv", "Тесты", "Варианты A/B, план выборки, результаты"],
  ["hypotheses.csv", "Гипотезы", "Очередь идей для тестов"],
  ["content.csv", "Контент", "Публикации: охват, пересылки, сохранения, заявки — найти «залёты»"],
  ["orders.csv", "Заказы", "customer_id, дата, сумма — повторные продажи и сегменты"],
];

const PR_FIELDS = {
  brand: "Бренд", capability: "Что умеет продукт/технология", human_pro: "С кем соревноваться (человек-профи)",
  task: "Задача для соревнования", market: "Рынок / ниша", feat: "Что сделаете первыми",
  data_asset: "Какие данные есть или можно собрать", finding: "Какой вопрос они решают",
  product: "Продукт для демо", extreme: "Экстремальное условие демо", secret: "Что на рынке скрывают, а вы покажете",
  result: "Ваш результат (для «Давид против Голиафа»)", small_budget: "Ваш бюджет", big_rival: "Крупный игрок",
  big_budget: "Его бюджет", industry_norm: "От какой нормы рынка отказываетесь", reason: "Почему",
  absurd_idea: "Абсурдный образ/идея", event: "Инфоповод недели", response: "Ваша реакция за 24 часа",
  admission: "Что честно признаёте", fix: "Что с этим сделали", action: "Что делает аудитория",
  reward: "Что получает", limit: "Лимит участников",
};
const PLAN_PR_KEYS = ["brand", "capability", "human_pro", "task", "market", "feat", "data_asset", "finding",
  "product", "extreme", "secret"];
const PR_DEFAULTS = {
  brand: "thewater.studio", capability: "AI-пайплайн thewater.studio", human_pro: "студийный фотограф с командой",
  task: "кампания для одной капсулы бренда", market: "fashion-контент в России",
  feat: "полную кампанию бренда без единой физической съёмки",
  data_asset: "100 карточек товаров fashion-брендов на маркетплейсах",
  finding: "какой визуал продаёт лучше — студийный или AI", product: "AI-пайплайн",
  extreme: "кампания за 24 часа от брифа до публикации", secret: "реальную себестоимость AI-съёмки против студийной",
};
const DEFAULT_CHANNELS = ["telegram_ads", "vk_ads", "yandex_direct", "cold_telegram", "cold_email"];

/* ---------- утилиты ---------- */
const store = {
  get(k, d) { try { const v = localStorage.getItem("mb:" + k); return v === null ? d : JSON.parse(v); } catch { return d; } },
  set(k, v) { try { localStorage.setItem("mb:" + k, JSON.stringify(v)); } catch { /* приватный режим */ } },
};
function md(el, text) { el.innerHTML = DOMPurify.sanitize(marked.parse(text || "")); }
function esc(s) { return String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c])); }
function download(name, text, type = "text/plain") {
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([text], { type: type + ";charset=utf-8" }));
  a.download = name;
  a.click();
  setTimeout(() => URL.revokeObjectURL(a.href), 1000);
}
function setStatus(text, kind = "loading") {
  $("#status").className = "status " + kind;
  $("#status-text").textContent = text;
}
async function busy(btn, fn) {
  const label = btn.innerHTML;
  btn.disabled = true;
  btn.innerHTML = '<span class="spinner"></span> Считаю…';
  await new Promise(r => setTimeout(r, 40));
  try { await fn(); } catch (e) { console.error(e); alert("Ошибка: " + (e.message || e).toString().slice(-600)); }
  finally { btn.disabled = false; btn.innerHTML = label; }
}
function saveForm(form, key) {
  const out = {};
  for (const el of form.elements) {
    if (!el.name || el.type === "file") continue;
    if (el.type === "checkbox") {
      const group = form.querySelectorAll(`input[type=checkbox][name="${el.name}"]`);
      if (group.length > 1) { out[el.name] = [...group].filter(x => x.checked).map(x => x.value); }
      else out[el.name] = el.checked;
    } else out[el.name] = el.value;
  }
  store.set(key, out);
  return out;
}
function restoreForm(form, key) {
  const saved = store.get(key, null);
  if (!saved) return;
  for (const el of form.elements) {
    if (!el.name || !(el.name in saved) || el.type === "file") continue;
    const v = saved[el.name];
    if (el.type === "checkbox") el.checked = Array.isArray(v) ? v.includes(el.value) : !!v;
    else el.value = v;
  }
}
function num(v) { return v === "" || v === null || v === undefined ? null : Number(v); }

/* ---------- вкладки ---------- */
function initTabs() {
  const open = name => {
    $$("#tabs button").forEach(b => b.classList.toggle("active", b.dataset.tab === name));
    $$(".tab").forEach(t => t.classList.toggle("active", t.id === "tab-" + name));
    store.set("tab", name);
  };
  $$("#tabs button").forEach(b => b.addEventListener("click", () => open(b.dataset.tab)));
  open(store.get("tab", "week"));
}

/* ---------- Неделя ---------- */
function initWeek() {
  $("#file-inputs").innerHTML = DATA.map(([name, title, desc]) => `
    <div class="file-card" data-file="${name}">
      <b>${title}</b><p>${desc}</p>
      <input type="file" accept=".csv,text/csv">
      <div class="row"><a href="app/templates/data/${name}" download>шаблон ${name}</a><span class="st muted"></span></div>
    </div>`).join("");
  $$("#file-inputs .file-card").forEach(card => {
    $("input", card).addEventListener("change", async e => {
      const f = e.target.files[0];
      if (!f) return;
      state.files[card.dataset.file] = await f.text();
      markLoaded();
    });
  });
  $("#btn-demo").addEventListener("click", async () => {
    for (const [name] of DATA) {
      const r = await fetch("app/examples/demo/" + name);
      if (r.ok) state.files[name] = await r.text();
    }
    markLoaded("демо (вымышленные данные)");
  });
  $("#btn-week").addEventListener("click", e => busy(e.currentTarget, () => {
    const res = JSON.parse(web.run_weekly(JSON.stringify(state.files)));
    md($("#week-out"), res.report);
    $("#week-out").scrollIntoView({ behavior: "smooth", block: "start" });
  }));
}
function markLoaded(note) {
  $$("#file-inputs .file-card").forEach(card => {
    const ok = !!state.files[card.dataset.file];
    card.classList.toggle("loaded", ok);
    $(".st", card).textContent = ok ? "загружено ✓" : "";
  });
  const n = Object.keys(state.files).length;
  $("#week-loaded").textContent = n ? `Таблиц: ${n}${note ? " — " + note : ""}` : "";
}

/* ---------- План 360 ---------- */
function initPlan() {
  const ch = state.catalog.channels;
  const avail = v => v === true ? "" : v === false ? " — недоступен из РФ" : " — частично";
  $("#channel-list").innerHTML = Object.entries(ch).map(([k, v]) =>
    `<label class="check"><input type="checkbox" name="ch" value="${k}" ${DEFAULT_CHANNELS.includes(k) ? "checked" : ""}>
     <span>${esc(v.name || k)}<span class="muted small">${avail(v.available_from_ru)}</span></span></label>`).join("");
  const checks = JSON.parse(web.offer_checks());
  const preset = { outcome: 1, audience: 1, time: 1, proof: 1, risk_reversal: 1, alternative: 1, honest_scarcity: 1 };
  $("#offer-checks").innerHTML = checks.map(c =>
    `<label class="check"><input type="checkbox" name="offer_${c.key}" ${preset[c.key] ? "checked" : ""}> ${esc(c.q)}</label>`).join("");
  $("#pr-fields-plan").innerHTML = PLAN_PR_KEYS.map(k =>
    `<label>${PR_FIELDS[k]}<input name="pr_${k}" value="${esc(PR_DEFAULTS[k] || "")}"></label>`).join("");

  const form = $("#plan-form");
  restoreForm(form, "plan");
  form.addEventListener("input", () => saveForm(form, "plan"));
  form.addEventListener("submit", e => {
    e.preventDefault();
    busy($("#btn-plan"), () => {
      const v = saveForm(form, "plan");
      const req = {
        task: v.task, business_model: v.business_model, industry: v.industry, market: v.market,
        audience: v.audience, budget_month: num(v.budget_month), currency: v.currency || "RUB",
        avg_check: num(v.avg_check), margin: num(v.margin), repeat_purchases: num(v.repeat_purchases),
        lead_to_deal: num(v.lead_to_deal), has_tracking: v.has_tracking,
        channels_available: Array.isArray(v.ch) ? v.ch : (v.ch ? [$("input[name=ch]:checked", form).value] : []),
        offer: { text: v.offer_text, checks: Object.fromEntries(checks.map(c => [c.key, !!v["offer_" + c.key]])) },
        pr: Object.fromEntries(PLAN_PR_KEYS.filter(k => v["pr_" + k]).map(k => [k, v["pr_" + k]])),
      };
      const res = JSON.parse(web.run_plan(JSON.stringify(req), JSON.stringify({ currency: req.currency })));
      state.planMd = res.markdown;
      md($("#plan-out"), res.markdown);
      $("#dl-plan").disabled = false;
      $("#plan-out").scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
  $("#dl-plan").addEventListener("click", () => download("plan-360.md", state.planMd, "text/markdown"));
}

/* ---------- Баннеры ---------- */
function initBanners() {
  const form = $("#banner-form");
  restoreForm(form, "banners");
  form.addEventListener("input", () => saveForm(form, "banners"));
  let image = null;
  $("#banner-image").addEventListener("change", e => {
    const f = e.target.files[0];
    if (!f) { image = null; return; }
    const r = new FileReader();
    r.onload = () => { image = r.result; };
    r.readAsDataURL(f);
  });
  form.addEventListener("submit", e => {
    e.preventDefault();
    busy($("#btn-banners"), () => {
      const v = saveForm(form, "banners");
      const brief = {};
      for (const k of ["benefit", "time", "pain", "solution", "audience", "proof", "offer", "alternative",
        "sub", "cta", "logo_text"]) if (v[k]) brief[k] = v[k];
      brief.n = Number(v.n) || 6;
      brief.sizes = Array.isArray(v.size) ? v.size : ["square"];
      if (!brief.sizes.length) brief.sizes = ["square"];
      brief.colors = { bg: v.bg, text: v.text, accent: v.accent };
      if (v.image_fit) brief.image_fit = v.image_fit;
      const heads = (v.headlines || "").split("\n").map(s => s.trim()).filter(Boolean)
        .map(line => { const [t, a] = line.split("|").map(s => s.trim()); return { text: t, angle: a || "custom" }; });
      if (heads.length) brief.headlines = heads;
      const res = JSON.parse(web.run_banners(JSON.stringify(brief), image));
      state.manifest = res.manifest;
      $("#dl-manifest").disabled = false;
      $("#banner-out").innerHTML = res.banners.map(b => {
        const r = b.row;
        return `<div class="banner">
          <a href="data:image/png;base64,${b.png}" download="${b.creative_id}.png"><img src="data:image/png;base64,${b.png}" alt="${esc(r.headline)}"></a>
          <div class="meta"><b>${esc(r.layout)}</b> · ${esc(r.size)} · угол: ${esc(r.angle)}<br>
          текст ${Math.round(r.text_area_share * 100)}% площади · контраст ${r.contrast_headline}
          ${r.warnings ? `<div class="warn">⚠ ${esc(r.warnings)}</div>` : ""}</div></div>`;
      }).join("");
    });
  });
  $("#dl-manifest").addEventListener("click", () => download("banners-manifest.csv", state.manifest, "text/csv"));
}

/* ---------- СМИ ---------- */
function initPR() {
  const form = JSON.parse(web.pr_form());
  const saved = store.get("pr", null);
  if (saved) state.pr = saved;
  const defaults = { A1_surprise: 1, A2_exclusive: 1, A3_visual: 1, A4_conflict: 1, A5_timeliness: 0.5, A6_people: 0.5,
    B1_emotion: 0.5, B2_value: 1, B3_participation: 1, C1_product_hero: 1, C2_right_to_play: 1, C3_path_measure: 0.5,
    C4_capacity: 0.5, D1_budget: 1, D2_control: 0.5, D3_second_wave: 0.5 };
  if (!saved) state.pr.answers = defaults;

  $("#pr-criteria").innerHTML = Object.entries(form.blocks).map(([block, crits]) => `
    <div class="block-title"><span>${esc(block)}</span><span class="muted small" data-block="${esc(block)}"></span></div>
    ${Object.entries(crits).map(([k, c]) => `
      <div class="crit"><div>${esc(c.q)} <span class="w">вес ${c.w}</span></div>
        <div class="seg" data-k="${k}">${[0, 0.5, 1].map(x =>
          `<button type="button" data-v="${x}">${x === 0 ? "нет" : x === 1 ? "да" : "½"}</button>`).join("")}</div></div>`).join("")}
  `).join("");
  $("#pr-flags").innerHTML = Object.entries(form.flags).map(([k, q]) =>
    `<label class="check"><input type="checkbox" data-flag="${k}" ${state.pr.flags[k] ? "checked" : ""}> ${esc(q)}</label>`).join("");

  const paint = () => $$(".seg").forEach(seg => {
    const v = state.pr.answers[seg.dataset.k] ?? 0;
    $$("button", seg).forEach(b => b.classList.toggle("on", Number(b.dataset.v) === Number(v)));
  });
  const rescore = () => {
    const idea = { title: $("#pr-form [name=title]").value, answers: state.pr.answers, stop_flags: state.pr.flags };
    store.set("pr", state.pr);
    const res = JSON.parse(web.run_pr_score(JSON.stringify(idea)));
    $("#pr-score").textContent = res.result.score;
    $("#pr-verdict").textContent = res.result.verdict;
    for (const [b, s] of Object.entries(res.result.blocks)) {
      const el = document.querySelector(`[data-block="${CSS.escape(b)}"]`);
      if (el) el.textContent = `${Math.round(s.score)} из ${s.max}`;
    }
    md($("#pr-out"), res.markdown.split("\n").slice(4).join("\n"));
  };
  $("#pr-criteria").addEventListener("click", e => {
    const b = e.target.closest(".seg button");
    if (!b) return;
    state.pr.answers[b.parentElement.dataset.k] = Number(b.dataset.v);
    paint(); rescore();
  });
  $("#pr-flags").addEventListener("change", e => {
    state.pr.flags[e.target.dataset.flag] = e.target.checked;
    rescore();
  });
  $("#pr-form [name=title]").addEventListener("change", rescore);
  paint(); rescore();

  $("#pr-fields").innerHTML = Object.entries(PR_FIELDS).map(([k, label]) =>
    `<label>${label}<input name="${k}" value="${esc(PR_DEFAULTS[k] || "")}"></label>`).join("");
  const ideas = $("#pr-ideas-form");
  restoreForm(ideas, "pr-ideas");
  ideas.addEventListener("input", () => saveForm(ideas, "pr-ideas"));
  ideas.addEventListener("submit", e => {
    e.preventDefault();
    busy($("#btn-ideas"), () => {
      const v = saveForm(ideas, "pr-ideas");
      const brief = Object.fromEntries(Object.entries(v).filter(([, x]) => x));
      md($("#pr-ideas-out"), web.run_pr_ideas(JSON.stringify(brief)));
    });
  });
}

/* ---------- Тесты ---------- */
function initTests() {
  $("#ab-form").addEventListener("submit", e => {
    e.preventDefault();
    const f = new FormData(e.target);
    const r = JSON.parse(web.run_abtest(+f.get("ca"), +f.get("na"), +f.get("cb"), +f.get("nb")));
    const pct = x => (x * 100).toFixed(1) + "%";
    $("#ab-out").innerHTML = `<p><b>P(B лучше A) = ${r.p_b_better.toFixed(3)}</b><br>
      Прирост B к A: ${r.lift_mean >= 0 ? "+" : ""}${pct(r.lift_mean)} (90%: ${pct(r.lift_low)} … ${pct(r.lift_high)})</p>
      <p class="muted small">Решение — только когда набран запланированный объём. Порог системы: 0.95.</p>`;
  });
  $("#ss-form").addEventListener("submit", e => {
    e.preventDefault();
    const f = new FormData(e.target);
    try {
      const n = web.run_sample_size(+f.get("p"), +f.get("mde"));
      $("#ss-out").innerHTML = `<p><b>≈${Number(n).toLocaleString("ru-RU")} попыток на вариант</b></p>
        <p class="muted small">Если трафика меньше — тестируйте крупные различия (угол, оффер), а не отдельные слова.</p>`;
    } catch (err) { $("#ss-out").textContent = "Проверьте числа: доли должны быть между 0 и 1."; }
  });
}

/* ---------- База знаний ---------- */
async function initKB() {
  const cases = state.catalog.cases;
  const files = [...new Set(cases.map(c => c._file))];
  const names = { "global_ecom.json": "E-com / DTC (мир)", "b2b_services.json": "B2B и услуги",
    "ru_cis.json": "РФ / СНГ", "earned_media.json": "Попадание в СМИ" };
  $("#kb-file").innerHTML += files.map(f => `<option value="${f}">${names[f] || f}</option>`).join("");
  const render = () => {
    const q = $("#kb-q").value.toLowerCase();
    const fsel = $("#kb-file").value;
    const ev = $("#kb-ev").value;
    const list = cases.filter(c => (!fsel || c._file === fsel) && (!ev || c.evidence === ev) &&
      (!q || JSON.stringify(c).toLowerCase().includes(q)));
    $("#kb-count").textContent = `Кейсов: ${list.length}`;
    $("#kb-cases").innerHTML = list.slice(0, 120).map(c => `
      <div class="case">
        <span class="tag ${esc(c.evidence)}">${esc(c.evidence)}</span><span class="tag">${esc(c.market)}</span>
        ${(c.channels || c.news_values || []).slice(0, 4).map(x => `<span class="tag">${esc(x)}</span>`).join("")}
        <h4>${esc(c.title)}</h4>
        <p>${esc(c.what_they_did)}</p>
        ${c.mechanism || c.why_media_covered ? `<p class="muted">Почему: ${esc(c.mechanism || c.why_media_covered)}</p>` : ""}
        ${c.test_to_run ? `<p><b>Тест:</b> ${esc(c.test_to_run)}</p>` : ""}
        ${c.risks_or_backlash ? `<p class="muted">Риски: ${esc(c.risks_or_backlash)}</p>` : ""}
        <p><a href="${esc(c.source_url)}" target="_blank" rel="noopener">источник</a></p>
      </div>`).join("");
  };
  ["#kb-q", "#kb-file", "#kb-ev"].forEach(s => $(s).addEventListener("input", render));
  render();
  const r = await fetch("app/knowledge/principles.md");
  if (r.ok) md($("#kb-principles"), await r.text());
}

/* ---------- загрузка ---------- */
async function boot() {
  initTabs();
  try {
    py = await loadPyodide();
    setStatus("Загружаю numpy и Pillow…");
    await py.loadPackage(["numpy", "pillow"]);
    setStatus("Загружаю движок и базу кейсов…");
    const files = await (await fetch("files.json")).json();
    await Promise.all(files.map(async f => {
      const buf = await (await fetch(f)).arrayBuffer();
      const path = "/" + f;
      py.FS.mkdirTree(path.slice(0, path.lastIndexOf("/")));
      py.FS.writeFile(path, new Uint8Array(buf));
    }));
    py.runPython("import sys; sys.path.insert(0, '/app')");
    web = py.pyimport("moneyball.web");
    web.setup("/app", "/app/fonts");
    state.catalog = JSON.parse(web.catalog_json());
    initWeek(); initPlan(); initBanners(); initPR(); initTests(); await initKB();
    $$("button[disabled]").forEach(b => { if (!["dl-plan", "dl-manifest"].includes(b.id)) b.disabled = false; });
    setStatus(`Готово · кейсов в базе: ${state.catalog.cases.length}`, "ready");
  } catch (e) {
    console.error(e);
    setStatus("Не удалось загрузить: " + (e.message || e), "error");
  }
}
boot();
