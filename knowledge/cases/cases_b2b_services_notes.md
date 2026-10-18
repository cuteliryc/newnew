# Кейсы B2B, услуг, агентств, студий, SaaS и лидогенерации: что меняли и что сработало (кросс-кейсовые паттерны)

Библиотека: `cases_b2b_services.json` — 40 кейсов. Все страницы-источники открыты целиком (`source_seen: full_page`), если в кейсе не сказано иное. Цифры, которые мы видели только в поисковых сниппетах, помечены прямо в полях `note` или вынесены в раздел Gaps.

Распределение по надёжности: vendor 26, medium 6, weak 6, strong 2 (оба — академические рандомизированные эксперименты).

---

## 1. Что меняли, в каком канале, для какой аудитории, какие цифры до/после и за какой период?

### Takeaway
Самые крупные и воспроизводимые сдвиги дают изменения не в бюджете, а в трёх местах:
1. Что именно просят у человека в первом касании.
2. Кому пишут и насколько узко позиционирован оффер.
3. Что считается конверсией: сигналы для алгоритмов и атрибуция.

Большинство цифр взяты из вендорских датасетов и кейсов. Они годятся как направление для гипотезы, но не как ожидаемая величина эффекта.

### Cited Findings

**Холодный outreach (email, LinkedIn)**
- Gong: CTA «интересно ли вам?» — самый результативный тип CTA в холодных письмах. Конкретное время лучше просить после проявленного интереса. Точные значения есть только на графике — [Gong](https://www.gong.io/blog/cold-email-stats/)
- Gong: ROI-язык снижает успешность на 15%. Слово «thoughts» снижает шанс встречи на 20%. «I never heard back» снижает встречи на 14%. «Hope all is well» коррелирует с +24% встреч. Письма в 30–150 слов лучше бронируют встречи, чем ≤30 слов — [Gong](https://www.gong.io/blog/cold-email-stats/)
- Hunter: 34 млн писем 2022–2024. Лучший reply rate у писем в 20–39 слов; письма <100 слов дают 3,9%, длиннее — 3,7% — [Hunter](https://hunter.io/blog/cold-email-word-count). Это противоречит Gong по длине, но метрики разные: ответы у Hunter, встречи у Gong.
- Lavender: выборка 231 818 писем (февраль 2026). Письма уровня «A» в operations дают 5,4% ответов (+58%). В finance только 6,1% писем получают «A», но такие письма дают +79% — [Lavender](https://www.lavender.ai/blog/the-cold-email-benchmark-report)
- Belkins: 7,5 млн писем 2025 года. Средний reply rate 0,45% (ответы/все отправки). Founders/owners 0,57%, C-level 0,42%, VP 0,32%. Компании 0–10 человек 0,72%, 10 000+ — 0,22%. Утро 8–12 ч 0,54%, вечер и ночь 0,40% — [Belkins](https://belkins.io/blog/cold-email-response-rates)
- Belkins: follow-up дают 58,6% всех ответов. Шаг 3 бронирует больше встреч, чем шаги 1 и 2 вместе; шаги 3–5 дают 53,5% встреч. LinkedIn после email даёт 7%+ ответов. Звонок дозванивается до 18,6% и даёт 33,6% всех встреч — [Belkins](https://belkins.io/blog/sales-follow-up-statistics). Противоречит Instantly: по их данным 58% ответов приходят на первое письмо, средний reply rate 3,43% — [Instantly](https://instantly.ai/blog/email-sequence-benchmarks-2026-whats-a-good-open-rate-reply-rate-and-cost-per-meeting/)
- Данные Expandi (15 млн контактов): записка к запросу на коннект в LinkedIn снижает accept с 27,56% до 25,31%, но поднимает ответы среди принявших с 5,28% до 8,18%. Messenger-кампании по уже существующим контактам дают 12,22% — [Belkins](https://belkins.io/blog/sales-follow-up-statistics)
- Smartlead: агентства, пишущие одному названному сегменту, получают 6,8% ответов. Широкий B2B-маркетинг — 4,7%, full-service — 3,5% — [Smartlead](https://www.smartlead.ai/email-templates/digital-marketing-agencies-cold-email). Креативные агентства с video-led письмами — 3,8% при медиане по всем отраслям 0,74%. Отвечают на письма, которые показывают работу, а не описывают её — [Smartlead](https://www.smartlead.ai/email-templates/creative-agencies-cold-email)
- devlo: персональные картинки в письмах. 714 лидов, 306 ответов (42%), 75 позитивных (10%); средний показатель агентства за 2023 год — 43% — [lemlist](https://www.lemlist.com/success-stories/devlo)
- Письмо 150 e-com брендам «записал видео-разбор вашей воронки — прислать?»: 34% ответов, 31 созвон, 8 клиентов, около EUR 12K. Автор не назван — [Prospeo](https://prospeo.io/s/cold-email-examples)
- Corporate Visions, полевой тест на 7 000 проспектов: персонализация по отрасли дала CTR на 17–24% выше, чем по компании, и больше встреч. Лучший open rate (26,17%) был у варианта «личное + компания» — [Corporate Visions](https://tourial.corporatevisions.com/answers/research-reveals-the-most-effective-kind-of-abm-personalization)
- Рандомизированный эксперимент Sahni и соавторов: имя получателя в теме дало +20% открытий, +31% лидов, −17% отписок — [EconPapers](https://econpapers.repec.org/paper/eclstabus/3409.htm)

**Платная лидогенерация (LinkedIn, Google)**
- Metadata 2026: 153 рекламодателя, $57,6 млн расходов 2025 года, CRM-пайплайн у 90 из них.
  - CPL по форматам: document ads $142, image $200, video $265, conversation $362 — [Metadata](https://metadata.io/benchmark-report-2026/insights/document-ads-nobody-runs)
  - Lead-форма: $193 за лид и 9,3x пайплайна на $1. Лендинг: $346 и 5,3x. Ретаргетинг: 9,6x пайплайна на $1 — [Metadata](https://metadata.io/benchmark-report-2026/insights/forms-beat-pages)
  - Стоимость клиента на LinkedIn: малый бизнес $31k, mid-market $103k, enterprise $78k — [Metadata](https://metadata.io/benchmark-report-2026/insights/document-ads-nobody-runs)
- O'Reilly (APAC): always-on и расширение на senior IC дали −65% CPL к прошлому кварталу и 2x лидов. При 6–10 показах вероятность конверсии в 2–3 раза выше — [LinkedIn](https://business.linkedin.com/advertise/customer-stories/oreilly)
- Payhawk: переход от bottom-funnel на холодную аудиторию к full-funnel контенту дал CPL на 85% ниже отраслевого бенчмарка — [LinkedIn](https://business.linkedin.com/marketing-solutions/case-studies/payhawk)
- Valueships: Thought Leader Ads стоили $0,15 за клик на лендинг против $10,02 у image ads; 12 встреч за $391 — [ZenABM](https://zenabm.com/blog/winning-linkedin-thought-leader-ads-case-study-valueships). Опровергает: парный бенчмарк Kiin Labs показал паритет landing-page CTR (0,449% против 0,441%) при более дорогом CPM у TLA — [Understory](https://www.understoryagency.com/blog/thought-leader-ads-vs-brand-ads)
- Lucanet: LinkedIn CAPI и сигналы из CRM дали за квартал в 4 раза больше лидов и конверсию выше в 3+ раза — [Front Row](https://www.frontrowgroup.com/en/cases/lucanet-improves-lead-volume-and-quality-with-linkedin-conversion-api-customer-snapshot)
- Brandwatch: value-based bidding по стадиям из Salesforce дал −53% cost per SQL и −18% стоимости встречи — [Precis](https://www.precis.com/work/brandwatch-value-based-bidding-b2b)

**Лендинги, формы, скорость реакции**
- Workato: мгновенная запись из формы подняла lead-to-meeting с 40–55% до 75–80%, демо +50%, выручку +10–15% — [Chili Piper](https://www.chilipiper.com/customers/workato)
- Navattic: form-to-demo вырос с 70% до 85% — [Chili Piper](https://www.chilipiper.com/customer-story/navattic-demo-conversions-chili-piper)
- ChowNow: speed-to-lead сократился с недели до мгновенного, такие встречи закрывались в 4 раза чаще — [Chili Piper](https://www.chilipiper.com/customers/chownow)
- Appcues: переписали главную по фидбэку ICP, A/B показал +73% visit-to-trial — [Wynter](https://wynter.com/case-studies/appcues)
- Cognism: демо-страница +43%, главная +40,22% — [Wynter](https://wynter.com/case-studies/cognism)

**Позиционирование и бренд**
- Databook: новая категория SRM дала +67% конверсии сайта за 2 недели и 10x лидов — [Wynter](https://wynter.com/case-studies/databook)
- Okta: Silver Effie 2026, #1 по спонтанной узнаваемости, вдвое лучшие лиды — [The MX Group](https://www.themxgroup.com/news/themxgroup-and-okta-win-effie-for-advertising-effectiveness)
- LBBW: Gold Effie B2B, во время кампании ЛПР вдвое чаще заходили на сайт — [LBBW](https://www.lbbw.de/artikel/pressemitteilung/lbbw-gewinnt-gold-effie_ab1je62bio_d.html)
- Atlassian: CTV в LinkedIn перед конверсионными кампаниями дал +120% CTR; подсказанная узнаваемость +17% при норме 2% — [LinkedIn](https://business.linkedin.com/marketing-solutions/case-studies/atlassian-ctv)

**Оффер и прайсинг**
- Designjoy: продуктизированная подписка с фиксированной ценой, $1 млн+ в год соло — [Memberstack](https://memberstack.io/showcase/how-i-built-designjoy). Сервис $1,3 млн в год и курс $540K в год — [High Spirit](https://highspirit.substack.com/p/the-2m-dollar-designer)
- Changelogfy: убрали free-план и потребовали карту для триала, MRR +50% — [Substack](https://paulocastellano.substack.com/p/why-we-killed-our-free-plan-and-grew)
- Опрос 200 продуктов: триал с картой даёт 30% free-to-paid, в 5+ раз больше, чем без карты; медиана 8% — [Growth Unhinged](https://growthunhinged.com/p/free-to-paid-conversion-report)
- Платные пилоты конвертируются в годовой контракт на 60–90%+; зрелые вендоры переходят на opt-out за 60 дней — [SaaStr](https://www.saastr.com/what-is-the-typical-conversion-from-paid-pilot-to-annual-contract-in-b2b-saas)

**Контент (inbound)**
- Blue Triangle убрал формы с контента. Тест показал +61% вовлечённых при −95% стоимости вовлечения. Через год: демо-запросы +265%, пайплайн +242% — [CMI](https://contentmarketinginstitute.com/content-marketing-strategy/cmo-ungated-everything)
- RevenueZen: личный LinkedIn CEO даёт около трети пайплайна и выручки агентства — [Databox](https://databox.com/metrics-and-chill-revenuezen)
- Sumsub: YouTube-шоу. Первая интеграция за €339 принесла 1 млн+ просмотров; позже 50 млн просмотров. Число лидов не раскрыто — [Substack](https://olyalakt.substack.com/p/how-we-achieved-30m-views-and-250k)

**Рефералы**
- Компания топливных карт: двусторонняя программа дала 5 691 лид и 3 758 конверсий (66%) — [Referral Factory](https://referral-factory.com/learn/case-study-how-this-b2b-financial-services-business)
- SmartBear: рекомендации от промоутеров из NPS принесли $6 млн и 47% close rate за 18 месяцев — [CustomerGauge](https://customergauge.com/blog/b2b-referral-program-examples)
- Рандомизированный эксперимент (JMR, GiftAMeal): бонус другу работает незначительно лучше бонуса рекомендателю. При этом только 2,6% из 351 программы награждают получателя — [WashU Olin](https://olin.washu.edu/about/news-and-media/news/2020/07/research-into-social-dynamics-shows-how-firms-can-win-more-customers.php)

**Измерение и инкрементальность**
- Refine Labs: подкаст дал 53% выручки ($11,4 млн) по ответам «откуда узнали» и 0% по софтверной атрибуции; разрыв измерения 90% — [Refine Labs](https://www.refinelabs.com/article/hybrid-attribution-framework)
- Lift-тест LinkedIn на уровне кампании: видевшие кампанию конвертировались на 26% чаще контроля. Цифра из блога LinkedIn, независимо не проверена — [TechWyse](https://www.techwyse.com/news/platform-updates/linkedin-campaign-level-conversion-lift-testing-brand-lift-roi-measurement)

### Inferences

Паттерны, которые повторяются в нескольких кейсах:

- **P1. Уменьшайте размер первой просьбы.** Об этом говорят сразу несколько независимых линий:
  - запрос интереса вместо встречи (Gong);
  - «прислать видео-разбор?» (e-com, 34%);
  - контент без формы (Blue Triangle);
  - lead-форма вместо лендинга (Metadata);
  - мгновенная запись после формы (Workato, Navattic, ChowNow).

  Механизм один и тот же: меньше трения в момент намерения. Это самый надёжный кросс-кейсовый сигнал.
- **P2. Показывайте результат на материале получателя.** Персональные картинки (devlo), «работа, а не описание работы» (Smartlead), видео-разбор воронки, кадры «до/после» в рекламе. Для визуальной студии отправить работу почти ничего не стоит, это её естественное преимущество.
- **P3. Узкий сегмент побеждает широкий оффер.** Примеры: Smartlead (6,8% против 3,5%), Databook (новая категория), совет основателя Designjoy выбрать нишу уже, отраслевая персонализация у Corporate Visions. Узость работает и в позиционировании, и в таргетинге: Belkins показывает, что founders маленьких компаний отвечают в 1,3–3 раза чаще.
- **P4. Последовательность и смена канала.** Третье письмо с новым углом, затем LinkedIn, затем звонок (Belkins). Частота 6–10 показов (O'Reilly). Бренд-показы перед performance (Atlassian, Payhawk). Это практическое применение принципа B2B Institute и Ehrenberg-Bass о том, что бренд и спрос работают вместе. Мы видели его только в платформенных кейсах, не в отчётах самого B2B Institute.
- **P5. Учите алгоритмы на значимых конверсиях.** Lucanet (CAPI и CRM), Brandwatch (value-based bidding), Metadata (оценивать по пайплайну на доллар, а не по CPL). Небольшому бизнесу это доступно уже на десятках конверсий в месяц.
- **P6. Атрибуция «откуда узнали» обязательна для контента и LinkedIn.** RevenueZen, Refine Labs и Blue Triangle показывают, что эффект личного бренда и контента не виден в UTM. Без поля «откуда узнали» планировщик будет системно недофинансировать эти каналы.
- **P7. Обязательство на входе повышает качество.** Карта для триала (Growth Unhinged, Changelogfy), платный пилот и opt-out (SaaStr). Для студии это значит: платный мини-пилот, засчитываемый в заказ, вместо бесплатных тестов.
- **P8. Рефералы — самый дешёвый канал с конверсией 47–66%.** Нужен правильный момент (NPS 9–10), двусторонний или «подарочный» бонус и передача рекомендации прямо в CRM.

Приоритет тестов для небольшой AI-контент- и креатив-студии, продающей fashion- и e-com-брендам (по соотношению стоимости, скорости и силы сигнала):
1. Холодное письмо узкому сегменту с бесплатной демонстрацией на их SKU и CTA-вопросом про интерес. Кейсы: gong-interest-cta, smartlead-agency-narrow-segment, ecom-video-offer-34pct, lemlist-devlo-custom-images.
2. Последовательность из 3–5 писем, затем LinkedIn-коннект с запиской, затем звонок топ-аккаунтам. Кейсы: belkins-followup-step3-channel-switch, expandi-linkedin-connection-note.
3. Таргет на founders и owners DTC-брендов на 1–50 человек. Кейс: belkins-targeting-founders-small-companies.
4. Мгновенная запись после заявки и SLA ответа меньше 15 минут. Кейсы: chilipiper-*.
5. Продуктизированная подписка с якорем на стоимость фотосессии и платный пилот вместо бесплатного теста. Кейсы: designjoy-productized-subscription, growth-unhinged-credit-card-trials.
6. Реферальный запрос после NPS 9–10 с бонусом-подарком рекомендуемому. Кейсы: smartbear-nps-driven-referrals, giftameal-prosocial-referral-incentive.
7. Поле «откуда узнали» и CAPI с квалифицированным лидом до запуска платного трафика. Кейсы: refine-labs-self-reported-attribution, lucanet-linkedin-capi-crm-signals.
8. Только после этого — платная реклама: LinkedIn document ad или TLA основателя, ретаргетинг вовлечённых, holdout-сравнение.

### Gaps
- **Telegram и DM.** Не найдено ни одного B2B-кейса с reply rate или встречами для Telegram-outreach. Кейсов по Instagram DM для B2B тоже нет. В библиотеке этих кейсов нет.
- **Гарантии (money-back, risk reversal).** Не найдено рандомизированного исследования для сервисных фирм. Поисковые сниппеты дают противоречивые практические A/B-тесты: от +21–26% продаж до падения продаж у KitchenAid при 90-дневной гарантии. Страницы мы не открывали, поэтому в библиотеку не включали. Ближайший аналог в библиотеке — opt-out контракт (saastr-paid-pilot-to-optout).
- **Лид-магниты.** Нет именованного A/B-теста «калькулятор против e-book» с контрольной группой. Цифры вида «калькуляторы 8,3% против PDF 3,8%» найдены только в непроверяемых блогах. Единственный хорошо задокументированный кейс про гейтинг — Blue Triangle.
- **B2B-рассылки.** Не найдено кейса агентства или студии с цифрами «рассылка → клиенты → выручка». Найденные материалы — анекдоты или платформенные кейсы без выручки.
- **Инкрементальность в B2B.** Нет опубликованного именованного B2B holdout или гео-теста с полной методологией. Есть только цифра 26% от неназванной компании (из блога LinkedIn) и вендорские иллюстрации. Тест брендового поиска в B2B с результатами не найден.
- **Отчёты B2B Institute.** Не найдено кейса компании, явно применившей правило 95-5 с цифрами пайплайна. Есть только платформенные кейсы, которые иллюстрируют связку бренда и спроса (Atlassian, Payhawk, O'Reilly).
- **Только по поисковым сниппетам (в JSON не включены или помечены):**
  - Marketing Science (DOI 10.1287/mksc.2020.1242): в эксперименте на 160 000+ клиентов банка крупные реферальные награды привели больше клиентов, но менее прибыльных. Страница вернула 403.
  - Кейс Neo4j на Think with Google: страница рендерится JavaScript-ом, цифры не видны.
  - Belkins-2025 (16,5 млн писем 2024 года): одношаговая последовательность дала 8,4% ответов.
  - Лестница цен Designjoy ($449 → $8 000 в месяц).
  - Сравнение видео и текста у Vidyard (77 против 9 ответов) — выглядит неправдоподобно.
- **Отсеяны** из-за внутренних противоречий или слабых данных:
  - Кейс Visionary Marketing по Google Ads: на одной странице £1,2 млн против £1,6 млн пайплайна и £180→£65 против £234→£84 cost per SQL. Ссылка: https://visionary-marketing.co.uk/case-studies/b2b-google-ads-pipeline
  - Census: только краткое зеркало на casestudies.com.
  - lemlist / The Atomic Agency: только «10x встреч, +15% выручки» без базы.

---

## 2. Механизм, переносимый урок и конкретный тест для малого сервисного бизнеса

### Takeaway
Почти все сильные эффекты объясняются тремя механизмами: снижение трения или цены «да», демонстрация ценности до просьбы и релевантность узкому сегменту. Их можно проверить дёшево, на выборках 150–300 контактов и бюджете $300–2 000 на ветку. Конкретные тесты прописаны в поле `test_to_run` каждого кейса.

### Cited Findings
- Логика Gong: запрос интереса продаёт разговор, а не встречу — [Gong](https://www.gong.io/blog/cold-email-stats/)
- По Smartlead, получатель решает за 2 секунды, про него ли письмо, и названный сегмент отвечает на этот вопрос. Одна работа для похожего бренда убеждает сильнее общего шоурила — [Smartlead](https://www.smartlead.ai/email-templates/digital-marketing-agencies-cold-email), [Smartlead](https://www.smartlead.ai/email-templates/creative-agencies-cold-email)
- Belkins объясняет эффект третьего письма двумя причинами: двум касаниям нужно время, чтобы человек узнал отправителя, а сам шаг 3 должен быть новым углом, а не напоминанием — [Belkins](https://belkins.io/blog/sales-follow-up-statistics)
- Metadata советует делать lead-форму на 3–5 полей с автозаполнением и одним квалифицирующим вопросом, а лендинги оставлять для ретаргетинга — [Metadata](https://metadata.io/benchmark-report-2026/insights/forms-beat-pages)
- У Brandwatch разным лидам задавали разную ценность (встреча с enterprise на 32% ценнее, демо в 3 раза ценнее триала), и это научило алгоритм искать покупателей — [Precis](https://www.precis.com/work/brandwatch-value-based-bidding-b2b)
- У Blue Triangle до демо-запроса в среднем 50–60 касаний, поэтому метрикой вместо MQL стали вовлечение аккаунта и демо-запрос — [CMI](https://contentmarketinginstitute.com/content-marketing-strategy/cmo-ungated-everything)
- Фиксированная цена, SLA 48 часов и якорь «$60K против $120–200K за штатного дизайнера» убирают трение покупки — [High Spirit](https://highspirit.substack.com/p/the-2m-dollar-designer)
- Бонус для друга снижает социальный барьер рекомендации: рекомендатель выглядит щедрым — [WashU Olin](https://olin.washu.edu/about/news-and-media/news/2020/07/research-into-social-dynamics-shows-how-firms-can-win-more-customers.php)

### Inferences
- Для AI-студии, работающей с fashion и e-com, механизмы P1 и P2 сливаются в один оффер: «3 AI-кадра вашего реального SKU — прислать?». Он одновременно снижает цену «да», показывает работу и проверяет интерес.
- Для правил планировщика: если `business_model` равен agency, freelance или creative_services, а бюджет small, начинайте с кейсов с `levers` offer, copy и positioning в cold_email и linkedin. Платные каналы с `evidence: vendor` подключайте только при наличии `measurement` (CAPI, «откуда узнали»).
- Метрика успеха теста — встречи и сделки на 100 контактов, а не reply rate. Gong показывает, что формулировки, поднимающие ответы, могут снижать встречи.
- Минимальная гигиена теста: случайное разбиение списка, одинаковое время отправки (утро среды или четверга по Belkins), не меньше 150 контактов на ветку. Разметка ответов на позитивные и негативные.

### Gaps
- Нет данных о том, как переносятся эффекты именно на fashion и e-com покупателей B2B-услуг. Ближайшие кейсы — пример про 150 e-com брендов (weak) и креативные агентства у Smartlead (vendor).
- Нет данных о влиянии картинок и видео в холодных письмах на доставляемость. Это риск для теста «картинка в письме».
- Нет надёжных бенчмарков стоимости встречи для малых креативных студий. Цифра Instantly $152,73 за встречу через email против $2 777,78 через звонки — вендорская и без методики — [Instantly](https://instantly.ai/blog/email-sequence-benchmarks-2026-whats-a-good-open-rate-reply-rate-and-cost-per-meeting/)

---

## 3. Надёжность источников

### Takeaway
Сильных (рандомизированных) свидетельств в B2B-маркетинге мало: в библиотеке 2 академических эксперимента, оба не про холодный B2B. Основная масса — вендорские датасеты (корреляции на миллионах писем) и кейсы платформ или вендоров с отбором успешных историй. Использовать их стоит как приоритизацию гипотез, а не как прогноз эффекта.

### Cited Findings
- Belkins сменил знаменатель reply rate: раньше считали от открывших, теперь от всех отправок. Поэтому 0,45% в 2025 году против прежних 5–8% — это изменение методики, а не обвал канала — [Belkins](https://belkins.io/blog/cold-email-response-rates)
- Hunter критикует Boomerang (2016, тёплые письма, 51% ответов) и Lavender (15–25% ответов, вероятно, включая не только первое касание) — [Hunter](https://hunter.io/blog/cold-email-word-count)
- Lavender и Hunter явно отмечают, что данные самоотчётные и корреляционные — [Lavender](https://www.lavender.ai/blog/the-cold-email-benchmark-report), [Hunter](https://hunter.io/blog/cold-email-word-count)
- Metadata пишет, что широкие пайплайн-цифры не доказывают причинного преимущества конкретного формата LinkedIn — [Metadata](https://metadata.io/benchmark-report-2026/insights/document-ads-nobody-runs)
- Understory: почти все публичные pipeline-кейсы по TLA — самоотчёты агентств или вендоров, ни один не изолирует TLA на стадии opportunity. Большинство говорят о влиянии, а не об инкрементальности — [Understory](https://www.understoryagency.com/blog/thought-leader-ads-vs-brand-ads)
- TechWyse не смог независимо проверить цифру 26% из lift-теста LinkedIn — [TechWyse](https://www.techwyse.com/news/platform-updates/linkedin-campaign-level-conversion-lift-testing-brand-lift-roi-measurement)
- Effie присуждается по доказанной эффективности на основе маркетинговых исследований (трёхступенчатое жюри) — [LBBW](https://www.lbbw.de/artikel/pressemitteilung/lbbw-gewinnt-gold-effie_ab1je62bio_d.html). Но метрики в пресс-релизах неполные: «вдвое лучше лиды» у Okta без методики — [The MX Group](https://www.themxgroup.com/news/themxgroup-and-okta-win-effie-for-advertising-effectiveness)
- Кейс Chili Piper по ChowNow сравнивает встречи, записанные через инструмент, со средним close rate. Возможен самоотбор более горячих лидов — [Chili Piper](https://www.chilipiper.com/customers/chownow)

### Inferences
- Шкала для планировщика:
  - **strong** — только рандомизированные эксперименты (Sahni; GiftAMeal).
  - **medium** — независимые статьи с цифрами (CMI, Growth Unhinged), Effie и собственный полевой тест компании (Corporate Visions).
  - **vendor** — платформенные и вендорские кейсы и датасеты.
  - **weak** — анекдоты, маленькие выборки, несостыковки (prospeo e-com, Valueships, Changelogfy, SaaStr, RevenueZen, Sumsub).
- Рекомендуемое правило: кейсы с `evidence` vendor или weak генерируют гипотезы для теста, но не прогнозы. Ожидаемый эффект стоит дисконтировать (например, брать нижнюю границу или половину заявленного) и обязательно проверять собственным A/B или holdout.
- Когда вендоры противоречат друг другу (Belkins и Instantly о доле ответов на первое письмо; ZenABM и Kiin Labs о TLA; Hunter и Gong о длине письма), правило должно предлагать тест, а не выбирать сторону.
- Многие платформенные кейсы (LinkedIn: O'Reilly, Payhawk, Atlassian; Chili Piper) не указывают год. В JSON для них `year: null`, придумывать год мы не стали.

### Gaps
- Не удалось открыть оригинальный PDF Gong «7 Laws of Highly Effective Sales Emails» (404). Точные проценты по CTA остались только во вторичных источниках.
- Не удалось открыть статью Marketing Science о размере реферальной награды (403) и кейс Neo4j на Think with Google (JavaScript-рендеринг).
- Независимых репликаций для бенчмарков Metadata, Lavender, Belkins не найдено.
