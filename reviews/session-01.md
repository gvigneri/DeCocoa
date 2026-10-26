# Independent design review 01

Date: October 11, 2026. Reviewer: GPT-6 Astra, High. Frozen version: `hero-r1`, identified by `reviews/hero-r1-files.json`; all listed SHA-256 hashes matched during this review. This is session 1 of the maximum 5. Only the header and hero are in scope. No implementation files were edited.

## Verdict

**Accept the visual direction; correct two major keyboard issues before expansion.** The warm cream/orange composition, large supplied product image, light/bold headline contrast, and restrained pattern panel provide a strong starting point. No confirmed brand violation was found. The missing later homepage sections are intentional at this stage.

## Evidence and coverage

- Viewed actual browser screenshots `hero-r1/1920.png` (1920 x 1080), `1440.png` (1440 x 1000), `768.png` (768 x 1024), `390.png`, and `320.png`. The saved mobile images show viewport portions with vertical scrollbars, not complete-page flow.
- Independently operated the local preview at `http://127.0.0.1:4173/prototype/` in CUA Chrome tab `158815674`, at 1440 x 1000, 390 x 844, and 320 x 760. The coordinator's original tab was unavailable in this agent session. Temporary viewport settings were reset and the review tab closed afterward.
- Viewed manual page 17 palette, page 19 type, logo variant preview, page 23 clear-space construction, and page 24 prohibitions in `references/source-previews/`. Viewed the source logo raster, original `Bark filled.png`, and Stripes export. Read the source hierarchy, rules, exceptions, and export manifest.
- All three rendered image elements reported complete and nonzero natural dimensions: `decocoa-horizontal.svg`, `stripes.png`, and `filled-chocolate.webp`. Compared the rendered horizontal logo to `horizontal-source-cropped.png`; its geometry and source brown are consistent. Preserving source #582011 is correct; the website token exception #512316 does not authorize recoloring it.
- The logo is static, proportional, and on solid cream, separate from the pattern (manual pp. 23-24). At 320px the measured logo is 150 x 38.953px, with 20px reserved padding and 20px left inset, consistent with approximately half-mark-height Y. The other frozen sizes visibly retain clear space.
- Font stylesheet uses local Montserrat files with 300/400/700 declarations and `font-synthesis:none`; provenance and OFL are present. Browser computed family is Montserrat, Arial, sans-serif, with title weight 300 and strong weight 700; the rendered appearance matches the manual. The browser's read-only DOM scope did not expose an iterable FontFaceSet, so this reviewer did not independently verify network/font-load status per face. Susa is absent and optional.
- Chocolate on orange calculates to 4.503448:1, meeting 4.5:1 without rounding up; chocolate on cream is comfortably above the threshold. No text contrast failure found in this stage.
- Tested desktop click, Enter and ArrowDown submenu opening; ArrowDown to Products; Escape closing and returning focus to Our Chocolate; Products destination dialog and Escape. Tested mobile Menu click/Enter, Tab to Our Chocolate, nested submenu Enter, Products click/dialog/Escape, nested Escape to Our Chocolate, second Escape to Menu, and tabbing beyond the last navigation item. Checked the resulting DOM focus and viewed the mobile open-menu screenshot.
- At 1440px and 390px, document scrollWidth equaled the viewport; at 320px it was 305px excluding the vertical scrollbar. No horizontal page scroll was observed. At 768px the product and pattern deliberately extend beyond the right edge; the result feels cramped compared with the desktop and stacked mobile compositions, but the headline and controls remain clear.
- Hero is static. Source review found no automatic animation and a reduced-motion rule disabling smooth scroll, animation, and transition. OS-level reduced-motion emulation was not exercised; no animated behavior is claimed as tested. Native touch hardware and screen-reader output were not tested. No form exists at this stage.

## Findings

### DC-001 — Major — Accessibility / interaction — Desktop dialog loses return focus

**Status: Open.** At 1440px, open Our Chocolate, activate Products, then press Escape on the destination dialog. The submenu closes when focus enters the dialog. On closing the dialog, `document.activeElement` is BODY and `#chocolate-menu.hidden` is true. The return target is now hidden, so focus does not return to a usable control. This reproduces with keyboard activation; the browser snapshot after closing contains no active navigation item.

Requested correction: preserve the submenu while its destination dialog is open, or explicitly return focus to the visible Our Chocolate trigger when the original submenu control is hidden. Apply the same rule to every close mechanism and submenu destination. Verify the next Tab continues predictably.

Authority: master brief sections 6 and 8, predictable keyboard focus return. No manual page applies.

### DC-002 — Major — Accessibility / interaction — Mobile focus passes behind the menu

**Status: Open.** At 390 x 844, open Menu with the Chocolate submenu closed, then focus Let's Talk and press Tab. The active element becomes Experience With Us while the navigation remains expanded and body overflow remains hidden. The active hero button is covered by the menu, with no visible focus indicator. See `hero-r1/mobile-focus-obscured.jpg`, viewed during this review. The browser snapshot explicitly marks Experience With Us active while the screenshot displays the covering menu.

Requested correction: choose a consistent mobile-menu focus model. Either contain focus within the open menu and its toggle, or close the menu when keyboard focus leaves navigation so the next focused content control is visible. Preserve Escape, dialog return, and scroll restoration.

Authority: master brief sections 6 and 8, visible focus and correct mobile menu state. No manual page applies.

### DC-003 — Minor — Design — Supporting hero text becomes too small

**Status: Open. Design judgment, not a brand-rule violation.** The figure caption is 8px at tablet/mobile, and the bottom strip is 8px on mobile. These labels are difficult to read in `hero-r1/768.png`, `390.png`, and `320.png`; the caption adds another very small line below already expressive product imagery.

Requested correction: remove the redundant figure caption at small widths, or use a readable minimum around 11-12px. Bring the bottom-strip labels to a similarly readable size or simplify that strip when the complete homepage is added. Preserve the clear headline/CTA hierarchy.

## Carry forward

Keep the original artwork and current logo treatment. Correct DC-001 and DC-002 before expanding. Treat DC-003 as modest legibility polish; do not replace the strong visual direction. Recheck the tablet's right-edge crop when the page-wide spacing system is finalized. No extra independent pass was started in this session.
