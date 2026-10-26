# homepage-r4 implementation verification

Checked October 11, 2026. This is coding-agent self-QA, not an independent review invocation. Browser interactions used CUA Chrome only. Screenshots were viewed for the visual findings below; final deliverable captures belong to the coordinator after review.

## Responsive observations

| Viewport | Geometry and viewed result |
| --- | --- |
| 1920 × 1080 | Outer content container measured exactly1500px; document scroll width1905px including15px scrollbar allocation, no horizontal overflow. Centered stacked header, complete settled pretzel composition and full Experience Growth cover/photo mask viewed. |
| 1440 × 1000 | Document scroll width1425px; no overflow. Hero and source-comparison gallery viewed. Final Craft image measured666.531 × 498.281px, matching original931:696 ratio; complete face and tray remain visible. |
| 768 × 1024 | Scroll width753px, all containers fit. Hero CTAs11px. Centered original nav; separate sticky header uses Menu control. People full-cover pattern and complete source worker photo viewed. |
| 390 × 844 | Scroll width375px, hero CTAs11px. Settled clean pretzels and centered logo viewed. Touch navigation, local contact errors and contact journey exercised. |
| 320 × 900 | Scroll width305px, all section containers fit. Hero CTAs11px and190px wide, stacked. Experience cover and chocolate silhouette viewed. Contact inputs/select/textarea each265px wide with right edge285px, inside viewport. |

Main container includes its own padding. Source photos use complete original framing. People uses a quiet cream frame; the exact icon photo mask is in Experience with original chocolate photography, so it implies no facility appearance and clips no face.

## Actual browser behavior checks

- Desktop Our Chocolate click and ArrowDown opened submenu and focused Products. Escape returned focus to the toggle and collapsed it.
- Tablet scroll Menu opened; Shift+Tab from Menu wrapped to its final visible contact link. Escape closed and returned focus to Menu. Mobile original Menu and nested Chocolate submenu worked; selecting Gifting closed both and preselected Gifting in contact.
- Orange scroll header appeared on downward scroll beyond original header. Upward scroll with focus elsewhere hid it and set inert=true/aria-hidden=true. Focused scroll Chocolate control remained visible and non-inert after returning to scrollY=0, preserving focus above the threshold.
- Back to top settled at scrollY=0 with original logo link top3px, revealing the complete stacked header. Brand and footer top links use the real body #top anchor.
- Empty message attempt produced three field errors and focused Name. Filled local test values, pressed Enter in email: no native submission, status stayed hidden and URL stayed unchanged. Clicking Send Message displayed only “Message delivery is not connected yet.” No form element exists.
- Contact status was blank initially and after reload. Fields were blank after reload. Experience CTA preselected Experience Center.
- Pause motion stopped pattern paths. Reload preserved the paused preference and showed Resume motion. Static hero remained visible while paused. Resuming worked; motion was left resumed before tab closure.
- Viewed People pattern reported running; offscreen hero and Experience covers reported paused. Source handles document visibility changes as an additional pause condition. Document-hidden transition and OS reduced-motion switch were not emulated by available browser capability; their CSS/JS paths were checked directly.
- Finite hero animation measured1.8s with0/.18/.36s delays, total2.16s. All settled image opacities1. Continuous highlights have different individual source-path phases (observed0s/-26s,0s/-7s,0s/-1s,0s/-11s,0s/-5s,0s/-15s).
- No missing loaded images and no browser error/warning logs in the final desktop pass. All inline SVG IDs were unique.

## Source and asset checks

- `scripts/prepare_assets.py` rerun completed successfully; strict vector export runs first, legacy incomplete logo converter removed. `scripts/build_homepage.py` regenerated portable inline SVG markup. `scripts/check_homepage.py` passed; results and hashes in source-checks.json. Node `--check prototype/script.js` passed.
- Six editable SVG masters have paths/groups/clips, no image/text embedding, and resolving clip IDs. All six viewed against original AI raster renders. The horizontal filled underline rectangle now matches the original. Complete brandmark and exact last exterior contour compared visually.
- No missing relative HTML/CSS assets or anchors, duplicate IDs, button arrows, prototype/provisional draft wording in public text/meta/aria, forbidden customer words or em dashes.
- Zero native forms/submit buttons; fieldset disabled in source until handlers are installed. No fetch/XHR/beacon/WebSocket transport. The only localStorage key is decocoa-motion-paused, storing the boolean pause preference; inputs have no storage code. Static scripts perform no external reads.
- Reduced-motion media rule removes all decorative animation, header transitions and smooth scrolling; JS recognizes preference before adding motion-ready. Hidden scroll header starts inert in HTML. Dark pattern sections put interactive copy on solid cream panels with visible currentColor focus outlines; orange footer and controls retain brown outlines.

## Remaining production limitations

This remains a local homepage only. Message delivery, commerce, interior/legal pages and actual visit booking are not connected. Supplied trust marks and wireframe photos require production approval/rights confirmation; their caveats are in documentation rather than public page copy per the revised instruction. Draft factual copy uses supplied Vigneri/Sicilian heritage and source craft labels without additional claims. Original source files remain untouched.

Browser released: motion resumed, temporary viewport override reset, coding-agent tab closed.
