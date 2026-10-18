# Competitive Ad Intelligence and Continuous Experimentation and Learning Systems for Marketing

Scope note: the research ran in October 2026. Most web fetches of primary PDFs (airbnb.tech, scribd, engineering.atspotify.com) failed because of network or proxy errors. Many findings below therefore come from search-result summaries of primary sources rather than full-text reads, and each one is flagged where that matters. Vendor claims are labelled **[VENDOR]**. Peer-reviewed or first-party technical sources are labelled **[PRIMARY]**. Practitioner blogs and secondary write-ups are labelled **[SECONDARY]**.

---

## 1. Competitor ad intelligence: what the transparency libraries actually expose, and is ad longevity a valid performance proxy?

### Takeaway
The free platform libraries (Meta Ad Library, Google Ads Transparency Center, TikTok Creative Center/Top Ads) reliably show **which creatives, offers and angles competitors are running and for how long**. They give little or no performance data. Exceptions are coarse impression or reach ranges and, on TikTok, percentile CTR ranks. Treating "ad longevity" as a performance proxy is a reasonable heuristic built on revealed preference, but it has **no peer-reviewed or platform validation**. Its evidence base is vendor archives and vendor-run lifespan datasets.

### Cited Findings
**Meta Ad Library**
- **[SECONDARY]** All ads delivered to users in the UK or EU in the past year are in the Ad Library. In most countries outside the UK and EU, non-political ads are not archived after they stop running. That makes EU/UK views the richest source for historical competitor creative. — [Mida guide](https://www.mida.so/blog/meta-ads-library); [PPC Land](https://ppc.land/ads-library/)
- **[SECONDARY]** For EU-delivered ads of any subject, the API adds:
  - the selected targeting (age, gender, included and excluded locations)
  - an estimated total EU reach
  - the declared beneficiary and payer

  This is attributed to DSA Art. 39. — [Zernio docs](https://docs.zernio.com/platforms/meta-ads/ad-library); [Apify scraper page](https://apify.com/scraper-engine/facebook-ads-library-scraper?fpr=p2hrc6)
- **[SECONDARY]** Spend and impressions fields exist only for political/issue ads. Impressions for EU commercial ads could not be confirmed. — [Zernio docs](https://docs.zernio.com/platforms/meta-ads/ad-library)
- **[SECONDARY]** Watchdog criticism: the DSA reach and age/gender breakdowns fall short because Custom and Lookalike audience targeting is not disclosed. — [Who Targets Me](https://whotargets.me/en/?p=533)
- **[SECONDARY]** API access requires identity and location confirmation (facebook.com/ID). — [admanage.ai](https://admanage.ai/blog/facebook-ads-library-api)

**Google Ads Transparency Center**
- **[SECONDARY]** The UI generally shows ads served in the last 30 days. Political ads stay visible for 7 years. New ads appear about 48–72 hours after publication. — [Cyberclick](https://www.cyberclick.net/numericalblogen/google-ads-transparency-center-shedding-light-on-advertising-insights)
- **[SECONDARY]** Impression ranges have been tracked only since 1 March 2023 and publish with a 90-day privacy delay. The Center does not reveal campaign type. — [AdMake AI](https://admakeai.com/blog/google-ads-transparency-center)
- **[SECONDARY/VENDOR]** There is no official API for the UI. Google publishes EEA creative stats as a public BigQuery dataset. — [Apify Google Ads Transparency scraper](https://apify.com/s-r/google-ads-transparency?fpr=ewv9tm)

**TikTok Creative Center (Top Ads)**
- **[SECONDARY]** Top Ads can be filtered by region, industry, objective and period (last 7, 30 or 180 days). CTR appears as a **percentile within the industry**, not a raw rate: "Top 28%" means the ad beat 72% of ads in its industry. — [Stackmatix](https://stackmatix.com/blog/using-tiktok-creative-center-for-ad-research)
- **[VENDOR]** Sort modes include For You, CTR, Cost, Likes, Like rate and 6s play rate. Sources disagree on whether comments and shares are shown. — [Apify TikTok Creative Center scraper](https://apify.com/dltik/tiktok-creative-center)
- **[SECONDARY]** Sample sizes can be small. One 30-day industry search returned only 16 ads, and the source recommends 180-day windows. — [Stackmatix](https://stackmatix.com/blog/using-tiktok-creative-center-for-ad-research)
- Note: TikTok Top Ads is a **curated set of high performers**, not a full competitor library. It is useful for category creative norms, not for complete coverage of one competitor. (Inference from the filter design described above.)

**Ad longevity as a performance proxy**
- **[VENDOR]** AdSpyder argues that run length is the most reliable public stand-in for performance, because advertisers kill underperformers. It recommends combining longevity with **variation count**: several live variants of one hook signal scaling, while one lone long-running ad may just be abandoned. — [AdSpyder](https://adspyder.io/blog/competitor-best-performing-ad-format/)
- **[VENDOR]** Base rates from vendor datasets:
  - In a dataset of 82,856 DTC ads, the median lifespan was **17 days** and only **0.6%** survived a full year.
  - In a second set of 47,392 ads, **11.3%** ran more than 60 days and **4.7%** ran 90 days or more.

  Creatify recommends ranking by impression range first and longevity second. — [Creatify guide](https://creatify.ai/blog/meta-ad-library-how-to-use-it-to-search-for-competitor-ads-in-2026-(complete-guide))
- No Meta statement and no peer-reviewed study validating longevity against ROAS or CPA was found (based on the search summary). Known confounds include always-on brand ads, budget inertia, and evergreen catalog/DPA ads. — [search summary of AdSpyder and Creatify sources above]

### Inferences
- Use longevity as a **filter for "worth studying"**, not as a measure of winners. Build a composite signal from:
  1. survival beyond a base-rate threshold (for example, past the about-17-day median and ideally past 60 days, which only about 11% of ads reach in vendor data)
  2. the number of concurrent variants of the same hook or offer
  3. reappearance of the angle across formats and platforms
  4. EU reach or impression range where available
- The best workflow is to snapshot weekly and store diffs. Libraries often drop ended ads outside the EU and UK, and Google's UI covers only about 30 days. History you don't capture yourself is lost.
- For Moneyball-style decision making, competitor ads are **hypothesis generators for your own tests**, not evidence of what works. You only learn whether an angle works for *your* brand by testing it in your own account.

### Gaps
- No primary Meta or Google developer documentation was successfully fetched. Re-verify field availability, especially EU impressions for commercial ads, against the current Ad Library API docs.
- No independent validation study of longevity against performance was found.
- No reliable evidence was found on the accuracy of creative-intelligence tools such as Foreplay, Atria, Minea or AdSpy. They mostly resurface library data plus their own scrapes, and no accuracy audits were found.

---

## 2. Share of voice estimation and third-party tool accuracy (Similarweb, Semrush, SpyFu, etc.)

### Takeaway
Share of voice (SOV) matters strategically: the IPA rule is that excess SOV of about 10 points brings about 0.5–0.7 points of annual share growth. However, the digital inputs used to estimate competitor SOV and traffic carry **large errors**, typically a standard deviation around ±45–67% versus first-party analytics, and worse for small sites. Use these tools for **direction and rank order**, not absolute numbers.

### Cited Findings
- **[SECONDARY, summarizing IPA/Binet & Field 2007]** The rule of thumb is that 10 points of ESOV (SOV minus share of market) brings about **0.5 pp** of annual market share growth. It comes from the IPA Databank. — [DPR & Co](https://dprandco.com/excess-share-of-voice-a-key-driver-of-increased-market-share/); [Marketing Architects](https://www.marketingarchitects.com/blog/v36-n4-the-science-behind-market-share-growth)
- **[PRIMARY-ish, LinkedIn B2B Institute with Binet & Field]** 10% ESOV gives about **0.7%** annual share growth in B2B and about **0.6%** in B2C. — [LinkedIn B2B Institute](https://business.linkedin.com/en-uk/marketing-solutions/blog/posts/B2B-Marketing/2020/The-B2B-Marketers-Guide-To-The-Share-of-Voice-Rule)
- **[SECONDARY]** Highly creative or fame campaigns beat the 10:0.5 ratio. Brands with negative ESOV lost share in about 80% of cases studied. These figures are secondhand and need verification against the IPA original. — [search summary: DPR & Co / Brand24](https://brand24.com/blog/share-of-voice-vs-share-of-market/)
- **[SECONDARY, independent test]** OWOX compared 787 sites against Google Analytics:
  - Similarweb's standard deviation was **57–61%** across traffic groups, and it tended to underestimate.
  - Semrush was better on large sites (45% vs 57% for sites over 1M sessions) but worse on small sites (**67%**).

  The study date was not confirmed and may predate 2024. — [OWOX](https://www.owox.com/blog/articles/Semrush-vs-similarweb/)
- **[SECONDARY]** Promodo compared 184 sites against GSC in H1 2024. Similarweb was inaccurate below about 5,000 visits and fairly accurate overall after its July 2024 update. Vendors do not fully disclose their methodologies. — [Promodo](https://promodo.com/blog/data-accuracy-at-similarweb-ahrefs-and-semrush)
- **[SECONDARY]** Screaming Frog tested 25 sites:
  - Similarweb usually overestimated but was the most accurate on average for organic traffic. Its total visits were off by about 17%.
  - Ahrefs and Semrush mostly underestimated.
  - Results varied widely by site.

  — [Screaming Frog](https://www.screamingfrog.co.uk/how-accurate-are-website-traffic-estimators/)
- **[SECONDARY, anecdotal]** In a single-site test (May–Jul 2025), Semrush showed 29,454 organic clicks against 30,000 in GSC, while Similarweb showed 51.5k. — [Bloggerspassion](https://bloggerspassion.com/?p=1080730)
- Conclusion across these tests: no tool is consistently most accurate. Error depends on site size and on which metric is compared (Similarweb visits vs Semrush organic traffic). — [search synthesis of the four tests above]

### Inferences
- Practical SOV estimation for paid social and search should triangulate several proxies:
  - **ad count share** and **active-days share** from the ad libraries
  - **auction insights** (Google impression share and overlap rate, the only first-party competitor SOV metric available to advertisers)
  - **branded search volume share** (Google Trends or keyword tools)
  - **social mention share** from listening tools
- Track each proxy as a **trend and rank**, never as an absolute level.
- When one tool's estimate drives a decision, require that two independent sources agree on direction before acting.
- Small competitors (under about 5k visits per month) are essentially unmeasurable with these panels.

### Gaps
- SpyFu's ad-spend and keyword estimates had no independent accuracy audit in what I found.
- The original Binet & Field IPA 2007 document was not fetched, so the "negative ESOV loses share in 80% of cases" figure is unverified.

---

## 3. Academic evidence on competitive advertising response

### Takeaway
The best large-sample evidence (400+ CPG categories) finds that **most competitors do not react** to rivals' advertising or promotion attacks. When firms do react, they mirror the instrument (ads against ads, promotions against promotions), and reactions **rarely change long-run sales**. Reflexively matching a competitor's ad push is usually wasted money. Consumer response, not competitor vigilance, determines outcomes.

### Cited Findings
- **[PRIMARY]** Steenkamp, Nijs, Hanssens & Dekimpe (2005) used VAR models on short- and long-run responses to promotion and ad shocks across **400+ consumer product categories over four years**. — *Marketing Science* 24(1):35–54 — [IDEAS/RePEc](https://ideas.repec.org:443/a/inm/ormksc/v24y2005i1p35-54.html); [Kellogg](https://www.kellogg.northwestern.edu/academics-research/research/detail/2005/competitive-reactions-to-advertising-and-promotion-attacks/)
- **[PRIMARY]** Main results:
  - Passive response, meaning no reaction, is the predominant behavior and "is often a sound strategy."
  - Firms that do retaliate often use ineffective instruments, resulting in "spoiled arms."
  - Retaliation mirrors the attack instrument.
  - Accommodation is rare, and reducing promotional support often misses sales opportunities.
  - There are very few long-run effects of any type of reaction.
  - Impact "depends primarily on the nature of consumer response, not the vigilance of competitors."

  — [EUR working paper](https://repub.eur.nl/pub/175/erimrs20020306112058.pdf); [Tilburg repository](https://research.tilburguniversity.edu/en/publications/competitive-reactions-to-advertising-and-promotion-attacks/)
- **[PRIMARY]** Bandit-optimized display campaigns: Schwartz, Bradlow & Fader (2017), *Marketing Science* 36(4):500–522. This study is relevant to "data, then decisions" loops; see section 8.

### Inferences
- Default decision rule: **don't mirror; monitor and test.** Use competitor-move alerts to trigger a hypothesis ("does their new offer cut our conversion rate?") and check it against your own KPIs, such as CVR changes, CPM inflation in shared auctions, and branded search share. Only respond when your own metrics show damage.
- The findings come from CPG and offline media in the 1990s–2000s. Digital auctions add a direct cost channel that offline media didn't have: competitor spend inflates your CPMs and CPCs. Monitoring auction-insight metrics is therefore more actionable online than in the original setting.

### Gaps
- Full-text effect sizes were not accessed; abstracts only.
- No recent (2020+) peer-reviewed study of competitive reaction in digital/social ad auctions was found within the search budget.

---

## 4. Competitive positioning frameworks: differentiation vs distinctiveness (Ehrenberg-Bass vs Ritson)

### Takeaway
Ehrenberg-Bass (Sharp, Romaniuk) shows that **perceived differentiation between competing brands is low** in most categories. They argue that distinctive brand assets and mental and physical availability drive growth. Ritson and others argue for "bothism": brands need distinctiveness *and* **relative** differentiation, meaning more of a valued attribute than rivals rather than true uniqueness. The empirical dispute is about **how much** differentiation matters, not whether brands differ at all, and neither side has a decisive causal dataset.

### Cited Findings
- **[PRIMARY, via summary]** Romaniuk, Sharp & Ehrenberg found low perceived differentiation across competing brands in many categories, yet customers keep buying these brands. — [Academia.edu copy](https://www.academia.edu/107196735/Evidence); [Brandknew summary](https://www.brandknewmag.com/?p=21380)
- **[SECONDARY]** Ritson's "bothism" is the view that salience/distinctiveness and differentiation are complementary. He argues for **relative differentiation**: "more of something than other brands do within the category." — [Marketing Week (Ritson)](https://www.marketingweek.com/salience-differentiation-bothism-wins/)
- **[SECONDARY]** Ritson accused the Institute of "consulting, dogma, ideology" rather than science. He conceded that the 20th-century USP approach was weak but said Ehrenberg-Bass "has taken the theory too far." — [Mi-3](https://mi-3.com.au/30-08-2023/dont-call-it-science-call-it-what-it-really-consulting-dogma-ideology-mark-ritson-why)
- **[SECONDARY]** At Cannes, Sharp called perceived differentiation "shockingly low" and said it matters little. His line: "If you need complicated market research to torture data to find your differentiation, you haven't got any." — [Marketing Science Institute (Ehrenberg-Bass) Cannes recap](https://marketingscience.info/news-and-insights/from-mental-availability-to-mass-marketing-purpose-nonsense-and-consistency-what-ritson-and-sharp-did-and-didnt-agree-on-at-this-years-cannes)
- **[SECONDARY]** Felipe Thomaz argues that growth depends on perceived differentiation. He cites a Google/YouTube analysis in which asset distinctiveness did not make the top 10 drivers of ad performance. That analysis was not independently verified. — [SRH Agency](https://srh.agency/dispatch/4-out-of-5-marketers-recommend)

### Inferences
- For a competitive-intelligence program, the debate suggests tracking two separate things:
  1. **Distinctiveness audit:** which brand assets (colors, characters, sounds, taglines) each competitor uses consistently across ads, measured by recurrence in ad-library snapshots.
  2. **Claim/angle map:** which category entry points, benefits, offers and price points each competitor emphasizes. This shows where relative differentiation is still available.
- Both can be measured cheaply from ad libraries, and LLM-assisted coding helps (see section 9).
- Test claims against your own outcomes. The Thomaz/YouTube point suggests that ad-level creative features can be ranked empirically within your own account, which is the Moneyball-compatible stance.

### Gaps
- I did not read the Romaniuk/Sharp/Ehrenberg paper or Thomaz's work in full.
- No randomized evidence directly pitting distinctiveness against differentiation was found.

---

## 5. Experimentation culture: win rates, OEC, guardrails and trust (Microsoft, Bing, Booking, Amazon, Airbnb)

### Takeaway
At mature experimentation organizations, **most ideas fail**. About one third of ideas succeed at Microsoft broadly, about 10–20% at optimized products like Bing, Google Ads, Booking and Netflix, and about 8% at Airbnb search. Good programs therefore emphasize volume, a single overall evaluation criterion (OEC), guardrail metrics, automated trust checks (SRM), and skepticism toward surprising wins (Twyman's law).

### Cited Findings
- **[PRIMARY, Kohavi et al. via secondary summaries]** At Microsoft, about one third of ideas were positive and significant, one third flat, and one third negative and significant. — [Bytepawn summary](https://bytepawn.com/experimentation-lessons-google-bing-netflix-alibaba.html); [exp-platform talk deck](https://www.exp-platform.com/Documents/2016-12PavelUPittNR.pdf)
- **[SECONDARY]** On Lenny's Podcast, Kohavi said 66%, 85% and 92% of experiments at Microsoft, Bing and Airbnb respectively failed to improve key metrics. That implies success rates of about 34%, 15% and 8%. — [PodPulse summary of Lenny's Podcast](https://podpulse.ai/podcast-notes-and-takeaways/lennys-podcast-product-growth-career-the-ultimate-guide-to-ab-testing-ronny-kohavi-airbnb-microsoft-amazon)
- **[SECONDARY]** Secondary sources put Booking.com, Google Ads, Netflix and Bing at about 10–15% success. I found no primary Booking-specific figure; the Kohavi/Deng/Vermeer KDD 2022 paper *A/B Testing Intuition Busters* reportedly tabulates these but could not be fetched. — [Aakash Gupta newsletter](https://www.news.aakashg.com/p/metrics-experiments); [Koji base-rate note](https://www.koji.so/docs/product-idea-base-rate-outside-view)
- **[SECONDARY]** False positive risk: with a low prior success rate, a p-value of 0.05 implies a much higher probability that a "win" is false. Attributed to Kohavi: at an 8% success rate, p<0.05 gives about **26% FPR**. Kohavi's glossary entry says FPR "can be 4 to 5 times higher than the p-value" in domains with 10–20% success rates. — [Convert glossary (Kohavi entry)](https://www.convert.com/glossary/type-i-error-false-positive); [skill summary of Kohavi](https://skills.cat/skills/wdavidturner/product-skills/trustworthy-experiments)
- **[PRIMARY]** Kohavi, Deng & Vermeer (KDD 2022), *A/B Testing Intuition Busters*: "some seemingly intuitive concepts being touted, including by A/B tool vendors and agencies, are misleading, often badly so." — [Airbnb-hosted PDF](https://airbnb.tech/wp-content/uploads/sites/19/2025/10/ABTestingIntuitionBusters.pdf) (could not be fetched; abstract via search)
- **[PRIMARY]** A Kohavi-coauthored 2025 preprint, later published at KDD 2026 with eight replications across four patterns, finds that underpowered studies (below 50% power) suffer from the **winner's curse**. The authors re-ran a published button-rounding result with tests using more than 2,000 times the users. — [arXiv 2512.24521](https://arxiv.org/abs/2512.24521v2); [Vermeer publication page](https://www.lukasvermeer.nl/publications/paper/2026/09/02/trustworthy-ab-patterns-and-the-winners-curse.html)
- **[PRIMARY]** Guardrails, as described by Dmitriev et al. (KDD 2017), are metrics "not clearly indicative of success of the feature… but which we do not want to significantly harm." Page load time at MSN and Bing is the example. — [Morning Paper summary of Dmitriev et al.](https://blog.acolyer.org/2017/09/25/a-dirty-dozen-twelve-common-metric-interpretation-pitfalls-in-online-controlled-experiments/)
- **[PRIMARY]** *Trustworthy Online Controlled Experiments* (Kohavi, Tang, Xu, Cambridge 2020) separates organizational guardrails from **trust-related guardrails** such as SRM. — [Cambridge chapter page](https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/sample-ratio-mismatch-and-other-trustrelated-guardrail-metrics/8DBB0F59AC7729D7BC6B94690DB9CCD5)
- **[PRIMARY]** Dmitriev et al. list 12 metric pitfalls, including:
  - metric SRM
  - misreading ratio metrics, such as a CTR that "dropped 40%" while the module was actually seen and clicked more
  - Simpson's paradox
  - bots
  - primacy and novelty effects
  - carryover effects

  They recommend automatic SRM detection, typically with a chi-square test. — [Morning Paper](https://blog.acolyer.org/2017/09/25/a-dirty-dozen-twelve-common-metric-interpretation-pitfalls-in-online-controlled-experiments/)
- **[SECONDARY]** Twyman's law: "if you see a massive improvement to your OEC, … find the flaw." The exact wording is unverified. — [Antoine Buteau's Kohavi notes](https://www.antoinebuteau.com/lessons-from-ronny-kohavi/)
- **[SECONDARY]** Booking.com runs "well over a thousand" concurrent experiments on an in-house platform built in the mid-2000s. Its culture emphasizes no HiPPOs, letting anyone run a test without bureaucratic approval, and sharing results openly. — [Silicon Canals](https://siliconcanals.com/sc-n-booking-com-runs-well-over-a-thousand-simultaneous-a-b-tests-at-any-moment-from-its-amsterdam-headquarters-on-an-experimentation-platform-engineers-built-in-the-mid-2000s-and-have-patched-contin/); [VWO on Booking](https://vwo.com/blog/cro-best-practices-booking/)
- **[PRIMARY]** For early-stage programs (not Big Tech), a 2024 arXiv paper covers statistical and data challenges in building experimentation capability at smaller organizations. — [arXiv 2405.03579](https://arxiv.org/pdf/2405.03579)

### Inferences
- For a marketing team, plan around a **10–30% win rate**. A roadmap needing 5 real wins per quarter needs roughly 20–50 well-powered tests per quarter, or fewer, bigger bets.
- Treat any test with a lift above about 2–3 times the historical median with Twyman-level suspicion. Rerun it before scaling.
- A marketing OEC should be close to business value: for example, contribution margin per visitor, or new-customer profit at 30/60/90 days. CTR is not a suitable OEC; Schwartz et al. show that optimizing CTR instead of conversions cost about 10% of acquisitions (see section 8).
- Guardrails for marketing tests could include unsubscribe and complaint rate, refund rate, CPM inflation, and brand-search volume.
- Ad-platform A/B tools (Meta split tests, Google experiments) don't automatically flag SRM or check cross-arm audience overlap. Teams need their own checks.

### Gaps
- The exact per-company success-rate table and FPR values in *Intuition Busters* could not be read directly. The 8% to 26% FPR figure comes via secondary summaries.
- Amazon-specific win-rate figures were not found in this pass.

---

## 6. Statistical methods: peeking, sequential testing, Bayesian vs frequentist, CUPED, winner's curse

### Takeaway
The main technical risks are **peeking**, meaning stopping on a favorable interim result, and **low power**, which brings the winner's curse. Peeking inflates false positives under **both** frequentist and naive Bayesian setups. The fixes are pre-registered fixed horizons, or properly designed sequential methods (always-valid p-values, mSPRT, group-sequential designs). CUPED-style variance reduction using pre-period covariates commonly cuts variance by about 40–50%. That cuts the required sample size by roughly the same fraction.

### Cited Findings
- **[PRIMARY]** Johari, Pekelis & Walsh (arXiv 2015; *Operations Research* 2021, with Koomen) found that continuous monitoring makes standard p-values and CIs invalid. They propose **always-valid p-values and confidence intervals** that stay valid at any stopping time, extend the approach to multiple testing, and deployed it at Optimizely. — [arXiv 1512.04922](https://arxiv.org/abs/1512.04922)
- **[PRIMARY]** Deng et al. (2017) propose Bayesian continuous monitoring ("Peeking at A/B tests: continuous monitoring without pain"). — [Morning Paper summary](https://blog.acolyer.org/2017/09/28/peeking-at-ab-tests-continuous-monitoring-without-pain/)
- **[SECONDARY, independent]** Georgiev/Analytics-Toolkit: "Bayesian AB Testing is Not Immune to Optional Stopping Issues." Outcome-based stopping inflates error rates under Bayesian procedures too. — [Analytics-Toolkit (2017)](https://blog.analytics-toolkit.com/2017/bayesian-ab-testing-not-immune-to-optional-stopping-issues/)
- **[SECONDARY]** Molas (2025): stopping at a fixed 95% posterior threshold inflates false positives just as frequentist peeking does, but "your posterior remains interpretable at any sample size." — [Alex Molas](https://www.alexmolas.com/2025/10/30/bayesian-ab-test-peeking.html)
- **[PRIMARY, Spotify engineering, Sept 2026; via search summary only]** "A flat-prior that stops on a posterior-probability threshold, the default in almost every platform offering Bayes, reproduces the false positive rate of frequentist peeking." Bayes-factor stopping can control false positives. Spotify explains why it doesn't use Bayesian A/B testing. — [Spotify Engineering](https://engineering.atspotify.com/2026/9/why-spotify-is-not-using-bayesian-a-b-testing/)
- **[VENDOR/PRIMARY — Spotify Confidence docs]** Combining CUPED with sequential tests changes the information fraction, so boundaries must be recalculated. A sequential method without the right variance estimation, sample-size calculation and multiple-testing correction is "a partial implementation." — [Spotify Confidence: sequential testing](https://confidence.spotify.com/glossary/sequential-testing.md); [CUPED](https://confidence.spotify.com/glossary/cuped)
- **[PRIMARY]** Deng, Xu, Kohavi & Walker (2013), "CUPED": using pre-experiment data **cut variance by about 50% at Bing**, giving the same power with half the users or duration. — [exp-platform CUPED page](https://exp-platform.com/cuped/)
- **[SECONDARY]** Netflix (2016) reportedly saw about 40% variance reduction on some engagement metrics. Gains depend on the correlation between the pre-period covariate and the outcome. — [Statsig docs](https://docs.statsig.com/stats-engine/variance_reduction); [search summary]
- **[PRIMARY]** Winner's curse: significant results from studies with power below 50% systematically overstate effects. See also Gelman & Carlin on Type M error. — [arXiv 2512.24521](https://arxiv.org/abs/2512.24521v2)

### Inferences
- Practical protocol for a marketing team:
  1. Pre-register the metric, minimum detectable effect (MDE), duration and stopping rule.
  2. Use either a fixed horizon with whole-week durations to cover day-of-week effects, or a platform with mSPRT or group-sequential boundaries.
  3. Apply CUPED or a regression adjustment whenever pre-period data exist. CRM or email tests with prior-purchase covariates gain most; prospecting ad tests have no pre-period data for new users, so they gain little.
  4. Shrink reported lifts toward the historical prior (see section 8) before forecasting impact.
- "Bayesian" is not a peeking license. Choose Bayesian for interpretability and decision-theoretic stopping (expected loss), not to escape error control.
- Platform-native ad tests have extra issues: auction dynamics, algorithmic delivery imbalance between arms, and audience overlap. Even with the stats right, their results describe "ad + delivery algorithm" bundles rather than pure creative effects. (Inference; not directly sourced in this pass.)

### Gaps
- Numeric Type I inflation from peeking (for example, how it grows with 10 looks) was not retrieved from Johari et al.'s full text.
- The Spotify 2026 post could not be fetched in full.

---

## 7. Hypothesis prioritization (ICE, PIE, RICE) and experiment knowledge bases

### Takeaway
I found **no empirical evidence** that ICE, PIE or RICE improve experiment outcomes. They are consensus-building heuristics. The evidence-backed alternative is to **calibrate priors with your own historical win rates and effect sizes** (the "outside view") and to keep a searchable learning repository so that win rates by area and hypothesis type can be computed.

### Cited Findings
- No independent study validating ICE, PIE or RICE was found in the search (summary: "No results addressed ICE prioritization or its evidence base"). — [search result, Analytics-Toolkit query](https://blog.analytics-toolkit.com/t/conversion-rate-optimization/page/2/)
- **[SECONDARY]** "Outside view" approach: use experiment-portfolio base rates (about 10–33% success) as the prior for whether a new product or marketing bet will work. — [Koji: base rate for a product bet](https://www.koji.so/docs/product-idea-base-rate-outside-view)
- **[SECONDARY]** Booking.com shares results openly across the company as part of experimentation democratization. — [VWO on Booking](https://vwo.com/blog/cro-best-practices-booking/); [Marpipe](https://marpipe.com/blog/how-booking-com-uses-1000s-of-experiments)

### Inferences
- Replace subjective "Confidence" scores in ICE/RICE with **empirical win probability by category**, taken from the repository. For example, past win rates might be 25% for offer tests, 12% for headline tests and 8% for landing-page layout tests. Replace "Impact" with **shrunken historical median lift × traffic exposed**.
- A minimal repository schema:
  - hypothesis and mechanism
  - competitor or insight source (for example, "competitor X has run angle Y for more than 60 days")
  - metric, MDE, power and sample size
  - result: lift, CI and posterior
  - SRM and guardrail outcomes
  - decision
  - tags: channel, funnel stage, angle, offer type
  - re-test date
- Each completed test then updates the category priors (section 8).
- Run a periodic **meta-analysis** across tests by tag to find which angle types reliably work. This is the actual knowledge-base payoff.

### Gaps
- No primary Booking.com, Microsoft or Thomke source on repository design was retrieved. Thomke's *Experimentation Works* (HBR Press 2020) is the canonical reference but was not accessed.
- No evidence was found on whether repositories measurably raise win rates.

---

## 8. Bayesian updating, bandits and the automated learning loop

### Takeaway
Bayesian shrinkage (Beta-Binomial or hierarchical models) is the right tool for many small, noisy marketing cells such as ads, creatives, segments and landing pages: it stops you chasing lucky small-sample winners. Multi-armed bandits (e.g., Thompson sampling) beat static A/B splits when the goal is **earning while learning**. The strongest field evidence is an **8% lift in customer acquisitions** with no additional spend, from a hierarchical, attribute-based bandit in a bank's display campaign of 750M+ impressions.

### Cited Findings
- **[PRIMARY]** Schwartz, Bradlow & Fader (2017), *Marketing Science* 36(4):500–522: a multi-armed bandit policy in a live display campaign for a large retail bank (750M+ impressions, two months) improved the **customer acquisition rate by 8%** versus a control policy at no extra cost. — [IDEAS/RePEc](https://ideas.repec.org/a/inm/ormksc/v36y2017i4p500-522.html); [Penn repository](https://repository.upenn.edu/handle/20.500.14332/48003)
- **[PRIMARY]** In the same paper, counterfactuals show that **optimizing CTR instead of conversions would cut acquisitions by about 10%**. Standard bandits miss the problem's real structure: hierarchy (ads within sites), shared creative attributes across ads, and batched decisions over millions of impressions. — [Penn repository](https://repository.upenn.edu/handle/20.500.14332/48003)
- **[PRIMARY]** High-dimensional bandits for jointly optimizing media and target audience. — [arXiv 2209.08403](https://arxiv.org/pdf/2209.08403)
- **[PRIMARY]** A Stanford GSB working paper modifies Thompson sampling for real-time bidding, learning the bidding policy and the ad's effect at the same time. — [Stanford GSB: Online inference in advertising auctions](https://www.gsb.stanford.edu/faculty-research/working-papers/online-inference-advertising-auctions)
- **[PRIMARY]** Scott (2010), Bayesian bandit and Thompson sampling foundations for online experiments. — [arXiv 1111.1797](https://arxiv.org/pdf/1111.1797)
- **[SECONDARY]** Thompson sampling glossary. — [Agile Brand Guide](https://agilebrandguide.com/wiki/statistics/thompson-sampling)

### Inferences
These are standard methods. This pass did not fetch a specific citation for the formulas.

- **Beta-Binomial shrinkage for conversion rates:**
  1. Fit a Beta(α, β) prior to the historical distribution of CVRs across past ads or campaigns, for example by method of moments.
  2. Each new ad's posterior is Beta(α + conversions, β + non-conversions).
  3. The posterior mean (α + c)/(α + β + n) pulls small-n ads toward the portfolio mean.
  4. Rank ads by posterior, or by the probability of beating the incumbent, not by raw CVR.
- **Hierarchical models** (ad within ad set within campaign, or creative attribute effects) extend this. They are the structure that made the Schwartz et al. bandit work.
- **Thompson sampling:** sample from each arm's posterior and allocate traffic in proportion to the probability of being best. It suits short-lived creatives where regret matters more than a clean effect estimate.
- Use A/B tests instead when you need an **unbiased effect size for the knowledge base**. Bandits trade inference quality for reward.
- **Weekly cadence for the loop:**
  - Monday: automated ingest of your own platform data plus competitor-library snapshots and diffs.
  - Then: update posteriors and the shrunken leaderboard, and refresh dashboards with posterior intervals rather than point estimates.
  - Weekly review meeting: decide whether to scale, kill or test, and choose new hypotheses with competitor-angle inputs and empirical priors (section 7).
  - Launch tests with pre-registered parameters.
  - Monthly: meta-analysis and prior recalibration.
  - Quarterly: incrementality tests (geo or conversion lift) to recalibrate platform-reported attribution.
- Note that ad platforms (Meta Advantage+, Google PMax) already run internal bandit-like delivery optimization. A team's own bandit layer is most valuable **across** platforms and for landing pages, email and offers, where the team controls the randomization.

### Gaps
- Whether Schwartz et al. used Thompson sampling specifically was not confirmed; the summary describes a hierarchical, attribute-based policy.
- No evidence was found comparing bandits against A/B tests on long-run knowledge accumulation in marketing teams.

---

## 9. LLMs and AI agents for marketing analytics and competitor monitoring (2025–2026): what is credible

### Takeaway
LLMs are credibly useful for **coding unstructured competitor data at scale**: classifying ad angles, offers and claims, summarizing library diffs and transcribing video ads. They also help draft hypotheses and analysis code. **No rigorous published accuracy benchmark** exists for LLM agents in marketing CI. The main documented risk is hallucinated facts, and most commercial "agents" are fixed workflows. Human verification against source data remains necessary.

### Cited Findings
- **[PRIMARY, review]** A 2025 arXiv review of LLMs in marketing management cites a 2024 study in which LLMs processed competitor textual data for competitive intelligence in tech. The review reports no accuracy figures. — [arXiv 2501.10685](https://arxiv.org/pdf/2501.10685)
- **[PRIMARY]** SOMONITOR (2024) is an explainable LLM pipeline for marketing data processing and competitor/social monitoring. It is an academic system description. — [arXiv 2407.13117](https://arxiv.org/html/2407.13117v1)
- **[VENDOR/SECONDARY]** CI agent products are new 2025–2026 launches:
  - Klue Compete Agent
  - Crayon Spark Agent and Field Agent
  - Contify Athena
  - Quid Q Agents

  — [Rework 2026 guide](https://resources.rework.com/tools/ai-agents/best-ai-agents-for-market-research-2026)
- **[SECONDARY]** The same guide cites Menlo Ventures as reporting that only a small share of production "AI agents" plan and adapt autonomously, with most being fixed workflows. This is secondhand. It also cites Stanford HAI work raising concerns that LLM-simulated survey respondents fail to capture subgroup variance. — [Rework 2026 guide](https://resources.rework.com/tools/ai-agents/best-ai-agents-for-market-research-2026)
- **[VENDOR]** Practitioner guidance says a single fabricated funding round, executive name or integration can derail competitive strategy. It recommends hallucination benchmarks such as Vectara HHEM and human review of anomalies. This is advocacy, not measurement. — [Development Corporate](https://developmentcorporate.com/tag/gemini/); [Meltwater](https://meltwater.com/en/blog/llm-monitoring)
- **[VENDOR]** Apify-based "ads intelligence" agent skills scrape the Meta, Google and TikTok libraries for LLM analysis. This shows that the tooling exists, but its accuracy is unvalidated. — [Apify ads-intelligence skill](https://claudeskills.info/skills/apify/awesome-skills/apify-ads-intelligence/)

### Inferences
- Credible uses, which keep the LLM on **grounded** inputs:
  1. Classify ad creative into a fixed taxonomy (angle, offer, price point, CTA, format, distinctive assets).
  2. Summarize weekly snapshot diffs: new ads, killed ads, angle shifts.
  3. Draft hypotheses for the backlog.
  4. Write and QA analysis code, such as SQL and Bayesian scripts.
- Validate the classification by having a human double-code a sample of, say, 100 ads and reporting agreement (Cohen's κ) before trusting the trend lines.
- Less credible uses:
  - letting agents infer competitor spend or performance with no data
  - synthetic consumer panels in place of tests
  - fully autonomous budget changes without guardrails
- Every agent output that feeds a decision should link to its source ad ID or URL.

### Gaps
- No peer-reviewed 2025–2026 benchmark of LLM agent accuracy on marketing analytics or CI tasks was found.
- The Menlo Ventures and Stanford HAI figures were not verified at their original sources.
