# DeCocoa local draft site

This continues the established DeCocoa design as a portable, responsive informational site. Guy approved the local draft build in [the consolidated plan](handoff/site-build-plan.md) and authorized temporary GitHub Pages hosting on October 25, 2026. WordPress transfer remains a later phase. Inquiry fields do not send or save messages.

The complete ten-chapter chocolate-history timeline is in `/experience-center/#museum-virtual-exhibition`, following Guy's reference image through A Sweeter Tomorrow. The approved first four chapters are preserved. [Artwork, sources and editing notes](handoff/chocolate-history-complete.md).

November 1 GitHub revision: Guy requested pushing the latest homepage, People, Craft and Experience Center changes to this repository and its existing Pages workflow. The update includes the chocolate bark hero, Orange homepage sections, shared page introductions, Cream product cards, Key Segments cards and updated partner/certification logos. [Release scope and verification](handoff/github-release-2026-11-01.md).

November 1 refinements: semantic date/region/title headings with equal spacing, centered museum introduction, shared Ripe text links with Brown subnavigation, compact timeline arrows, borderless main sections, and a combined Tours and Classes ending. How It's Made now has one Explore Our Craft primary button. [Latest revision checks](reviews/chocolate-history-2026-11-01/order-arrow-action-verification.md).

## GitHub Pages

The public homepage is [gvigneri.github.io/DeCocoa/](https://gvigneri.github.io/DeCocoa/). The workflow in `.github/workflows/pages.yml` builds and checks the site, exports the generated pages and runtime assets into `_site/`, validates their URLs under `/DeCocoa/`, then deploys that artifact. The repository's Pages publishing source must be **GitHub Actions**. Pushes to `main` deploy automatically; the workflow can also be run manually.

The published artifact has `index.html`, `styles.css`, `script.js`, `assets/` and the page directories at its root. `prototype/` remains the editable/generated source folder in this repository. Compatibility pages redirect the old `/DeCocoa/prototype/index.html` and related legacy URLs to the new public routes. Original artwork, templates and review/handoff records are not included in the website artifact.

To check the same artifact locally after rebuilding:

```powershell
python scripts/check_site.py
python scripts/export_pages.py --base-path /DeCocoa/
python scripts/check_pages_export.py --base-path /DeCocoa/
python scripts/preview_pages.py --port 4180 --base-path /DeCocoa/
```

Open `http://127.0.0.1:4180/DeCocoa/`. This separate preview reproduces the GitHub Pages project path and nested 404 handling; it does not replace the normal local preview below.

## Preview

From this folder in PowerShell:

```powershell
.\Start-Preview.ps1
```

Open http://127.0.0.1:4173/ . Press Ctrl+C in the serving terminal to stop. To use a different port, run `./Start-Preview.ps1 -Port 4174`. The helper uses Codex's bundled Python when present, or an installed Python otherwise. The current review session uses http://127.0.0.1:4174/ .

The public site starts at `/`, with standard paths such as `/products/`, `/gifting/`, `/our-people/` and `/lets-talk/`. `prototype/` remains an internal source/output folder; it is not part of the site's public slugs. Older `/prototype/…` preview URLs redirect to their clean equivalents. The retired `/work-with-us/` route redirects to Let's Talk; its former service fragments forward to their new destinations.

The delivered pages are already generated. All fonts and website assets are local, and preview needs no package installation.

## Edit and rebuild

Use Python 3 to regenerate the complete site:

```powershell
python scripts/build_homepage.py
```

The existing generator name is retained for continuity; it now generates the entire approved local site using Python's standard library.

| Editable source | Responsibility |
| --- | --- |
| `prototype/site-content.json` | One navigation source, product examples, inquiry topics and supporting-page draft content |
| `prototype/partials/header.html` | One master header, including original and scroll variants |
| `prototype/partials/footer.html` | One master footer |
| `prototype/partials/inquiry.html` | Shared inquiry interface used once on Home and once on Let's Talk |
| `prototype/site.template.html` | Shared document structure and asset includes |
| `prototype/homepage.template.html` | Homepage sections and established visual composition |
| `prototype/trust-section.template.html` | Shared Partners/Certifications section; content and individual logo paths come from `site-content.json` |
| `prototype/product-detail.template.html` | Reusable product detail layout |
| `prototype/styles.css`, `prototype/script.js` | Shared responsive styling and behavior |
| `assets/js/category-motion.js` | Full-width single-copy category row, keyboard access and interaction/motion gates |
| `prototype/chocolate-history.json`, `prototype/chocolate-history-chapter.template.html` | Experience timeline copy, source links, scene/layer controls and reusable chapter markup |
| `assets/css/chocolate-history.css`, `assets/js/chocolate-history.js` | Experience-only responsive timeline styling and optional once-only artwork entrances |
| `assets/chocolate-history-assets.json` | Generated PNG provenance, dimensions, transparency bounds, responsive variants and review status |
| `prototype/chocolate-history-artwork.json`, `scripts/prepare_chocolate_history_assets.py` | Incremental artwork preparation, preserved source archives and alpha QA sheets |
| `scripts/build_homepage.py` | Relative URLs, shared-part assembly and decorative SVG instances |
| `scripts/prepare_trust_assets.py` | Reproducible PNG preparation from preserved external logo sources; provenance in `assets/trust-export-details.json` |
| `scripts/prepare_factory_media.py` | Preserve the supplied factory GIF and export a lossless first-frame reduced-motion fallback; provenance in `assets/factory-media-details.json` |

Edit sources, then rebuild. Generated `index.html` files and `prototype/404.html` are outputs; edits made directly to those files are overwritten by the generator. Faithful `assets/patterns/*-master.svg` files and original artwork remain separate from generated website SVG instances.

## Pages and behavior

The revised scope is eighteen pages: Home; Products with five presentation categories; three descriptive product examples; Gifting; Craft Your Own; Fundraising; Wholesale; B2B; Our People; Our Craft; Experience Center; Let's Talk; three pending draft destinations for Privacy Policy, Terms and Conditions and Accessibility; and a not-found recovery page. Home's centered, stacked `#talk` section and the dedicated Let's Talk `#inquiry` section reuse the same inquiry component and validation, once per document. Chocolate Bars and Baskets remain sections of Craft Your Own. Local links carry only public product/topic context. No catalog specifications, prices, checkout, accounts, booking or delivery backend are added.

The four main navigation groups share one model in both headers. Our Chocolate links to the product and service pages. Our People, Our Craft and Experience Center open submenus that jump to sections on their respective pages. Legacy section anchors are retained where they previously existed.

Existing copy and artwork are authorized local draft inputs. Final product names, offering facts, history, partner/certification status, photography and legal content still need approval. The October 25 footer links use `/privacy-policy/`, `/terms-and-conditions/` and `/accessibility/`; those three local pages explicitly state that their content is being prepared. They contain no invented policy terms or conformance claims. Other factual gaps remain in the handoff.

Navigation supports keyboard and touch-sized controls. The full-width category row shows four cards across on desktop, two on tablet and one on phones. Guy's latest revision removes visible motion and previous/next controls. Motion retains reduced-motion, offscreen and hidden-page handling; the category row also stops during hover or keyboard focus. No manual motion preference is stored. Inquiry fields validate locally; a valid attempt reports that message delivery is not connected. Fields remain disabled if their script does not initialize.

## Records and artwork

The Git repository includes the site sources, generated pages, runtime assets, extracted original artwork and handoff/review records. Duplicate ZIP packages, local preview logs and Python caches remain local and are ignored. The original intake archive is retained in the working folder; its extracted originals are versioned under `brand/source/`. Git preserves file bytes to keep artwork provenance checks stable across clones.

- [Completion and verification](handoff/review-summary.md): delivered local scope, checks and limitations.
- [Implementation evidence](reviews/site-build-2026-10-24/implementation-verification.md): the 50 route/width checks, browser interactions and static-check commands.
- [Current site-build plan](handoff/site-build-plan.md): approved tasks, route inventory, findings, content gaps and verification.
- [Elementor transfer map](handoff/elementor-map.md): native assembly responsibilities for the later WordPress phase.
- [Production open items](handoff/open-items.md): content, target environment and delivery decisions.
- [Review ledger](reviews/ledger.md): the four October 24 baseline reviews, separate from the five historical prototype sessions.
- `brand/brand-rules.md`, `brand/brand-exceptions.md`, `brand/asset-manifest.md`: brand decisions and provenance.
- `assets/`: web artwork, imagery, six editable pattern masters and licensed local Montserrat fonts.
- `brand/source/`: preserved supplied originals. The original ZIP remains unchanged in the full workspace.
- `handoff/pretzel-cutout-provenance.json`: provenance for two Imagegen-assisted reconstructed pretzel cutouts.
- `DeCocoa-Site-Build-Master-Brief.md`: current supplied brief; the older `DeCocoa-Codex-Master-Brief.md` is historical where superseded.

Earlier `DeCocoa-preview*.zip` packages and r3–r6 reports describe historical homepage builds. They are not evidence of the current site's completion or an Elementor import package.

The preview helper serves only public pages and runtime assets through `scripts/preview_server.py`. Unknown routes return the shared recovery page with HTTP 404. The layout is also available at `/404.html`. WordPress will need its own equivalent routing when transferred.

