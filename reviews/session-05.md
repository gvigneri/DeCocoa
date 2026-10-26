# Independent design review 05 — final

October 11, 2026. Reviewer: GPT-6 Astra, High. Frozen version `homepage-r5`, identified by `reviews/homepage-r5-files.json`. **Session 5 of maximum 5.** All 78 frozen file hashes matched at both the start and end. Reviewer made no implementation or asset edits.

## Acceptance verdict

**Accepted for the requested responsive local homepage and Elementor handoff. No essential defect remains in the reviewed revision.** The new typography, button geometry/hover behavior, Orange eyebrows, Chocolate patterned hero, three distinct source pretzels and supplied dark footer badge satisfy the latest direction. Changed navigation and layout behavior passed the targeted regressions below.

The review loop ends here at 5/5. No sixth review is authorized. If changes follow this frozen version, disclose that they have not received another independent review. This acceptance does not certify production content/rights, partner relationships, certification status, live delivery or a completed Elementor build; the existing handoff qualifications remain applicable.

## Latest requirements and independent evidence

| Requirement and authority | Observed result | Verdict |
| --- | --- | --- |
| Default/body/button 1rem; main navigation 1.25rem, latest user revision; Montserrat manual p.19 | Browser computed body and every `.button` at 16px, every `.nav-link` at 20px. At 1920, 768, 390 and 320, the complete set of paragraph/link/button/field/label computed sizes was only 16px or 20px; no old small responsive override remains. Larger hero introduction text is retained on desktop. Local FontFaceSet reported loaded, with 300/400/700 checks all true. | Pass |
| Double borders with new 8px/4px radii, animated hover, no underlines | Every CTA computed outer radius 8px and inner radius 4px. Source retains outer 2px and inset 1px borders. Actual primary and secondary pointer-hover states settled at translateY(-3px), with 0.22s transitions, contrasting fill/border changes and text-decoration none. Keyboard focus outline was visible. No underline-hover rule remains in source. | Pass |
| Let's Talk secondary treatment | Header CTAs use secondary Orange borders. Original header has transparent fill; scrolling header uses its documented quiet Cream backing to preserve border contrast against Orange. Mobile menu contact entries and footer contact links remain ordinary navigation links. | Pass |
| Orange eyebrows close to headings | Orange labels sit 12px above their headings; compact Chocolate backing on light sections supplies contrast. Viewed Products, People, Craft, trust, Experience and contact at narrow widths. The long Connections & commitments label wraps within its column at 320px. | Pass |
| Chocolate hero with full-height source pattern; remove yellow circle | Viewed current hero at all five required widths. Chocolate/Orange Stripes fills the complete hero; a quiet Chocolate copy panel protects readability. No yellow disc remains. Content container measures 1500px at 1920. | Pass |
| Three distinct supplied pretzels, finite entrance | Current hero matches the intact source core: red drizzle, chunky sprinkles and red/green sugar pearls. Source inspection and export proof show only the detached faint duplicate excluded. No invented hidden edge or detached cut fragment appears. Complete settled image remains inside the hero/page at every width; at 320 its bounding box is x6.83–298.17 within 305px content width. Entrance is one finite 2s group animation. | Pass |
| Chocolate footer, original supplied badge, Orange titles; manual pp.23–24 | Footer computes #512316; titles compute #E87933. Source render and SVG comparison show the same full dark-background badge, e underline, circular text, central mark and three outer circles. Original #FA7110/#FAF0E6 fills are retained, not replaced with site tokens. Badge is static and complete on a quiet solid background with clear surrounding space. | Pass |
| Header identity and existing exceptions | Horizontal identity, six master SVG patterns and exterior icon-mask asset retain r4 hashes. The restored header e underline is visible. The explicit pattern motion/recolor and icon-photo-mask approvals continue to apply; older prohibitions were not incorrectly reapplied. | Pass |

Source/reference material read: current AGENTS, `prototype/implementation-checks-r5.md`, `handoff/revision-05.md`, brand exceptions and updated asset manifest, complete current CSS/JS and trio preparation helper. The supplied manual's palette/typography/identity rules and original artwork remain authoritative except for the recorded user overrides. No re-review of the unchanged six-pattern gallery was necessary: all six masters match their r4 reviewed hashes.

The new hero composition preserves original overlaps while giving each of the three supplied treatments a distinct presence. The taller mobile stack keeps the requested text size and intact art. The larger text produces longer sections, but inspected content remains readable and contained. No new source-copy or trust-status claim was added.

## Responsive and interaction evidence

Used independent CUA Chrome tab `158815757` at the local preview. Actual `innerWidth` and scroll widths were inspected. These are browser viewport checks, not inferred from saved image dimensions.

| Viewport | Document scrollWidth with page unlocked | Current coverage |
| --- | --- | --- |
| 1920 × 1080 | 1905 | Hero, complete trio, 1500px container, typography/radii, actual primary/secondary hover, desktop dropdown keyboard behavior, footer/badge |
| 1440 × 1000 | 1425 | Hero/header, focused navigation, products and scrolling header |
| 768 × 1024 | 753 | Tablet hero/trio, requested type sizes, original menu and final-item focus reachability |
| 390 × 844 | 375 | Hero and complete trio after scrolling; original and two-row scrolling menu, expanded Chocolate submenu, last-item reachability, focus loop and Escape |
| 320 × 740 | 305 | Hero/trio, type sizes, both expanded menus, People/Craft/trust/Experience/contact/footer flow, wrapped eyebrow, contact errors and return-to-top |

Additional 1100×900 check exercises the new gap between header breakpoints: original header uses normal navigation while scrolling header uses Menu. The scrolling header measures 104px, with 796px maximum navigation height. Shift+Tab from Menu reaches the last Let's Talk item; Tab returns to Menu; Escape closes and restores focus. During open-menu scroll lock, scrollbar removal makes scrollWidth equal the viewport, as expected.

At 390×844, the original header measures 176px and its expanded navigation maximum is 668px. The final focused item ends at 842.66px, within the viewport. The two-row scrolling header measures 139px; its navigation maximum is 705px and final item ends at 758.20px. At 320×740, corresponding values are original 168px / 572px / final 738.66px and scrolling 132px / 608px / final 730.97px. The navigation scrolls internally to reveal the last item; full-size text does not strand it below the screen.

Desktop ArrowDown opens Our Chocolate and focuses Products; Escape returns to the disclosure. On mobile, nested Escape first closes the submenu and returns to Our Chocolate, then closes navigation and returns to Menu. Tab wrapping remains inside the active navigation. Section anchors close the menu and focus the destination heading. Downward scrolling reveals the Orange header; upward scrolling away from header focus hides it and sets `inert` plus `aria-hidden=true`. Back to top reaches scrollY 0 and reveals the complete original header. Header metrics are now measured and propagated through CSS variables; inspected runtime dimensions agree with the changed source.

No page-level horizontal overflow or clipped customer text was observed in this coverage. All image elements were complete with nonzero natural dimensions after traversal. Viewed 320px sections confirm that larger text wraps inside the cream panels, field widths and footer. Keyboard focus remains visible against both Cream and Chocolate contexts. This report does not claim every section/control was re-tested at every width.

## Carried-forward checks and stable findings

All recorded findings DC-001 through DC-007 remain resolved. DC-007 is the historical missing e underline, explicitly corrected in r4; its asset hash is unchanged and the current header still shows it. The new badge independently preserves its own underline as well.

Contact remains structurally local-only: zero live form elements, non-submit activation, initially disabled source fieldset, no input transport/storage and no native form owner. Empty activation at 320 produced all three associated field errors and focused Name; status stayed empty. Full invalid-address/valid-unavailable-message/Enter checks from r4 are carried forward because the validation and delivery logic is unchanged. No new successful-transmission claim was added.

Motion was exercised on the new hero: Pause removes the fall animation and leaves all pattern motifs paused; Resume restores the 2s hero rule and motion state. Motion was left resumed. Existing pause persistence, offscreen checks and prior source-master comparisons carry forward from r4. Current source still handles reduced motion, hidden documents, missing observers and local pause storage; changed button hover transitions/lift are explicitly removed for reduced motion.

## Evidence, limits and closure

Fresh reviewed captures in `reviews/homepage-r5/`: `1920-hero.jpg`, `1920-footer.jpg`, `1440-hero.jpg`, `768-hero.jpg`, `390-hero.jpg`, `390-trio.jpg`, `320-hero.jpg`, `320-trio.jpg`, `320-footer.jpg`. Other intermediate viewport images were viewed during navigation. Also independently viewed `assets/images/inspect-Pretzels.jpg`, `assets/images/pretzel-trio-export-proof.jpg` and `prototype/qa-r5/badge-source-comparison.jpg` against the new live artwork. Coordinator deliverable captures remain separate under `handoff/screenshots/`.

No full-page screenshot API was used because it previously timed out; coverage used viewport screenshots, section anchors and native scrolling. Actual hover was inspected by positioning the pointer through a context click, dismissing the context menu, then reading the settled hover style; no CSS state was injected. Reduced-motion OS emulation, disabled-JavaScript runtime, physical touch devices, cross-browser compatibility and a formal accessibility conformance audit were not performed. Reduced-motion/disabled-script behavior was assessed from source, not described as a runtime pass. The fall was checked by timing rules, pause/resume and final composition rather than a frame-by-frame recording.

Cleanup complete: motion resumed, viewport override reset and reviewer tab closed. Retained user-facing tab `158815740` was not operated or closed. Browser ownership was explicitly released to the coordinator. **Final independent review complete; review loop closed at 5/5.**

