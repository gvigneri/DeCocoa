# Shared review baseline

ID: **DC-LOCAL-R6-2026-10-24**. Recorded October 24, 2026, 08:18 EDT (12:18 UTC), before implementation changes. Guy then confirmed local-first work in this existing project; WordPress integration is deferred.

URL: http://127.0.0.1:4174/prototype/

## Source and ownership

- Workspace: `C:/Users/guyta/Documents/Codex/Decocoa`.
- Existing version: homepage-r6; authoritative HTML authoring file `prototype/homepage.template.html`; generated browser output `prototype/index.html`; shared styles `prototype/styles.css`; behavior `prototype/script.js`; generator `scripts/build_homepage.py`.
- No Git repository is present. `local-source-manifest.json` hashes 146 files across prototype, assets, scripts, and brand/source. No implementation files were edited to establish this baseline.
- No unsaved WordPress/editor changes can be assessed. No WordPress source, configuration, database dump, template IDs, or deployment process was located here.
- The connected WordPress tool identifies Bonfire Consulting, the historical reference, in production. It is excluded from this review; see `connection-evidence.json`. No changes were made there.
- Header, scroll header, footer, and contact controls currently live in the same homepage template. Reusable CSS/JS already use external files. There is no existing local multipage build or synchronized master partial mechanism.

## Common reviewer inputs

Read the current root `AGENTS.md`, `DeCocoa-Site-Build-Master-Brief.md`, this baseline, and `handoff/site-build-plan.md`. Guy's local-first follow-up overrides the brief's immediate WordPress requirement. Do not report WordPress deferral as a discovered defect.

Use `brand/brand-rules.md`, `brand/brand-exceptions.md`, `brand/asset-manifest.md`, `handoff/copy-notes.md`, and `handoff/open-items.md` to distinguish approved treatments from unapproved factual content. Local source package contains 2 PDFs, 16 logo AIs, 6 pattern AIs, and 18 product PNGs. Six editable SVG pattern masters and local Montserrat 300/400/700 exports already exist. Fonts include OFL/provenance records; Susa is unavailable and optional. Two hero pretzel cutouts include disclosed AI reconstruction.

During review Guy clarified: "Just use what we have so far as drafts and we will work on what is missing after". This changes the disposition of content findings: existing material can support the local draft; verification gaps remain for later content completion/publication. It does not change the frozen source or authorize inventing missing facts. Findings gathered before this clarification should be reconciled by the coordinator accordingly.

Original manual and nine-page wireframe: `brand/source/Decocoa Get Started/`. Extracted text and existing source renders: `references/`. Historical screenshots and review outcomes are supporting history only, not fresh visual verification.

## Frozen review contract

Reviewers are read-only. Do not edit files, templates, code, styles, content, or settings. Return findings to the coordinator in messages using IDs MSG-xx, DES-xx, UX-xx, A11Y-xx and the fields in brief section 7. Distinguish confirmed findings from proposed improvements and not-tested checks. Include what works and should be preserved. Source references should include file/line or exact selector/copy; browser evidence should include dimensions, interaction, and outcome.

The coordinator alone writes the consolidated backlog. Browser viewport overrides affect the shared browser, so only the reviewer holding the browser turn may interact or resize. Messaging and Design may inspect supplied fresh screenshots plus frozen source while UI/UX operates its own tab. Accessibility gets the next serialized browser turn. Do not claim to have manually exercised an interaction from source alone.

The earlier 5/5 cap is preserved historically; the October 24 brief explicitly authorizes this new four-discipline cycle. No implementation starts before the consolidated review checkpoint.
