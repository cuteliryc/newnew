# Visual Composition & Layout Rules in Advertising/Banner Design: Evidence, Myths, and Computable Predictors (as of Oct 2026)

Evidence tags used throughout: **[STRONG]** = multiple studies / large-N field or eye-tracking data / replicated; **[MEDIUM]** = a few consistent studies or one large high-quality study; **[SINGLE]** = single study, small N, or lab-only; **[VENDOR]** = platform guidance or vendor/agency claim, not peer reviewed; **[MYTH]** = popular rule not supported by evidence.

Method note: Many full texts (arXiv, PMC, Harvard, UMich) could not be fetched in this session due to DNS failures. Findings below come from search-returned abstracts and summaries unless stated. Items marked "(abstract-level / recalled, verify)" are from well-known papers whose exact numbers I could not re-check in full text.

---

## 1. Golden ratio: is there evidence it improves preference or ad performance?

### Takeaway
**[MYTH] for ads.** Fechner's 1876 golden-rectangle preference has not held up under better methods. McManus found weak group-level preference, with strong but very different individual preferences. Web-layout tests are null or mixed. I found **no study linking golden-ratio proportions to ad CTR, attention or sales**. A layout generator should not hard-code phi.

### Cited Findings
- Fechner (1876): observers picking their favourite of 10 rectangles of varying aspect ratio chose the golden-ratio one. Later critics, McManus (1980) among them, challenged this on method. Thorndike (1917) noted that averaging can make preference look more uniform than it is. — [Frontiers in Human Neuroscience 2016 review (PMC4937063)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4937063)
- McManus (1980) and McManus et al. (2010) used paired comparisons. **Group preference for the golden section was weak.** Individual preference functions were strong and stable over months or years but varied widely between people. A Q-mode analysis found two factors (one group prefers near-squares, one prefers elongated rectangles), which together explained **44%** of the variance. **[MEDIUM]** — [Frontiers 2016 (PMC4937063)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4937063); [Phillips & Norman, aesthetics 2010 PDF](https://www-prod01.wku.edu/psychological-sciences/labs/vision_and_haptics/downloads/phillips_norman_aesthetics2010.pdf)
- A review concludes that recent findings suggest "Fechner's results were anomalous and/or due primarily to methodology." — [Frontiers 2016 (PMC4937063)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4937063)
- Tractinsky, David & Krupnik (AMCIS 2013), N=91: golden-ratio proportions were preferred for **mobile device** shapes but **not for web page designs**. **[SINGLE]** — [AIS eLibrary AMCIS 2013](https://aisel.aisnet.org/amcis2013/HumanComputerInteraction/GeneralPresentations/12)
- Menu-to-content screen-ratio study (N=98): screen ratio significantly affected task performance. In a summary of the work, users of the golden-ratio layout were on average several seconds **slower** and viewed more pages. **[SINGLE]** — [Teesside Univ. record](https://research.tees.ac.uk/en/publications/the-effects-of-screen-ratio-and-order-on-information-retrieval-in/); [cs4fn summary](https://www.cs4fn.org/usability/goldenweb.php)
- Univ. of Twente thesis (N=150, e-retail): layout balance affected emotion, and the author recommended a golden-section layout over a symmetric one. This is student work. **[SINGLE, weak]** — [Twente thesis](https://essay.utwente.nl/60504/)
- A photo-composition study found "no inherent preference towards GR photos overall" and advised skepticism toward GR composition rules. Low-tier venue. **[SINGLE, weak]** — [JSR](https://jsr.org/hs/index.php/path/article/download/1346/617/6689)

### Inferences
- Individual differences dominate aspect-ratio preference, so a population-wide "optimal ratio" is unlikely to exist. Ad aspect ratios are fixed by placement anyway (1:1, 4:5, 9:16, 300x250…). Phi should at most be **one candidate value in a parameter search** (e.g., image/text split 62/38) and be tested against alternatives. Never use it as a prior constraint.
- If the generator learns from results and a ~0.6 split wins, that is more likely a balance or hierarchy effect than "phi".

### Gaps
- No peer-reviewed study found that tests golden-ratio placement inside ads against CTR, conversion or eye-tracking outcomes.
- I could not fetch McManus et al. (2010, Perception) in full to confirm effect sizes beyond the 44% factor figure.

---

## 2. Rule of thirds: evidence from computational aesthetics, eye-tracking and ads

### Takeaway
**[MYTH-not-supported / weak]** as a general driver of aesthetic quality. Large-sample computational work finds it plays "a minor, if any, role" in highly rated photos and paintings. It shows up somewhat in amateur cropping behaviour. I found **no ad-performance evidence** for it. Off-centre placement may matter for leaving room for text or gaze cues, not because of thirds lines.

### Cited Findings
- Amirshahi, Hayn-Leichsenring, Denzler & Redies (2014, *Art & Perception*), "Evaluating the Rule of Thirds in Photographs and Paintings". Computed ROT scores were compared with subjective ROT judgments from **30 participants**. Agreement was good for photos that broke the rule and moderate for photos that followed it. **Aesthetic ratings correlated only weakly with subjective ROT and not at all with computed ROT.** Highly aesthetic photos and many paintings scored about as low on computed ROT as non-compliant photos. Conclusion: ROT plays "a minor, if any, role" in large sets of high-quality images. **[MEDIUM]** — [Amirshahi et al. 2014 PDF (Jena)](https://uniklinikum-jena.de/anatomie1_media/Inhalte/AmirshahiARTP2014-font-1.pdf); [Jena bib record](https://pub.inf-cv.uni-jena.de/bib/Amirshahi_2013_ROT)
- Hoh, Zhang & Dodgson (2023, salient-region placement): the ROT guideline "is not generally valid", though it may help in some situations. **[SINGLE]** — [Victoria Univ. of Wellington record](https://openaccess.wgtn.ac.nz/articles/journal_contribution/Salient-Centeredness_and_Saliency_Size_in_Computational_Aesthetics/25856824)
- "When might we break the rules? A statistical analysis of aesthetics in photographs" (2022, PLOS/PMC): a statistical treatment of composition rules versus ratings. It is the most relevant modern large-sample reference, but I could not read the full numbers. — [PMC9249203](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9249203/)
- Crowdsourced cropping (Berkeley tech report 2012): among the guidelines tested, people most consistently followed the rule of thirds when cropping. This is evidence about **behaviour**, not about the effect on viewer preference. **[SINGLE]** — [Berkeley EECS-2012-94](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2012/EECS-2012-94.pdf)
- Datta et al. (2006, ECCV), "Studying aesthetics in photographic images using a computational approach": one of the first computational-aesthetics papers. It included a rule-of-thirds feature among ~56 low-level features (colourfulness, saturation, texture, depth-of-field, etc.) for high/low aesthetic classification. (Recalled, verify: ROT was not among the dominant predictors, and overall accuracy was ~70%.) — [patent version of the work](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8755596)

### Inferences
- For a banner generator, "subject on a thirds intersection" is a weak feature. Treat it as a learnable coordinate (subject centroid x,y normalized), not a rule. The model can discover whether centred or off-centre placement works for each format.
- In ads, off-centre subjects may help **indirectly**: they free space for headline/CTA (lower clutter), and a face or gaze can point into the copy (see section 4).

### Gaps
- I could not locate Svobodova et al.'s eye-tracking study of the rule of thirds in this session. Its findings are unverified and were not included.
- No study found that tests ROT inside display or social ads against CTR.

---

## 3. Grid systems (modular grids, Swiss style): evidence on readability, fluency, perceived quality

### Takeaway
**Direct evidence is thin.** I found no controlled study that isolates "modular grid / Swiss style" and its effect on ad performance. Support is **indirect**: alignment and order raise processing fluency (Reber et al.), and low complexity plus high prototypicality drive first-impression appeal (Tuch et al.; Reinecke et al.). Margins and whitespace help reading comprehension (Chaparro et al.). Read the grid as a way to cut feature clutter and raise prototypicality, not as a proven effect of its own. **[indirect / MEDIUM via mechanism]**

### Cited Findings
- Processing-fluency theory: the more fluently an object is processed, the more positive the aesthetic response. Variables covered include figural goodness, figure-ground contrast, repetition, **symmetry** and **prototypicality**, all traced to fluency. **[STRONG as theory/review]** — [Reber, Schwarz & Winkielman 2004, PSPR (PDF)](https://pages.ucsd.edu/~pwinkielman/reber-schwarz-winkielman-beauty-PSPR-2004.pdf)
- Tuch et al. (2012, IJHCS): **low visual complexity + high prototypicality = most appealing** websites. Both effects appear within **50 ms**, and complexity has an effect even at **17 ms**. Prototypicality's effect is weaker at very short exposures and catches up with longer ones. Study 1: 119 screenshots at 50/500/1000 ms. **[MEDIUM-STRONG]** — [Google Research pub page](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/); [Google Research blog](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/)
- Chaparro et al. (2004, *Usability News*): four whitespace layouts (margins x leading). **Margins improved both reading speed and comprehension** relative to no margins. Leading did not affect performance but did affect preference. Users were more satisfied with margined text. Small sample (reportedly ~20). **[SINGLE]** — [ERAU portfolio record](https://portfolio.erau.edu/en/publications/reading-online-text-a-comparison-of-four-white-space-layouts/); [bepress](https://works.bepress.com/barbara-chaparro/115)
- Popular claims such as "whitespace improves comprehension by 20%" or a "2021 NN/g study: +32%" could not be traced to primary sources. **[MYTH/unverified]** — [UX Movement discussion](https://uxmovement.com/content/how-margins-and-line-lengths-affect-readability/)

### Inferences
- Implement the grid as a **constraint that raises alignment and reduces the number of distinct edges/positions**, and measure its effect through computable proxies (alignment score, number of distinct left edges, whitespace ratio). Learn the effect from results instead of assuming one.
- Prototypicality is category-relative. A "Swiss" layout may be less prototypical than the category norm in some verticals (e.g., auto dealers, retail promos), which could hurt first impressions. A prototypicality feature (embedding distance to category centroid) is worth computing.

### Gaps
- No peer-reviewed study found that compares grid-based versus free-form ad layouts on attention or CTR.
- No study found that quantifies an "optimal whitespace ratio" for banners.

---

## 4. Visual hierarchy & attention in ads: element size, complexity, faces/gaze, product/logo, text amount, contrast

### Takeaway
This is the best-evidenced area. **[STRONG]** Pieters & Wedel's eye-tracking of 1,363 print ads shows: the **pictorial** captures attention regardless of its size, the **text** element gains attention in proportion to its size, and enlarging the brand or pictorial does not raise total ad attention. The **brand** element is what drives brand memory (Wedel & Pieters 2000). **Feature complexity** (pixel clutter) hurts brand attention and ad attitude, while **design complexity** (creative arrangement) helps (Pieters, Wedel & Batra 2010). **Faces with gaze averted toward the product** raise attention to the product and brand, plus memory and purchase intention **[MEDIUM]**. Meta's 20% text rule was dropped in 2020. Its remaining "less text performs better" line is **[VENDOR]**.

### Cited Findings
**Element surface size (Pieters & Wedel 2004, J. Marketing 68(2):36-50)**
- Data: infrared eye-tracking of **>3,600 consumers** viewing **1,363 full-page print ads** in 65 Dutch magazines. **[STRONG]** — [Scinapse record](https://www.scinapse.io/papers/2147156975)
- **Whole ad:** a 1% increase in ad surface gives about a 1% increase in attention (elasticity ≈ 1). **Text:** a 1% increase in text space raises **overall ad attention by ~0.15%**. **Pictorial and brand:** enlarging them does **not** increase attention to the ad. The authors advise against enlarging the picture to boost attention. — [U. Michigan News summary](https://news.umich.edu/print-ad-pictures-less-is-more)
- **Pictorial** draws the most attention to itself, independent of size. **Text** is size-sensitive. — [U. Michigan News](https://news.umich.edu/print-ad-pictures-less-is-more)
- A 2013 review notes the size effects are not fully consistent. P&W 2004 found significant effects of text size on fixation likelihood and gaze duration but none for brand or pictorial. Later feature-ad work found the reverse pattern, with only text non-significant. "Despite a strong and robust effect of surface size on attention, a deeper inspection... produces a mixed picture." — [Frontiers in Psychology 2013 review (PMC3856423)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3856423/)
- (Abstract-level / recalled, verify) The 2004 abstract also reports that the **brand element is superior at transferring attention** to the other elements, and that brand size increases attention to the brand itself. — [JM DOI 10.1509/jmkg.68.2.36.27794 via Scinapse](https://www.scinapse.io/papers/2147156975)

**Feature ads under clutter (Pieters, Wedel & Zhang 2007, Management Science 53(11):1815-1828)**
- Eye-tracking of **>1,100 feature (retail flyer) ads** with five elements: brand, text, pictorial, **price**, promotion. Attention is measured by selection and gaze duration as a function of element surface sizes. Two **entropy-based salience-under-clutter measures** were introduced. "Significant improvements in attention... can be achieved without increase in costs" by reallocating space. **[MEDIUM-STRONG]** — [INFORMS abstract](https://pubsonline.informs.org/doi/abs/10.1287/mnsc.1070.0732); [RePEc](https://ideas.repec.org/a/inm/ormnsc/v53y2007i11p1815-1828.html)
- The authors flag that whether more attention leads to store sales was untested. — [UMD Smith release](https://rhsmith.umd.edu/news/optimal-feature-advertising-design)

**Visual complexity (Pieters, Wedel & Batra 2010, J. Marketing 74(5):48-60)**
- **249 eye-tracked ads.** **Feature complexity** (dense perceptual features: colour, edges, luminance) **reduces attention to the brand and attitude toward the ad**. **Design complexity** (elaborate creative arrangement of objects) **increases attention to the pictorial and the whole ad, comprehensibility, and ad attitude**. Design complexity is "under direct control of the advertiser." **[STRONG]** — [Tilburg repository](https://repository.tilburguniversity.edu/items/3fddf97a-469e-4d38-9c26-8dbd00c750b2); [Scinapse](https://www.scinapse.io/papers/2180553342)
- (Recalled, verify) In that paper, **feature complexity was operationalized as the JPEG file size** of the ad image. Design complexity was coded on six principles: quantity of objects, irregularity of objects, dissimilarity, detail, asymmetry of arrangement, irregularity of arrangement. This gives a directly computable proxy (see section 7). — [Tilburg repository](https://repository.tilburguniversity.edu/items/3fddf97a-469e-4d38-9c26-8dbd00c750b2)
- Replication-like finding: ad complexity raises attention to the ad but **lowers attention to the brand** (Pilelienė & Grigaliūnaitė 2016). **[SINGLE]** — [RePEc / Eurasian Business Review](https://ideas.repec.org/a/spr/eurasi/v6y2016i2d10.1007_s40821-015-0040-2.html)
- Exposure-time caveat: "mystery" ads, whose visual complexity takes work to decode, are liked less in the initial glimpse but gain approval over time (Wedel, Elsen, Pieters). This matters for scroll-feed exposures of about 1 second. **[SINGLE]** — [UMD Smith "Why clever ads can backfire"](https://www.rhsmith.umd.edu/news/why-clever-ads-can-backfire)

**Faces & gaze cueing**
- Sajjacholapunt & Ball (2014, *Frontiers in Psychology*): banner ads **with human faces drew more attention** than banners without faces. **Averted gaze toward the product** raised attention to the product region compared with direct gaze, and improved brand and message memory. **[MEDIUM]** — [Frontiers 2014](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00166/full); [UCLan repository PDF](https://clok.uclan.ac.uk/id/eprint/13559/1/Frontiers%20-%20Ball%202014.pdf)
- Frontiers 2017 follow-up (mock shopping page): **animated** faces drew more and longer looks than static faces. Gaze toward the product increased product looks whether animated or not, and gave **higher purchase intention**. **[MEDIUM]** — [Frontiers 2017](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.00881/full)
- Adil, Lacoste-Badie & Droulers (J. Advertising Research, pp. 443-455): face presence plus product-directed gaze, compared with no face or viewer-directed gaze, "strongly influence attention, memorization, brand evaluation and purchase intention." **[MEDIUM]** — [HAL archive](https://halshs.archives-ouvertes.fr/halshs-01910205v1)
- Hutton & Nolte (2011, print): viewers spent longer on the ad and the product when the model looked at the product rather than at the viewer. **[SINGLE]** — cited in [Frontiers 2017](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.00881/full)
- **Vampire effect** caveat: celebrity faces can hold attention much longer than other elements and hurt brand recall (Chan & Chau 2023). A 2025 EMAC paper (Kopka et al.) finds celebrity ads get more attention while brand-element attention is unaffected, and the relative vampire effect did not harm downstream outcomes. **[MIXED]** — [HKBU record](https://scholars.hkbu.edu.hk/en/publications/mitigating-the-vampire-effect-of-using-celebrity-in-advertising-a/); [EMAC 2025 PDF](https://proceedings.emac-online.org/pdfs/A2025-126276.pdf)

**Text amount (Meta 20% rule)**
- Facebook/Meta stopped penalizing ads with more image text in auction and delivery from **September 2020**. The text-overlay tool and exceptions list were removed. **[VENDOR/platform fact]** — [Social News Desk](https://www.socialnewsdesk.com/facebooks-20-rule-is-no-more); [Jon Loomer](https://www.jonloomer.com/facebook-text-in-ad-image-rule/)
- Meta still says (informally, to Matt Navarra, with no formal doc) that images with **<20% text perform better**. **[VENDOR]** — [Social News Desk](https://www.socialnewsdesk.com/facebooks-20-rule-is-no-more)
- Third-party "<15% text" advice (2025) is the blog's own number. **[VENDOR, unverified]** — [Madgicx blog](https://madgicx.com/blog/image-optimization-for-meta-ads)

### Inferences
- Encode the ad as **element areas** (brand/logo, pictorial/product, headline, body text, price, CTA) and let the model learn elasticities. Priors from P&W: the pictorial earns attention cheaply (size-insensitive), text area converts roughly linearly into attention to the text, and brand size mainly helps brand fixations. Brand **fixation**, not ad fixation, is what drives brand memory.
- The two complexity findings conflict only on the surface. **Lower pixel-level clutter while keeping creative/semantic arrangement interesting.** Compute both: JPEG size / edge density (feature) and object count / asymmetry (design).
- Faces: add features `has_face`, `face_area`, and `gaze_direction_toward_product/CTA` (from a head-pose model). The prior is positive for product-directed gaze. Watch brand-attention dilution, especially with celebrities.
- Text-amount effects on Meta today flow through user response, not a policy penalty, so learn them from data. The <20% prior is reasonable but vendor-sourced.

### Gaps
- Exact elasticities by element from P&W 2004 (e.g., text-on-text, brand-on-brand) could not be confirmed from full text. Only the ~1.0 (ad size) and ~0.15 (text on overall ad) figures were confirmed via secondary summary.
- The "baby looking at the product" heatmap demo (James Breeze, ~2009, Australian usability blog) is widely cited. It is a small-N vendor demo, and I could not find its primary source this session. Treat it as **[VENDOR]**.
- No peer-reviewed finding located on **logo position** (left vs right, top vs bottom) and ad recall or CTR. The commonly cited NN/g "left logo more memorable" claim was not verified.
- No peer-reviewed evidence found that a specific **CTA button colour** (red vs green, etc.) improves CTR in general. Popular A/B anecdotes are vendor case studies, and the effect is most likely contrast with the surroundings, not the hue. **[MYTH as a universal rule]**, unverified this session.
- Effects of colour contrast between elements (e.g., the WCAG ratio) on ad performance: no ad-specific study found.

---

## 5. Processing fluency, symmetry, prototypicality, colourfulness, whitespace and first impressions

### Takeaway
**[STRONG] mechanism, [MEDIUM] for screens.** Fluent processing (symmetry, contrast, prototypicality, simplicity) increases liking. Website first impressions form in 17-50 ms and are driven by visual complexity and prototypicality. Computed **complexity + colourfulness** (plus demographics) explain about **half the variance** in 500 ms appeal ratings. Ad-specific validation is limited, and short exposure favours simple, upfront designs.

### Cited Findings
- Reber, Schwarz & Winkielman (2004, PSPR 8(4):364-382): aesthetic pleasure increases with processing fluency. Figural goodness, figure-ground **contrast**, repetition/priming, **symmetry** and **prototypicality** all work through fluency. **[STRONG review]** — [PSPR 2004 PDF](https://pages.ucsd.edu/~pwinkielman/reber-schwarz-winkielman-beauty-PSPR-2004.pdf)
- Reinecke et al. (CHI 2013): **548 participants rated 450 websites** after **500 ms** exposure. Computational models of perceived **visual complexity** and **colourfulness** from screenshots, plus demographics (age, education), **explain roughly half the variance** in aesthetic appeal. The first impression later shapes perceived usability and trust. **[MEDIUM-STRONG]** — [Harvard abstract page](https://www.eecs.harvard.edu/~kgajos/papers/2013/reinecke13predicting.shtml); [UW PDF](https://wildlab.cs.washington.edu/Publications_files/Reinecke_CHI2013.pdf)
- (Recalled, verify) Reinecke et al. report that appeal peaks at **low-to-moderate complexity** and **moderate colourfulness**, with preferences varying by age, education and country. Their complexity model used features such as quadtree decomposition, number of text/image areas and a text-area ratio. Colourfulness used Hasler-Süsstrunk-type metrics. — [UW PDF](https://wildlab.cs.washington.edu/Publications_files/Reinecke_CHI2013.pdf)
- Tuch et al. (2012): low complexity + high prototypicality gives the highest appeal, with effects at 17-50 ms. — [Google Research](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/)
- Colourfulness is not linearly tied to aesthetics: a UCL user study found "no direct linear dependence between colourfulness and aesthetics." **[SINGLE]** — [UCL/FAU "A Study of Image Colourfulness"](https://reality.cs.ucl.ac.uk/projects/image-colourfulness/image-colourfulness.html)
- Whitespace/margins: margins improve reading speed and comprehension (Chaparro et al. 2004). **[SINGLE]** — [ERAU record](https://portfolio.erau.edu/en/publications/reading-online-text-a-comparison-of-four-white-space-layouts/)

### Inferences
- Expect **inverted-U** relations for complexity and colourfulness. Model them with nonlinear terms or tree models, not linear coefficients.
- Fluency can conflict with "stopping power". Highly fluent, prototypical banners may be ignored more (banner blindness, section 6). Design complexity can counter this (P,W&B 2010) as long as pixel clutter stays low. This tension is a good candidate for online learning per placement.
- Demographic and cultural moderation (Reinecke) implies interaction terms between visual features and audience segment.

### Gaps
- Lindgaard et al.'s (2006) "50 ms" website impression study was not retrieved this session.
- No study found that links symmetry of ad layout to CTR.

---

## 6. Display banner research: banner blindness, CTA design, position, creative features and CTR

### Takeaway
**[STRONG]** Banner blindness is real but partial. Relevance to the user's goal and position/format change fixation. **[STRONG, platform data]** Viewability depends strongly on position: just-above-the-fold is best, and the 2014 Google study found ~56% of impressions never viewable. **[MEDIUM]** Industrial papers (Yahoo, Google, Alibaba) show that **visual features of the creative add predictive power for CTR**, especially for new ads (cold start). They mostly report AUC/log-loss gains, not interpretable design rules.

### Cited Findings
**Banner blindness & attention**
- Benway & Lane (1998) first described banner blindness: users avoided looking at attention-grabbing ads. — cited in [Sajjacholapunt & Ball 2014](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00166/full)
- Drèze & Hussherr (2003): users fixate more on banners **relevant to their goal-directed search**, which also improves memorability. **[MEDIUM]** — cited in [Frontiers 2014](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00166/full)
- Simola et al. (2011): banners do attract overt attention, especially **vertical banners to the right of the page text**. **[SINGLE]** — cited in [Frontiers 2014](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00166/full)
- Resnick & Albert (Bentley): eye-tracking of 18 site homepages with top or right banners under goal-directed versus free-viewing tasks. Banner blindness emerges with goal-directed tasks. I could not confirm the exact numbers. — [CORE record](https://core.ac.uk/works/7959914)
- A more recent eye-tracking study ("Is banner blindness genuine?", EM Lyon): most participants **fixate ads at least once**. Congruent ads were better memorized, but congruency did not change fixation duration. **[SINGLE]** — [EM Lyon record](https://research.em-lyon.com/esploro/outputs/journalArticle/Is-banner-blindness-genuine-Eye-tracking/9917675609453)

**Position / viewability (Google, 2014 data)**
- **56.1%** of display impressions were never viewable. Median viewability was **68% above the fold vs 40% below**. The most viewable position is **just above the fold**, not the top of the page. By size, **120x240 was highest (55.6%)** and **300x250 lowest (41.0%)**, with vertical formats generally more viewable. **[STRONG for 2014; dated]** — [MarTech summary of Google study](https://martech.org/affects-ad-viewability-5-factors-google-study/); [AdExchanger](https://adexchanger.com/data-exchanges/google-viewability-benchmark-more-than-half-of-all-ads-arent-seen)
- NN/g citing the same data: 73% viewability just above the fold vs 44% just below. — [NN/g page-fold manifesto](https://nngroup.com/articles/page-fold-manifesto)

**Creative visual features and CTR (industry ML papers)**
- Azimi, Zhang, Zhou, Navalpakkam, Mao & Fern (Yahoo; WWW 2012 short, CIKM 2012 full, pp. 495-504): **43 visual features** (some novel, some from aesthetics literature) computed from creatives on RightMedia (then the largest display exchange). They were tested for CTR prediction, ranking and performance classification, and the most CTR-relevant features were selected. Visual features improved CTR prediction. (Recalled, verify: the features covered colour/HSV statistics, number of colours, colour harmony, presence of faces/people, text amount, salient objects and contrast.) **[MEDIUM]** — [CIKM anthology record](https://ir.webis.de/anthology/2012.cikm_conference-2012.53); [arXiv 1202.2158](https://arxiv.org/pdf/1202.2158); [WWW'12 companion PDF](https://archives.iw3c2.org/www2012/proceedings/companion/p457.pdf)
- Cheng et al. (Google, KDD 2012), "Multimedia features for click prediction of new ads in display advertising": image/multimedia features help **cold-start** CTR prediction for new ads. **[MEDIUM]** — [Google Research](https://research.google/pubs/multimedia-features-for-click-prediction-of-new-ads-in-display-advertising)
- Chen et al. (Alibaba/SJTU, ACM MM 2016), "Deep CTR Prediction in Display Advertising": CNN on **raw ad pixels** plus basic features, trained end-to-end. Evaluated on **>50M records**. It beats logistic regression on hand-crafted image features and generalizes to unseen ad images. **[MEDIUM-STRONG]** — [arXiv 1609.06018](https://arxiv.org/pdf/1609.06018); [Papers with Code](https://astro.paperswithcode.com/paper/deep-ctr-prediction-in-display-advertising)
- A 2022 new-ad CTR paper notes that frozen pre-trained image extractors (Mo et al., Ge et al.) may not suit CTR because they are not trained for the task. This argues for fine-tuning on your own outcomes. — [arXiv 2209.11727](https://ar5iv.labs.arxiv.org/html/2209.11727)
- Mishra et al. (Yahoo Research, CIKM 2020), "Learning to Create Better Ads": trains on **pairs of inferior/superior creatives from advertisers' A/B tests** on Yahoo Gemini. It recommends image tags (objects in the image) and generates CTR-oriented text. **Ranking approaches were more robust than generation for unseen advertisers.** **[MEDIUM]** — [CIKM 2020 record](https://ir.webis.de/anthology/2020.cikm_conference-2020.334); [Papers with Code](https://astro.paperswithcode.com/paper/learning-to-create-better-ads-generation-and)

### Inferences
- **Placement/position explains more variance than composition.** Control for placement, size and viewability before attributing CTR differences to layout, or the generator will learn spurious design rules.
- The Mishra et al. pairwise-A/B framing matches a results-learning banner generator. Train a **pairwise ranker on within-campaign creative pairs** to cancel audience and placement confounds.
- Raw-pixel CNNs predict CTR but are opaque. Use them together with interpretable features (sections 4 and 7) so the generator can act on the output (e.g., "reduce text area" or "add a product-directed gaze").

### Gaps
- No peer-reviewed study found that isolates CTA button design (shape, colour, size, copy) in display ads. Evidence is vendor A/B anecdotes.
- Exact feature rankings and effect directions from Azimi et al. could not be verified because the full text was unreachable.
- No post-2020 public Google/IAB viewability-by-position benchmark found. The 2014 numbers are historical.

---

## 7. Computable predictors from a banner image/layout, and their published links to effectiveness

### Takeaway
Several features can be computed automatically and have **published links to attention or aesthetic first impressions**. Few have published links to **CTR or conversions**. The best-supported are: **visual complexity/clutter** (JPEG size, edge density, Feature Congestion), with feature-type complexity hurting brand attention and ad attitude (P,W&B 2010); **colourfulness** (Hasler-Süsstrunk), inverted-U with appeal (Reinecke 2013); **element area ratios** (text/brand/pictorial), which drive element attention (P&W 2004); **faces and gaze**, which raise attention and intention; and **saliency maps**, which validly predict fixations, though their link to sales is not established. Learned CNN features predict CTR (Chen et al. 2016) but are not interpretable.

### Cited Findings
- **Compression-based complexity:** visual complexity can be defined as the file size after JPEG/ZIP compression. It is an algorithmic proxy whose fit to human judgment has to be tested. — [SAVOIAS dataset paper, arXiv 1810.01771](https://arxiv.org/pdf/1810.01771)
- **Clutter metrics:** Rosenholtz et al. (2007, J. Vision) introduced **Feature Congestion** and **Subband Entropy**, plus Edge Density, as clutter measures. They tracked visual search performance on increasingly busy displays. **[MEDIUM]** — [MIT DSpace](https://dspace.mit.edu/handle/1721.1/37593); [MIT Perceptual Science Group](https://persci.mit.edu/?p=459)
- A 2025 crowdsourced study of **1,800 visualizations**: **edge density was a dominant factor** in perceived visual complexity, and Feature Congestion worked well for displays with similar colour/texture variation. **[SINGLE, large-N]** — [arXiv 2510.08332](https://arxiv.org/pdf/2510.08332v1)
- **Link to ads:** feature complexity reduces brand attention and ad attitude, while design complexity increases ad attention and attitude (249 ads). (Recalled, verify: feature complexity was measured by JPEG file size.) — [Tilburg repository](https://repository.tilburguniversity.edu/items/3fddf97a-469e-4d38-9c26-8dbd00c750b2)
- **Colourfulness (Hasler & Süsstrunk 2003):** a metric from the mean and standard deviation of opponent-colour channels, `M = sqrt(σ_rg² + σ_yb²) + 0.3·sqrt(μ_rg² + μ_yb²)` with rg = R−G and yb = 0.5(R+G)−B. It correlates **>90%** with category-scaling ratings on 7 categories (the commonly cited "0.95" was not confirmed). Hue is ignored. Bands run from "not colourful" ≈ 0 to "extremely colourful" ≈ 109. **[STRONG as a metric]** — [EPFL Infoscience](https://infoscience.epfl.ch/record/33994?ln=en); [ColorNet arXiv 1908.08505](https://arxiv.org/pdf/1908.08505); [HSM3 implementation](https://github.com/DrNickRedfern/HSM3)
- **Link to appeal:** computed colourfulness + complexity (+ demographics) explain ~half the variance in 500 ms website appeal. — [Reinecke et al. CHI 2013](https://wildlab.cs.washington.edu/Publications_files/Reinecke_CHI2013.pdf)
- **Saliency models:** they predict fixation locations in ads and shopping scenes (Itti-style saliency, USC 2011, 14 subjects). An ad-specific neural fixation model was evaluated on **400 print ads from 21 brands** (2017). In fashion ads, **DeepFeat** outperformed five other saliency models (2020). A 2025 packaging study combined logo detection with saliency into a "brand attention score" consistent with prior psychophysics. **None show a direct link to sales or CTR at scale.** **[MEDIUM for fixation prediction; gap for performance]** — [USC iLab 2011](https://ilab.usc.edu/publications/Chiang_etal11vss.html); [NITK saliency-for-ads chapter](https://idr.l1.nitk.ac.in/jspui/bitstream/123456789/6698/1/9%20Saliency%20Prediction.pdf); [Springer 2025 brand attention score](https://link.springer.com/article/10.1007/s42452-025-07043-9)
- Vendor attention-prediction tools (e.g., claims of "97% accuracy") are not independently validated. **[VENDOR]** — [Brainsuite](https://brainsuite.ai/en/?p=4829); [Memorable](https://memorable.io/blog/the-role-of-attention-in-effective-advertising)
- **Entropy-based salience under competitive clutter** (Pieters, Wedel & Zhang 2007) is a published, ad-validated way to quantify an element's distinctiveness relative to surrounding ads. — [INFORMS](https://pubsonline.informs.org/doi/abs/10.1287/mnsc.1070.0732)
- **Learned pixel features → CTR:** a CNN on raw ad images improves CTR prediction on >50M records. — [Chen et al. 2016](https://arxiv.org/pdf/1609.06018)
- **Hand-crafted visual features → CTR:** 43 features on Yahoo RightMedia improve CTR prediction and ranking. — [Azimi et al. 2012](https://ir.webis.de/anthology/2012.cikm_conference-2012.53)

### Inferences
Recommended feature set for the generator, ordered by strength of evidence that the feature is related to attention or performance:
1. **Element area ratios** (computable from the layout JSON directly, no vision needed): brand/logo area, product/pictorial area, headline area, body-text area, CTA area, price area, and **total text-area ratio** (OCR or layout). Evidence: P&W 2004, PW&Z 2007, Meta <20% guidance [VENDOR].
2. **Feature complexity:** JPEG file size at fixed quality and resolution (bytes per pixel), Canny edge density, Rosenholtz Feature Congestion / Subband Entropy. Expect a negative effect on brand attention above a threshold. Evidence: PW&B 2010, Rosenholtz 2007.
3. **Design complexity proxies:** object count (detector), size variance of objects, layout asymmetry (mass-centroid offset), number of distinct alignment lines. Expect a positive effect on ad attention within limits. Evidence: PW&B 2010 (coding scheme).
4. **Colourfulness** (Hasler-Süsstrunk M) and its square term for an inverted U. Evidence: Reinecke 2013, UCL study.
5. **Faces:** count, area share, gaze/head-pose vector, and an indicator for gaze pointing toward the product, CTA or headline. Evidence: Sajjacholapunt & Ball 2014/2017, Adil et al.
6. **Predicted saliency share** per element: run DeepGaze or similar, then compute the fraction of saliency mass on logo, product and CTA, and the rank order of first predicted fixation. Valid for attention, unvalidated for CTR, so let the outcome model weight it.
7. **Contrast:** WCAG relative-luminance contrast ratio between text/CTA and the local background (WCAG 2.x AA threshold 4.5:1 for normal text, 3:1 for large text). Also CTA-vs-surround colour distance (ΔE). There is a fluency rationale (Reber 2004) but no ad-CTR evidence was found.
8. **Prototypicality:** cosine distance of the creative's CLIP-type embedding to the vertical's centroid. Evidence: Tuch 2012 (web), with ad validation missing.
9. **Learned embeddings** (fine-tuned CNN/ViT) as a residual predictor. Evidence: Chen 2016, with fine-tuning favoured per the 2022 cold-start paper.
- Low-value or myth features to avoid using as constraints: golden-ratio adherence, rule-of-thirds score (keep subject x/y as raw features instead), and "best CTA colour".
- Always control for placement, size, format and viewability first (section 6). Train **pairwise within-campaign** (Mishra et al. 2020) to reduce confounding.

### Gaps
- No published study found that links **WCAG contrast ratio** directly to ad CTR or recall. The 4.5:1 figure is an accessibility standard (W3C WCAG 2.1 SC 1.4.3), not a performance finding.
- No published correlation found for **JPEG size vs perceived complexity** in ads beyond its use in PW&B 2010 (recalled). The SAVOIAS paper gives the method but no number in the retrieved snippet.
- No public study found that links **DeepGaze** (specifically) outputs to ad CTR or conversions.
- Effect sizes for most visual features on CTR in Azimi 2012, Cheng 2012 and Chen 2016 could not be extracted (full texts unreachable). Those papers report model-level gains, not per-feature elasticities usable as priors.
