# Content and component checks — November 11, 2026

The following checks passed against the generated 19-page local build. These results cover source fidelity, markup, runtime logic and build determinism. Browser layout and interaction evidence is recorded separately.

| Command | Result |
|---|---|
| `python scripts/check_content_components.py` | 643 checks, no errors. Independently reads the archived client brief, compares exact supplied lines at their mapped destinations with whitespace normalization only, checks 11 categories and ordering, all shared heroes/main links, retained detailed content, family/chocolate histories, legacy capability anchors and actual external-logo image wrappers. |
| `python scripts/check_site.py` | 19 routes, 2,838 local references, 57 protected original/source files; no errors. One H1/main/footer per page, matching shared navigation, valid IDs/resources/fragments, no nested links, unchanged non-transmitting inquiry behavior, shared-partial propagation and deterministic rebuild all passed. Sentinel rebuilds are isolated temporary outputs; the checked public files are not rewritten by the test. |
| `node scripts/check_navigation.js` | Desktop hover, keyboard focus/Escape, outside click, mobile inert closing, reduced motion, legacy B2B topic and capability destination logic passed. |
| `node scripts/check_category_motion.js` | All 11 cards tested at five responsive view widths, with stable wrapping, focus reveal, six motion pause gates and automatic manual-pause expiry. |
| `node scripts/check_chocolate_history.js` | Four/ten independent once-only entrances, duplicate initialization, reduced-motion changes and fail-open behavior passed. |
| `node --check prototype/script.js` and the category/history runtime scripts | JavaScript syntax passed. |

Machine-readable details are in `exact-copy-checks.json` in this directory and `prototype/qa-site-build/static-checks.json` and `category-motion-checks.json`. The navigation and history harnesses report their passing assertions to the console.

The existing GitHub Actions Pages workflow now includes the independent content checker and navigation/category runtime harnesses before export and upload. Its existing main-branch trigger, Pages configuration and deployment destination remain unchanged. Updating this workflow does not publish the local revision.

The specific remaining content dependency is the HACCP logo destination: the existing badge identifies no issuing organization. Eight other official organization/program destinations were verified and linked; HACCP remains visible and unlinked. See `handoff/logo-links-2026-11-11.md` for the evidence and missing information.
