# Independent design review 04

October 11, 2026. Reviewer: GPT-6 Astra, High. Frozen version: `homepage-r4`, recorded in `reviews/homepage-r4-files.json`. Session **4 of maximum 5**. All 59 frozen file hashes matched at the beginning and end. No implementation or asset edits were made.

## Verdict

**Accepted for the requested local homepage and handoff. No remaining essential defect found in this revision.** The requested header, buttons, pretzel hero, pattern covers/motion, corrected wordmark, and icon photo mask are present. No additional aesthetic revision or independent review is necessary for this scope.

Acceptance is for the local prototype. It does not certify partner relationships, certification status, photo rights, final copy approval, production delivery, or Elementor assembly. The supplied marks and photographs remain subject to the documented handoff approvals.

## Requirements and brand evidence

| Requirement / authority | Independent evidence | Verdict |
| --- | --- | --- |
| Palette, manual p.17 and approved brown exception | CSS uses the eight prescribed tokens. Identity artwork retains source #582011 rather than forcing the site token #512316. Brown text on cream/orange remains legible. | Pass |
| Typography, manual p.19 | Local Montserrat; browser FontFaceSet reports loaded and returns true for 300, 400 and 700 at 16px. No synthetic weight or new serif introduced. | Pass |
| Complete identity and quiet backgrounds, manual pp.23–24 | Main, scrolling and footer wordmarks remain complete, static and unmasked on cream/orange. Source-based padding scales with logo size: e.g. 32px around the 240px wordmark, 24px around 180px, 15px around 110px, consistent with Y approximately half the mark height. | Pass |
| Restored e underline, original AI authority | Inspected the source/gallery comparison and separately opened the current SVG with a fresh query string. The underline is visibly present. The ninth painted path is the filled source rectangle, x1852.346–2050.007, SVG y1111.514–1155.518. Saved `logo-underline.jpg`. This specifically corrects an export omission that previous reviews missed. | Pass; see DC-007 |
| Six faithful editable pattern masters | Viewed `scripts/vector-qa.html`: Circles, Flower of Life, Growth, Luxury, Rings and Stripes beside source renders. Arrangement, pod geometry and proportions agree. The master SVGs use vector paths/clips rather than embedded raster substitutes. Website copies introduce the separately approved palette highlights and row motion. | Pass |
| Exact CTA design, direct user revision | Computed primary: Orange background, Chocolate type, outer 2px Cream border/radius16, inner 1px Cream border/radius12. Secondary: transparent, Chocolate type, Orange borders at the same geometry. Shared `.button` rule covers CTAs; no CTA arrow characters found. Mobile size changes preserve the border/radius rules. | Pass |
| Header and container revision | Main logo centered over navigation with top-right Let's Talk. Separate Orange horizontal header appears after downward scrolling and hides on upward scrolling; focused sticky controls keep it visible. Actual 1920px container width is 1500px. | Pass |
| Approved icon-mask exception to pp.23–24 | Experience uses the standalone exterior silhouette at its source aspect ratio 1309.676:1511.664, with a chocolate product photograph. The wordmark is not used as a mask. People uses a separate rectangular image with the full face visible. | Pass |
| No public prototype explainers | Initial page has no route dialogs, provisional captions, implementation explanation, or unbuilt legal links. Contact's conditional valid-input response is exactly “Message delivery is not connected yet.” | Pass |

The whole-page sequence is coherent: hero, products, People, Craft, reference marks, Experience, contact and footer. Stronger pattern covers surround quiet cream reading panels; the large mask and product cutouts keep the imagery chocolate-focused. The People paragraph retains the source-grounded Vigneri/Sicilian-patisserie draft assessed against the supplied Our Roots material in session 03. No new operational, availability or relationship claim was introduced by this revision.

## Stable issue status

| ID | Severity / category | Current status and evidence |
| --- | --- | --- |
| DC-001 | Prior keyboard interaction defect | Resolved. Old destination dialogs are removed. Current desktop submenu keyboard opening and Escape return focus to Our Chocolate. Anchor destinations focus their section heading. |
| DC-002 | Prior mobile focus defect | Resolved. At 390px, Tab from the last navigation link loops to Menu in both original and scrolling headers. Escape closes navigation and returns focus to its Menu button. Nested Escape first closes Our Chocolate and focuses its trigger. |
| DC-003 | Prior hero readability defect | Resolved/superseded. Old tiny caption is absent; current hero copy and CTAs fit at all requested widths, including stacked CTAs at 320px. |
| DC-004 | Prior local-only form contract defect | Resolved. Live DOM has zero forms. Inputs have no native form submission owner; original fieldset is disabled and Send Message is type=button. Source enables the controls after installing local handlers. Enter in a populated field did not navigate or reveal a success state. |
| DC-005 | Prior contact topic defect | Resolved. Find your chocolate navigates to contact and preselects Chocolate & products. Current selector includes the requested topic routes. |
| DC-006 | Prior photo cropping defect | Resolved. Current desktop Craft rendering preserves face, hands and tray. Mobile image remains proportionate; a scroll position hiding its top under the fixed header is not a crop in the image itself. |
| DC-007 | Historical identity export defect, source fidelity | Resolved in r4. Tracks the user-discovered missing e underline, which previous acceptance missed. Current source rectangle, direct browser render and header/footer sightings confirm restoration. No new correction required. |

## Actual responsive and interaction coverage

CUA Chrome review tab `158815728`; temporary source/gallery tabs closed after inspection. All reported widths were checked with actual `innerWidth`, not inferred from a resized screenshot. The 15px difference in scrollWidth is the vertical scrollbar.

| Viewport | Document scrollWidth | Coverage in this session |
| --- | --- | --- |
| 1920 × 1080 | 1905 | Hero/header, direction and focus states, People and Experience covers, motion state checks |
| 1440 × 1000 | 1425 | Hero, product destination, Craft, contact validation/status and footer |
| 768 × 1024 | 753 | Hero, tablet navigation dropdown and Escape |
| 390 × 844 | 375 | Hero, both mobile menus/focus loops, People, Craft, reference marks, Experience, contact and footer through native scrolling |
| 320 × 740 | 305 | Hero, stacked CTAs, scrolling header and product flow; source responsive rules checked for remaining sections |

No page-level horizontal overflow or clipped customer text was observed. All image elements were complete with nonzero natural dimensions after traversal. No claim is made that every section/control was re-tested at every width.

Navigation checks included desktop dropdown ArrowDown and Escape, actual down/up scrolling, the focused-sticky-header exception at the top of the page, mobile click opening, submenu opening, nested Escape, Tab looping and section anchors. Hidden sticky navigation is `inert` and `aria-hidden`; original navigation becomes inert after leaving its region unless it still owns focus. Anchor navigation closes menus and moves focus into the destination. Current browser observations and source agree on these behaviors.

Contact checks used synthetic data only. Empty input focused Name with associated errors. An invalid address focused Email and marked it invalid. With valid inputs, the only result was the agreed unavailable-delivery message; URL remained `#talk`. Pressing Enter before activation left the URL/status unchanged. Initial status was empty. Source contains no input transport, native submission route or storage of contact data. The pause preference is the sole local-storage value.

Motion checks: observed in-view pattern motifs running and offscreen motifs paused; inspected active individual palette highlights. Pause stopped pattern animation, survived reload, and yielded static visible hero art. Resume restored motion. The pretzel entrance is a finite 1.8s fall with staggered delays, ending within 2.16s, rather than continuous falling. Source provides IntersectionObserver pausing, document-visibility pausing, media-query/JS reduced-motion handling and static fallbacks. Continuous motion uses slight row translation and phased individual highlights while preserving master geometry.

## Evidence and limits

Viewed screenshots are in `reviews/homepage-r4/`: `1920-hero.jpg`, `1920-people.jpg`, `1920-experience.jpg`, `1440-hero.jpg`, `1440-contact.jpg`, `768-hero.jpg`, `390-hero.jpg`, `390-people.jpg`, `390-experience.jpg`, `390-footer.jpg`, `320-hero.jpg`, `vector-logo-comparison.jpg`, and `logo-underline.jpg`. Other intermediate viewport captures were viewed in the browser tool. These are review evidence; coordinator final delivery captures are separate.

No full-page screenshot was attempted because that API previously timed out. Review used viewport captures, section anchors and native scrolling. A transient field-action detachment was resolved by refreshing the UI state; the affected value had already been entered, and the validation checks were then completed. One intermediate desktop capture showed a transient scaled paint after resizing; subsequent settled screenshots rendered normally.

Reduced-motion emulation, disabled-JavaScript runtime testing, physical touch devices and background-tab visibility automation were not available/tested in this pass. Their handling was inspected in source; they are not represented as runtime passes. The finite entrance was checked through implementation timing and settled visuals, not recorded as a frame-by-frame animation audit. Cross-browser testing and a formal accessibility conformance audit are outside this review.

Browser cleanup completed: motion resumed, viewport override reset, review/source tabs closed. Browser ownership explicitly released to the coordinator. The remaining fifth review slot is unused.
