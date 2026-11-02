# Chocolate history sample verification

Historical single-sample evidence. See [four-chapter verification](four-chapter-verification.md) for the current extension and preview status.

Date: October 31, 2026. One local sample chapter only. Implementation checks by the coding owner and coordinator; no independent review invocation. No push, deployment, or WordPress changes.

## Delivered

The existing `/experience-center/#museum-virtual-exhibition` section contains a chronological ordered-list chapter, researched HTML caption and source link, three independent transparent PNG groups with smaller variants, a working link to `/craft-your-own/#chocolate-bars`, and optional once-only artwork entrances. The existing Museum paragraphs and How It's Made / Tours and Classes content remain. Experience section navigation is horizontal so the timeline can use the full content width. The other seventeen generated HTML pages remain byte-identical to the starting version.

Editable records: `prototype/chocolate-history.json`; reusable item: `prototype/chocolate-history-chapter.template.html`; integration: `scripts/build_homepage.py` and `prototype/site.template.html`; Experience-only runtime: `assets/css/chocolate-history.css` and `assets/js/chocolate-history.js`. Placement and animation use separate wrappers. Per-layer x/y/width/rotation/z/delay and scene ratios have breakpoint overrides. The current sample uses the same relative composition at each width, with the text and track rearranged by CSS.

## Checks completed

- Existing generator, deterministic rebuild, shared component propagation and site checks pass: eighteen pages, 1,342 local references and 57 protected original inputs checked, no errors.
- Root preview HTTP checks pass. Export checks pass for root and `/DeCocoa/`; final export has eighteen content pages, 42 runtime resources, 84 artifact files and 1,603 references. The project-path preview passed 110 HTTP cases. Source/handoff/original artwork files are excluded from the publication artifact.
- Export testing exposed an existing root-path preview redirect from `/` back to `/`. `scripts/preview_pages.py` now applies that redirect only for a non-root base path; the corresponding export check was updated. This affects the preview helper, not the website's content or public deployment.
- `node scripts/check_chocolate_history.js` passes once-only reveal, duplicate initialization, reduced-motion initialization/change, unsupported observer and thrown-observer fail-open cases. The module removes observation after reveal; CSS default artwork is visible.
- Hidden in-app browser checks at 320, 390, 700, 768, 1024, 1050, 1440 and 1920 CSS px found no document horizontal overflow, all three images loaded, and separate text/art regions. Desktop uses the centered track, tablet a left track, and phone a stacked sequence. Ordinary caption text is 20px at desktop and 16px below 1200px. [Measurements](browser-width-checks.json).
- Viewed desktop, tablet and phone screenshots. Text is not baked into artwork; no artwork overlaps the caption or CTA. The three art layers reach opacity 1 and their final position after entrance, and remain visible during later scrolling.
- The primary local preview had no captured browser warning/error logs. Keyboard Tab from the source link reaches the CTA with the site's visible underline cue. At 320px the focused CTA is inside the viewport and its long label wraps within its double border. Enter reaches the existing Chocolate Bars section and focuses its heading.
- A QA-only server fixture sends CSP `script-src 'none'` for the Experience page. With scripts blocked, the caption remains readable, all three images load at opacity 1 with no animation, and the CTA remains a native link. [Measurements](browser-no-script-checks.json), [phone screenshot](chapter-no-script-390.jpg).
- A separate QA-only response injects `html { font-size:200% !important }`. At 1440, 390 and 320px the root is 32px; caption text becomes 40px desktop / 32px phone. The page has no horizontal overflow, chapter height grows with the copy, and artwork stays separate. The phone CTA expands to accommodate its label. This is a root-text enlargement fixture, not a browser zoom test. [Measurements](browser-large-text-checks.json), [phone screenshot](chapter-large-text-320.jpg).
- All six PNGs have true RGBA alpha. The three primary artworks were visually inspected on Cream, Dark Brown and checkerboard backgrounds: no obvious embedded background, checkerboard or edge halo at intended sizes. The main canvas was retained because nonzero alpha reaches its bounds; no visible major silhouette clipping was observed. [Alpha QA](alpha-qa.png), [asset manifest](../../assets/chocolate-history-assets.json).
- `git -c core.whitespace=cr-at-eol diff --check` passes; existing Windows CRLF conventions are retained.

## Evidence and limits

[Desktop sample](sample-desktop.jpg), [tablet sample](chapter-tablet-768.jpg), [phone CTA](chapter-phone-320.jpg). The approved hidden browser workflow was used throughout; the user's visible browser was not used for testing. Loopback preview required an approved sandbox escalation so that the browser could reach the server.

The reduced-motion branches were tested in the JavaScript fixture and the CSS rule was inspected; an actual OS/browser reduced-motion preference toggle was not exercised. Safari/WebKit, screen readers and Elementor are not tested. These checks do not establish whole-site accessibility conformance. The historical opening caption is supported by the sources in the handoff; the generated bowl is interpretive and is not a verified archaeological replica. Artwork/style approval from Guy is still pending. The other chapters are intentionally not built.

The QA-only server script and evidence remain under this review directory, outside the published resource allowlist. Preview processes are stopped at handoff; restart the ordinary site with `./Start-Preview.ps1`, then visit `/experience-center/#museum-virtual-exhibition`.
