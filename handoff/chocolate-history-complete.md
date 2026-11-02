# Complete chocolate-history timeline

November 1 latest refinement: chapter headings now read date, region, then title. Subnavigation is Brown at rest, and timeline source links have compact Font Awesome long arrows. How It's Made retains one Explore Our Craft primary button. [Current revision checks](../reviews/chocolate-history-2026-11-01/order-arrow-action-verification.md). The preceding checks remain historical evidence.

November 1 heading semantics: date/title/region now form each chapter's single h3, and the closing invitation is an h3 under the museum section. The appearance and content are preserved. [Heading verification](../reviews/chocolate-history-2026-11-01/heading-verification.md) records the reported heuristic before and after this correction.

November 1: Guy's layout/link/copy refinement changes the chapter metadata order and shared link styling, centers the museum introduction, and combines the former museum-context copy with Tours and Classes after the timeline. Chapter captions, source destinations and artwork are preserved. The redundant body Let's Talk CTA is removed; the specific Experience Center inquiry and Craft Your Own invitation remain. [Current revision verification](../reviews/chocolate-history-2026-11-01/verification.md). The creation record below remains unchanged.

October 31, 2026. Guy requested the rest of the timeline after reviewing the first four chapters. The same vertical exhibition now covers all ten items in his supplied panorama, inside `/experience-center/#museum-virtual-exhibition`. This continues the existing application and leaves the approved first four chapter records and production artwork intact. No publication or WordPress work is part of this extension.

## Remaining six reference items

| Era | Title | Copy and art direction |
| --- | --- | --- |
| 1800s | The Industrial Revolution | Larger factories, machinery and chocolate's wider availability; interpretive cacao mill, chocolate bars and beans. |
| 1900s | Innovation and Iconic Brands | Cadbury, Hershey and Nestlé retained from the reference copy; original generic confection packaging, bars and truffles. |
| Mid 1900s | A Global Obsession | International distribution, regional tastes and celebration; decorative globe, chocolates and cacao botanicals. |
| Late 1900s | Craft and Fine Chocolate | Cacao origin, single-origin and bean-to-bar work, flavor and technique; chocolatier at a workbench with separate foreground chocolates. |
| 2000s | Sustainability and Impact | Ethical sourcing, farmer livelihoods, forests and accountability; fruiting cacao tree, seedling and beans. |
| Today & Tomorrow | A Sweeter Tomorrow | Flavor, ingredient choices, creativity, fairness and traceability; original chocolate sculpture with separate bars and truffles. |

Era labels and titles follow the reference. These are broad, overlapping thematic periods, not claims that each development began or ended at one precise boundary. The reference's sustainability language is qualified as aims and ongoing challenges. Its unspecified “healthier options” phrase becomes “ingredient choices”; the site makes no new health or nutrition claims. No statement implies DeCocoa holds a certification, participates in the cited programs, owns the depicted factory or made a named brand's products. Existing corrected Aztec chronology remains unchanged.

## Factual sources

- [Lindt & Sprüngli history](https://www.lindt-spruengli.com/company/history/) supports nineteenth-century factory development and conching, international distribution beginning in the 1920s, and mid-century products associated with everyday enjoyment and celebration. The mill artwork is generic, not a reconstruction of Lindt's conche.
- [Cadbury timeline](https://www.cadbury.co.uk/about/history/timeline/) supports Dairy Milk in 1905, Milk Tray in 1915 and later advertising/assortment development.
- [Hershey Community Archives](https://hersheyarchives.org/encyclopedia/hershey-chocolate-company-1894-1900/) supports the transition to milk chocolate in 1900 and early products/packaging.
- [Nestlé UK history](https://www.nestle.co.uk/en-gb/media/newsfeatures/celebrating-150-years) supports entry into chocolate export sales in 1904. Brand names appear in the historical copy; no brand packaging art or logos are reproduced.
- [Valrhona history](https://www.valrhona.us/about-valrhona/our-values/100-years-of-history) supports late-twentieth-century chocolate craft, the 1986 Guanaja blend, 1990 Manjari single-origin chocolate, and creative chocolate work. [ICCO fine flavour cocoa](https://www.icco.org/fine-or-flavor-cocoa/) supports the connection between growing conditions, handling and flavor.
- [Scharffen Berger's 2010 company release](https://www.prnewswire.com/news-releases/scharffen-berger-chocolate-maker-series-releases-new-ben-tre-single-origin-bar-from-vietnam-102428559.html) supports its 1997 founding and late-1990s artisan chocolate work; no claim of the first-ever bean-to-bar maker is made.
- [World Cocoa Foundation sustainability approach](https://worldcocoafoundation.org/our-approach/sustainability-standards-and-regulatory-assurance), [Cocoa & Forests Initiative](https://worldcocoafoundation.org/programmes-and-initiatives/cocoa-and-forests-initiative), and [traceability strategy](https://worldcocoafoundation.org/programmes-and-initiatives/traceability-strategy) support the sustainability and future themes. The captions do not make claims about current legal deadlines or guaranteed outcomes.

The first four chapters' sources remain in [their handoff](chocolate-history-four-chapters.md). All copy is a concise synthesis close to the user-supplied reference, not a verbatim reproduction of the source websites.

## Assets and editing

Nine new usable illustrations were created with the **built-in image generation tool**: six chapter mains plus separate bar, truffle and seedling groups. Existing supports are reused. Each logical group has genuine alpha PNG artwork and smaller responsive variants. Originals are archived under `brand/source/chocolate-history-2026-10-31/`; production assets are under `assets/images/chocolate-history/05-industry/` through `10-today/` and `shared/`. The chocolatier's first output had clipped hair/workbench legs; an image-generation framing edit restored the full silhouette. The superseded original is retained separately.

The sculpture is an original interpretive showpiece. The globe is decorative, with approximate geography and no factual place labels. The tree and seedling are interpretive botanical illustrations. New machinery, people and packaging are not exact historical reconstructions or product photographs.

[Exact new prompts](chocolate-history-complete-prompts.json) record the generation and framing-edit instructions. Earlier prompt records remain. `assets/chocolate-history-assets.json` records source paths, archives, hashes, dimensions, alpha bounds, variants and placements. `prototype/chocolate-history-artwork.json` drives preparation; `prototype/chocolate-history.json` controls all ten captions, sources and scene placements. The same template, CSS and once-only entrance module serve every chapter.

Rebuild with `scripts/build_homepage.py`; restart an already-running preview when new resource paths are added. The closing Craft Your Own Chocolate Bar link follows chapter ten and keeps its existing destination. [Implementation verification](../reviews/chocolate-history-2026-10-31/complete-timeline-verification.md) records final checks and screenshots. The historical independent-review ledger remains unchanged.
