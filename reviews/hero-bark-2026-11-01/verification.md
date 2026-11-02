# Homepage bark hero implementation verification

November 1, 2026. Implementation checks only; no independent design review.

## Result

- Three generated transparent bark pieces based on Guy's supplied image replace the three pretzels. The guide, generated originals and old pretzel files remain intact.
- Hero background is Primary Orange `#E87933`. Hero pattern markup is removed. The copy area has no background, border or shadow.
- Heading, eyebrow, paragraph and transparent CTA use Primary Brown `#3A170D`; both CTA borders remain Brown at rest and focus/hover. Brown/Orange contrast is approximately 5.51:1.
- Wording and the single CTA destination remain unchanged. All homepage content after the hero and the 17 other pages remain unchanged apart from the shared CSS cache query.
- Desktop/tablet retain two columns; phones reserve a clipped art row above the normal-flow copy. A 16px vertical gap separates phone art and copy. Deliberate edge cropping is retained.

## Verification

Hidden CUA in-app browser checks at 1920, 1440, 768, 390 and 320 CSS pixels found all three images loaded, no horizontal overflow and no artwork over the copy. Each screenshot was viewed. Alpha QA was also viewed on Orange, Cream and checkerboard surfaces.

Computed animation durations remain 1.2, 1.3 and 1.4 seconds, with delays of 0, 0.1 and 0.2 seconds and the existing cubic-bezier easing. Scrolling the hero out of view pauses all three animations. Shared JavaScript is byte-identical to the prior export. Existing reduced-motion and document-visibility rules remain in source; OS reduced-motion emulation is unavailable in the current browser controls, so no OS preference simulation is claimed.

Keyboard focus reaches the hero CTA with Brown text and both Brown borders; activating it opens `/lets-talk/#inquiry`. The production preview reported no console errors or warnings in the inspected log.

A local-only response fixture verified the 390px hero with JavaScript blocked and with root text enlarged to 200%. All bark images remain visible; the copy and button stay in normal flow and the hero grows without horizontal overflow. The pre-existing header logo/contact crowding at 200% text is outside this hero revision. The fixture does not alter production files and its server was stopped after checks.

Build, full static validation, deterministic rebuild and whitespace checks pass. The local GitHub Pages artifact passes 1,688 reference checks and 143 project-path HTTP cases across 18 pages and 75 runtime resources. No public push/deployment or WordPress changes were performed.

## Evidence

- [Responsive DOM and interaction results](browser-checks.json)
- [Desktop final](hero-final-desktop.png), [wide desktop](hero-1920.png), [tablet](hero-768.png), [phone](hero-390.png), [small phone](hero-320.png)
- [No-script phone](hero-no-script-390.png), [enlarged-text phone](hero-large-text-390.png), [alpha QA](alpha-qa.png)
- [Preservation checks](../../prototype/qa-site-build/hero-bark-2026-11-01-checks.json)
- [Static checks](../../prototype/qa-site-build/hero-bark-2026-11-01-static-log.txt)
- [Pages artifact checks](../../prototype/qa-site-build/pages-export-checks.json)
- [Generation prompts and selected outputs](../../handoff/hero-bark-generation-2026-11-01.json)
- [Archived source and runtime metadata](../../assets/hero-bark-details.json)

The generated bark is illustrative. It does not establish an actual DeCocoa product recipe or ingredient specification.
