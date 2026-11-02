# Four-chapter implementation verification

Historical milestone. The first four chapters are preserved in the [complete ten-chapter verification](complete-timeline-verification.md).

October 31, 2026. Scope: extend the approved local sample to four chapters from Guy's reference image. Coding-owner implementation checks and coordinator browser checks only; no independent review invocation, push, deployment or WordPress changes.

## Delivered

The existing Experience Center Museum section contains Ancient Origins, The Aztec Empire, Chocolate Comes to Europe and A Taste Spreads, in that order. The first caption now follows the reference's Mesoamerican subject. The Aztec Empire date is corrected to 1428–1521 CE; editorial sources and adjustments are recorded in [the handoff](../../handoff/chocolate-history-four-chapters.md).

The first chapter's six production PNG files remain byte-identical. Six new usable images add twelve responsive production PNGs; the page uses twelve rendered layers from nine unique illustration groups. New originals are archived with hashes, and the initially clipped Aztec version is separately preserved as superseded. Main artwork has descriptive alternative text; supporting groups are decorative. Artwork is interpretive, not a verified historical reconstruction.

The existing reusable template, editable JSON and dedicated stylesheet supply four chapters. Text comes first in chronological DOM order. Desktop chapters alternate sides; tablet uses a left track with consistent copy/art columns; phones stack text before art. Existing Museum context, other Experience sections, navigation and the final Craft Your Own link remain. Other generated HTML pages are unchanged.

## Verification

- Build, deterministic rebuild, shared component propagation and static site checks pass: 18 pages, 1,369 local references and 57 protected original inputs checked, no errors.
- Root preview and both export configurations pass. Final `/DeCocoa/` export: 18 content pages, 54 runtime resources, 96 artifact files, 1,630 references and 122 loopback HTTP cases. The root export passed 121 HTTP cases. Originals, source manifests and handoff records are excluded from the website artifact.
- Four-scene JavaScript checks pass: each scene reveals independently once; already revealed scenes stay visible; duplicate initialization is safe; reduced-motion initialization/change, missing observer and thrown-observer branches fail open.
- Hidden in-app browser checks at 1920, 1440, 768, 390 and 320 CSS px found no horizontal document overflow or text/art-region overlap. All twelve images loaded after scrolling through the chapters. Desktop text is 20px, below 1200px it is 16px. All four meaningful artwork descriptions appear in the accessibility tree in chronological order. [Measurements](four-chapter-width-checks.json).
- The three new chapter compositions were visually inspected on desktop; the longest title and full ship composition fit the 320px phone. The court chapter was also inspected at 768px. Artwork remains separate from copy and neighboring chapter content. All four scenes settled at opacity 1 after their entrances.
- The QA-only 200% root-text fixture passes at 1440, 390 and 320px: 32px root, 40px desktop/32px phone captions, no horizontal overflow, and no copy/art overlap. Chapter height expands with the text. This is text enlargement, not native browser zoom. [Measurements](four-chapter-large-text-checks.json).
- The QA-only CSP fixture blocks all scripts. At 320px all twelve images load at opacity 1 with no animation; all four captions remain present. Keyboard Tab from the final source link reaches the existing Craft Your Own Chocolate Bar link. [Measurements](four-chapter-no-script-checks.json), [screenshot](four-chapters-no-script-320.jpg).
- Production preview console inspection returned no captured warning/error messages. The expected CSP errors belong only to the script-blocked fixture.
- New artwork was inspected on Cream, Dark Brown and checkerboard backgrounds. No obvious embedded background or major silhouette clipping was seen at intended sizes. [Aztec alpha QA](alpha-qa-chapter-02.png), [Europe/court alpha QA](alpha-qa-chapters-03-04.png).
- `git -c core.whitespace=cr-at-eol diff --check` passes. Windows line endings are retained.

## Evidence and preview

[Aztec desktop](four-chapters-aztec-desktop.jpg), [Europe desktop](four-chapters-europe-desktop.jpg), [court desktop](four-chapters-court-desktop.jpg), [court tablet](four-chapters-court-tablet-768.jpg), [Europe phone](four-chapters-europe-phone-320.jpg).

Testing used a hidden in-app browser. Its temporary viewport override was reset, the QA tab was closed and the QA-only server stopped. The ordinary preview remains running on port 4174 as Guy requested. A fresh visible preview tab was opened at `/experience-center/#museum-virtual-exhibition` because the older user-owned tab could not be controlled through the available browser API; the older tab was left untouched.

An actual OS reduced-motion setting, screen readers, Safari/WebKit and Elementor were not exercised. These implementation checks do not establish whole-site accessibility conformance. Guy's review of the new chapter artwork remains the next editorial/design checkpoint; the scope stops at four.
