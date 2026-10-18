# Empirical "Laws" of Marketing & Brand Growth — Strategic Foundation for a Data-Driven ("Moneyball") Marketing System

Research note, compiled 2026-10-18. Scope: Ehrenberg-Bass laws, Binet & Field / IPA, advertising elasticities, unit economics, customer-base (CLV) models. Note on method: several primary-source domains (ipa.co.uk, marketingscience.info, metricgate.com, alexmurrell.co.uk) were unreachable from the research environment (DNS failure), so some figures rest on secondary write-ups; these are flagged. Formulas that are purely definitional (unit economics) or standard textbook statements that could not be re-fetched in this session are placed in "Inferences" or "Gaps" with an explicit "not re-verified" flag rather than presented as cited facts.

---

## 1. Ehrenberg-Bass / Byron Sharp "How Brands Grow": Double Jeopardy, NBD-Dirichlet, Duplication of Purchase, Penetration vs Loyalty, Light Buyers, Mental & Physical Availability, Category Entry Points — evidence and criticisms

### Takeaway
The Ehrenberg-Bass "laws" (Double Jeopardy, Duplication of Purchase, Pareto ~60/20, NBD-Dirichlet stationarity) are among the best-replicated regularities in marketing and imply that brands grow mainly by increasing penetration (reaching more, mostly light, category buyers) via mental and physical availability; however, they are descriptive of stationary markets, the "loyalty can't be grown" corollary and the anti-targeting stance are contested (Ritson, Oldham, some retailer data showing more extreme Pareto), and the pattern looks more like a curve than a line.

### Cited Findings
**Double Jeopardy (DJ)**
- Canonical paper: Ehrenberg, Goodhardt & Barwise (1990), "Double Jeopardy Revisited," *Journal of Marketing* 54(3), 82–91: smaller brands have fewer buyers in a period AND those buyers buy them somewhat less often (and like them a bit less) — [Wikipedia: Double jeopardy (marketing)](https://en.wikipedia.org/wiki/Double_jeopardy_(marketing)); [DeepDyve abstract](https://www.deepdyve.com/lp/sage/double-jeopardy-revisited-M5fQR2kwNT)
- DJ has a mathematical approximation "w(1−b)" (w = average purchase frequency among brand buyers, b = penetration; the product w(1−b) ≈ constant w0 across brands in a category) that can be compared against the full NBD-Dirichlet; an LSBU "DJ 50 years on" paper explicitly sets out to "revive interest in the now somewhat overlooked mathematical derivation of Double Jeopardy, in order to compare predictions from its w(1-b) approximation with the output of the more widely adopted NBD-Dirichlet" — [LSBU Open Research, "DJ 50 Years On"](https://openresearch.lsbu.ac.uk/download/08387f082771262a1dbbd7b4de6429f49d80d28f4f39ee1795230898531e1cd8/407668/DJ%2050%20Years%20on.docx)
- Habel & Lockshin (2013, *Journal of Business Research* 66(9), 1448–1456) tested DJ across 37 cross-sectional categories and a 40-quarter longitudinal dataset: the DJ relationship is better described as an upward-sloping *curve* than a straight line — [Adelaide repository](https://digital.library.adelaide.edu.au/items/6e7be46a-99dc-448d-9fa3-e87e20a9900e); [RePEc](https://ideas.repec.org/a/eee/jbrese/v66y2013i9p1448-1456.html)
- Bemmaor (1994 commentary) argued the standard Dirichlet fails to capture DJ fully because distribution (physical availability) differs across brands — i.e., part of DJ is driven by availability differences the plain model ignores — [ESSEC faculty record](https://faculty.essec.edu/en/research/3465-commentary-on-asc-ehrenbergs-theory-or-well-based-results-which-comes-first)
- Ehrenberg-Bass has published a rebuttal piece "A short critique of 'a critique of Double Jeopardy'" (content not retrievable in this session) — [marketingscience.info](https://marketingscience.info/news-and-insights/a-short-critique-of-a-critique-of-double-jeopardy)
- DJ holds in B2B: Romaniuk, Dawes & Faghidno (May 2021) report DJ in B2B and conclude "it is not possible to sustainably grow by focusing on loyalty alone" — [Ehrenberg-Bass, "The Double Jeopardy law in B2B shows the way to grow"](https://marketingscience.info/the-double-jeopardy-law-in-b2b-shows-the-way-to-grow/)
- DJ patterns have also been reproduced in choice experiments (stated preference), not just panel data — [WARC / JMRS](https://www.warc.com/content/article/jmrs/using_choice_experiments_to_find_double_jeopardy_patterns/105506)

**NBD-Dirichlet**
- The NBD-Dirichlet is the standard repeat-purchase model predicting brand penetration, purchase frequency, share of category requirements and duplication from only category buying rate, category penetration and each brand's market share; penetration can be written b_j = 1 − Σ_r P(R = r)(1 − w_j)^r (R = number of category purchases, NBD-distributed) — [metricgate.com Dirichlet calculator, via search snippet](https://metricgate.com/calculator/dirichlet-repeat-purchase) (page itself unreachable; formula from search excerpt)
- Kantar (2020s "Decoding brand success") still uses category-specific penetration-vs-loyalty decompositions consistent with Dirichlet-style norms — [Kantar turtl](https://kantar.turtl.co/story/decoding-brand-success-p/page/3)

**Pareto / light buyers**
- "It's wrong to talk about an 80/20 law in marketing. A brand's heaviest 20% of buyers generally contribute not much more than half of a brand's sales"; ~half of sales come from the lightest 80% of buyers; the Pareto share rises with longer time windows — Sharp, Romaniuk & Graham (2019 draft, SSRN 3498097) — [LSBU Open Research PDF](https://openresearch.lsbu.ac.uk/download/8e33716ee01359e2dc575295fae393dfdb541db3cf4573a065b3a069423e027f/74869/SSRN-id3498097-2.pdf); [Ehrenberg-Bass "The value of Pareto's bottom 80%"](https://marketingscience.info/news-and-insights/value-paretos-bottom-80)
- Steenkamp's (2017) Europanel analysis reportedly put the ratio nearer 50/20 for most CPG brands — [The Daily Star summary](https://www.thedailystar.net/business/news/businesses-need-adopt-new-marketing-law-8020-rule-over-1974889) (secondary)
- Counter-evidence: a retailer dataset (Smith & Blair, Campaign Asia) found the majority of brands closer to 80/20 than HBG suggests, and smaller brands had *higher* Pareto scores; argued heavy buyers "matter more than Byron Sharp says" — [Campaign Asia](https://aws1.campaignasia.com/article/why-heavy-buyers-matter-more-than-byron-sharp-says/442271). Ehrenberg-Bass's response is that Pareto shares are mechanically more extreme for small brands and long windows, which does not imply higher loyalty (same search summary of [LSBU paper](https://openresearch.lsbu.ac.uk/download/8e33716ee01359e2dc575295fae393dfdb541db3cf4573a065b3a069423e027f/74869/SSRN-id3498097-2.pdf))
- Online brands that target only heavy buyers are "missing out" (WARC feed of an Ehrenberg-Bass online-retail study) — [WARC](https://www.warc.com/content/feed/online-brands-only-targeting-heavy-buyers-are-missing-out-says-study/en-GB/10916)

**Penetration vs loyalty; mental & physical availability**
- Sharp's thesis (building on Ehrenberg): brand growth is more likely to come from gaining new (mostly light) buyers than raising loyalty; growth therefore rests on physical availability (distribution/ease of buying) and mental availability (salience) — [WARC "Penetration vs loyalty"](https://www.warc.com/newsandopinion/opinion/warc-from-home-penetration-vs-loyalty---whats-the-best-way-for-a-brand-to-grow/3635)
- Before HBG (2010) loyalty/repeat was seen as the safe approach; WARC characterises the balance as still a "keen debate" — [WARC](https://www.warc.com/newsandopinion/opinion/warc-from-home-penetration-vs-loyalty---whats-the-best-way-for-a-brand-to-grow/3635)

**Category Entry Points (CEPs)**
- Romaniuk (July 2022): CEPs are "the cues category buyers use to access their memories when faced with a buying situation"; they determine which brands are initially mentally available — [Ehrenberg-Bass, "Category Entry Points in a B2B world"](https://marketingscience.info/news-and-insights/category-entry-points-in-a-business-to-business-b2b-world)
- Nov 2023 "How B2B Brands Grow" (Ehrenberg-Bass × LinkedIn B2B Institute) urges building more CEPs by being relevant to buying situations rather than pushing brand messages — [Ehrenberg-Bass B2B reports](https://marketingscience.info/b2b-reports/); [How B2B Brands Grow](https://marketingscience.info/news-and-insights/how-b2b-brands-grow)
- Later B2B Institute / Ehrenberg-Bass work argues physical availability ("easy to find, being where B2B buying happens") is B2B's biggest growth opportunity — [Marketing Week](https://www.marketingweek.com/b2b-growth-physical-availability/); [LinkedIn B2B Institute](https://business.linkedin.com/marketing-solutions/b2b-institute/easy-to-find-being-where-b2b-buying-happens)

**Criticisms / debates**
- Ritson v Sharp (Festival of Marketing debate): Ritson criticised Sharp's "child-like focus on science," arguing marketing is a social science; ~60% of the audience voted Ritson the winner — [Marketing Week, "Ritson versus Sharp: who won"](https://www.marketingweek.com/ritson-versus-sharp-won-clash/)
- Ritson: "those who bash segmentation and targeting are talking nonsense" — [Marketing Week](https://www.marketingweek.com/mark-ritson-bash-segmentation-and-targeting/); but also "Segmentation is not the prerequisite for success" — [Marketing Week](https://www.marketingweek.com/ritson-sgementation-pointless/) and "We should thank Byron Sharp, not attack him" — [Marketing Week](https://www.marketingweek.com/mark-ritson-thank-byron-sharp/)
- Ritson's practical objection to "sophisticated mass marketing": most firms "haven't got enough money to do it," so they segment/target out of necessity — [Marketing Week (Ritson v Sharp)](https://www.marketingweek.com/ritson-versus-sharp-won-clash/); see also [the7stars "Blow by blow: Ritson v Sharp"](https://www.the7stars.co.uk/blow-blow-ritson-v-sharp/)
- Oldham: about half of the 39 winning 2016 IPA cases showed a clear targeting strategy, which she argued undercuts "reach all category buyers" — [Marketing Week debate coverage](https://www.marketingweek.com/ritson-versus-sharp-won-clash/)
- Common ground (Cannes, "Five Marketing Truths We Can Actually Agree On"): both agree on consistency of brand assets/campaigns, importance of mental availability; they still differ on targeting and purpose — [Ehrenberg-Bass](https://marketingscience.info/news-and-insights/from-mental-availability-to-mass-marketing-purpose-nonsense-and-consistency-what-ritson-and-sharp-did-and-didnt-agree-on-at-this-years-cannes)
- Sharp in turn criticises Binet & Field's 60/40 as unscientific / based on award-entry data (secondary) — [BlckAlpaca blog](https://blckalpaca.at/de/wissen/social-media/social-media-grundlagen-strategie/brand-vs-performance-marketing-95-5-regel)

### Inferences
- **Formula set (standard statements, reproduced from the literature; not re-fetched in this session — verify before formal publication):**
  - *Double Jeopardy approximation* (Ehrenberg et al. 1990): w(1 − b) ≈ w0, where b = brand penetration, w = mean purchases per brand buyer, w0 a category constant. Consequence: brands differ hugely in b, only modestly in w; to double share you mostly need ~double penetration.
  - *NBD-Dirichlet* (Goodhardt, Ehrenberg & Chatfield 1984, JRSS-A): (i) each consumer's category purchases in period T are Poisson with rate λ; λ is Gamma(K, M/K) across consumers → number of category purchases is NBD with mean M and shape K; (ii) given n category purchases, brand choices are multinomial with probabilities p_j drawn from a Dirichlet(α_1…α_g), S = Σα_j (S = "polarisation"/switching parameter; small S → more loyalty), and E[p_j] = α_j/S ≈ brand market share. Inputs: category penetration, category purchase rate, brand shares, S → outputs: each brand's b, w, SCR, 100%-loyal %, duplication.
  - *Duplication of Purchase law*: b_{j|k} ≈ D × b_j — the % of brand k's buyers who also buy brand j is proportional to brand j's penetration; D ≈ constant for the category. Deviations (excess duplication) identify real market partitions (e.g., sub-categories, price tiers), which is the evidence-based alternative to attitudinal segmentation.
  - *Pareto*: top 20% of buyers ≈ 50–60% of sales (not 80%), window-dependent.
- Implication for **budget**: if DJ holds, share growth requires penetration growth, so budget should be weighted to reach (broad, continuous, many light/non-buyers) rather than only retargeting/CRM. For a direct-response SMB this does not mean TV — it means not confining spend to retargeting/lookalikes of existing heavy buyers.
- Implication for **targeting**: target the *category* (all potential category buyers, defined via CEPs/needs) rather than a narrow persona; use duplication analysis and partition evidence, not attitudinal personas, to decide where narrower targeting is justified. The Ritson position (segment-target-position where budget is limited) is especially relevant for SMBs, who cannot afford mass reach.
- Implication for **creative**: build and use distinctive brand assets consistently; link brand to many CEPs (when/where/why/with-whom buying situations) — creative briefs should name the CEP(s) a piece targets.
- Applicability to SMB/direct-response: the laws describe *stationary* categories of competitive brands. A small DTC seller in a growing niche or with a single product may show deviations; nonetheless DJ predicts that "loyalty-first" strategies (heavy retention spend) rarely move share without penetration growth.

### Gaps
- Primary Ehrenberg-Bass pages (marketingscience.info) were unreachable; numeric D-coefficients, typical S values, and the exact w(1−b) derivation were not re-verified from primary texts this session.
- Did not find the specific text of Kevin Lane Keller's critique (Keller is usually cited as defending customer-based brand equity and differentiation); no source retrieved — treat any "Keller vs Sharp" claim as unverified.
- Did not retrieve the Bain & Company loyalty-economics counterpoint (Reichheld) or Kantar "meaningful difference" critiques in primary form.
- Peter Field's direct critiques of Ehrenberg-Bass on targeting/creative differentiation not retrieved.
- No quantitative studies located on applying Dirichlet norms to small DTC/ecommerce brands specifically.

---

## 2. Binet & Field: Long vs Short Term, Brand Building vs Activation, ESOV, Fame, "Effectiveness in Context", later IPA work, B2B (5 Principles, 95-5)

### Takeaway
Binet & Field's IPA Databank work established that brand building (broad reach, emotional, long-term) and sales activation (targeted, rational, short-term) work differently and are best combined (headline ~60:40 brand:activation for consumer brands, varying by context), and that ESOV (SOV − SOM) predicts share growth (~0.5 pt share/yr per 10 pts ESOV); B2B work (B2B Institute) reproduces the ESOV and emotion findings, and Dawes's 95-5 rule (~5% of B2B buyers in-market per quarter) justifies investing to reach out-of-market buyers — but the data are award/case-study samples skewed to UK big-budget brands, and ratios are rules of thumb.

### Cited Findings
- 60:40 (brand:activation) is the headline takeaway of Binet & Field's work on the IPA Databank ("The Long and the Short of It", 2013) — [WARC, "Effectiveness in Context"](https://www.warc.com/en/content/article/warc-talks/effectiveness-in-context/en-gb/123932); [IPA key works page](https://ipa.co.uk/knowledge/effectiveness-research-analysis/les-binet-peter-field)
- "Effectiveness in Context" (IPA, 2018) is the second in the "Marketing Effectiveness in the Digital Era" series; it takes the rules of thumb from "Media in Focus" (2017) and shows how they vary by category, business model, brand life stage and size — [IPA](https://ipa.co.uk/knowledge/publications-reports/effectiveness-in-context); [WARC](https://www.warc.com/content/article/warc-talks/effectiveness-in-context/en-gb/123932)
- Reported refinements (secondary only): 2018 update ~62:38 on average; B2B ~46:54 brand:activation (LinkedIn B2B Institute, 2019) — [BlckAlpaca blog](https://blckalpaca.at/de/wissen/social-media/social-media-grundlagen-strategie/brand-vs-performance-marketing-95-5-regel) (NOT verified against IPA primary; note other commonly repeated figure for B2B is ~46:54 to 50:50)
- ESOV rule: for every 10 points of excess share of voice (SOV − SOM), brands gain on average ~0.5 pts of market share per year (Binet & Field / IPA Databank, 2007 "Marketing in the Era of Accountability" and later) — [Brandwatch glossary](https://www.brandwatch.com/social-media-glossary/share-of-voice-sov/); [ppc.land](https://ppc.land/share-of-voice/); looser "0.5–1 pt" range in [Ordinal](https://www.tryordinal.com/blog/share-of-voice). Fame/high-creativity campaigns are reported to beat this ratio — [shno.co stats](https://www.shno.co/marketing-statistics/share-of-voice-statistics) (secondary)
- B2B: Binet & Field's B2B lessons — brand building matters in B2B as in B2C — [WARC event report](https://www.warc.com/content/article/event-reports/binet-and-field-effectiveness-lessons-in-b2b/130287)
- **B2B Institute "5 Principles of Growth in B2B Marketing"** (Binet & Field for LinkedIn B2B Institute): (1) invest in share of voice — B2B brands with SOV > SOM tend to grow; (2) balance brand building and activation; (3) expand the customer base (reach all potential buyers); (4) maximise mental availability — campaigns aimed at share of mind are most effective, and the more famous they make the company the better the business results; (5) harness the power of emotion — [LinkedIn report PDF](https://news.linkedin.com/content/dam/me/news/en-us/linkedin-pressroom-page/LIN_B2B-Marketing-Report-Digital.pdf); [IPA EffWorks](https://ipa.co.uk/effworks/marketing-marketing-v2/five-principles-of-growth-in-b2b-marketing/); [WARC](https://www.warc.com/content/article/the-5-principles-of-growth-in-b2b-marketing-empirical-observations-on-b2b-effectiveness/en-gb/136353)
- Critique of the 5 Principles: small samples, case studies skewed to UK and big budgets — [CustomerThink "Unconventional Views on B2B Growth"](https://customerthink.com/unconventional-views-on-b2b-growth/)
- Mi-3 (2022) coverage linking B2B mental availability, brand rejection, Binet-Field ESOV and Ehrenberg-Bass B2B data — [mi-3](https://www.mi-3.com.au/28-03-2022/mental-availability-brand-rejection-binet-field-esov-and-ehrenberg-bass-new-b2b-data-0)
- **95-5 rule** (John Dawes, Ehrenberg-Bass, published by LinkedIn B2B Institute, 2021): up to ~95% of B2B buyers are not in-market at any one time; e.g., firms switch principal bank/law firm about once every five years → ~5% in-market per quarter. "To grow a brand, you need to advertise to people who aren't in the market now, so that when they do enter the market your brand is one they are familiar with." Dawes said the percentages are illustrative, not literal — [Marketing Week, "The 95:5 rule is the new 60:40 rule"](https://www.marketingweek.com/peter-weinberg-jon-lombardo-95-5-rule); [CustomerThink](https://customerthink.com/what-the-955-rule-means-for-b2b-marketing/); [mi-3](https://mi-3.com.au/29-08-2022/australia-leading-world-marketing-science-us-based-b2b-institute-says-955-rule-getting)
- Sharp criticises 60:40 as unscientific and based on award-entry data (secondary) — [BlckAlpaca](https://blckalpaca.at/de/wissen/social-media/social-media-grundlagen-strategie/brand-vs-performance-marketing-95-5-regel); B&T opinion piece on the Binet debate — [B&T](https://www.bandt.com.au/to-binet-or-not-to-binet-thats-not-the-question/)

### Inferences
- **ESOV formula:** ESOV = SOV − SOM (percentage points). Expected annual share change ≈ 0.05 × ESOV (i.e., +10 pts ESOV → ≈ +0.5 pt SOM/yr), on average, for established brands; to *hold* share, keep SOV ≈ SOM. Budget-setting rule derived: required spend ≈ (target SOV) × (category total adspend). For an SMB, "category adspend" can be proxied by competitor ad library / auction share (impression share in search, Meta Ad Library counts), but this is an approximation and the IPA relationship was estimated mainly on large brands.
- The mechanism logic aligns with Ehrenberg-Bass: brand building = broad reach to future (out-of-market) buyers → builds memory structures; activation = harvesting in-market demand. The 95-5 rule is the B2B version of "most of your future buyers aren't buying now."
- Ratios are context-dependent (category, brand size/stage, online-native vs not, price/consideration level). For a small direct-response seller, a much higher activation share than 60:40 is typical and rational initially (cash-flow constraint, small SOM), but pure activation leads to diminishing returns as the in-market pool is exhausted (rising CAC); a planned brand share that grows with scale is the Binet & Field implication.
- Creative: emotional, fame-oriented campaigns are associated with larger long-term effects; rational, product-message creative is associated with short-term activation — creative testing systems that optimise only for short-term CTR/CPA systematically underweight brand effects.

### Gaps
- Primary IPA pages were unreachable; exact category-specific ratios from "Effectiveness in Context" (e.g., financial services, durables, new launches, online brands) and any 2019+ updates ("The Crisis in Creative Effectiveness" 2019, "The Long and the Short of It" follow-ups, 2023–2026 IPA/System1 work such as "The Extraordinary Power of Emotion"/"Look Out") could not be verified this session.
- The 62:38 and 46:54 figures rest on a single secondary blog.
- Original ESOV confidence interval / R² and the sample definition not retrieved.
- No 2024–2026 updates retrieved on whether 60:40 has been revised for the walled-garden/retail-media era.

---

## 3. Advertising Elasticities, Price Elasticity Comparisons, Decay Rates

### Takeaway
Meta-analytic average short-term brand advertising elasticity is ~0.12 (Sethuraman, Tellis & Briesch 2011, JMR), long-term ~0.24, and it declined over time (later work finds ~0.09); by contrast average price elasticity is ~−2.6 (Bijmolt, van Heerde & Pieters 2005), i.e., price is ~20× more "powerful" per % change but far more costly in margin — advertising works slowly and modestly, so it must be judged on incremental profit over the full carryover period.

### Cited Findings
- Sethuraman, Tellis & Briesch (2011), "How Well Does Advertising Work? Generalizations from Meta-Analysis of Brand Advertising Elasticities," *JMR* (June 2011): 751 short-term and 402 long-term brand advertising elasticities from 56 studies (1960–2008); short-term mean = 0.12, substantially lower than the prior meta-analytic mean of 0.22 (Assmus, Farley & Lehmann 1984); elasticities have declined over time — [PDF (gwern mirror)](https://www.Gwern.net/doc/economics/advertising/2011-sethuraman.pdf); [SSRN working version (872 estimates, 57 studies — differs from published)](https://papers.ssrn.com/ab_id=1866002)
- Long-term mean ≈ 0.24 (751/402 short/long-run elasticities from 56/38 publications; average 0.12/0.24) — confirmed via secondary citation of the same dataset — [Springer article citing it](https://link.springer.com/article/10.1007/s11747-022-00916-0)
- Earlier benchmark: Assmus, Farley & Lehmann (1984) meta-analysis (~0.22 short-term) — [PDF (gwern mirror)](https://www.Gwern.net/doc/economics/advertising/1984-assmus.pdf)
- A 2015 follow-up found average current-period advertising elasticity of 0.09, smaller than 0.12 — [search-reported; see Springer/EMAC listings](https://link.springer.com/article/10.1007/BF03342755) (attribution of exact paper not verified)
- Price elasticity: Bijmolt, van Heerde & Pieters (2005), *JMR* 42(2), 141–156, meta-analysis of 1,851 price elasticities → mean ≈ −2.62 (vs ≈ −1.76 in Tellis 1988); higher inflation raises price sensitivity — [Tilburg repository](https://repository.tilburguniversity.edu/items/813834f9-4626-45f8-ad0a-2920a545e089); figure via [KU Leuven WP MO_0902](https://lirias.kuleuven.be/bitstream/123456789/229404/3/MO_0902.pdf) (secondary)
- Carryover: a JMR (2017, 54(6)) "Meta-Analysis of Marketing Communication Carryover Effects" exists (Köhler, Mantrala, Albers & Kanuri) — [Scinapse listing](https://www.scinapse.io/papers/2613795277) (estimates not retrieved)
- Small vs. large media / advertising effectiveness by medium (IJRM) — [Kenniswest PDF](https://www.kenniswest.be/file/publication/44200/44199/62045_Niet_publiek_MAIN_TEXT_SMALL_MEDIA_IJRM.pdf?v=3); recent ad-effectiveness meta-regression (Korkames, Stanley & Stremersch, IJRM 2025) — [EUR PDF](https://personal.eur.nl/stremersch/artikels/Korkames_Stanley_and_Stremersch_IJRM_2025_print.pdf) (contents not reviewed in detail)

### Inferences
- **Elasticity arithmetic (definitional):** %ΔSales ≈ ε × %ΔAdspend. With ε = 0.12, a 10% spend increase → ~1.2% sales increase short term (~2.4% including carryover at ε_LT = 0.24). Profit-maximising ad-to-sales ratio (Dorfman–Steiner condition): A/S = ε_ad / |ε_price| ≈ 0.12/2.62 ≈ 4.6% (short-term) or 0.24/2.62 ≈ 9% (long-term) — a useful sanity check for budget levels, though it assumes constant elasticities.
- **Carryover/decay (Koyck/adstock):** Adstock_t = Ad_t + λ·Adstock_{t−1}; long-run effect = short-run / (1 − λ). LT/ST ≈ 2 (0.24/0.12) implies λ ≈ 0.5 per period at the frequency of the underlying studies; half-life = ln(0.5)/ln(λ). Exact typical weekly decay rates were NOT retrieved — commonly quoted MMM ranges should be verified before use.
- Diminishing returns: low elasticities mean that the *marginal* return on the last unit of spend is far below the average return; decisions must be made at the margin (see §4).
- For SMB direct-response: platform-reported ROAS massively overstates incrementality relative to 0.1–0.2 elasticities; incrementality/geo-lift tests are required to estimate the brand's own elasticity.

### Gaps
- Published long-run 0.24 not quoted directly from the paper's text (secondary confirmation only).
- No primary figures on typical advertising half-lives (weeks) by medium; Köhler et al. (2017) carryover estimates not retrieved.
- No meta-analytic elasticities specific to digital/search/social retrieved (digital ad elasticities in recent MMM/geo-experiment literature not covered).
- Price promotion decomposition (e.g., most promo uplift = brand switching/stockpiling) not retrieved.

---

## 4. Profit / Unit Economics for Performance Marketing: CAC, LTV, Payback, Contribution Margin, MER/Blended ROAS, Marginal vs Average

### Takeaway
Performance decisions should be made on contribution-margin-based, incremental and *marginal* metrics: the last dollar's incremental contribution, not average platform ROAS; blended MER and contribution-margin LTV:CAC with payback period form the guardrails.

### Cited Findings
- No external sources were fetched for this section in this session (definitions are standard accounting/finance identities); see Inferences.
- The low average advertising elasticities above (0.12 ST / 0.24 LT) imply that average returns overstate marginal returns — [Sethuraman et al. 2011](https://www.Gwern.net/doc/economics/advertising/2011-sethuraman.pdf)

### Inferences
- **Definitions (definitional, not empirical):**
  - Contribution margin per order (CM) = Revenue − COGS − shipping/fulfilment − payment fees − returns − variable discounts (before marketing). CM% = CM / Revenue.
  - CAC = Acquisition marketing spend / New customers acquired (blended), or incremental spend / incremental new customers (marginal/incremental CAC).
  - LTV (contribution basis) = Σ_t (CM_t × retention survival_t) / (1+d)^t; simple steady-state approximation: LTV ≈ (avg order CM × orders per year) × (margin-retention multiple), or for subscription: LTV ≈ ARPU × CM% / churn.
  - LTV:CAC — a common heuristic target is ≥3:1 on a contribution basis (industry rule of thumb, not empirical law).
  - Payback period (months) = CAC / (monthly CM per customer); cash-constrained SMBs often target payback on first order or within 3–12 months.
  - ROAS = attributed revenue / ad spend; Breakeven ROAS = 1 / CM% (e.g., CM% 40% → break-even ROAS 2.5 on first purchase).
  - MER (marketing efficiency ratio, aka blended ROAS) = Total revenue / Total marketing spend; aMER/nc-ROAS = new-customer revenue / spend.
  - Contribution after marketing = Total CM − Total marketing spend (the true "north star" profit metric).
  - **Marginal vs average:** Optimal spend is where marginal incremental contribution of the last $1 = $1 (i.e., marginal ROAS × CM% = 1), NOT where average ROAS = breakeven. Because response curves are concave (diminishing returns, consistent with elasticities < 1), the average ROAS at optimum is always above breakeven.
- Linking to brand laws: brand-building spend lowers future CAC and raises conversion across channels (mental availability), so it shows up in MER and baseline sales rather than last-click ROAS; a Moneyball system should evaluate it via MMM/geo-lift and MER trend, not platform attribution.

### Gaps
- No empirical benchmark sources retrieved for typical DTC LTV:CAC, payback periods, or MER by vertical; any such benchmarks need separate sourcing.
- Origin/evidence for the "3:1 LTV:CAC" heuristic not retrieved (it is a SaaS/VC convention, not an empirical law).

---

## 5. Customer-Based Approaches: RFM, CLV Models (Fader & Hardie BG/NBD), When Targeting Heavy Users Is Justified

### Takeaway
Probabilistic "buy-till-you-die" models (Pareto/NBD, BG/NBD) turn simple RFM summaries (recency, frequency, T) into forward-looking customer-level purchase and CLV predictions and are cheap to implement (Excel, PyMC-Marketing, R CLVTools/BTYD); they complement rather than contradict Ehrenberg-Bass — the same NBD/Gamma heterogeneity underlies both — and heavy-user targeting is justified for retention/CRM economics and in categories with extreme concentration, but not as the main growth lever.

### Cited Findings
- Fader, Hardie & Lee (2005), "'Counting Your Customers' the Easy Way: An Alternative to the Pareto/NBD Model," *Marketing Science* 24(2), 275–284: BG/NBD is an easier-to-fit alternative to Pareto/NBD; parameters can be estimated in Excel; three stages: estimate parameters, generate aggregate sales forecast, predict individual future purchasing — [UPenn repository](https://repository.upenn.edu/marketing_papers/282/); [Hardie abstract](https://brucehardie.com/abstracts/abstract-fhl_2004-04.html); [paper PDF](https://www.brucehardie.com/papers/bgnbd_2004-04-20.pdf); [Excel note](https://brucehardie.com/notes/004/bgnbd_spreadsheet_note.pdf)
- Parameters: r, α = Gamma shape/scale for heterogeneity in purchase rate λ; a, b = Beta shape parameters for heterogeneity in dropout probability p — [CLVTools docs](https://rdrr.io/cran/CLVTools/man/bgnbd.html)
- Implementations: PyMC-Marketing (fitted on CDNOW data, compared with `lifetimes`) — [PyMC-Marketing BG/NBD notebook](https://pymc-marketing.readthedocs.io/en/latest/notebooks/clv/bg_nbd.html); R BTYD — [BTYD manual](https://ghuiber.r-universe.dev/BTYD/doc/manual.html)
- Heavy buyers deliver only ~50–60% of a brand's sales (top 20%); lightest 80% contribute ~half — [Sharp, Romaniuk & Graham 2019](https://openresearch.lsbu.ac.uk/download/8e33716ee01359e2dc575295fae393dfdb541db3cf4573a065b3a069423e027f/74869/SSRN-id3498097-2.pdf); some retailer data show heavier concentration, esp. for small brands — [Campaign Asia](https://aws1.campaignasia.com/article/why-heavy-buyers-matter-more-than-byron-sharp-says/442271)

### Inferences
- **BG/NBD structure (from Fader, Hardie & Lee 2005; formulas reproduced from standard statement, verify against PDF):** while active, purchases ~ Poisson(λ); λ ~ Gamma(r, α); after each purchase customer becomes inactive with probability p; p ~ Beta(a, b). Individual inputs are only (x = repeat transactions, t_x = time of last purchase, T = customer age) — i.e., RFM without monetary. Key outputs: E[Y(t) | x, t_x, T] (expected future purchases), P(alive | x, t_x, T). Monetary value modelled separately by Gamma-Gamma (Fader, Hardie & Lee 2005, "RFM and CLV") assuming spend independent of frequency. CLV = Σ E[transactions_t] × E[margin per transaction] × discount factor.
- **RFM** scoring (quintiles of recency/frequency/monetary) is a heuristic segmentation; BG/NBD gives a principled "probability alive" and expected-purchases ranking that supersedes ad-hoc RFM cells for CRM targeting.
- **Regression to the mean (Ehrenberg-Bass/NBD):** under NBD, this period's heavy buyers buy less next period and non-/light buyers buy more — so "top-customer" segments look worse later and campaigns aimed at them can show spurious decline; always use control groups.
- **When targeting heavy users is justified:** (a) retention/CRM communications where marginal contact cost is near zero (email/SMS) and P(alive) and expected CLV are high; (b) categories/brands where concentration is genuinely extreme (B2B key accounts, subscription, high-ticket repeat services) — check the brand's own Pareto curve over an appropriate window; (c) upsell/cross-sell to high-CLV customers; (d) when the budget is so small that mass reach is impossible (Ritson's argument). It is NOT justified as the main acquisition/growth strategy, because DJ implies loyalty metrics move little and growth is mainly penetration.
- For SMB/direct-response: BG/NBD + Gamma-Gamma is the practical way to produce cohort LTV for the LTV:CAC and payback calculations in §4, with acquisition targeting broad (category buyers) and retention targeting CLV-ranked.

### Gaps
- Did not retrieve primary empirical comparisons of BG/NBD vs. ML (e.g., gradient-boosted CLV) accuracy, nor 2020s extensions (e.g., Pareto/GGG, covariate models) — not needed for core laws but relevant for implementation.
- No retrieved study directly quantifying the ROI of heavy-user targeting vs. broad reach in digital DTC contexts; the "Online brands only targeting heavy buyers are missing out" WARC item was only seen as a headline — [WARC](https://www.warc.com/content/feed/online-brands-only-targeting-heavy-buyers-are-missing-out-says-study/en-GB/10916).
