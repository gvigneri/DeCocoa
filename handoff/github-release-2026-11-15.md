# DeCocoa GitHub revision, November 15, 2026

Guy requested pushing all current site changes to the existing `gvigneri/DeCocoa` repository. The target is `main` and the existing GitHub Actions Pages deployment. This release includes the November 11 content/component baseline and all November 15 follow-ups recorded in `presentation-revision-2026-11-15.md`.

Included changes:

- Shared Orange heroes without eyebrows, a dedicated Experience Center Coming Soon notice, 24px desktop body text, updated homepage colors, buttons and shadows, and borderless rounded media.
- Five full-width image menus ordered Our Chocolate, Our People, Our Craft, Our Segments and Experience Center; revised hover and keyboard states with no persistent current-page styling.
- Snacking, Gifting and Entertaining collection pages with eight chocolate formats each; informational homepage format cards; a segment hub and four dedicated segment pages.
- Requested People, Craft, Partner Brands, Craft Your Own and Experience Center copy and section changes, including the factory GIF, Sustainability logos and simplified CTAs.
- Removal of Wholesale, on-page jump menus, breadcrumbs and redundant links; semantic heading improvements and preserved mobile/motion behavior.
- Shared content, navigation and rendering sources, retained original media/provenance, and review screenshots. The Pages workflow now runs the content, navigation and category-motion checks alongside its existing checks.

Pre-push verification passed: 23 generated pages; 2,409 local references; 57 protected artwork inputs; deterministic rebuild and shared partial propagation; 617 retained-copy checks; syntax checks for all three runtime scripts; navigation, category and chocolate-history motion checks. The refreshed Pages export contains 84 runtime resources, 136 files and 25 compatibility redirects. Export validation passes 2,764 references and 167 loopback HTTP cases under `/DeCocoa/`, including nested recovery and legacy URLs.

The exported website contains only public generated pages, runtime resources, bundled licenses and compatibility redirects. Source artwork, templates, review evidence and handoff records remain repository-only. The local preview remains available on port 4174.

The dedicated Décor and Fulfillment PDF buttons remain disabled until the files are supplied. Book Your Appointment opens the existing Experience Center inquiry; no booking backend was added. Inquiry forms remain non-transmitting. Policy/accessibility drafts, WordPress transfer and other recorded production gaps are unchanged.

Hosted build and deployment results are available in the repository's [Pages workflow history](https://github.com/gvigneri/DeCocoa/actions/workflows/pages.yml).
