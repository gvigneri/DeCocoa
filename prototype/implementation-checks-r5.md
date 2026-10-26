# Homepage-r5 implementation self-check

October 11, 2026. Local Chrome checks through CUA, against the retained server at `http://127.0.0.1:4173/prototype/`. This is implementation evidence for the coordinator and final independent reviewer, not review approval.

## Actual responsive coverage

| Requested viewport | Observed layout width / scroll width | Inspected behavior and visual evidence |
| --- | --- | --- |
| 1920 × 1080 | 1905 / 1905px | Centered stacked header, 1500px outer content maximum, full-height Brown/Orange hero pattern, intact trio, Brown footer with Orange titles and exact badge. Saved `qa-r5/hero-1920.jpg`, `footer-1920.jpg`. |
| 1440 × 1000 | 1425 / 1425px | Body/button computed 16px, main `.nav-link` computed 20px. Outer radius8px / inner4px. Viewed final hero and source badge comparison. Saved `hero-1440.jpg`, `badge-source-comparison.jpg`. |
| 768 × 1024 | 753 / 753px | Both headers use Menu, navigation20px, all buttons16px. Final trio bounding box x354.2..734.6 remains inside753px. Viewed and saved `hero-768.jpg`. |
| 390 × 844 | 375 / 375px | Ordinary/button16px, nav20px. Two-row scroll header139.3px; menu max-height705px follows measured header. Nested Chocolate menu and focus wrap exercised. Last focused Let's Talk bottom758.2px remains inside844px viewport. Saved `hero-390.jpg`, `pretzel-trio-390.jpg`, `menu-390.jpg`. Trio outer box x15.0..360.0 inside375px. |
| 320 × 900 | 305 / 305px | Ordinary/buttons/fields16px, nav20px. Wrapped trust eyebrow removes intrinsic-width overflow without shrinking text. Fields265px. Scroll header132px, menu max-height768px; last focus bottom750.9px inside900px. Trio x6.8..298.2 inside305px. Saved `hero-320.jpg`, `pretzel-trio-320.jpg`. |

An additional 1100 × 900 check exercised the between-breakpoints case: original navigation remains visible at20px while the scroll header uses Menu. Scroll header104px, panel maximum796px. Shift+Tab wraps to the last menu item, Escape closes and returns focus to Menu. At390/320 the nested disclosure and Escape return were exercised. Back to top settled at scrollY0 and revealed the complete stacked header.

## Targeted interaction and source checks

- Actual desktop primary and secondary hover states inspected: both lift3px with0.22s transitions; primary fills Cream and secondary Orange, with appropriate contrasting double borders and no text decoration. Keyboard focus and visible mobile focus outline inspected. Reduced-motion fallback removes lift/transitions and animation in source; OS reduced-motion was not emulated in this browser.
- The hero uses one intact original trio rather than independently cropped pieces. Original overlaps and all exterior edges are preserved. Its finite entrance duration is2s; final opacity1 and complete settled composition inspected at five widths. The animation deliberately enters from above; no claim that entrance pixels remain inside the hero throughout the fall.
- Dark badge source rendering and editable SVG compared side by side in Chrome. Both source colors and geometry remain intact. Header underline stays in the strict source export. Six pattern masters remain editable paths/clips, without raster embeds. These unchanged masters retain prior r4 visual-comparison coverage.
- Pause/resume exercised, and motion was left resumed. Existing local pause preference, hidden/offscreen handling and local-only contact behavior retain prior r4 browser coverage; no repeated full form regression was run for this typography/assets revision. Static checks verify zero native forms/submits, initially disabled fields, no transport calls and only the motion preference storage key.
- Browser console capture contained two identical asynchronous message-channel listener errors, with no application stack. The page does not install extension message listeners. No further error-free console claim is made.
- Final screenshots were viewed before saving. Viewport override reset and the implementation-owned browser tabs closed after checks. No browser is held for further work.

Run `scripts/build_homepage.py`, `scripts/check_homepage.py` and Node `--check prototype/script.js` for build/source verification. `source-checks.json` contains current implementation hashes and the check results. Source artwork is untouched. Trust-mark production approval and photography rights remain handoff open items.
