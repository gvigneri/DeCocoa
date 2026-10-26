# DeCocoa homepage handoff

Updated October 11, 2026. Version: **homepage-r6**. This revision adds separate pretzel entrances and rounded component treatments. Guy now supplies design reviews; the design-review agent is stopped. Nothing has been published. The portable HTML/CSS/JavaScript site is not an Elementor import template.

## Preview and files

- Open `http://127.0.0.1:4173/prototype/` while the retained server is running, or use `Start-Preview.ps1` from the project/extracted package.
- `handoff/DeCocoa-preview.zip` contains the current editable site, referenced assets, local fonts/license, SVG library, screenshots and handoff documents.
- `handoff/DeCocoa-patterns-svg.zip` contains all six source-faithful vector masters and usage notes.
- `handoff/DeCocoa-preview-r3.zip`, `DeCocoa-preview-r4.zip` and `DeCocoa-preview-r5.zip` preserve preceding versions in the full workspace.
- Edit `prototype/homepage.template.html`, then run `python scripts/build_homepage.py`. The delivered index is already generated.
- `handoff/elementor-map.md` maps the components to later native assembly. `handoff/open-items.md` records production decisions.

## Current revision

- Three distinct image elements have independent eased drops and short staggered delays. Their finite entrances settle into a static composition; pause and reduced-motion states remain available.
- Two separate transparent cutouts were created with built-in Imagegen from the supplied pretzel composition. The tool reconstructed originally occluded edges; these are not pixel-identical source exports. The third beaded pretzel remains a direct source export. Exact prompts and paths: `handoff/pretzel-cutout-provenance.json`.
- Buttons retain 1rem type and 8px/4px corner radii. Both borders are now 2px. Primary/secondary hover feedback remains animated without text underlining; Let's Talk remains secondary.
- Orange eyebrow labels now have 8px rounded corners and retain the 12px heading gap.
- Content and photo cards use 16px outer corners, a 4px visible inset border and a 4px transparent outer ring showing the surrounding section. The original icon-mask silhouette remains intact.
- Previous typography, navigation, full-height Chocolate patterned hero, 1500px container, source badge footer, editable patterns and source wordmark underline remain.

## Verification and review status

Homepage-r5 was accepted in independent session 5. That acceptance applies to the archived r5 implementation only. All five sessions are consumed. Guy explicitly asked to stop the design-review agent and will provide reviews from r6 onward. No independent review or acceptance is claimed for this revision.

Current implementation evidence is recorded in `prototype/implementation-checks-r6.md`, with structured source checks in `prototype/source-checks.json`. Targeted checks at 1920, 1440, 768, 390 and 320px showed no horizontal page overflow. Computed button inner borders are 2px; eyebrows have an 8px radius; cards have 16px corners, transparent 4px outer borders and visible 4px inset rings. Three animation durations are 1.55/1.65/1.7 seconds with delays of 0/0.2/0.4 seconds, settling after 2.1 seconds overall. A saved pause reload shows every pretzel statically; mid-entry pause holds all three positions and resumes without restarting. Reduced-motion handling remains source-checked rather than OS-emulated.

Full browser evidence for unchanged navigation, contact and brand-master behavior remains in earlier reports. Do not treat those older reports as fresh tests of changed r6 behavior.

All 42 supplied originals remain unchanged against the initial source inventory. The existing six pattern SVG masters and identity assets remain source-faithful. Package CRC checks run during archive creation.

## Screenshots

Current r6 viewport captures are in `handoff/screenshots/`. Prior screenshots are retained in versioned subfolders in the full workspace. Screenshot pixel dimensions may exclude browser viewport edges/scrollbars; see the implementation report for actual requested widths and saved dimensions.

## Production limits

No WordPress implementation, message delivery, booking, commerce or public deployment is included. Contact fields validate locally without sending or storing input. Only the motion preference is persisted. The page does not claim a message was sent.

Native touch hardware, a screen reader, OS-level reduced-motion switching and a formal cross-browser/accessibility audit have not been performed. Source-checked fallbacks must not be described as runtime emulation. New edited product cutouts, supplied wireframe photography, partner/certification marks and historical copy still require final production content approval. The watermarked machinery image remains excluded. Those notes belong in this handoff, not the customer-facing page.
