# Copy and Words: What Is Proven About Ad Copy, Message Effectiveness, and How to Choose and Test Words

Research method note: Web search worked, but WebFetch and curl could not reach most primary hosts in this session (DNS and proxy errors for ncbi, arxiv, cxl, uchicago, spotify, NYU Stern). Many numbers below therefore come from search-engine summaries of primary papers, or from reputable secondary write-ups such as university press offices, Nieman Lab, NBER, and Econometrica listings. Each is flagged where relevant. Before quoting a number externally, check it against the primary paper.

Evidence grading used throughout:
- **[REPLICATED]**: reproduced across studies, a meta-analysis, or a large preregistered or field dataset.
- **[SINGLE]**: one peer-reviewed study or dataset with no direct replication found.
- **[VENDOR/PRACTITIONER]**: a vendor, agency, or blog claim, not independently validated.
- **[FAILED/WEAK]**: failed replication, or a meta-analytic effect near zero.

---

## 1. What academic research shows about language in ads, headlines and conversion (negativity, emotion, concreteness, specificity, numbers, fluency, framing, social-proof wording)

### Takeaway
The best causal evidence on word choice comes from tens of thousands of randomized headline A/B tests in the Upworthy Research Archive. Word-level features do move click-through, but each feature has a small effect, a few percent relative per word, and the direction often contradicts industry rules of thumb. Most other "classic" language effects either hold only under specific conditions or have near-zero meta-analytic averages. Gain-vs-loss framing is the clearest example. Concreteness (Packard and Berger) and high-arousal emotion (Berger and Milkman) are among the better-supported content findings, but their evidence is observational plus lab work, not ad-conversion A/B tests.

### Cited Findings

**Upworthy Research Archive: the core dataset**
- **[REPLICATED dataset]** The Upworthy Research Archive (Matias, Munger, Aubin Le Quere and Ebersole, *Scientific Data* 2021) holds 32,487 headline/image "package" A/B tests run January 2013 to April 2015. It covers 150,817 arms and 538,272,878 participant assignments, and the outcome is click-through. — [Penn State Pure record](https://pure.psu.edu/en/publications/the-upworthy-research-archive-a-time-series-of-32487-experiments-/); [Cornell CALS](https://cals.cornell.edu/news/2021/08/new-archive-reveals-treasure-trove-of-us-media-experiments)
- Data-quality caveat: an Author Correction found that 7,004 tests (22%), run between June 2013 and January 2014, may have had a randomization problem. The authors advise treating those tests as non-randomized. — [Author Correction, PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11239857/); [Matias 2024 archive update](https://upworthy.natematias.com/2024-06-upworthy-archive-update.html)
- The archive is split into exploratory (22,666 arms) and confirmatory (105,551 arms) releases, which lets researchers test preregistered hypotheses honestly. — [TEA-Time, arXiv 2603.07018](https://arxiv.org/pdf/2603.07018)

**Negativity raises clicks (Robertson et al. 2023, *Nature Human Behaviour*)**
- **[REPLICATED / registered report]** "Negativity drives online news consumption" is a Registered Report in *Nat Hum Behav* 7, 812–822 (2023). It analyzed about 105,000 headline variations with roughly 5.7 million clicks over more than 370 million impressions. Because Upworthy tested several headlines per story, story content is held constant. — [Nieman Lab](https://www.niemanlab.org/2023/03/negative-words-in-news-headlines-generate-more-clicks-but-sad-words-are-more-effective-than-angry-or-scary-ones/); [LMU press release](https://www.lmu.de/en/newsroom/news-overview/news/a-new-take-on-an-old-adage.html)
- Effect size: for a headline of average length, each additional negative word raised CTR by 2.3% (relative), and each additional positive word lowered CTR by about 1.0%. — [PsyPost](https://psypost.org/a-particular-type-of-language-boosts-online-news-consumption-study-suggests); [IDEAS/RePEc record](https://ideas.repec.org/a/nat/nathum/v7y2023i5d10.1038_s41562-023-01538-4.html)
- Discrete emotions: sad words were more effective at driving clicks than angry or fearful words. Exact coefficients were not retrieved. — [Nieman Lab headline/article](https://www.niemanlab.org/2023/03/negative-words-in-news-headlines-generate-more-clicks-but-sad-words-are-more-effective-than-angry-or-scary-ones/)
- Robustness: two teams, Robertson and Van Bavel's NYU group, independently found almost identical results on the same data and merged into one paper. — [Nieman Lab](https://niemanlab.org/?p=213135)
- Computational reproduction: a 2025 Institute for Replication (I4R) comment by Reiss and Roggenkamp reproduced both main claims "with only minor and inconsequential discrepancies." It notes the analysis covered 12,448 RCTs, which differs from the 22,743 figure cited in the abstract. — [RWI / I4R discussion paper](https://www.rwi-essen.de/i4r-discussion-paper-series/1/a-comment-on-negativity-drives-online-news-25022501)

**Headline features vs industry advice (Banerjee and Urminsky 2025, *Marketing Science*)**
- **[SINGLE, large-scale]** "The Language That Drives Engagement: A Systematic Large-scale Analysis of Headline Experiments" (*Marketing Science* 44(3): 566–592, 2025) maps text-analysis measures onto constructs from prior literature, validates them with human raters, and causally tests them on Upworthy click-through. Key conclusion: headline features do change CTR, but "prior research and industry advice does not always provide useful guidance as to the direction of the effects." — [INFORMS](https://pubsonline.informs.org/doi/fpi/10.1287/mksc.2021.0018); [IDEAS](https://ideas.repec.org/a/inm/ormksc/v44y2025i3p566-592.html)
- The earlier 2021 working paper warned that "final results from confirmatory dataset are likely to differ." Cite the published version. — [Banerjee & Urminsky working paper](https://home.uchicago.edu/ourminsky/Banerjee_Urminsky_Headlines.pdf)

**Linguistic effects registered report (Gligorić, Lifchits, West and Anderson 2023, *PLOS ONE*)**
- **[REPLICATED design / registered report]** This study tested preregistered hypotheses about headline linguistic features from a pilot partition of Upworthy, then confirmed them on the larger later-released data. The per-feature results, such as length, simplicity and pronouns, were not retrieved in this session. — [PMC: Registered Report](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10038272/); [Protocol](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8443035/)
- A separate ML model trained on hundreds of thousands of headline tests performed only modestly above baseline. The authors argue that reader behavior and context matter more than wording alone. — [NSF PAR record (Digital Journalism)](https://par.nsf.gov/biblio/10301845)

**Emotion and arousal (Berger and Milkman 2012, *JMR*)**
- **[SINGLE field dataset + lab experiments, widely cited]** The study covered nearly 7,000 NYT articles over three months. Content evoking high-arousal emotions, positive (awe) or negative (anger, anxiety), was more viral, while low-arousal sadness was less viral. Positive content was more viral on average. The results held after controlling for surprise, interest, usefulness and prominence, and lab experiments supported arousal as causal. — [Berger & Milkman PDF](https://cssh.northeastern.edu/pandemic-teaching-initiative/wp-content/uploads/sites/43/2020/09/What-Makes-Online-Content-Viral.pdf); [Scientific American](https://www.scientificamerican.com/article/the-secret-to-online-success-what-makes-content-go-viral)
- Tension worth noting: in Upworthy click data, sadness raised clicks (Robertson et al.). In NYT sharing data, sadness lowered sharing (Berger and Milkman). Clicking and sharing are different outcomes, so emotional-word rules do not transfer automatically across KPIs. — sources as above

**Concreteness (Packard and Berger, *JCR*)**
- **[SINGLE paper, 5 studies incl. field text analysis]** "How Concrete Language Shapes Customer Satisfaction" analyzed over 1,000 real customer–employee interactions at two firms (US and Canada) plus experiments. More concrete language ("shirt" instead of "that") raised customer satisfaction, willingness to buy, and later purchasing. — [Knowledge at Wharton](https://knowledge.wharton.upenn.edu/article/how-language-boosts-customer-satisfaction/); [Penn Today](https://penntoday.upenn.edu/news/how-language-boosts-customer-satisfaction-wharton-jonah-berger)
- One blog summary reports that a 5.6% increase in concreteness was associated with an 8.9% satisfaction increase. This comes from a secondary source and is unverified against the paper. — [IntoTheMinds](https://www.intotheminds.com/blog/en/words-influence-customer-satisfaction/)

**Processing fluency (Alter and Oppenheimer 2006, *PNAS*)**
- **[SINGLE, short-lived effect]** Easier-to-pronounce company names and tickers predicted better IPO performance after one day and one week, but not at six months or a year. One portfolio example gave a $333 advantage per $1,000, while a second sample showed only $20. The authors warned against acting on the result. No direct replication was found. — [Princeton news](https://www.princeton.edu/news/2006/05/29/study-stock-performance-tied-ease-pronouncing-companys-name); [Nature news](https://www.nature.com/news/2006/060529/full/news060529-2.html); [Erasmus thesis review](https://thesis.eur.nl/pub/43292/Trouwborst-J.-411038-.pdf)

**Gain vs loss framing: effect near zero**
- **[REPLICATED near-null]** O'Keefe and Jensen (2007) meta-analyzed disease prevention messages: 93 studies, N = 21,656. Gain frames had a tiny advantage, r = .03, driven almost entirely by dental-hygiene studies, with no difference for safer sex, skin cancer or diet. — [PubMed 17934941](https://pubmed.ncbi.nlm.nih.gov/17934941/)
- O'Keefe and Jensen (2009) meta-analyzed disease detection messages: 53 studies, N = 9,145. Loss frames were only slightly more persuasive, r = −.04, which contradicts the usual prospect-theory prediction. — [CBSM summary](https://www.cbsm.com/articles/33455-the-relative-persuasiveness-of-gain-framed-and-loss-framed-messages-for-encouraging-disease-detectio)
- O'Keefe and Wu (2012), on skin cancer prevention (33 studies, N = 4,168), found no significant difference. — [PMC3397368 / search summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC3397368)
- A large field test, UK HMRC tax letters (Hallsworth et al.), likewise found "no evidence that loss framing is more effective than gain framing." — [NBER w20007](https://www.nber.org/papers/w20007.pdf)

**Social-proof wording (descriptive norms)**
- **[REPLICATED in large field RCT]** UK HMRC letters went to more than 200,000 taxpayers. Adding "Nine out of ten people pay their tax on time" and related norm or public-goods messages to reminder letters raised compliance. A secondary table gives roughly +1.3pp for the basic norm, +2.1pp for a country norm, and +4.9pp for a minority norm ("you are in the minority who have not paid"); these need checking against the paper. — [NBER w20007](https://www.nber.org/papers/w20007.pdf); [NBER Digest](https://www.nber.org/digest/aug14/innovative-ways-increase-tax-compliance)
- Localized norm wording ("nine out of 10 people in Oxford") outperformed national wording, per King's College commentary on Hallsworth's work. — [KCL](https://www.kcl.ac.uk/news/nudges-might-be-more-effective-closer-to-home)
- **[PARTIAL replication]** Hotel towel reuse: Bohner and Schlüter (2014, *PLoS ONE*), N = 724 and N = 204 in German hotels, found that any message raised reuse versus no message. The descriptive-norm message ("75% of guests reuse") was *not* better than a standard environmental message, which fails to reproduce the specific advantage Goldstein, Cialdini and Griskevicius claimed for norm wording. — [PMC4118982](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4118982/)

### Inferences
- "Why this word" can be defended with evidence only at the level of feature classes and directional priors. Examples: negative or loss-salient words tend to lift clicks in news-like contexts; concrete nouns beat vague pronouns; local, specific social-proof wording beats generic wording. The evidence does not support claims like "this word will add X% to conversion." Per-word effects in the best dataset are about 1–2% relative CTR.
- Banerjee and Urminsky's finding that industry advice often gets the direction wrong is the strongest argument for testing over copywriting heuristics.
- Click-optimized negativity may conflict with downstream conversion and brand outcomes. None of the Upworthy studies measured purchases, so negativity findings should not be ported to conversion copy without a test.

### Gaps
- Exact per-feature coefficients from Banerjee and Urminsky and from Gligorić et al. (length, numbers, questions, pronouns, readability) were not retrieved because full texts could not be fetched.
- I found no rigorous public evidence specifically on numbers or listicles in headlines, or on "specificity" (e.g., "37%" vs "a lot") in ad conversion beyond practitioner claims.
- Robertson et al. did not report explained variance (R²) in any source I could retrieve. Explained variance is likely low but unconfirmed.
- Nearly all large-scale word evidence uses clicks on news headlines, not ad conversions or sales.

---

## 2. Message testing methods: monadic, MaxDiff, conjoint, A/B and multivariate, and LLM-based pre-testing or synthetic audiences

### Takeaway
In-market randomized tests (A/B, MVT, bandits) are the only method with direct validity for behavior. Survey methods such as monadic, sequential monadic, MaxDiff and conjoint are cheaper screening tools, but I found no published independent validation that their rankings predict in-market conversion. LLM pre-testing currently works as a prior or screening tool, not a replacement. Prompted LLMs pick Upworthy headline winners only modestly better than chance. LLM-simulated outcomes shrink treatment effects toward zero, yet LLM simulations predict the direction and relative size of social-science survey-experiment effects surprisingly well (r ≈ 0.85).

### Cited Findings

**Survey-based message testing (vendor and practitioner descriptions)**
- **[VENDOR]** Monadic testing shows each respondent only one message, which avoids contrast effects. It is typically run with 100–150 respondents per variant and is costly across many options, so it is best for final validation of top candidates. — [CleverX guide](https://cleverx.com/blog/copy-testing-complete-guide-to-message-testing-methods-and-best-practices/)
- **[VENDOR]** Sequential monadic testing shows several messages in rotated order; MaxDiff gives a ranked importance across many claims that a 5-point scale cannot produce. The same source cautions that "preference is not performance." — [Ballpark glossary](https://ballparkhq.com/research-glossary/message-testing)
- **[VENDOR]** One vendor's sample-size guide gives about 600+ for monadic confidence and about 350+ for MaxDiff with 12 variants, per audience, and says fatigue sets in above about 6 messages per respondent. It also notes the most-voted variant is not always the right winner. — [Koji messaging testing guide](https://www.koji.so/docs/messaging-testing-guide)
- **[VENDOR, competing position]** Conjointly argues that MaxDiff's "worst" picks are less useful than identifying the best options, and promotes its own choice-based "Claims Test." — [Conjointly](https://conjointly.com/blog/introducing-claims-test)
- Sawtooth Software, the MaxDiff and conjoint vendor, offers webinar material on experimental designs for messaging research. — [Sawtooth webinar](https://sawtoothsoftware.com/resources/events/webinars/finding-the-perfect-message-experiments-for-messaging-research)

**Survey experiments on persuasion: how predictable are winners?**
- **[REPLICATED/large archive]** Hewitt, Broockman, Coppock, Tappin et al., *APSR* 2024, analyzed 146 experiments by US campaigns on the Swayable platform in 2018 and 2020, covering 617 ads from 51 campaigns and more than 500,000 respondents. Ads differed in persuasiveness in "small but meaningful" ways. Common theories of what makes ads persuasive "have limited and context-dependent power to predict persuasiveness," which is why testing pays: well-funded campaigns test, then scale the winners. — [Yale ISPS](https://isps.yale.edu/resource/how-experiments-help-campaigns-persuade-voters-evidence-from-a-large-archive-of-campaigns); [Coppock PDF](https://alexandercoppock.com/hewitt_etal_2024.pdf); [IDEAS](https://ideas.repec.org/a/cup/apsrev/v118y2024i4p2021-2039_27.html)
- Hill and Vavreck tested 49 political ads in 59 experiments (about 34,000 people) and found small average effects. They also report that the small effects "do not mask substantial heterogeneity." — [search summary of Hill & Vavreck](https://www.poliscidata.com/insights/5469)

**LLMs as predictors and synthetic audiences**
- **[SINGLE, peer-reviewed in *Marketing Science* 2025]** LOLA (Ye, Yoganarasimhan and Zheng) used 17,681 Upworthy headline tests. Prompt-based LLMs picked the winning headline no more than about 65% of the time, against 50% chance. OpenAI-embedding classifiers and fine-tuned Llama-3-8B reached about 82–84% in one version, while the published version describes them as only "marginally higher accuracy than random." In either case they still fall short of experimentation with sufficient traffic. The best method was a hybrid: an LLM prior plus a bandit, which beat standard A/B testing especially when traffic is limited. — [LOLA arXiv](https://arxiv.org/html/2406.02611v3); [INFORMS Marketing Science](https://pubsonline.informs.org/doi/fpi/10.1287/mksc.2024.0990); [IDEAS](https://ideas.repec.org/a/inm/ormksc/v44y2025i5p995-1016.html)
- **[PRACTITIONER, credible engineering source]** Spotify Engineering (August 2026) used gpt-4o-mini predicted CTRs on the Upworthy archive. Plugging raw LLM predictions into standard experiment analysis recovered only 39% of the observed human treatment effect. The bias runs one way: LLM outcomes attenuate effects toward zero. — [Spotify Engineering](https://engineering.atspotify.com/2026/8/when-can-llms-replace-humans-in-a-b-tests/)
- **[REPLICATED across versions]** Hewitt, Ashokkumar, Ghezae and Willer (Stanford) used GPT-4 to simulate responses for 70 preregistered, nationally representative US survey experiments. Simulated predictions correlated r = 0.85 with actual treatment effects, matching or beating human forecasters, and r = 0.90 for unpublished studies that could not be in training data. A later version covers 469 effects and 119,330 participants. It reports that correlations stayed high for post-cutoff studies and open-weight models, but that predictions systematically *overestimated* effect sizes, and that correlations were lower on megastudies. — [Stanford GSB](https://www.gsb.stanford.edu/faculty-research/publications/large-language-models-can-predict-results-social-science-experiments); [Stanford AI4PB](https://ai4pb.stanford.edu/projects/predicting-results-of-social-science-experiments-using-large-language-models)
- Note the conflict on effect-size bias: Spotify found attenuation in a CTR setting, while Hewitt et al. found overestimation in survey-experiment effect sizes. Both agree that LLM magnitudes are not trustworthy. Hewitt et al. find rank and direction more reliable.
- **[VENDOR/INDUSTRY]** PyMC Labs with Colgate-Palmolive used a "semantic similarity rating" elicitation on 57 personal-care concept surveys. It reached about 90% of human test–retest reliability with realistic distributions. — [Research Live](https://www.research-live.com/article/news/llms-could-simulate-human-survey-responses-finds-study/id/5143836)
- **[SINGLE]** Personalized LLM agents did well on factual items but struggled on subjective ones and showed less variance than humans. — [CityU scholars](https://scholars.cityu.edu.hk/en/publications/surveying-with-ai-simulating-human-responses-using-personalized-l/)
- **[SINGLE]** A Chilean public-opinion study ran 128 prompt-model-question combinations. Accuracy and F1 exceeded 0.90 on trust items, but varied substantially by item. — [arXiv 2509.09871](https://arxiv.org/abs/2509.09871v1)
- For headline *generation*, a Yale SOM framework (Wang, Sudhir and Zhou) produced headlines preferred 44% of the time, versus about 30% for human and standard-AI headlines. This is a preference result, not a behavioral one. — [search summary; see LOLA/related coverage](https://letsdatascience.com/news/researchers-teach-llms-hypotheses-to-avoid-clickbait-5a8df083)

### Inferences
- Recommended funnel, inferred from the evidence above:
  1. Generate many variants, using VOC-sourced language and LLMs.
  2. Screen cheaply with an LLM or MaxDiff to cut obvious losers. Rankings are moderately informative; magnitudes are not.
  3. Use a monadic survey for the final 2–4 variants if traffic is low.
  4. Decide with an in-market A/B test or bandit on the business KPI.
- LLM screening is most defensible as a *prior* for a bandit (the LOLA design), or with prediction-powered-inference-style correction against a human holdout. Do not use it as the decision itself.
- Because persuasion theories predict winners poorly (Hewitt et al. 2024), the economic value lies in testing volume and the ability to scale winners, not in picking the "right" principle up front.

### Gaps
- I found no independent published validation showing that MaxDiff or monadic message rankings predict in-market ad CTR, CVR or sales. All method claims are vendor descriptions.
- No conjoint-for-messages validation study was found.
- No peer-reviewed test was found of LLM synthetic audiences predicting *ad conversion* (as opposed to clicks or survey attitudes).

---

## 3. Voice of customer (VOC) and customer-language mining: reviews, calls, search queries; Jobs-to-be-Done framing

### Takeaway
VOC mining is near-universal advice among conversion copywriters (Copyhackers, CXL). However, I found no controlled public evidence quantifying how much copy built from customer language lifts conversion compared with copy written in-house. Its best justification is as a high-yield *hypothesis generator* for tests. The concreteness and local-norm findings in section 1 indirectly support using the customer's own specific words.

### Cited Findings
- **[PRACTITIONER]** Copyhackers' conversion-copywriting method collects VOC from interviews, surveys, reviews, and the client's team, prospects, customers and ex-customers. — [Copyhackers: copywriting research](https://copyhackers.com/2022/06/copywriting-research/)
- **[PRACTITIONER]** Joanna Wiebe describes mining Amazon reviews of addiction-recovery books to find what pushed people toward treatment when direct interviews were impractical. No conversion lift was reported. — [Weidert interview](https://www.weidert.com/blog/tips-for-creating-content-that-converts-an-interview-with-joanna-wiebe)
- **[PRACTITIONER]** Review mining is described as the least time-consuming VOC method, used to collect phrases "in your customers' words." — [LiveChat](https://www.livechat.com/success/voice-of-customer)
- **[PRACTITIONER]** Review-derived objections are used to form A/B test hypotheses. — [Grade.us](https://blog.grade.us/reviews-copy-converts-like-crazy/)
- CXL publishes a VOC-for-conversions guide. Its content could not be retrieved in this session to check for quantified case studies. — [CXL](https://cxl.com/voice-of-customer/)
- Indirect academic support: concrete, specific language improves satisfaction and purchase in real service interactions. — [Knowledge at Wharton](https://knowledge.wharton.upenn.edu/article/how-language-boosts-customer-satisfaction/)
- Indirect support: localized, reference-group wording outperformed generic wording in HMRC field trials. — [KCL](https://www.kcl.ac.uk/news/nudges-might-be-more-effective-closer-to-home)

### Inferences
- A defensible "why this word" chain looks like this: (a) frequency and prominence of a phrase in reviews, calls or search queries (the customer actually uses it); (b) alignment with a feature class that has directional evidence (concrete, specific, locally framed social proof); (c) an in-market test result. Steps (a) and (b) justify putting a word *into the test*; only (c) justifies *shipping* it.
- Search-query data provides behavioral VOC: the words people type when they want something. It is likely a stronger relevance signal for search-ad copy than survey language. This is an inference; no study was found.

### Gaps
- No peer-reviewed or controlled study was found that measures conversion lift of VOC-derived copy against control copy.
- No rigorous empirical validation of Jobs-to-be-Done framing in copy was found. JTBD evidence is case-based and practitioner-driven. (Not searched in depth because of tool-call limits; treat as an open gap.)
- No public Copyhackers or CXL case-study numbers were verified.

---

## 4. Persuasion principles: what replicated vs what failed (Cialdini, behavioral economics, priming)

### Takeaway
Social norms and social proof hold up in large field RCTs, but with small absolute effects and only conditional superiority over plain messages. Gain/loss framing and choice overload average near zero in meta-analyses. Money priming and other social priming failed large multi-lab replications. Across the board, published academic effects are inflated: nudges run at scale by government nudge units averaged 1.4pp versus 8.7pp in academic journals.

### Cited Findings
- **[REPLICATED: effect-size inflation]** DellaVigna and Linos, *Econometrica* 2022, compared 126 RCTs from two US nudge units (more than 23 million people) with published academic nudges. The nudge units averaged +1.4pp (about +8% relative); academic papers averaged +8.7pp (+33.4%). Selective publication combined with low power explains about 70% of the gap in the published version, and "the full difference" in the 2020 working paper. — [Econometrica listing](https://www.econometricsociety.org/publications/econometrica/2022/01/01/rcts-scale-comprehensive-evidence-two-nudge-units); [NBER w27594](https://www.nber.org/system/files/working_papers/w27594/w27594.pdf)
- **[REPLICATED, field]** Social-norm wording in tax letters raised payment across more than 200,000 UK taxpayers. — [NBER w20007](https://www.nber.org/papers/w20007.pdf)
- **[PARTIAL]** The specific advantage of norm wording in hotel-towel messages did not replicate (Bohner and Schlüter 2014), although any message beat no message. A Bayesian meta-analytic dataset of towel studies exists (Scheibehenne, Jamil and Wagenmakers 2016); its pooled estimate was not retrieved. — [PMC4118982](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4118982/); [metaBMA towels dataset](https://search.r-project.org/CRAN/refmans/metaBMA/html/towels.html)
- **[FAILED/WEAK]** Gain/loss framing meta-analyses show r ≈ .03 to −.04 (see section 1). — [PubMed 17934941](https://pubmed.ncbi.nlm.nih.gov/17934941/)
- **[FAILED/CONTESTED]** Choice overload: Scheibehenne et al. (2010, *JCR*) meta-analyzed 63 conditions from 50 experiments (N = 5,036); the mean effect was "virtually zero" with large variance. Chernev et al. (2015) and McShane and Böckenholt (2018) identified moderators. — [Scheibehenne 2010 PDF](https://abcwest.cogs.indiana.edu/pmwiki/pdf/scheibehenne.options.2010.pdf); [NSF PAR review](https://par.nsf.gov/servlets/purl/10481276)
- **[FAILED]** Many Labs (36 labs) failed to reproduce currency priming and flag priming in most attempts (n = 6,333 for money priming). Rohrer et al. ran four high-powered replications of Caruso et al. (2013) and found no money-priming effect. A 2019 meta-analysis (Lodder et al., 246 experiments) found g = .31 but flagged strong publication bias, with the largest effects in lab studies involving handling money. — [PMC4831299](https://pmc.ncbi.nlm.nih.gov/articles/PMC4831299); [Tilburg meta-analysis](https://research.tilburguniversity.edu/en/publications/a-comprehensive-meta-analysis-of-money-priming/); [Lodder 2019 PDF](https://Www.Gwern.net/doc/statistics/bias/2019-lodder.pdf)
- **[UNVERIFIED]** Scarcity ("Only 1 room left"): no public Booking.com A/B results were found. Regulators and watchdogs found such claims misleading: Which? found 5 of 10 checked claims inaccurate, the Dutch ad authority ruled against Booking.com in 2014, and Belgian authorities reprimanded it. This creates legal risk for scarcity wording that is not literally true. — [Which?](https://www.which.co.uk/news/2019/09/booking-com-still-misleading-holidaymakers-with-1-room-left-claims/); [DutchNews](https://www.dutchnews.nl/news/2014/07/bookingcom_does_mislead_with_o); [Brussels Times](https://www.brusselstimes.com/belgium/1063448/only-one-room-left-booking-com-reprimanded-for-misleading-consumers/)
- An academic study ("Only one room left!", Airbnb/Booking data plus an online experiment) reports scarcity effects on value and urgency perceptions. Effect sizes were not retrieved. — [Datalearner listing](https://www.datalearner.com/academic/journal-papers/1567-4223/volumes-and-issues/94/paper-detail/31677)

### Inferences
- Use behavioral-science principles as *test ideas* and discount published effect sizes heavily. DellaVigna and Linos suggest expecting roughly one-sixth of the published lift when a principle is applied at scale.
- Social proof that is true, specific and local is the best-supported "principle wording" for behavior change. Framing swaps (gain vs loss) are low-priority tests.
- Avoid copy that relies on priming-style subtle cues. The replication record is poor.

### Gaps
- The decoy effect replication literature (e.g., Frederick, Lee and Baskin 2014) could not be verified from a reliable source in this session.
- No quantified, independent field evidence was found for authority, reciprocity, commitment or "liking" wording in ads specifically.

---

## 5. Typical effect sizes of copy changes in A/B tests, and sample sizes needed to detect them

### Takeaway
Most experiments fail. Only about a third of well-designed tests at Microsoft improve the target metric, and about 10–20% (8% at Airbnb) do at Google, Bing and Booking.com. Real word-level effects are a few percent relative. Detecting them on low-baseline metrics such as CTR and CVR needs tens of thousands to hundreds of thousands of users per arm. Huge copy wins exist but are rare. The Bing ad-title change (+12% revenue, more than $100M per year) happens "only once every few years."

### Cited Findings
- **[REPLICATED internally, flagship example]** Bing, 2012: lengthening ad titles by merging the title with the first line of ad text raised revenue about 12%, over $100M per year in the US, without hurting user-experience metrics. It was replicated multiple times over a long period. The idea sat in the backlog for more than six months. Kohavi says simple changes with such big gains happen "only once every few years." — [Kohavi, Tang & Xu book excerpt (Cambridge)](https://assets.cambridge.org/97811087/24265/excerpt/9781108724265_excerpt.pdf); [KDnuggets](https://www.kdnuggets.com/2020/04/trustworthy-online-controlled-experiments-book.html)
- That revenue jump triggered a "too good to be true" alert, an example of Twyman's law: implausibly large wins usually indicate bugs. — [Cambridge excerpt](https://assets.cambridge.org/97811087/24265/excerpt/9781108724265_excerpt.pdf)
- **[REPLICATED across companies, secondary summaries]** Success rates by company:
  - Microsoft: about one-third of well-designed experiments improved the key metric, with the rest roughly evenly split between flat and negative.
  - Google and Bing: about 10–20% positive.
  - Booking.com, Google Ads, Netflix and Bing: about 10–15%.
  - Airbnb relevance team: about 8% significantly improved key metrics.
  These figures come from secondary summaries; verify against Kohavi's book or papers. — [HBR via Stern PDF](https://web-docs.stern.nyu.edu/executive/The%20Surprising%20Power%20of%20Online%20Experiments.pdf); [Brainscape summary of Kohavi & Thomke 2017](https://brainscape.com/flashcards/kohavi-and-thomke-2017-the-surprising-po-18591048/packs/22809726); [Lenny's Podcast notes](https://podpulse.ai/podcast-notes-and-takeaways/lennys-podcast-product-growth-career-the-ultimate-guide-to-ab-testing-ronny-kohavi-airbnb-microsoft-amazon)
- **[REPLICATED]** Word-level effects in the largest headline dataset are about +2.3% relative CTR per negative word and about −1.0% per positive word (Robertson et al. 2023). — [PsyPost](https://psypost.org/a-particular-type-of-language-boosts-online-news-consumption-study-suggests)
- Political ad tests show small average persuasion effects with real but small variation between ads. — [Hewitt et al. 2024](https://isps.yale.edu/resource/how-experiments-help-campaigns-persuade-voters-evidence-from-a-large-archive-of-campaigns)
- At-scale nudges average +1.4pp, about +8% relative. — [Econometrica](https://www.econometricsociety.org/publications/econometrica/2022/01/01/rcts-scale-comprehensive-evidence-two-nudge-units)
- Sample-size rule of thumb: n ≈ 16σ²/δ² per variant (two-sided α = 0.05, 80% power). Example: a 5% baseline with a +0.5pp lift needs about 30,400 users per variant. Halving the detectable lift quadruples n. — [MetricGate](https://metricgate.com/blogs/ab-testing-minimum-sample-size/)
- Very small MDEs (e.g., +0.1pp on a 2% baseline) "will demand millions of observations." User-level variance can make large traffic deceptively underpowered. — [Analytics-Toolkit](https://blog.analytics-toolkit.com/?p=1071); [arXiv 1501.00450](https://arxiv.org/pdf/1501.00450)
- Underpowered tests exaggerate winners (the winner's curse). This is the same mechanism DellaVigna and Linos identify for publication inflation. — [Econometrica](https://www.econometricsociety.org/publications/econometrica/2022/01/01/rcts-scale-comprehensive-evidence-two-nudge-units)

### Inferences
Worked examples, my own arithmetic using the cited n ≈ 16·p(1−p)/δ² formula:

| Baseline | Relative lift to detect | Absolute δ | Users per arm |
|---|---|---|---|
| 2% CTR | 10% | 0.2pp | ≈ 78,400 |
| 2% CTR | 5% | 0.1pp | ≈ 313,600 |
| 3% CVR | 10% | 0.3pp | ≈ 51,700 |
| 3% CVR | 20% | 0.6pp | ≈ 12,900 |

- Implication: most SMB accounts cannot reliably detect single-word effects, which are about 1–3% relative, on conversion. They should do two things:
  - Test *big* message differences, such as different value propositions or angles, rather than single-word swaps.
  - Use higher-funnel proxies (CTR, thumb-stop rate) with caution, or run bandits or LLM-prior bandits (LOLA) when traffic is limited.
- Set the expectation that 70–90% of copy tests will be flat or negative. A program's value comes from volume of tests and from not shipping losers.
- Any copy test claiming +30% or more should trigger a Twyman's-law check: tracking bugs, sample-ratio mismatch, novelty effects, or underpowered noise.

### Gaps
- The "200,000 users" Kohavi rule of thumb could not be verified from a primary source.
- I found no public distribution of effect sizes specific to ad copy (as opposed to all experiments) from Kohavi, Booking or Bing. The Upworthy distribution exists, but its summary statistics were not retrieved.
- Booking.com's own copy experiments are not publicly quantified.

---

## 6. Brand-specific language and distinctive verbal assets (Ehrenberg-Bass)

### Takeaway
Ehrenberg-Bass treats taglines and other words as one class of distinctive brand assets. An asset is judged on **fame** (the share of category buyers who link it to the brand) and **uniqueness** (whether it evokes only that brand). The point of a verbal asset is brand linkage and memory, which is a different objective from short-term CTR optimization. Optimizing ad copy purely by A/B test can erode consistent brand language.

### Cited Findings
- **[ACADEMIC/PRACTITIONER framework]** Romaniuk's *Building Distinctive Brand Assets* (OUP) has chapters "Taglines and other words," "Metrics: Fame," "Metrics: Uniqueness" and "The Grid" (the Distinctive Asset Grid). — [OUP](https://www.oup.com.au/books/higher-education/business-marketing/9780190337148)
- Distinctive assets are non-brand-name elements that trigger brand recall among category buyers; taglines are listed among them. An element counts as distinctive only if it scores high on both fame and uniqueness. — [Perceptive](https://www.perceptive.co.nz/blog/brand-distinctiveness-what-does-it-mean-for-you); [Marketing Architects](https://www.marketingarchitects.com/blog/v41-n3-your-brand-assets-may-be-working-against-you)
- **[PRACTITIONER interpretation]** One practitioner argues that fame matters more than uniqueness in practice, because without fame the brand does not register. — [Marketing Architects](https://www.marketingarchitects.com/blog/v41-n3-your-brand-assets-may-be-working-against-you)
- Romaniuk warns that leaning on an asset's *meaning* can "put an expiry date on the asset" when strategy changes. Assets should be chosen for brand linkage, not for message content. — [Marketing Week](https://www.marketingweek.com/jenni-romaniuk-meaning-distinctive-assets/)
- Ehrenberg-Bass has run R&D on "what are the ingredients of a good tagline distinctive asset." — [ResearchWorld Q&A with Romaniuk](https://archive.researchworld.com/qa-with-jenni-romaniuk-of-the-ehrenberg-bass-institute)
- Mark Ritson (2025) discusses the industry converging on how to name and define distinctive marketing. — [The Drum](https://www.thedrum.com/news/2025/10/06/mark-ritson-we-know-what-distinctive-marketing-looks-now-let-s-agree-what-call-it)

### Inferences
- Use a two-layer copy system:
  - **Fixed** verbal assets (tagline, recurring phrase, product nicknames). Measure these by fame and uniqueness surveys among category buyers and keep them consistent.
  - **Variable** performance copy (hooks, offers, angles). A/B test this aggressively.
- "Why this word" therefore has two different justifications:
  - For a brand asset: survey-measured fame and uniqueness over time.
  - For performance copy: in-market test results.
- Do not A/B-test the tagline away for a short-term CTR gain. Short-term test metrics do not capture brand linkage, and nothing in the click studies measures it.

### Gaps
- I retrieved no quantitative Ehrenberg-Bass data on taglines or words specifically, such as typical fame or uniqueness levels or how long verbal assets take to build. Only the framework was found.
- No study was found linking distinctive verbal asset strength to ad conversion or sales lift. Ehrenberg-Bass work focuses on mental availability metrics.
