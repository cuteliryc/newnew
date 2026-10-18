# Evidence-Based Marketing Budget Allocation and Advertising Effectiveness Measurement

Notes on sourcing. Items marked **[verified]** were confirmed this session through search results that quote primary or near-primary sources. Items marked **[PK]** are prior knowledge: I could not re-fetch the source this session because DNS failed for developers.google.com, facebookexperimental.github.io, arxiv.org, warc.com and thinkbox.tv. Each [PK] item gives the canonical source URL. Check [PK] items before quoting them externally. The date is October 2026, and the year of each finding is given.

---

## 1. Marketing Mix Modeling: how Meta Robyn and Google Meridian work (exact formulas)

### Takeaway
Both open-source MMMs (Robyn, Meta, released 2021, R/Python; Meridian, Google, generally available since early 2025, Python/TensorFlow Probability) use the same core structure. Sales = baseline + controls + Σ β_m · Saturation(Adstock(media_m)). Adstock captures carryover and a Hill curve captures diminishing returns. They differ in estimation. Robyn uses ridge regression plus a multi-objective evolutionary hyperparameter search. Meridian is fully Bayesian and hierarchical across geos, with priors placed directly on ROI. Both can be calibrated with experiment results, and calibration is what makes them causally credible.

### Cited Findings

**Adstock (carryover)**
- Geometric adstock (Robyn and Meridian): A_t = x_t + θ·A_{t−1}, 0 ≤ θ < 1. The only parameter is θ, a fixed decay rate. Robyn's recommended θ ranges are TV 0.3–0.8, OOH/print/radio 0.1–0.4 and digital 0–0.3. — [Robyn CRAN reference manual](https://cran.rstudio.com/web/packages/Robyn/refman/Robyn.html) **[verified]**
- Weibull adstock (Robyn) has two parameters, shape and scale, with CDF and PDF variants. Weibull CDF bounds are about shape 0.0001–2 and scale 0–0.1. The PDF variant allows shape up to about 10 and supports *lagged peaks*, where the effect peaks some weeks after exposure. — [Robyn docs mirror](https://docsearch.algolia.com/mcp/docs/repo/facebookexperimental/robyn) **[verified, secondary mirror]**
- Robyn Weibull CDF mechanics **[PK]**: a time-varying decay θ_i = 1 − WeibullCDF(i; shape, scale·L) is applied as a cumulative product, so the weight at lag l is Π_{i≤l} θ_i. The PDF variant uses normalized Weibull PDF values as lag weights directly. — [Robyn analyst's guide](https://facebookexperimental.github.io/Robyn/docs/analysts-guide-to-MMM/)
- Meridian adstock is a normalized weighted average over lags 0…L: Adstock(x_t) = Σ_{l=0}^{L} w(l; α)·x_{t−l} / Σ_{l=0}^{L} w(l; α). The weight function is geometric or binomial, the decay α ∈ [0,1] and L = `max_lag`. — [Meridian model spec](https://developers.google.com/meridian/docs/basics/model-spec); [Media saturation and lagging](https://developers.google.com/meridian/docs/advanced-modeling/media-saturation-lagging) **[verified]**
- Geometric weight w(l) = α^l **[PK]**. Binomial weight w(l) = (1 − l/(L+1))^{α*} with α* = 1/α − 1 **[PK, check against the adstock_decay_spec page]**. — [Meridian model spec](https://developers.google.com/meridian/docs/basics/model-spec)
- The default `max_lag` in Meridian is 8 periods (weeks), and `None` means infinite lag. — [Meridian ModelSpec API](https://developers.google.com/meridian/reference/api/meridian/model/spec/ModelSpec) **[verified]**. A secondary source reports guidance of 2–10 periods for geometric decay and 4–20 for binomial. — [ppc.land](https://ppc.land/adstock/) (unverified against Google)

**Saturation (diminishing returns), Hill function**
- Robyn: x_sat = 1 / (1 + (γ / x_adstocked)^α), equivalently x^α / (x^α + γ^α). α is the shape (C-shaped when α ≤ 1, S-shaped when α > 1), with recommended bounds 0.5–3. γ sets the inflection point, with bounds 0.3–1. — [Robyn docs mirror](https://docsearch.algolia.com/mcp/docs/repo/facebookexperimental/robyn) **[verified, secondary mirror]**
- In Robyn, γ is a relative position. The actual inflexion = (1−γ)·min(x_adstocked) + γ·max(x_adstocked). **[PK]** — [Robyn features](https://facebookexperimental.github.io/Robyn/docs/features/)
- Meridian: Hill(q) = (1 + (q/ec)^(−slope))^(−1), with q, ec, slope > 0. `ec` is the half-saturation point and `slope` the steepness. The default order is Adstock then Hill (`hill_before_adstock = False`). — [Meridian model spec](https://developers.google.com/meridian/docs/basics/model-spec); [ModelSpec API](https://developers.google.com/meridian/reference/api/meridian/model/spec/ModelSpec) **[verified]**

**Model and estimation**
- Meridian outcome equation **[PK, structure]**: y_{g,t} = μ_t + τ_g + Σ_m β_{g,m}·HillAdstock(x_{g,t−L:t,m}) + Σ_c γ_{g,c}·z_{g,t,c} + ε_{g,t}. Here g is geo, μ_t is time effects (knots/splines) and τ_g is geo intercepts. Media effects β_{g,m} are drawn hierarchically across geos (log-normal by default, or normal). — [Meridian model spec](https://developers.google.com/meridian/docs/basics/model-spec); `media_effects_dist` defaults to log_normal and is not used in national models — [ModelSpec API](https://developers.google.com/meridian/reference/api/meridian/model/spec/ModelSpec) **[verified for defaults]**
- Meridian priors: the media prior type defaults to **ROI**, with options 'roi', 'mroi' and 'coefficient'. The default ROI prior is **LogNormal(0.2, 0.9)**, which implies a prior mean ROI of about 1.83, 80% of channels between 0.5 and 6.0, and 95% between 0.25 and 9.0. The default mROI prior is LogNormal(0.0, 0.5). When revenue per KPI is unknown, a "total paid media contribution" prior is recommended, with mean 40% and SD 20% of the KPI. — [Meridian default priors](https://developers.google.com/meridian/docs/advanced-modeling/default-prior-distributions); [ROI/mROI parameterizations](https://developers.google.com/meridian/docs/advanced-modeling/roi-mroi-contribution-parameterizations) **[verified]**
- Meridian calibration works by setting channel ROI priors from experiments, for example a lift-test ROI with a matching SD. It has `roi_calibration_period` and `rf_roi_calibration_period` parameters, and native reach & frequency inputs for YouTube-type channels. — [ModelSpec API](https://developers.google.com/meridian/reference/api/meridian/model/spec/ModelSpec) **[verified that the parameters exist; mechanics PK]**
- Robyn uses ridge regression for coefficients and Nevergrad, a gradient-free evolutionary optimizer, to search adstock and saturation hyperparameters. It optimizes several objectives together: NRMSE for fit and DECOMP.RSSD, a decomposition distance that "eliminates models where a small channel gets an unrealistically large effect". — [ppc.land on Robyn](https://ppc.land/metas-robyn-who-really-benefits-when-a-platform-builds-your-mmm/); [Resonance/Robyn docs](https://github.com/forward3d/Resonance) **[verified conceptually]**
- Exact Robyn objective formulas **[PK]**:
  - NRMSE = RMSE / (max(y) − min(y)).
  - DECOMP.RSSD = sqrt( Σ_m (effectShare_m − spendShare_m)² ), which penalizes decompositions far from spend shares. This is a business-plausibility *heuristic*, not a causal criterion.
  - MAPE.LIFT = mean_m | (modelled contribution_m over the test window − experimental lift_m) / experimental lift_m |, a third objective added when calibration data are supplied. — [Robyn features](https://facebookexperimental.github.io/Robyn/docs/features/); [Robyn arXiv paper 2403.14674](https://arxiv.org/abs/2403.14674)
- Robyn's CRAN description says it "allows ground-truth calibration to account for causation", using lift tests and geo-experiments. — [CRAN Robyn](https://cran.rstudio.com/web/packages/Robyn/index.html); [SourceForge mirror](https://sourceforge.net/mirror/robyn/) **[verified]**
- Robyn's output is a Pareto front of many candidate models, and the analyst picks one. That model choice is a known source of subjectivity. **[PK]** — [Robyn analyst's guide](https://facebookexperimental.github.io/Robyn/docs/analysts-guide-to-MMM/)

### Inferences
- The math is converging. Geometric or Weibull/binomial adstock followed by a Hill curve is the de facto standard, and practitioners argue mostly about **identification** (enough spend variation, priors, calibration), not functional form.
- Meridian's ROI-prior parameterization fits a "Moneyball" system well. Experiment results map directly onto priors, and with little data the posterior stays near the prior, which is honest. A Robyn point estimate can look precise without being so.
- DECOMP.RSSD builds in a bias toward "effect share ≈ spend share". That partly assumes away the reallocation opportunity MMM is supposed to find. Treat it as a regularizer, not truth.

### Gaps
- I could not fetch the exact current Meridian binomial-weight formula or the Robyn MAPE.LIFT formula from official docs, because of DNS failures. They are marked [PK].
- I did not verify 2025–2026 version changes, such as Meridian Scenario Planner (seen in search results as "Open Beta") or newer Robyn Python releases.

---

## 2. Optimal allocation principle: equalize marginal ROI; marginal vs average ROAS; response curves

### Takeaway
Theory and the tools agree. To maximize incremental profit for a fixed budget, move money until **marginal** ROI (the return on the next dollar) is equal across all funded channels, and set total budget where marginal ROI equals the cost of capital (mROI = 1 on a revenue-to-gross-margin basis). Average ROAS describes past spend and is the wrong signal for new spend. A channel with high average ROI can have low marginal ROI.

### Cited Findings
- Meridian defines mROI as the return on a small additional increment of spend. A channel near saturation can show mROI of about $0.80 even with a high average ROI, which "signals that money should go elsewhere". — [Meridian: ROI, mROI & response curves](https://developers.google.com/meridian/docs/basics/roi-mroi-response-curves) **[verified]**
- The Meridian optimizer has a fixed-budget scenario (best allocation for a given budget to maximize ROI) and flexible scenarios. One flexible scenario targets a minimum overall ROI. The other targets a minimum mROI per channel, which gives the maximum spend per channel that still clears that floor. The search space is bounded by `min_spend_shift_ratio` and `max_spend_shift_ratio`. Outputs include spend, ROI, mROI, incremental outcome and CPIK (cost per incremental KPI). — [Meridian: interpret the optimizations](https://developers.google.com/meridian/docs/post-modeling/interpret-optimizations) **[verified]**
- Robyn's allocator uses a gradient-based optimiser to shift spend across channels, aiming to equalize marginal return. Scenarios include `max_response` (fixed budget) and `target_efficiency` (target ROAS/CPA). — [ppc.land on Robyn](https://ppc.land/metas-robyn-who-really-benefits-when-a-platform-builds-your-mmm/); [Robyn GitHub issue #349](https://github.com/facebookexperimental/Robyn/issues/349) **[verified]**
- Most brands over-invest at the margin. Across 288 CPG brands, TV ads showed **negative marginal ROI for more than 80% of brands**, and the overall ROI of the observed schedule was positive for only about one third. Elasticities were well below earlier literature, and many were insignificant or negative. — [Shapiro, Hitsch & Tuchman, Econometrica 2021](https://jstor.econometricsociety.org/publications/econometrica/2021/07/01/tv-advertising-effectiveness-and-profitability-generalizable); [SSRN](https://papers.ssrn.com/abstract=3273476) **[verified]**. The median elasticity is about 0.01–0.02 **[PK; I could not confirm the commonly quoted 0.0233]**.
- Analytic Partners (vendor) reports that brands often overstate some channels' impact by **2–10x**, that about two thirds of advertising impact occurs after the first week, and that about 45% of advertising's impact comes from boosting other channels' ROI (halo). — [Analytic Partners ROI Genome report](https://analyticpartners.com/resources/report-roi-genome-intelligence-advertising-evolution-media-trends-taking-action/) **[verified as vendor claims; methodology not disclosed]**

**Formulas (standard economics; [PK] but textbook)**
- Problem: max_{x_1..x_n} Σ_i R_i(x_i) − Σ_i x_i subject to Σ_i x_i ≤ B. KKT gives R_i′(x_i) = λ for every channel with x_i > 0, and R_i′(x_i) ≤ λ for unfunded channels. When budget is unconstrained (profit-maximizing), λ = 1 on a margin basis, i.e. mROAS × gross margin = 1.
- Hill response R(x) = β·x^α/(x^α + γ^α). Marginal response: R′(x) = β·α·γ^α·x^{α−1} / (x^α + γ^α)². Average ROAS = R(x)/x. For a concave curve (α ≤ 1), mROAS < average ROAS everywhere. For an S-curve (α > 1), mROAS > average ROAS below the inflection point, which is the "under-invested channel" case.
- With adstock, the long-run marginal effect of one extra unit is about R′ × 1/(1−θ) under geometric decay. Short-window ROAS therefore understates high-carryover channels.
- The classic Dorfman–Steiner (1954) condition for the profit-maximizing ad/sales ratio is A/S = ε_A / |ε_P| (advertising elasticity over price elasticity). — [Dorfman & Steiner, AER 1954](https://www.jstor.org/stable/1807688) **[PK]**

### Inferences
- In practice, run the optimizer on posterior response curves, not point estimates, and cap shifts (for example ±20–30% per cycle) because curves are only identified near historical spend levels. Meridian's spend-shift ratios and Robyn's channel constraints exist for this reason.
- For a Moneyball system, rank channels by mROI with credible intervals. Average ROAS should be a diagnostic only.
- Shapiro et al. imply that the default prior for any channel should be "probably over-invested at the margin" unless an experiment shows otherwise.

### Gaps
- I found no independent, peer-reviewed validation that MMM-optimizer reallocations deliver the predicted uplift out of sample. Vendor claims exist but I did not verify them.

---

## 3. Incrementality and lift tests; how biased observational and attribution methods are

### Takeaway
The strongest evidence in the field says that **observational and attribution methods are unreliable for ad effects, even with rich data**. Randomized experiments are the gold standard. They are also noisy and expensive (Lewis & Rao), which is why the field calibrates models with periodic experiments instead of using experiments alone.

### Cited Findings
- **Gordon, Zettelmeyer, Bhargava & Chapsky (2019), *Marketing Science* 38(2):193–225.** They used 15 US Facebook ad RCTs with 500M user-experiment observations and 1.6B impressions, treating the RCT as ground truth. Matching and regression methods generally **overestimated** effectiveness. In about **half of studies the estimated percentage lift was off by a factor of three** or more, across all methods, even after conditioning on extensive demographic and behavioural variables. Conclusion: commonly used observational approaches based on typically available industry data "often fail to accurately measure the true effect of advertising." — [Kellogg summary](https://www.kellogg.northwestern.edu/academics-research/research/detail/2019/a-comparison-of-approaches-to-advertising-measurement-evidence-from/); [Kellogg whitepaper PDF](https://www.kellogg.northwestern.edu/faculty/gordon_b/files/kellogg_fb_whitepaper.pdf); [ppc.land](https://ppc.land/facebooks-own-tests-show-standard-ad-measurement-often-off-by-3x-dhir-says/) **[verified]**. The working-paper version used 12 studies.
- **Gordon, Moakler & Zettelmeyer (2023), "Close Enough?", *Marketing Science*.** They used **663** Facebook RCTs, each with more than 5,000 user- and experiment-level features, and tested double/debiased ML (DML) and stratified propensity-score matching (SPSM), including deep-learning nuisance models. DML beat SPSM, but **neither performed well**. The median absolute error in lift was **115% (upper funnel), 107% (mid) and 62% (lower funnel)** in percentage points, against median RCT lifts of only **28%, 19% and 6%**. The arXiv v1 reported 115%, 103% and 57% against 29%, 18% and 5%. The authors suggest observational methods may not work until platforms log auction-specific features. Conflict of interest: Gordon and Zettelmeyer were part-time Facebook employees and Moakler is a Meta employee. — [Marketing Science](https://pubsonline.informs.org/doi/fpi/10.1287/mksc.2022.1413); [arXiv 2201.07055](https://arxiv.org/pdf/2201.07055); [MSI working paper](https://www.msi.org/working-papers/close-enough-a-large-scale-exploration-of-non-experimental-approaches-to-advertising-measurement/) **[verified]**
- **Lewis & Rao (2015), *QJE* 130(4).** Across 25 large online field experiments (US retailers and brokerages, $2.8M in spend), the **median confidence interval on ROI was over 100 percentage points wide**. Individual sales are very volatile relative to per-capita ad cost, and a coefficient of variation of about 10 is common. Informative experiments can need **more than 10 million person-weeks**. A secondary summary puts it this way: a strong campaign (~25% ROI) moves mean sales by only about 5%, roughly 0.5% of one SD of sales. — [IDEAS/RePEc](https://ideas.repec.org/a/oup/qjecon/v130y2015i4p1941-1973.html); [2015 PDF](https://www.gwern.net/doc/economics/advertising/2015-lewis.pdf); [ClickZ summary](https://clickz.com/your-job-is-impossible/30557/) **[verified]**
- **Ghost ads (Johnson, Lewis & Nubbemeyer, JMR 2017, 54(6)).** The control group logs the impressions the advertiser *would* have won ("ghost" impressions) instead of serving PSAs. This removes PSA cost and lets you compare exposed users with would-be-exposed users. It improves precision over PSA and intent-to-treat A/B tests. Predicted ghost ads handle cases where delivery isn't fully controlled, and the authors' implementation logged more than 100M predicted ghost ads per day. Won the 2022 Weitz-Winer-O'Dell award. — [Kellogg](https://www.kellogg.northwestern.edu/faculty/research/detail/2017/ghost-ads-improving-the-economics-of-measuring-online-ad); [NBER PDF](https://conference.nber.org/conf_papers/f84173.pdf); [AMA](https://www.ama.org/2022/04/07/johnson-lewis-and-nubbemeyer-receive-2022-weitz-winer-odell-award/) **[verified; quantified precision gain not retrieved]**
- **Blake, Nosko & Tadelis (2015), *Econometrica*: eBay paid search.** Shutting off brand-keyword search ads produced almost no loss in traffic, because users clicked organic links instead. Non-brand search effects were concentrated among infrequent users, and the estimated overall ROI of paid search was negative (≈ −63%). **[PK]** — [Econometrica 83(1)](https://onlinelibrary.wiley.com/doi/10.3982/ECTA12423)
- **Experiment types [PK; methods well documented]:**
  - User-level conversion lift / holdout: platform-run RCTs such as Meta Conversion Lift and Google Conversion Lift, with ITT or ghost-ad control.
  - Geo experiments: randomize or match regions; analyse with Google TBR / trimmed-match or Meta GeoLift (synthetic control).
  - Matched-market tests.
  - On/off (switchback) tests.
  - Sources: [Meta GeoLift](https://github.com/facebookincubator/GeoLift); [Google "Estimating ad effectiveness using geo experiments" (Vaver & Koehler 2011)](https://research.google/pubs/estimating-ad-effectiveness-using-geo-experiments-in-a-time-based-regression-framework/)
- The incrementality metric to compute is iROAS = (Revenue_test − Revenue_control_scaled) / Spend_test. Lift % = (Y_T − Y_C)/Y_C. Incrementality factor = incremental conversions / platform-attributed conversions, used to "deflate" platform ROAS. **[PK, standard practice]**

### Inferences
- Platform-attributed conversions should be treated as an **upper bound**, adjusted by an incrementality factor measured per channel and tactic. Retargeting and brand search usually have the lowest factors (eBay result); prospecting and video often have higher factors than last-click implies.
- Gordon et al. found errors are largest in relative terms where true lifts are small, i.e. lower-funnel purchase outcomes relative to their 6% median lift. Attribution therefore looks most "confident" exactly where it is least reliable.
- Lewis & Rao say a small advertiser cannot run statistically conclusive user-level RCTs on sales for most campaigns. Geo tests with large spend shifts (including full on/off), longer windows and higher-signal KPIs are the practical alternative.

### Gaps
- I did not retrieve the quantified variance reduction from the ghost-ads paper.
- I found no 2024–2026 large-sample replication outside Meta. Evidence from Google, TikTok and Amazon RCT meta-analyses is mostly vendor-published and was not verified here.

---

## 4. MTA vs MMM vs experiments: the triangulation / "unified measurement" consensus

### Takeaway
Since about 2021, the practitioner and vendor consensus has been **"triangulation"**. MMM sets strategic, cross-channel budgets including offline and long-term effects. Experiments supply causal ground truth to calibrate MMM priors and attribution. MTA or platform attribution is kept only for fast, within-channel tactical optimization, after being deflated by incrementality factors. Signal loss from iOS 14.5 ATT, cookie deprecation and privacy rules weakened user-level MTA and drove a return to MMM. The consensus is mostly practitioner opinion and vendor positioning, not peer-reviewed proof that the combination works.

### Cited Findings
- The common framing is that MMM is for long-term budgeting, MTA for day-to-day tactics and experiments to validate both. MTA data can strengthen MMM inputs, and MMM can calibrate MTA. Geo holdout or incrementality tests are the validation step. — [Roivenue](https://roivenue.com/articles/three-lenses-one-system-making-sense-of-mta-mmm-experiments/); [Fairing](https://fairing.co/learn/attribution-academy/chapter2/triangulation-in-marketing-measurement); [Rockerbox](https://www.rockerbox.com/analysis) **[verified; vendor sources]**
- Dissent: layering all three "doesn't guarantee clarity; it often creates confusion, misallocation, and significant effort for the analytics team" — [Nexoya](https://www.nexoya.com/?p=23211). Another view is that merging methods into one number hides informative disagreement, and "divergence across methods can highlight risk… worth investigating" — [Roivenue](https://roivenue.com/articles/three-lenses-one-system-making-sense-of-mta-mmm-experiments/) **[verified; vendor opinions]**
- Both Robyn (MAPE.LIFT calibration) and Meridian (ROI priors from experiments) build experiment-calibration in as a first-class feature. That is a structural endorsement of triangulation by the two biggest platforms. — [CRAN Robyn](https://cran.rstudio.com/web/packages/Robyn/index.html); [Meridian ModelSpec](https://developers.google.com/meridian/reference/api/meridian/model/spec/ModelSpec) **[verified]**
- Platforms that build MMMs have a conflict of interest: their default choices may favour their own channels. — [ppc.land: "Meta's Robyn: who really benefits"](https://ppc.land/metas-robyn-who-really-benefits-when-a-platform-builds-your-mmm/) **[verified as commentary]**
- Gordon et al. (2019, 2023) are the main academic reason MTA without experiments is distrusted. See section 3.

### Inferences
- A defensible operating loop for a Moneyball system:
  1. Run an MMM with weakly informative ROI priors.
  2. Find the channels with the widest posterior or the largest proposed reallocation.
  3. Run geo or lift tests on those channels.
  4. Feed the results back as priors or calibration targets.
  5. Use platform attribution × incrementality factor for in-flight bid and creative decisions.
  6. Re-estimate quarterly.
- Where methods disagree, treat the experiment as authoritative for its time window and tactic. Use MMM to extrapolate to other spend levels and to long-term effects.

### Gaps
- I found no independent survey quantifying adoption of triangulation, and no peer-reviewed evidence that calibrated MMM beats uncalibrated MMM in allocation outcomes. Simulation studies exist, e.g. [IJECS simulation study](https://ejournal.radenintan.ac.id/index.php/IJECS/article/view/30533), but were not reviewed.

---

## 5. Brand vs performance split, long vs short term, and share of voice vs share of market (ESOV)

### Takeaway
Binet & Field's IPA databank work, which uses awards-entry case studies with known selection bias, is the main evidence base. Their original **~60:40 brand:activation** rule (2013) was later broken down by category and context in *Effectiveness in Context* (2018). Brand shares run higher in some sectors and lower in B2B and some contexts. The **ESOV rule** says that about 10 points of excess share of voice ≈ 0.5 points of annual market-share growth. Both are rules of thumb backed by correlational evidence with large variance, not causal laws.

### Cited Findings
- *Effectiveness in Context* (Binet & Field, IPA 2018) breaks down the 60:40 rule by category, consideration type, brand type and life stage. The authors say "there is no context in which short-term sales activation is the primary driver of growth." — [the7stars review](https://www.the7stars.co.uk/effs-sake-looking-latest-report-binet-field/); [IPA review by Michael Lee](https://ipa.co.uk/knowledge/ipa-blog/effectiveness-in-context-reviewed-by-michael-lee/) **[verified, secondary]**
- One review reports that the recommended brand share for for-profit sectors rose from **55:45 (1998–2010) to 76:24 (2004–16)**. — [the7stars review](https://www.the7stars.co.uk/effs-sake-looking-latest-report-binet-field/) **[verified as a secondary report; conflicts with a blog claiming ~62:38 — [markhub24](https://www.markhub24.com/post/performance-branding-balancing-long-term-brand-building-and-short-term-roi), which I treat as unreliable]**
- Selling online "doesn't necessarily mean you should focus your marketing spend there" — [IPA / Michael Lee](https://ipa.co.uk/knowledge/ipa-blog/effectiveness-in-context-reviewed-by-michael-lee/). Binet & Field (Thinkbox, a TV trade body, so a promotional source) argue that online businesses need offline brand-building, especially TV. — [Thinkbox](https://www.thinkbox.tv/news-and-opinion/opinion/advertising-effectiveness-for-dot-coms-by-les-binet-and-peter-field) **[title and snippet verified; page not fetched]**
- Commonly cited sector splits from *Effectiveness in Context* **[PK; verify in the IPA report before use]**: B2B ≈ 46:54 (from the LinkedIn B2B Institute "5 Principles of Growth in B2B Marketing", 2019); financial services ≈ 80:20; FMCG ≈ 60:40; durables ≈ 60:40; services ≈ 60:40. Newer, smaller or high-growth brands may need *more* activation, while market leaders need more brand. — [IPA Effectiveness in Context](https://ipa.co.uk/knowledge/publications-reports/effectiveness-in-context-a-manual-for-brand-building)
- **ESOV definition:** ESOV = SOV − SOM, in percentage points. Rule: **+10 pts ESOV ≈ +0.5 pts annual share growth** (IPA databank, 2007 analysis; often tied to a 2013 analysis of 171 campaigns). — [brand24](https://brand24.com/blog/share-of-voice-vs-share-of-market/); [shno.co](https://www.shno.co/marketing-statistics/share-of-voice-statistics); [DPR / Jon Lombardo](https://dprandco.com/excess-share-of-voice-a-key-driver-of-increased-market-share/) **[verified, secondary]**
- B2B variant: 10% ESOV → ~0.7% annual growth in B2B vs ~0.6% in B2C (LinkedIn B2B Institute with Binet & Field). — [LinkedIn](https://business.linkedin.com/en-uk/marketing-solutions/blog/posts/B2B-Marketing/2020/The-B2B-Marketers-Guide-To-The-Share-of-Voice-Rule) **[verified]**
- Heterogeneity: Nielsen (2009, cited via WARC) found that leaders gained 1.4 share points per 10 pts ESOV vs 0.4 for challengers. A Nielsen FMCG analysis cited via McCann found brands above 10% share get about 2.5× the ESOV return, and highly creative campaigns beat the 10:0.5 ratio. — [ppc.land](https://ppc.land/share-of-voice/); [shno.co](https://www.shno.co/marketing-statistics/share-of-voice-statistics) **[verified, secondary; conflicting magnitudes]**
- The ESOV rule originates with John Philip Jones (1990, HBR, "Ad Spending: Maintaining Market Share"), who showed that small brands tend to "underspend" (SOV < SOM) and large brands "overspend" relative to their share. **[PK]** — [HBR 1990](https://hbr.org/1990/01/ad-spending-maintaining-market-share)

### Inferences
- A usable formula: expected Δshare/yr (pts) ≈ k × (SOV − SOM), with k ≈ 0.05 as the base. k is higher for leaders, for strong creative and for B2B, and lower for challengers. Use it to set a **total** brand-budget floor, not channel splits.
- The evidence is observational and comes from award-entry cases, so it has survivor and selection bias. Binet & Field themselves stress context. For performance-led SMBs selling online, the brand share should be tested with geo-based brand holdouts, not assumed at 60%.
- The 60:40 guideline and Shapiro et al.'s "over-investment at the margin" finding for CPG TV don't strictly conflict, since one is about mix and the other about total level. They do pull in opposite directions on whether to spend more on brand TV.

### Gaps
- I could not access the primary IPA report to confirm exact sector splits or any "online-only brand" split. The Thinkbox page could not be fetched.
- I found no independent causal (experimental) test of the 60:40 rule.

---

## 6. Explore/exploit: multi-armed bandits, Thompson sampling and test budget share

### Takeaway
Bandits are proven to improve in-flight allocation among comparable options, such as creatives, audiences or sites, with a strong field result of +8% acquisitions at no extra cost. They suit tactical allocation with fast feedback, not strategic channel budgets with long lags. For "how much to spend on testing", profit-maximizing test design (Feit & Berman's "Test & Roll") gives much smaller tests than classical power analysis. The popular "70/20/10" split is a heuristic with no empirical basis that I could find.

### Cited Findings
- **Schwartz, Bradlow & Fader (2017), *Marketing Science* 36(4):500–522.** A hierarchical, attribute-based, batched bandit served display ads for a large retail bank, delivering more than 750M impressions over two months. It gave **+8% customer acquisition rate vs control at no extra cost**. Counterfactual: optimizing CTR instead of conversions would have *cut* acquisitions by about 10% (a Goodhart example). Won the John D.C. Little Best Paper Award. — [IDEAS](https://ideas.repec.org/a/inm/ormksc/v36y2017i4p500-522.html); [INFORMS](https://pubsonline.informs.org/doi/pdf/10.1287/mksc.2016.1023); [UPenn repository](https://repository.upenn.edu/handle/20.500.14332/48003) **[verified]**. The policy is built on Thompson sampling with a hierarchical logit **[PK; abstract doesn't name it]**.
- **Feit & Berman, "Test & Roll: Profit-Maximizing A/B Tests"** (Marketing Science 2019; arXiv 1811.00457). A standard hypothesis test for a small effect (d = 0.19) would need about 4.78M per arm, which is infeasible for most advertisers per Lewis & Rao. — [arXiv](https://arxiv.org/pdf/1811.00457) **[verified]**. Profit-maximizing sample size per arm for population N, with response noise s and prior SD of mean response σ **[PK]**: n* = sqrt( N·s²/(4σ²) + (3s²/(4σ²))² ) − 3s²/(4σ²). This is often orders of magnitude smaller than power-based sizes, and scales with √N.
- **Thompson sampling for budget [PK, standard]:** keep a posterior over each arm's conversion rate or ROAS (e.g. Beta(α+conversions, β+non-conversions)). Each period, draw a sample per arm and allocate budget in proportion to the probability that each arm is best (sample many times and count wins). Arms with low posterior probability still get some traffic until evidence accumulates. This is "probability matching".
- **Delayed and carryover rewards:** bandits assume quick, independent rewards. Ad effects with adstock or brand carryover violate this, which is why bandits are used within-channel (creatives, bids). Cross-channel budgets need MMM plus experiments. **[inference, consistent with section 1 adstock evidence]**

### Inferences
- Suggested test budget practice:
  - Keep a standing **experimentation budget** for incrementality tests on the 1–3 channels with the most decision value, i.e. highest spend × posterior uncertainty.
  - Use bandits inside channels for creative and audience selection.
  - "10–20% for testing" is a defensible *heuristic*, not an evidence-based number. Use Test & Roll or value-of-information calculations when possible.
- Optimize bandits on a business outcome (conversions, margin), never on proxies like CTR (Schwartz et al.'s −10%).

### Gaps
- I found no rigorous source for a recommended "test budget share" such as 70/20/10. That figure appears in practitioner content only.

---

## 7. Known pitfalls: small-sample noise, Goodhart's law, last-click bias, platform self-reporting; applicability to small and medium advertisers

### Takeaway
The biggest risks are: (1) noise far larger than the signal (Lewis & Rao); (2) correlational attribution that inflates retargeting and brand search (Gordon et al.; eBay); (3) platforms grading their own homework; (4) optimizing proxies (Goodhart); (5) MMMs fit on too little or too collinear data. Small advertisers have the least data and the most need for priors, big deliberate spend variations and simple models.

### Cited Findings
- Noise: median ROI confidence intervals are more than 100 pp wide even in large experiments, and informative experiments can need more than 10M person-weeks. — [Lewis & Rao, QJE 2015](https://ideas.repec.org/a/oup/qjecon/v130y2015i4p1941-1973.html) **[verified]**
- Attribution bias: observational methods are off by ≥3× in half of Facebook studies (2019). Even DML with 5,000+ features misses lift by 62–115 pp at the median (2023). — [Gordon et al. 2019](https://www.kellogg.northwestern.edu/academics-research/research/detail/2019/a-comparison-of-approaches-to-advertising-measurement-evidence-from/); [Gordon et al. 2023](https://pubsonline.informs.org/doi/fpi/10.1287/mksc.2022.1413) **[verified]**
- Goodhart/proxy metrics: optimizing CTR instead of conversions would have cut acquisitions by about 10%. — [Schwartz et al. 2017](https://ideas.repec.org/a/inm/ormksc/v36y2017i4p500-522.html) **[verified]**
- Channel over-statement of 2–10x by brands' own reporting (vendor claim). — [Analytic Partners](https://analyticpartners.com/resources/report-roi-genome-intelligence-advertising-evolution-media-trends-taking-action/) **[verified as claim]**
- Platform-built MMMs carry a conflict of interest. — [ppc.land](https://ppc.land/metas-robyn-who-really-benefits-when-a-platform-builds-your-mmm/). The key Facebook RCT papers were written by Meta-affiliated researchers. They show Meta's *own* observational methods failing, which cuts against interest, but they still rely on Meta data. — [INFORMS COI note](https://pubsonline.informs.org/doi/fpi/10.1287/mksc.2022.1413) **[verified]**
- Last-click bias: brand search largely captures demand that would convert anyway (eBay brand-keyword shutoff showed near-zero incremental traffic). **[PK]** — [Blake, Nosko & Tadelis 2015](https://onlinelibrary.wiley.com/doi/10.3982/ECTA12423)
- MMM requirements **[PK]**: Robyn guidance suggests about 2+ years of weekly data and an observations-to-variables ratio of about 10:1. Meridian's geo-level hierarchy partly addresses small national samples by pooling across geos. — [Robyn analyst's guide](https://facebookexperimental.github.io/Robyn/docs/analysts-guide-to-MMM/); [Meridian docs](https://developers.google.com/meridian/docs/basics/model-spec)
- Meridian's default priors are deliberately wide (95% of ROI between 0.25 and 9.0). With weak data, the posterior ≈ prior, so "results" can just be the prior echoed back. — [Meridian default priors](https://developers.google.com/meridian/docs/advanced-modeling/default-prior-distributions) **[verified for prior; inference for implication]**

### Inferences (applicability for small and medium advertisers)
- **MMM**: viable only with about 100+ weekly observations, a handful of channels (aggregate small ones), and real spend variation over time. Many SMBs fail on the last requirement because always-on, flat spend gives collinear inputs. **Create variation on purpose** with pulses, dark periods and geo staggering. Use Meridian with experiment-informed or conservative ROI priors rather than default Robyn Pareto picking.
- **Experiments**: user-level sales RCTs are mostly underpowered for SMBs (Lewis & Rao). Prefer:
  - Platform conversion-lift tests where eligible.
  - Geo on/off tests with large spend changes (100% on/off) over 4–8 weeks plus a post-period for carryover.
  - Higher-frequency, higher-signal KPIs (leads or first purchases rather than revenue) when they're validated as proxies.
- **Attribution**: use platform numbers only relative to each other within a channel, and multiply by an incrementality factor from tests. Never compare platform ROAS across platforms, since each over-claims and there is double counting.
- **Allocation decisions**: move budget in steps of about 10–30% toward higher *marginal* returns. Keep a holdout or test cell running at all times, and re-estimate quarterly.
- **Brand budget**: use ESOV as a sanity check on total brand spend. For a tiny-share SMB, SOM is small, so modest spend can already give positive ESOV in a niche. Define the market narrowly and correctly.

### Gaps
- I found no rigorous, peer-reviewed minimum-data thresholds for MMM. The figures above are practitioner guidance.
- I did not verify current (2025–2026) eligibility minimums for Meta and Google lift studies, or newer platform features such as Meta's "incremental attribution" setting.
