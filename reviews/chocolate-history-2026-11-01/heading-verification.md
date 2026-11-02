# Experience Center heading semantics

November 1, 2026. Scoped correction of Guy's reported possible-heading warning on `/experience-center/`. Local implementation checks, not an independent review or a whole-site accessibility certification.

## Change

Each chapter's date, title and region now form one native h3, with three styled spans in the approved order. The existing heading ID remains on that h3, so article labels and fragment destinations still resolve. This gives heading navigation the complete chapter label without introducing three separate headings for one chapter. The closing “What will your chocolate story look like?” invitation becomes an h3 beneath the museum h2. Text size, weight, spacing, content and artwork are unchanged.

Authoritative edits are in `prototype/chocolate-history-chapter.template.html`, `assets/css/chocolate-history.css` and `scripts/build_homepage.py`. The CSS cache version advances to 3; shared CSS and JavaScript are unchanged.

## Verification

- At 1440px before the correction, the user-supplied paragraph heuristic identified 21 candidates: ten dates, ten region labels and the closing invitation. [Before evidence](heading-warning-before.json).
- After correction, zero paragraphs match that rule at 1920, 1440, 768, 390 or 320px. All ten metadata wrappers are h3 elements containing spans, and their gaps remain 16px. No document horizontal overflow occurs. [After evidence](heading-warning-after.json).
- Exact before/after comparisons at 1440px and 320px found no differences in text, font size, weight, line height, letter spacing, color, element dimensions or document position for all thirty metadata parts and the invitation.
- The main outline remains one h1, three section h2 elements and eleven h3 elements beneath the museum section. All ten article `aria-labelledby` targets resolve to their original native h3 IDs. [Outline and labels](heading-outline.json).
- [Desktop screenshot](semantic-headings-desktop.jpg) was viewed to verify the approved appearance is preserved.
- The reported paragraph algorithm was reproduced against rendered DOM and computed styles; this was not a run of the user's browser extension.

Build/static/deterministic checks pass. Both existing export checks pass: 114 files and 1,683 references; 139 root-path HTTP cases and 140 `/DeCocoa/` cases, with no errors. Final local `_site` uses `/DeCocoa/`. No deployment or push is part of this correction; the normal local preview remains running at port 4174. The hidden QA tab is closed and the temporary viewport override is reset. A refreshed visible preview is open for Guy.
