# Earned media: что делает событие новостью, почему журналисты пишут о компаниях и как оценить PR-идею до запуска (заметки исследования, октябрь 2026)

**Легенда доказательности.**
- **[STRONG]** — рецензируемое исследование, официальная статистика или факт, подтверждённый несколькими независимыми СМИ.
- **[MEDIUM]** — качественные деловые СМИ, отраслевые базы (WARC, Marketing Week), данные третьих сторон (Similarweb, YouGov).
- **[VENDOR]** — самоотчёт бренда, агентства, наградной заявки или PR-платформы (Cision, Muck Rack). Методика непрозрачна, интерес заинтересованный.
- **[WEAK]** — блоги, самоописания, студенческие работы.

**Сопутствующий файл:** библиотека из 45 кейсов `cases_earned_media.json` в этой же папке. 35 — глобальные/США/ЕС, 10 — РФ/СНГ. 6 — чистые анти-паттерны, ещё 2 со смешанным или обратным эффектом (Cybertruck, Domino's Россия).

**Методические оговорки.**
- (1) WebFetch в этой среде не резолвил DNS, поэтому большинство кейсов проверено по поисковой выдаче с краткими пересказами (`source_seen: search_snippet`). Полностью прочитаны 5 страниц кейсов, статья Harcup & O'Neill (2016/2017), статья Berger & Milkman (2012), пресс-релиз Cision 2025, обзор Muck Rack 2026 (через UMN) и гид по маркировке рекламы.
- (2) Библиотека — выборка выживших: провалы, о которых никто не написал, в неё не попадают по определению.
- (3) Почти все метрики «impressions», «earned media value» и рост продаж — самоотчёты брендов и агентств, часто для наградных заявок.

---

## 1. Что делает событие новостью: академические «news values»

### Takeaway
Классика (Galtung & Ruge, 1965) и её обновления (Harcup & O'Neill, 2001 и 2016/2017) сходятся в главном. Событие попадает в новости, если удовлетворяет нескольким критериям сразу: чем больше критериев, тем выше шанс. В британской прессе 2014 года лидируют «плохие новости», «сюрприз» и «развлечение». В соцсетях лидируют «развлечение» и «сюрприз», а «власть и элита» почти не работают. В современный список официально добавлены **эксклюзивность, конфликт, аудиовизуальность и шерабельность**. Для бизнеса это прямой рецепт: эксклюзивные данные + сюрприз + сильная картинка + повод для шеринга.

### Cited Findings
- **Galtung & Ruge (1965), «The Structure of Foreign News», Journal of Peace Research 2(1): 64–91** — считается первым эмпирическим исследованием критериев отбора новостей. Материал: освещение кризисов в Конго, на Кубе и Кипре в четырёх норвежских газетах. Предложено 12 «новостных факторов»:
  - частота: событие укладывается в цикл выпуска СМИ;
  - порог интенсивности;
  - однозначность;
  - значимость, или культурная близость;
  - консонанс: соответствие ожиданиям СМИ;
  - неожиданность;
  - продолжение уже идущей истории;
  - композиция: баланс выпуска;
  - отсылка к элитным нациям;
  - отсылка к элитным персонам;
  - персонификация;
  - негатив.
  — [DOI](https://doi.org/10.1177/002234336500200104); [Wikipedia: News values](https://en.wikipedia.org/wiki/News_values) [STRONG]
- **Три гипотезы Galtung & Ruge:**
  - аддитивность: чем больше факторов, тем выше вероятность попасть в новости;
  - комплементарность: факторы взаимозаменяемы;
  - исключение: событие с очень малым числом факторов в новости не попадёт.

  Ту же статью описывает «цепочку» новостной коммуникации: отбор → «искажение» (акцентирование новостных факторов) → тиражирование. — [Wikipedia: News values](https://en.wikipedia.org/wiki/News_values) [STRONG]
- **Сам Galtung позже говорил,** что СМИ неверно истолковали его работу и стали слишком негативными, сенсационными и конфликтными. — [Wikipedia: News values](https://en.wikipedia.org/wiki/News_values) [MEDIUM]
- **Harcup & O'Neill (2001), «What is news? Galtung and Ruge revisited», Journalism Studies 2(2): 261–280.** Контент-анализ трёх ведущих британских газет, выборочный месяц 1999 года. Предложено 10 ценностей:
  1. the power elite (власть и элита);
  2. celebrity;
  3. entertainment;
  4. surprise;
  5. bad news;
  6. good news;
  7. magnitude (масштаб);
  8. relevance;
  9. follow-up;
  10. newspaper agenda.

  Новое по сравнению с 1965 годом: рост роли знаменитостей и значимость «хороших новостей». — [Harcup & O'Neill 2016, PDF](https://besmart.uny.ac.id/v2/pluginfile.php/1009991/mod_resource/content/1/News%20Value_harcup2016.pdf) [STRONG]
- **Harcup & O'Neill, «What is news? News values revisited (again)».** Journalism Studies, онлайн 01.03.2016, печатная версия 2017, 18(12): 1470–1488, DOI 10.1080/1461670X.2016.1150193.
  - **Выборка:** 711 главных (page-lead) материалов 10 британских национальных газет (The Sun, Daily Mail, Telegraph, Mirror, Express, Times, Guardian, Independent, Metro, Evening Standard) за выборочную неделю ноября 2014 года.
  - **Отдельно:** 25 самых шерящихся британских новостей 2014 года (топ-10 Facebook и топ-15 Twitter).

  — [PDF статьи](https://besmart.uny.ac.id/v2/pluginfile.php/1009991/mod_resource/content/1/News%20Value_harcup2016.pdf); [Huddersfield eprints](https://eprints.hud.ac.uk/id/eprint/27268/) [STRONG]
- **Ранжирование ценностей в печатной выборке (711 материалов), по частоте:**

  | Место | Ценность | Число материалов |
  |---|---|---|
  | 1 | bad news | 442 |
  | 2 | surprise | 345 |
  | 3 | entertainment | 332 |
  | 4 | follow-up | 221 |
  | 5 | power elite | 216 |
  | 6 | relevance | 209 |
  | 7 | magnitude | 165 |
  | 8 | celebrity | 145 |
  | 9 | good news | 137 |
  | 10 | newspaper agenda | 51 |

  — [PDF статьи, табл. 2](https://besmart.uny.ac.id/v2/pluginfile.php/1009991/mod_resource/content/1/News%20Value_harcup2016.pdf) [STRONG]
- **Ранжирование среди 25 самых шерящихся новостей:**

  | Место | Ценность | Число |
  |---|---|---|
  | 1 | entertainment | 17 |
  | 2 | surprise | 16 |
  | 3 | bad news | 14 |
  | 4 | follow-up | 9 |
  | 5 | relevance | 8 |
  | 6 | magnitude | 7 |
  | =7 | celebrity | 5 |
  | =7 | good news | 5 |
  | 9 | power elite | 3 |
  | 10 | agenda | 2 |

  Самые популярные онлайн-истории «редко касаются власти и элиты». Визуально сильные материалы (замёрзший маяк, видео о готовке для питомцев) лидировали и в Facebook, и в Twitter. — [PDF статьи, табл. 3](https://besmart.uny.ac.id/v2/pluginfile.php/1009991/mod_resource/content/1/News%20Value_harcup2016.pdf) [STRONG]
- **Итоговый список 2016/2017** (истории должны удовлетворять «одному, а лучше нескольким» требованиям):
  - **Эксклюзивность** — истории, сгенерированные изданием или доступные ему первым: интервью, письма, расследования, опросы.
  - **Плохие новости.**
  - **Конфликт** — споры, расколы, забастовки, столкновения.
  - **Сюрприз** — неожиданное, контраст, необычное.
  - **Аудиовизуальность** — яркие фото, видео, аудио или возможность проиллюстрировать инфографикой.
  - **Шерабельность** — вероятность шеринга и комментариев в соцсетях.
  - **Развлечение** — шоу-бизнес, спорт, человеческий интерес, животные, юмор, «списки».
  - **Драма** — побеги, поиски, спасения, суды.
  - **Follow-up.**
  - **Власть и элита** — включая корпорации.
  - **Релевантность.**
  - **Масштаб** — число затронутых людей или экстремальность события.
  - **Знаменитости.**
  - **Хорошие новости** — прорывы, победы, излечения.
  - **Повестка издания.**

  — [PDF статьи](https://besmart.uny.ac.id/v2/pluginfile.php/1009991/mod_resource/content/1/News%20Value_harcup2016.pdf) [STRONG]
- **Данные можно сделать новостью без «пега».** Harcup & O'Neill со ссылкой на Dick (2014) отмечают: то, что не считается новостью само по себе (нет нового новостного «повода»), может стать популярным, если данные за период подать инфографикой. — [PDF статьи](https://besmart.uny.ac.id/v2/pluginfile.php/1009991/mod_resource/content/1/News%20Value_harcup2016.pdf) [STRONG]
- **Schultz (2007), цитируется у Harcup & O'Neill:** доминируют шесть ценностей — своевременность, релевантность, идентификация, конфликт, сенсация, эксклюзивность. — [PDF статьи](https://besmart.uny.ac.id/v2/pluginfile.php/1009991/mod_resource/content/1/News%20Value_harcup2016.pdf) [STRONG]
- **Авторы подчёркивают:** таксономия — инструмент анализа, а не закон. Отбор зависит от ресурсов, времени, аудитории и давления кликов. Рекламодатели и коммерческие интересы влияют на отбор (со ссылкой на Lewis, Williams & Franklin 2008). — [PDF статьи](https://besmart.uny.ac.id/v2/pluginfile.php/1009991/mod_resource/content/1/News%20Value_harcup2016.pdf) [STRONG]

### Inferences
- **Перевод на язык библиотеки кейсов** (поле `news_values` в JSON):
  - `exclusive_data` ≈ эксклюзивность;
  - `conflict` и `david_vs_goliath` ≈ конфликт и драма;
  - `surprise`, `humor_absurd` ≈ сюрприз и развлечение;
  - `visual`, `spectacle` ≈ аудиовизуальность;
  - `celebrity`, `human_vs_machine` ≈ знаменитости, элита и драма;
  - `timeliness` ≈ follow-up и частота, то есть привязка к идущей истории;
  - `first_or_record` ≈ масштаб и сюрприз;
  - `moral_stance`, `utility` ≈ релевантность и хорошие новости.
- **Гипотеза аддитивности наблюдается в библиотеке.** В 39 «успешных или смешанных» кейсах в среднем 4,1 тега ценностей на кейс, в 6 анти-паттернах — 3,3. Это авторская разметка, а не независимое измерение, поэтому вывод иллюстративный, а не доказательный.
- **Самые частые теги в библиотеке:** surprise (29 из 45), humor_absurd (21), conflict (18), timeliness (16), visual (15). Это согласуется с рейтингом Harcup & O'Neill, где сюрприз и развлечение в топ-3 и в печати, и в соцсетях.
- **Для малого бизнеса доступны все ценности, кроме «элиты» и «знаменитостей»** (их можно заменить локальными известными людьми). Эксклюзивность (свои данные, свой опрос), сюрприз, визуальность и шерабельность не требуют большого бюджета.

### Gaps
- Полный текст Galtung & Ruge (1965) не загрузился (PDF на eclass.uoa.gr отдал HTML). Список 12 факторов приведён по канонической версии и Wikipedia и частично подтверждён выдачей.
- Сопоставимых исследований новостных ценностей российских СМИ не найдено. Применимость британских рангов к российским изданиям и Telegram-каналам не проверена.

---

## 2. Что делает контент вирусным (шеринг) — эмоции, польза, STEPPS

### Takeaway
Самое цитируемое исследование (Berger & Milkman, 2012; почти 7 000 статей NYT) показывает: шеринг двигают **эмоции высокой активации**, как положительные (восхищение, awe), так и отрицательные (гнев, тревога). Эмоции низкой активации, прежде всего грусть, шеринг снижают. Практическая польза и «интересность» тоже сильно повышают распространение. Модель STEPPS Бергера (социальная валюта, триггеры, эмоции, публичность, практическая ценность, истории) — популярный практический каркас, но в найденных источниках он подтверждён в основном пересказами книги.

### Cited Findings
- **Berger & Milkman, «What Makes Online Content Viral?», Journal of Marketing Research (2012; препринт © 2011 AMA).**
  - **Данные:** 6 956 статей с главной страницы nytimes.com за 30.08–30.11.2008. 20% из них попали в список самых пересылаемых по почте. Контролировались позиция на главной странице, время, автор, длина и раздел. — [PDF статьи](https://qubeshub.org/app/site/collections/4299/Berger__Milkman.pdf) [STRONG]
- **Изменение вероятности попасть в «most emailed» при росте характеристики на одно стандартное отклонение:**

  | Характеристика | Изменение |
  |---|---|
  | гнев | +34% |
  | awe (восхищение, благоговение) | +30% |
  | практическая ценность | +30% |
  | интерес | +25% |
  | тревога | +21% |
  | время в топе главной страницы | +20% |
  | эмоциональность | +18% |
  | сюрприз | +14% |
  | позитивность | +13% |
  | грусть | −16% |

  Эффект +1 SD гнева равен дополнительным 2,9 часа в позиции главной истории сайта, что почти в 4 раза больше среднего времени в этой позиции. — [PDF статьи, рис. 2](https://qubeshub.org/app/site/collections/4299/Berger__Milkman.pdf) [STRONG]
- **Лабораторные эксперименты в той же статье.** Ролики и истории (об ад-кампании и опыте обслуживания) с большей долей веселья или гнева шерят охотнее. Эффект опосредован уровнем физиологической активации (arousal). Грусть снижает шеринг. — [PDF статьи](https://qubeshub.org/app/site/collections/4299/Berger__Milkman.pdf) [STRONG]
- **STEPPS (J. Berger, «Contagious: Why Things Catch On»):**
  - Social currency — делиться тем, что делает делящегося «умным» или «крутым»;
  - Triggers — привязка к повседневным триггерам, «top of mind, tip of tongue»;
  - Emotion — «when we care, we share»;
  - Public — видимое копируется;
  - Practical value — полезное;
  - Stories — идея внутри истории.

  — [SmartCompany](https://www.smartcompany.com.au/business-advice/contagious-jonah-berger-on-why-things-catch-on/); [Shortform](https://www.shortform.com/blog/stepps-marketing/) [MEDIUM: пересказ книги]
- **Шерабельность у журналистов.** Harcup & O'Neill цитируют бывшего редактора сайта Guardian Джанин Гибсон: самые шерящиеся истории — это «то, что заставляет смеяться, и то, что заставляет злиться». — [PDF Harcup & O'Neill](https://besmart.uny.ac.id/v2/pluginfile.php/1009991/mod_resource/content/1/News%20Value_harcup2016.pdf) [STRONG]
- **Пример в кейсах — Moldy Whopper.** Brandwatch за две недели: 59,2% упоминаний с тональностью негативные, доминирующая эмоция — отвращение (высокая активация). Агентство при этом заявляет рост продаж на 14% (другие источники — на 4%). — [Brandwatch](https://www.brandwatch.com/?p=145954); [WPP](https://www.wpp.com/en/case-studies/david---burger-king-moldy-whopper) [MEDIUM / VENDOR]

### Inferences
- **Для PR-идеи важна сила реакции, а не её знак.** Восторг, смех и даже управляемое негодование (против несправедливости или скучной нормы категории) распространяются. Грусть и «тихая трогательность» распространяются хуже.
- **Гнев — мощный, но опасный двигатель.** В анти-кейсах (Pepsi, BK Россия, ВкусВилл, Bud Light) гнев аудитории был направлен на сам бренд. В успешных (Whopper Detour, Popeyes, Ситимобил и кот Виктор) — на «общего противника» или норму категории.
- **Практическая ценность (+30%) по силе сопоставима с awe.** Поэтому дата-PR (индексы, «итоги года», локальные исследования) распространяется без шока.

### Gaps
- Исследование Berger & Milkman — шеринг статей NYT по email в 2008 году. Перенос на TikTok, Telegram и «ВКонтакте» 2026 года прямо не проверен. Российских аналогов не найдено.
- Первичных исследований, валидирующих STEPPS как целостную модель, в рамках поиска не найдено.

---

## 3. Как журналисты выбирают истории и чего ждут от PR; связь earned media с продажами

### Takeaway
Опросы журналистов, которые проводят PR-платформы ([VENDOR]), стабильно показывают одно и то же. Главный фильтр — **релевантность теме и аудитории автора**: около 86% отклоняют нерелевантный питч. Ценятся доступ к спикерам и **оригинальные данные** (40% в Muck Rack 2026), а пресс-релизы остаются полезным инструментом (72% в Cision 2025). Академически подтверждено, что заметная доля новостей опирается на PR-материалы. Earned media в традиционных СМИ даёт наибольший эффект на продажи в расчёте на одно упоминание, но соцсети выигрывают частотой (Stephen & Galak, 2012). Метрика AVE («рекламный эквивалент») профессиональными стандартами измерения не признаётся мерой ценности.

### Cited Findings
- **Cision, 2025 State of the Media** [VENDOR]: более 3 000 журналистов, 19 рынков.
  - 86% сразу отклоняют питч, не совпадающий с их темой или аудиторией.
  - 72% называют пресс-релизы самым полезным ресурсом от PR; с мультимедиа эффект «значительно выше».
  - Больше половины используют генеративный ИИ, при этом 72% опасаются фактических ошибок в PR-контенте, созданном ИИ.
  - 85% считают лучшим способом знакомства простое письмо-представление даже без питча.

  — [Cision, пресс-релиз 07.05.2025](https://www.cision.com/about/press-releases/2025-press-releases/cisions-2025-state-of-the-media-report-reveals-a-tipping-point-for-trust-technology-and-pr-journalist-partnerships-302448410/)
- **Cision, 2026 State of the Media** [VENDOR]: 66% журналистов опираются на PR-контент (пресс-релизы, питчи, медиа-киты) в поиске идей. В питчах больше всего ценятся оригинальные исследования, доступ к экспертам и эмбарго-информация; проценты в выдаче не приведены. — [AAP/Cision 13.05.2026](https://www.aap.com.au/aapreleases/cision20260513ae56180/)
- **Muck Rack, State of Journalism 2026** [VENDOR], пересказ Университета Миннесоты:
  - 86% журналистов говорят, что хотя бы часть их работы началась с PR-питча;
  - 43% редко получают релевантные питчи;
  - ценнее всего в питче: релевантность теме (70%), доступ к спикерам (58%), оригинальные данные или исследования (40%), фото высокого разрешения (37%);
  - 62% предпочитают индивидуальное письмо;
  - 78% — до полудня;
  - 69% — питч короче 200 слов.

  — [UMN University Marketing Communications](https://umarcomm.umn.edu/blog/2026/04/13/pitching-journalists-muck-racks-state-journalism-2026)
- **Muck Rack 2025** [VENDOR]: размер выборки в источниках расходится (1 890 или «более 1 500»). Вторичный обзор утверждает, что журналисты стали предпочитать эксклюзивы оригинальным исследованиям; по первоисточнику не подтверждено. — [PR News](https://www.prnewsonline.com/the-state-of-journalism-in-2025-insights-to-optimize-your-media-relations/); [BuzzStream](https://www.buzzstream.com/?p=10444)
- **Lewis, Williams & Franklin (2008), «A compromised Fourth Estate? UK news journalism, public relations and news sources», Journalism Studies 9(1): 1–20.** Классическая работа о зависимости британской прессы от PR и агентских материалов; на неё опирается концепция «churnalism» Ника Дэвиса. Часто цитируемую цифру «54% материалов» в найденных источниках подтвердить не удалось. Из того же исследования приводится, что 92% опрошенных журналистов используют больше PR-материалов, чем раньше (через блог, [WEAK]). — [Cardiff ORCA](https://orca.cardiff.ac.uk/id/eprint/18259/); [Research Fortnight / City](https://city-test.eprints-hosting.org/id/eprint/12298/1/St%20Louis%20%20Research%20Fortnight%2023%20Jan%202013%20Don%27t%20let%20the%20PR%20industry%20annex%20Science%20Journalism.pdf) [STRONG по факту работы / WEAK по цифрам]
- **Stephen & Galak (2012), «The Effects of Traditional and Social Earned Media on Sales: A Study of a Microlending Marketplace», Journal of Marketing Research 49(5).**
  - **Данные:** 14 месяцев продаж (займов) и упоминаний Kiva.org.
  - **Эффект на одно упоминание:** у традиционных СМИ (пресса, ТВ, радио) самый большой, около 894 продаж новым клиентам и 403 повторных на единицу публикации. Блог даёт около 90/63, сообщество — около 99/48.
  - **Совокупный эффект:** соцсети выигрывают за счёт частоты.
  - **Взаимосвязь:** social earned media подталкивает традиционную.

  Цифры взяты из пресс-релиза Carnegie Mellon. — [CMU News, 09.11.2012](https://www.cmu.edu/news/stories/archives/2012/november/nov9_socialmedia.html) [STRONG: рецензируемая статья; цифры через пресс-релиз]
- **Barcelona Principles 3.0 (AMEC, 2020)** сохраняют позицию, что AVE не измеряет ценность коммуникаций. По глобальному опросу членов AMEC, лишь 3% практиков считают AVE релевантной для оценки. Источники расходятся в тоне: CARMA пишет, что тема AVE «осталась в обсуждении». — [MediaGuru (cz)](https://www.mediaguru.cz/clanky/2020/12/mereni-pr-komunikace-metrika-ave-ustupuje-do-pozadi/); [CARMA](https://carma.com/tms/barcelona-principles-get-a-facelift/); [Open University](https://business-school.open.ac.uk/alumni/professional-knowledge-bank/barcelona-principles) [MEDIUM]
- **Независимые данные часто расходятся с самоотчётами.** IHOb: руководство заявило 32,3 млрд earned impressions, 20 000 статей и рост продаж бургеров в 4 раза. Данные Foursquare не показали значимого роста посещений; YouGov зафиксировал рост доли людей, обсуждавших бренд, с 19% до 30%. — [Marketing Dive](https://marketingdive.com/news/ihops-burger-sales-jumped-4x-following-controversial-name-change-stunt/529378); [FSR Magazine](https://www.fsrmagazine.com/chain-restaurants/did-ihops-ihob-campaign-drive-sales-results-are) [MEDIUM]

### Inferences
- **Отбор работает в два этапа.** Сначала журналист фильтрует по релевантности своей теме: это не news value события, а соответствие конкретному автору. Затем работают news values. Сильная идея, отправленная не тому журналисту, проваливается так же, как слабая.
- **«Оригинальные данные» прямо востребованы** (40% у Muck Rack, топ-ценности у Cision 2026) и при этом дёшевы для малого бизнеса: есть собственная статистика или небольшой опрос.
- **Цифры EMV и AVE в кейсах** (Popeyes $65 млн, Moldy Whopper $40 млн, Whopper Detour $37–40 млн) нельзя сравнивать с медиабюджетами как эквивалент денег. Для бизнес-решений нужны продажи, регистрации, брендовый поиск и прямой трафик против контрольного периода или региона.

### Gaps
- Полные отчёты Cision и Muck Rack не прочитаны: цифры взяты из пресс-релизов и вторичных обзоров. Это вендорские опросы с самоотбором респондентов.
- Не найдено опросов российских журналистов о том, что они хотят от PR (например, от Pressfeed, «Медиалогии», АКОС). Это ключевой пробел для РФ.
- Цифра «54%» из Lewis et al. (2008) не подтверждена.

---

## 4. Повторяющиеся формулы: что объединяет 45 кейсов

### Takeaway
Кейсы сводятся примерно к 12 повторяющимся формулам. Почти все успешные сочетают **3–5 новостных ценностей** (аддитивность). Почти всегда есть **сюрприз** (нарушение ожиданий категории) и **одна картинка или фраза**, понятная без объяснений. Часто есть **вторая волна**: реакция на трюк становится новостью отдельно (футболки Oatly для хейтеров, упавший сервер DSC, досрочное закрытие акции Domino's, продажа сайта Glitter). Большой бюджет не обязателен: Wendy's, Oreo, Ситимобил, DSC, Liquid Death и Glitter стоили от нуля до нескольких тысяч долларов. Самые дорогие кейсы (Stratos, Супербоул, космос) покупают **масштаб и рекорд**, а не сам факт попадания в СМИ.

### Cited Findings
**P1. «Человек против машины».** Узнаваемый чемпион, бинарный исход, первая победа.
- IBM Deep Blue: матч 1996 года IBM сама оценила более чем в $250 млн «бесплатной рекламы». — [UAlberta](https://webdocs.cs.ualberta.ca/~jonathan/PREVIOUS/Grad/Papers/db.html)
- IBM Watson и Jeopardy!: трафик ibm.com +556% за месяц, по самоотчёту. — [Love the Work](https://lovethework.com/work-awards/entries/watson-242031)
- DeepMind AlphaGo: «более 200 млн зрителей», по данным DeepMind. — [DeepMind](https://deepmind.google/research/breakthroughs/alphago/)
- Бот OpenAI против Dendi на TI 2017. — [OpenAI](https://openai.com/index/dota-2)

**P2. Рекорд или «первый» в прямом эфире.**
- Red Bull Stratos: более 8 млн одновременных зрителей, рекорд Guinness. — [Guinness](https://www.guinnessworldrecords.com/world-records/105276-most-concurrent-views-for-a-live-event-on-youtube)
- Tesla Roadster на Falcon Heavy: более 2,3 млн одновременных зрителей. — [Space.com](https://www.space.com/39612-spacex-starman-tesla-roadster-live-views.html)
- #NuggsForCarter: рекорд ретвитов, 3,42 млн. — [Twitter Blog](https://blog.twitter.com/2017/nuggsforcarter-is-now-the-most-retweeted-tweet-of-all-time)

**P3. Демо продукта как зрелище или экстремальный тест.**
- Blendtec: рост продаж на 700%, по заявлению компании. — [BYU Magazine](https://magazine.byu.edu/article/will-it-blend)
- Volvo Epic Split: более 114 млн просмотров. — [The Drum](https://www.thedrum.com/news/2022/06/14/world-s-best-ads-ever-38-van-damme-volvo-combo-runway-success-with-epic-split)
- «Яндекс» на CES 2019. — [TechInsider](https://www.techinsider.ru/vehicles/news-451772-yandeksu-razreshili-ispolzovat-bespilotniki-na-dorogah-nevady/)
- Открытое демо ChatGPT: 1 млн пользователей за 5 дней, по Альтману. — [Interesting Engineering](https://interestingengineering.com/innovation/fastest-growing-app-chatgpt-tiktok-and-instagram)
- Обратная сторона, провал демо: Cybertruck, акции −6,1% на следующий день. — [Fortune](https://fortune.com/2019/11/25/elon-musk-tesla-cybertruck-200000-orders)

**P4. Давид против Голиафа и троллинг лидера.**
- Dollar Shave Club против Gillette: $4 500 → 12 000 регистраций за 48 часов. — [Entrepreneur](https://www.entrepreneur.com/growing-a-business/how-a-dollar-shave-clubs-ad-went-viral/224282)
- Whopper Detour: 1,5 млн загрузок, по данным BK. — [Adweek](https://www.adweek.com/creativity/whopper-detour-burger-kings-masterpiece-of-trolling-wins-direct-grand-prix-at-cannes/)
- Popeyes против Chick-fil-A. — [QSR](https://www.qsrmagazine.com/fast-food/just-how-big-deal-was-popeyes-chicken-sandwich)
- «Ситимобил» на стороне хозяина кота Виктора против «Аэрофлота». — [AdIndex](https://adindex.ru/news/creative/2019/11/13/277018.phtml)

**P5. Эксклюзивные данные: индекс, исследование, «итоги года».**
- Spotify Wrapped: 50+ млн шерингов в 2020 году, по наградной заявке. — [D&AD](https://www.dandad.org/work/d-ad-awards-archive/your-2020-wrapped)
- Городские исследования Airbnb. — [HR&A](https://hraadvisors.com/?p=3102)
- OkCupid OkTrends: около 1 млн уникальных просмотров на пост. — [Contently](https://contently.com/2014/07/29/oktrends-the-greatest-brand-blog-ever-is-back-heres-why-it-went-away)
- «Лаборатория Касперского» и Flame. — [Kaspersky](https://www.kaspersky.com/about/press-releases/2012_kaspersky-lab-and-itu-research-reveals-new-advanced-cyber-threat)
- СберИндекс. — [Коммерсантъ](https://www.kommersant.ru/doc/8194524)
- Открытые результаты «Додо». — [Spot.uz](https://www.spot.uz/ru/2022/07/05/dodopizza/)
- Обратная сторона: Strava Heatmap раскрыла военные базы. — [NBC](https://www.nbcnews.com/news/amp/ncna841871)

**P6. Моральная позиция или парадокс** (бренд говорит против собственной выгоды).
- Patagonia «Don't Buy This Jacket». — [Patagonia](https://www.patagonia.ca/story-18615.html)
- Яма Cards Against Humanity: $100 573. — [NPR](https://www.npr.org/sections/thetwo-way/2016/11/27/503502142/people-donated-nearly-100-000-to-dig-a-big-pointless-hole-in-the-ground)
- Fearless Girl: 3–4 Гран-при Cannes Lions. — [Fortune](https://fortune.com/2017/06/20/fearless-girl-cannes-awards)
- Moldy Whopper. — [WPP](https://www.wpp.com/en/case-studies/david---burger-king-moldy-whopper)
- Обратная сторона:
  - Pepsi и Дженнер. — [CBC](https://www.cbc.ca/lite/story/1.4056850)
  - Bud Light: выручка AB InBev в США −9,5% за 2023 год. — [Fox Business](https://foxbusiness.com/markets/bud-light-remains-drag-parent-dylan-mulvaney-hit-lingers)
  - ВкусВилл. — [Новая газета](https://novayagazeta.ru/articles/2021/07/04/vkusvill-udalil-reklamu-s-lgbt-paroi-i-izvinilsia-za-nee)

**P7. Абсурдный юмор и «бренд-мир» в скучной категории.**
- Liquid Death: ролик за $1 500, около 3 млн просмотров. — [Wikipedia](https://en.wikipedia.org/wiki/Liquid_Death)
- Сова Duolingo «умерла»: загрузки Android +38% на следующий день, по Similarweb. — [TechCrunch](https://techcrunch.com/2025/02/18/duolingo-killed-its-mascot-with-a-cybertruck-and-its-going-weirdly-well/)
- Squatty Potty: онлайн-продажи +600%, по словам CEO. — [Utah Business](https://www.utahbusiness.com/potty-talk-marketing-unconventional-product/)
- ShipYourEnemiesGlitter: продан за $85 000. — [SlashGear](https://www.slashgear.com/shipyourenemiesglitter-com-owner-selling-site-tired-of-dealing-with-glitter-18365110/)
- Самолётик Авиасейлс в Blink: 1,5+ млрд органических просмотров UGC, по данным бренда. — [Sostav](https://www.sostav.ru/publication/kejs-blink-i-aviasejls-kak-prevratit-reklamu-na-3d-karte-v-virusnyj-trend-86553.html)

**P8. Ньюсджекинг в реальном времени.**
- Oreo во время блэкаута: около 15 000 ретвитов за час. — [Digiday](https://digiday.com/marketing/oral-history-oreo-tweet/)
- «Ситимобил» и кот Виктор. — [AdIndex](https://adindex.ru/news/creative/2019/11/13/277018.phtml)
- Обратная сторона: Burger King Россия на ЧМ-2018. — [Gulf News](https://m.gulfnews.com/news/europe/burger-king-russia-apologises-for-world-cup-impregnation-ad-1.2240083)

**P9. Самоирония и честность в кризисе.**
- KFC «FCK». — [Marketing Week](https://www.marketingweek.com/kfc-print-advert-to-apologise-for-chicken-shortage/)
- Ryanair в TikTok. — [PPC Land](https://ppc.land/is-ryanair-going-soft-the-sarcasm-that-built-a-brand-may-be-fading/)
- Oatly превратила хейт в мерч. — [Fox News](https://www.foxnews.com/food-drink/oatlys-super-bowl-commercial-shirt-haters-out-stock-24-hours.amp)
- Вне JSON: Domino's US «Pizza Turnaround» (2009–2010) — публичное признание критики пиццы. WARC приводит рост сопоставимых продаж на 14,3% в Q1 2010 года, «крупнейший квартальный рост в истории фастфуда». — [WARC](https://www.warc.com/content/article/dominos-pizza-turnaround/en-gb/94400) [MEDIUM]

**P10. Фейковое изменение, интрига или «смерть» символа бренда.**
- IHOb. — [Marketing Dive](https://marketingdive.com/news/ihops-burger-sales-jumped-4x-following-controversial-name-change-stunt/529378)
- Сова Duo. — [TechCrunch](https://techcrunch.com/2025/02/18/duolingo-killed-its-mascot-with-a-cybertruck-and-its-going-weirdly-well/)

**P11. Экстремальный обмен или конкурс.**
- Domino's Россия «100 пицц в год на 100 лет за тату»: закрыли досрочно через несколько дней, лимит 350, по vc.ru 381 победитель, позже налоговые уведомления на НДФЛ около 4 000 руб. — [The Moscow Times](https://www.themoscowtimes.com/2018/09/05/russians-tat-up-for-a-lifetime-of-pizza-a62776); [vc.ru](https://vc.ru/59995)
- Вне JSON: Burger King «Whopper Sacrifice» (2009) — удали 10 друзей в Facebook и получи Воппер. Удалено 233 906 «друзей»; Facebook отключил уведомления удалённым из-за нарушения своих правил приватности, и акция закрылась. — [MediaPost](https://www.mediapost.com/publications/article/98464/burger-king-kills-whopper-sacrifice-campaign.html) [MEDIUM]

**P12. Громкие покровители и миссия.**
- Запуск OpenAI: заявленные обязательства около $1 млрд, позже выяснилось, что фактически внесено существенно меньше. — [TechCrunch](https://techcrunch.com/2015/12/11/non-profit-openai-launches-with-backing-from-elon-musk-and-sam-altman)

**Дополнительные примеры вне JSON:**
- **Pizza Hut доставила пиццу на МКС (2001).** Логотип был на ракете «Протон», стоимость около $1 млн. Пиццу съел космонавт Юрий Усачёв. — [AOL](https://www.aol.com/wild-story-pizza-hut-got-165446435.html); [Spaceflight Now](https://spaceflightnow.com/station/stage6a/010523food) [MEDIUM]
- **Dove Real Beauty Sketches (2013).** Guinness: самая просматриваемая онлайн-реклама, 124 875 719 просмотров на 02.11.2013. — [Guinness](https://www.guinnessworldrecords.com/world-records/most-viewed-online-video-advertisement) [STRONG]
- **Old Spice Response (2010).** 186 персональных роликов за 2,5 дня. Продажи геля +107% после роликов-ответов, по данным Nielsen в наградной заявке. — [Love the Work](https://lovethework.com/work-awards/campaigns/deodorant-and-body-wash-264386) [VENDOR]

### Inferences
- **Общие «молекулы» успешных кейсов:**
  1. **Нарушение ожидания категории** — сюрприз: блендер ломает iPhone, вода «убивает жажду», бургер в плесени, бренд просит не покупать.
  2. **Бинарный или измеримый исход** — победил или нет, рекорд или нет, набрали 50 млрд XP или нет.
  3. **Одна картинка или фраза**, понятная в заголовке.
  4. **Повод по времени**: Супербоул, Чёрная пятница, 8 марта, ЧМ, CES, выход iPhone, конец года.
  5. **Механика участия**: ретвиты, XP, загрузки, поиск объекта, татуировки.
  6. **Право бренда на историю**: Patagonia давно о ремонте, «Касперский» — о кибербезопасности.
- **Владеть событием выгоднее, чем спонсировать его** (Stratos, Detour, Wrapped). Встроиться в чужое популярное событие дешевле всего (TI 2017, Jeopardy!, CES, Супербоул через Twitter).
- **Для малого бизнеса реалистичны в первую очередь** P5 (свои данные), P7 (юмор), P8 (локальный ньюсджекинг), P9 (честность), P3 (простой зрелищный тест), P4 (мягкий вызов лидеру). P1, P2 и P12 доступны в «локальном масштабе»: рекорд города, вызов местному эксперту, известные в нише партнёры.
- **Систематическая ошибка выборки:** в библиотеке нет трюков, которые никто не заметил. Реальная вероятность успеха любого трюка неизвестна и, вероятно, низка.

### Gaps
- Нет базы с долей «трюков без освещения» для оценки базовой вероятности успеха.
- Для большинства RU-кейсов нет измерений охвата (Медиалогия, Brand Analytics) и бизнес-эффекта. Почти нет независимых данных о малом бизнесе в РФ, получившем earned media на минимальном бюджете; найденные кейсы — крупные бренды.
- Тинькофф/Т-Банк представлен только бренд-медиа Т—Ж со слабыми данными (самооценка 26 млн читателей в месяц). Документированного «стант»-кейса Т-Банка с источниками не найдено. Для Авиасейлс найден только кейс 2026 года с самоотчётными цифрами.

---

## 5. Риски, анти-паттерны и правовые ограничения (включая РФ)

### Takeaway
Типовые провалы:
- присвоение чужой борьбы или трагедии (Pepsi);
- поляризующий жест без учёта ядра аудитории (Bud Light, ВкусВилл с двойным ударом после отречения);
- оскорбление групп (BK Россия, BK UK 8 марта 2021);
- объект, похожий на угрозу (Cartoon Network, $2 млн);
- утечка через «безобидные» данные (Strava);
- неограниченные обязательства и налоги на призы (Domino's Россия);
- нарушение правил платформы (Whopper Sacrifice);
- провал демо (Cybertruck).

В РФ к этому добавляется формальный слой: обязательная маркировка интернет-рекламы (erid, ЕРИР) со штрафами, требования закона «О рекламе», налоги на призы, законодательство о персональных данных, а также чувствительные темы с прямым юридическим риском.

### Cited Findings
- **Pepsi (2017):** ролик сняли после волны критики за тривиализацию протестов, компания извинилась («Clearly we missed the mark»). — [CBC](https://www.cbc.ca/lite/story/1.4056850) [STRONG]
- **Bud Light (2023):** выручка AB InBev в США −9,5% за 2023 год и −17,3% в Q4; Bud Light потерял первое место в США. — [Fox Business](https://foxbusiness.com/markets/bud-light-remains-drag-parent-dylan-mulvaney-hit-lingers) [STRONG]
- **Peloton (2019):** после критики рождественского ролика «The Gift That Gives Back» акции падали в течение дня до 10%. Потеря капитализации около $942 млн за день, по Business Insider через InsideHook. — [Bloomberg](https://www.bloomberg.com/news/articles/2019-12-03/peloton-backlash-over-gift-that-gives-ad-pummels-stock); [InsideHook](https://www.insidehook.com/wellness/peloton-lost-942m-of-its-market-value-in-one-day-after-controversial-ad) [MEDIUM]
- **Burger King UK (8 марта 2021):** твит «Women belong in the kitchen» был задуман как начало треда о стипендиях для женщин-поваров. Первый твит вырвали из контекста; после 12 часов споров его удалили, компания извинилась. — [Adweek](https://www.adweek.com/brand-marketing/burger-king-apologizes-and-deletes-tweet-that-said-women-belong-in-the-kitchen/) [STRONG]
- **Burger King Россия (ЧМ-2018):** приз 3 млн руб. за беременность от футболистов. Пост удалили, компания извинилась, назвав рекламу «слишком оскорбительной». — [Gulf News](https://m.gulfnews.com/news/europe/burger-king-russia-apologises-for-world-cup-impregnation-ad-1.2240083) [STRONG]
- **ВкусВилл (2021):** материал удалили; извинение подписали основатель и 11 топ-менеджеров, назвав публикацию ошибкой «отдельных сотрудников». Аудитория разделилась, семья-героиня уехала из страны. — [Новая газета](https://novayagazeta.ru/articles/2021/07/04/vkusvill-udalil-reklamu-s-lgbt-paroi-i-izvinilsia-za-nee); [Zona.media](https://zona.media/news/2021/08/03/lgbtvkus) [STRONG]
- **Cartoon Network (2007):** $2 млн урегулирования, отставка главы канала, уголовные обвинения двум исполнителям. — [NBC News](https://www.nbcnews.com/id/16990202/) [STRONG]
- **Strava (2018):** агрегированная карта активностей раскрыла военные базы. Минобороны США начало проверку. — [NBC News](https://www.nbcnews.com/news/amp/ncna841871) [STRONG]
- **Domino's Россия (2018):** изначально не было лимита, затем ввели лимит в 350 и досрочно закрыли акцию. В 2019 году победители получили уведомления о НДФЛ (около 4 000 руб.), сообщалось о коллективном иске. — [vc.ru](https://vc.ru/59995); [Moskvich Mag](https://moskvichmag.ru/?p=304255); [Adindex](https://adindex.ru/news/adyummy/2018/09/4/174017.phtml) [MEDIUM]
- **Whopper Sacrifice (2009):** Facebook посчитал уведомления удалённым «друзьям» нарушением правил приватности и отключил механику, акция закрылась. — [MediaPost](https://www.mediapost.com/publications/article/98464/burger-king-kills-whopper-sacrifice-campaign.html) [MEDIUM]
- **Маркировка интернет-рекламы в РФ.** Закон действует с 1 сентября 2022 года, штрафы за отсутствие идентификатора — с сентября 2023 года. Реклама должна содержать пометку «Реклама», сведения о рекламодателе и токен erid, полученный до публикации через ОРД; данные передаются в ЕРИР. Маркировка нужна при любом вознаграждении, включая бартер, скидку «за пост», партнёрскую ссылку, процент с продаж. — [Kokoc Group](https://kokoc.com/blog/markirovka-reklamy/); [SecurityLab](https://www.securitylab.ru/blog/personal/SimlpeHacker/359248.php) [MEDIUM: агентские гайды; первоисточник — ст. 18.1 38-ФЗ и КоАП]
- **Штрафы по гиду Kokoc** (нормативная основа: ст. 18.1 ФЗ «О рекламе», ст. 14.3 КоАП РФ):

  | Нарушение | Физлица | ИП / должностные лица | Юрлица |
  |---|---|---|---|
  | Нет пометки «Реклама» или данных о рекламодателе | 2–2,5 тыс. ₽ | 4–20 тыс. ₽ | 100–500 тыс. ₽ |
  | Нет erid или он размещён некорректно | 30–100 тыс. ₽ | 100–200 тыс. ₽ | 200–500 тыс. ₽ |
  | Данные в ЕРИР не переданы, переданы с опозданием или недостоверны | 10–30 тыс. ₽ | 30–100 тыс. ₽ | 200–500 тыс. ₽ |

  — [Kokoc Group](https://kokoc.com/blog/markirovka-reklamy/) [MEDIUM: проверить по актуальной редакции КоАП]
- **Изменения 2025–2026 по тому же гиду:**
  - с 1 марта 2025 года социальная реклама маркируется на общих основаниях;
  - с 1 сентября 2025 года реклама на заблокированных в РФ ресурсах запрещена, и токен не освобождает от ответственности;
  - с 2025 года действует ежеквартальный сбор 3% с дохода от интернет-рекламы (база — данные ЕРИР);
  - выделение товара на собственном сайте (сквозной баннер, закреплённый пост) ФАС и Роскомнадзор могут считать саморекламой, требующей идентификатора.

  — [Kokoc Group](https://kokoc.com/blog/markirovka-reklamy/) [MEDIUM]

### Inferences
- **Earned media в строгом смысле** (журналист пишет сам, без оплаты) маркировке не подлежит. Но в РФ стант почти всегда сопровождается собственными постами бренда, посевами, блогерами, бартером и призами. Каждый такой элемент — потенциальная реклама, которой нужен erid. Граница между «информацией» и «рекламой» оценивается регулятором, и при сомнении безопаснее маркировать.
- **Юмор на грани непристойности** (Squatty Potty, Авиасейлс в Blink) и сравнение с конкурентом (Whopper Detour) в РФ требуют проверки на соответствие закону «О рекламе». По памяти исследователя это ст. 5 38-ФЗ о недобросовестной и недостоверной рекламе, некорректном сравнении, непристойных и оскорбительных образах. В этом исследовании по тексту закона не проверялось, нужен юрист.
- **Конкурсы и призы:** налоговые последствия (НДФЛ с призов сверх необлагаемого лимита) и правила проведения нужно прописать заранее. Domino's показывает, что иначе налог становится второй негативной новостью.
- **Самый дорогой риск — не провал, а «успешный» скандал против бренда:** Bud Light, Peloton, Pepsi. Малый бюджет жеста не ограничивает масштаб ущерба.

### Gaps
- Тексты 38-ФЗ «О рекламе» (ст. 5, ст. 18.1) и КоАП (ст. 14.3) напрямую не проверены. Суммы штрафов взяты из гида агентства, сверить с актуальной редакцией на consultant.ru или pravo.gov.ru.
- Правовой статус тем, связанных с ЛГБТ, и других чувствительных тем в рекламе РФ на 2026 год в этом исследовании не исследовался. Нужна отдельная юридическая проверка.
- Не найдено данных о судебной и ФАС-практике по стант-акциям малого бизнеса в РФ.

---

## 6. Скоринговая форма: как оценить PR-идею до запуска

### Takeaway
Валидированной научной модели «оценки стант-идеи» не найдено. Ниже — **предложение исследователя**, собранное из доказательной базы:
- аддитивность новостных факторов (Galtung & Ruge);
- современный список ценностей (Harcup & O'Neill 2016/2017);
- эмоции высокой активации и практическая польза (Berger & Milkman);
- что ценят журналисты: релевантность, доступ, данные, изображения (Muck Rack 2026, Cision 2025);
- паттерны и анти-паттерны 45 кейсов.

Веса — экспертное суждение, их нужно калибровать на собственной истории запусков (Moneyball-логика: записывать прогноз до запуска и сверять с фактом).

### Cited Findings
- Чем больше новостных факторов удовлетворяет событие, тем выше вероятность попасть в новости; событие почти без факторов не станет новостью. — [Wikipedia: News values](https://en.wikipedia.org/wiki/News_values) [STRONG]
- Современный список ценностей включает эксклюзивность, конфликт, сюрприз, аудиовизуальность и шерабельность; истории должны удовлетворять «одному, а лучше нескольким» требованиям. — [Harcup & O'Neill PDF](https://besmart.uny.ac.id/v2/pluginfile.php/1009991/mod_resource/content/1/News%20Value_harcup2016.pdf) [STRONG]
- Гнев +34%, awe +30%, практическая ценность +30%, интерес +25%, тревога +21%, сюрприз +14%, грусть −16% к вероятности шеринга (на +1 SD). — [Berger & Milkman PDF](https://qubeshub.org/app/site/collections/4299/Berger__Milkman.pdf) [STRONG]
- В питче журналисты ценят релевантность теме (70%), доступ к спикерам (58%), оригинальные данные (40%), фото высокого разрешения (37%); 69% хотят питч короче 200 слов. — [UMN / Muck Rack 2026](https://umarcomm.umn.edu/blog/2026/04/13/pitching-journalists-muck-racks-state-journalism-2026) [VENDOR]
- 86% журналистов отклоняют нерелевантный питч. — [Cision 2025](https://www.cision.com/about/press-releases/2025-press-releases/cisions-2025-state-of-the-media-report-reveals-a-tipping-point-for-trust-technology-and-pr-journalist-partnerships-302448410/) [VENDOR]
- Показы и упоминания не равны визитам: IHOb — миллиарды impressions, но Foursquare не увидел роста посещений. — [Marketing Dive](https://marketingdive.com/news/ihops-burger-sales-jumped-4x-following-controversial-name-change-stunt/529378) [MEDIUM]
- AVE не мера ценности коммуникаций (Barcelona Principles); только 3% практиков AMEC считают AVE релевантной. — [CARMA](https://carma.com/tms/barcelona-principles-get-a-facelift/) [MEDIUM]

### Inferences

#### 6.1. Форма «PR-идея: стоит ли делать» (100 баллов + стоп-флаги)

Каждый критерий оценивается по шкале 0 / 0,5 / 1 и умножается на вес.

**A. Новостная ценность — 40 баллов** (основа: Galtung & Ruge, Harcup & O'Neill)

| № | Критерий | Вес | Проверочный вопрос |
|---|---|---|---|
| A1 | Сюрприз / контраст / «впервые» / рекорд | 10 | Нарушает ли идея ожидание категории? Можно ли написать заголовок со словом «впервые», «самый» или «вопреки»? |
| A2 | Эксклюзивные данные или доступ | 8 | Что журналист получит только от нас: цифры, доступ на площадку, спикера, первый показ? |
| A3 | Визуальность: одна картинка объясняет всё | 6 | Что снимет фотограф? Понятен ли кадр без подписи? |
| A4 | Конфликт или Давид против Голиафа (без агрессии к людям) | 6 | Есть ли понятный «противник»: норма категории, лидер рынка, несправедливость? Направлен ли гнев не на нас и не на клиентов? |
| A5 | Повод по времени: timeliness / follow-up | 5 | Почему именно сейчас? К какому событию, сезону или идущей истории привязано? |
| A6 | Люди: знаменитость, эксперт, «человек против машины», герой-клиент | 5 | Кто лицо истории? Есть ли узнаваемый человек хотя бы на локальном уровне? |

**B. Шерабельность — 20 баллов** (основа: Berger & Milkman, STEPPS)

| № | Критерий | Вес | Проверочный вопрос |
|---|---|---|---|
| B1 | Эмоция высокой активации: смех, восторг/awe, азарт, праведное негодование против нормы | 8 | Какую одну эмоцию вызовет идея? Если «умиление» или «грусть» — минус. |
| B2 | Практическая польза или социальная валюта | 6 | Будет ли человеку полезно или «круто» переслать это другу? |
| B3 | Механика участия или UGC | 6 | Может ли аудитория что-то сделать: найти, проголосовать, повторить, «спасти»? |

**C. Связь с бизнесом — 25 баллов**

| № | Критерий | Вес | Проверочный вопрос |
|---|---|---|---|
| C1 | Продукт — герой истории (демонстрирует ключевое свойство) | 10 | Вспомнят ли через неделю, что именно продаём и чем лучше? (Blendtec — да; «просто смешно» — нет) |
| C2 | Право на позицию: история бренда подтверждает | 7 | Делали ли мы что-то в этом направлении до трюка? Готовы ли держать позицию под давлением? (урок ВкусВилла и Pepsi) |
| C3 | Путь к действию и измеримость | 5 | Куда приходит человек после статьи (страница, промокод, бот)? Какой KPI: брендовый поиск, прямой трафик, регистрации, продажи против контрольного периода? |
| C4 | Готовность к пику спроса | 3 | Выдержат ли сайт, склад и поддержка рост ×10–×100? (DSC, Glitter) |

**D. Исполнимость и контроль — 15 баллов**

| № | Критерий | Вес | Проверочный вопрос |
|---|---|---|---|
| D1 | Бюджет и масштабируемость вниз | 5 | Сработает ли «малая версия»? Есть ли бесплатные каналы усиления? |
| D2 | Контроль исхода и план Б | 5 | Что, если провалится в прямом эфире (Cybertruck)? Что, если никто не заметит? |
| D3 | Готовая «вторая волна» | 5 | Какой будет следующая новость: реакция, итог, реванш, цифры через неделю? |

**Пороги** (предложение для калибровки):
- **≥70 и ни одного стоп-флага** — делать;
- **50–69** — доработать слабые блоки, обычно A2, A3 или C1;
- **<50** — не делать;
- **любой стоп-флаг** — стоп или эскалация юристу, независимо от баллов.

**Минимальное правило аддитивности:** в блоке A должно быть не менее 3 критериев с оценкой ≥0,5.

#### 6.2. Стоп-флаги (red flags)
1. **Ложь или фабрикация:** фейковые данные, отзывы, «жертвы», поддельные документы. Это прямой юридический и репутационный риск; журналистские разоблачения вроде The Shed at Dulwich показывают, что СМИ любят именно разоблачения.
2. **Использование чужой трагедии, протеста, войны или катастрофы** как фона для продукта (Pepsi).
3. **Унижение или сексуализация групп людей,** сексизм (BK Россия, BK UK 8 марта).
4. **Политически или культурно поляризующая тема** без связи с миссией и без готовности держать позицию (Bud Light, ВкусВилл). В РФ — обязательная юридическая оценка.
5. **Безопасность:** объект или действие можно принять за угрозу, есть риск для жизни и здоровья участников или зрителей (Cartoon Network).
6. **Неограниченные или бессрочные обязательства,** призы «навсегда», отсутствие лимитов участников (Domino's Россия).
7. **Механика требует от людей необратимых действий:** татуировки, отказ от чего-то значимого.
8. **Данные клиентов:** возможна деанонимизация, не проверено соответствие 152-ФЗ (Strava).
9. **Нарушение правил платформы:** приватность, механики вовлечения (Whopper Sacrifice).
10. **РФ-формальности:**
    - нет плана маркировки для оплачиваемых элементов (erid, ЕРИР, пометка «Реклама»);
    - размещение на заблокированных ресурсах;
    - не просчитан НДФЛ с призов;
    - сравнение с конкурентом не проверено юристом.
11. **Ключевая цифра анонса не выдержит проверки** через месяц или год (обязательства OpenAI на $1 млрд против фактически внесённого).

#### 6.3. Чек-лист перед отправкой журналистам (основа: Muck Rack, Cision)
- Сформулируйте новость в заголовке до 10 слов и лиде до 200 слов (69% хотят питч короче 200 слов).
- Составьте список 5–15 конкретных авторов, которые писали на эту тему за последние 3 месяца. Релевантность — фильтр номер один: её ценят 70%, а 86% сразу отклоняют нерелевантное.
- Предложите эксклюзив одному изданию или эмбарго; подготовьте спикера, готового к интервью в день выхода (доступ ценят 58%).
- Приложите собственные данные с методикой (40%) и фото или видео высокого разрешения (37%).
- Отправляйте индивидуальное письмо (62%) до полудня (78%).
- Заранее подготовьте Q&A на неудобные вопросы и пост на случай провала.

#### 6.4. Как измерять результат (вместо AVE)
- Число публикаций в **целевых** СМИ и их качество: заголовок, упоминание продукта, ссылка.
- Рост брендового поиска (Wordstat / Google Trends), прямого трафика и регистраций против контрольного периода; по возможности сравнить с контрольным городом или регионом.
- Продажи по выделенному промокоду или лендингу; для офлайна — посещения, а не impressions (урок IHOb).
- Записывать прогноз по форме до запуска и факт после него. Через 10–20 запусков пересчитать веса по фактическим корреляциям баллов с результатом.

### Gaps
- Веса формы не валидированы эмпирически. Это экспертная сборка из доказательной базы, а не результат регрессии.
- Нет данных о доле успешных трюков среди всех попыток (base rate), поэтому прогнозная точность формы неизвестна.
- Не найдено исследований, связывающих конкретные новостные ценности с бизнес-эффектом (продажи), а не только с попаданием в СМИ или шерингом. Stephen & Galak (2012) связывают упоминания с продажами, но без разбивки по типу истории.
