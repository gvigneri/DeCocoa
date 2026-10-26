# Independent design review 02

Date: October 11, 2026. Reviewer: GPT-6 Astra, High. Frozen version: `homepage-r2`, identified by `reviews/homepage-r2-files.json`. All listed hashes matched at review start. Session 2 of maximum 5. Implementation was not edited.

## Verdict

**The complete homepage is visually coherent and responsive. Make the form fail closed before handoff, then correct two minor issues.** All three session-01 findings are resolved in the tested states. No new confirmed brand violation, clipped customer text, or horizontal page scrolling was found. The strongest parts are the product presentation, the cream-to-chocolate Craft transition, and the clear mobile stacking. The full content sequence and footer satisfy the intended homepage scope.

## Prior findings

| ID | Current status | Verification |
| --- | --- | --- |
| DC-001 | Resolved | Desktop Gifting destination opened by keyboard; Escape returns to Gifting with submenu visible. Clicking Return to homepage closes the submenu through outside-click handling and returns focus to the visible Our Chocolate trigger. Both are predictable. Products is now an in-page anchor. |
| DC-002 | Resolved | At 390px, Tab from the last navigation link cycles to Menu; Shift+Tab from Menu cycles to Let's Talk. Focus stays visible. Nested Escape closes submenu then main menu and returns focus correctly; body overflow is restored. Mobile dialog Escape returns to Gifting. |
| DC-003 | Resolved | Hero caption is hidden at tablet/mobile and the bottom discovery link is readable at 11px. Desktop caption is 11px. The redundant mobile strip label is removed. |

## New findings

### DC-004 — Major — Interaction / content — Form can submit when JavaScript is unavailable

**Status: Open. Source-confirmed fallback defect; not reproduced by disabling JavaScript.** `prototype/index.html:93` defines a real form without action or method, with named fields. Line 97 renders an enabled `type="submit"` button. Only the listener installed at `prototype/script.js:112` prevents native submission. If the script fails to load or is disabled, the native form defaults to a GET request to the current document, placing entered values in the URL and sending them to the local server. This contradicts the visible promise that nothing is sent or saved and the explicit no-transmission brief. Browser DOM inspection confirmed absent action/method and enabled submit. The coordinator raised this fallback concern; this reviewer verified the actual frozen markup and listener independently.

Requested correction: make the original HTML inert for submission, and enable a local preview action only after its handler is installed. A non-submit button bound to validation avoids implicit submission; disabling the entire form until initialization is another option. Include a useful no-JavaScript explanation. Verify both button activation and Enter in fields cannot submit natively when the script is unavailable. Do not add a backend.

### DC-005 — Minor — Interaction — Primary contact topic is not selectable

**Status: Open.** The selector at `prototype/index.html:95` contains `Chocolate & products</option>` without its opening `<option>`. The actual select options are Choose a topic, Gifting, Experience Center, Wholesale / B2B, Fundraising, and Something else. Chocolate & products appears as stray text in the accessibility snapshot, not as an option, and cannot be selected.

Requested correction: restore the opening option tag and verify all intended topics through the rendered selector. This is a functional defect, not a copy preference.

### DC-006 — Minor — Design / responsive — Wide-desktop Craft crop removes the subject's eyes

**Status: Open. Design judgment.** At 1920 x 1080, `craft-photo img` uses a wide 460px-high cover crop that cuts the photograph across the upper face. `homepage-r2/1920-craft.jpg` shows only the lower face and mouth, whereas the inspected `assets/images/chocolate-craft.webp` includes the eyes. The 1440px, tablet, and mobile views preserve more of the face.

Requested correction: use a top-biased object position for the wide-desktop crop, or a proportional image height/aspect ratio that preserves both the face and tray. No image retouching is needed. Keep the provisional photography provenance.

## Visual and brand assessment

- Reviewed every homepage section and footer through native browser scrolling and existing links. The source capability labels are appropriately grouped under Craft rather than represented as product categories. Products, people, process, partner/certification references, visitor invitation, contact, and legal/footer destinations are present. No interior pages, commerce, booking, live contacts, or social destinations are invented.
- Customer copy is short and restrained. The experience CTA sets Experience Center in the contact selector and makes no availability claim. The form status explicitly says no message was sent or saved. Partner/certification status is visibly provisional, and the asset manifest records extracted photography as provisional. No prohibited words or em dashes were found in the customer copy reviewed.
- Manual pp. 17 and 19: palette and local Montserrat 300/400/700 remain consistent with the approved system. Chocolate #512316 is used for website tokens; the original logo #582011 remains preserved. Body weight is 400; no unauthorized serif or synthetic weight is introduced. Source font licensing/provenance is unchanged from session 01.
- Manual pp. 23-24: header and footer horizontal logos retain source shape, proportions, and colors, with no rotation, masking, component separation, or pattern underlay. Footer is solid orange. At 768px the footer logo measured 190 x 49.344px with 25px padding, satisfying the approximately half-mark-height Y construction; desktop and mobile screenshots show the same reserved-space approach. No neighboring content enters the logo's clear space.
- Viewed each actual partner/certification export at native resolution. Marks retain full source forms and backgrounds; Wegmans' white block is preserved. They occur once each, are not recolored, and are labeled reference assets. Their small taglines are necessarily reduced on mobile; final approved original files and applicable minimum-size guidance remain production prerequisites, not prototype verification claims.
- Patterns retain source colors and aspect ratio, use cropped panels rather than an unvalidated repeat tile, and remain clear of both DeCocoa logos. Source artwork and raster photos were not replaced by invented branded art.
- All text pairings in this page use chocolate on cream/orange/sunrise or cream on chocolate. Chocolate/orange is 4.503448:1; cream/chocolate is approximately 11.51:1; chocolate/sunrise approximately 7.94:1. The Craft control's keyboard outline is cream and visibly readable on chocolate.

## Coverage and evidence

Browser: own CUA Chrome tab `158815685`, local preview only. Viewport overrides tested: 1920 x 1080, 1440 x 1000, 768 x 1024, 390 x 844, 320 x 760. Observed innerWidth matched each request. Document scrollWidth values were respectively 1905, 1425, 753, 375, 305 because of the vertical scrollbar, with no horizontal overflow.

At 1920px, inspected the entire page using sequential viewport captures. At 390px, likewise inspected the whole stacked page. At 768px, inspected the product grid, People, Craft, trust, Experience, contact and footer; the saved hero was also viewed. At 320px, inspected saved hero plus products, Experience, contact/feedback and footer, and measured every section's bounds. At 1440px, inspected saved hero and live Craft/navigation states. This is broad responsive coverage, not a claim that every control was exercised at every width.

Saved screenshots under `reviews/homepage-r2/` include `1920-products.jpg`, `1920-people.jpg`, `1920-craft.jpg`, `1920-experience.jpg`, `1440-craft.jpg`, `768-products.jpg`, `768-trust-experience.jpg`, `768-footer.jpg`, `390-people-craft.jpg`, `390-trust.jpg`, `390-form-footer.jpg`, `320-experience.jpg`, and `320-footer.jpg`. These were viewed during this review. Some capture names describe the main content rather than the entire visible viewport.

Evidence caveat: the supplied `1920-hero.png` is actually 1440 x 1000, identical in dimensions to `1440-hero.png`. The reviewer separately set and verified a real 1920px viewport and viewed its hero live; regenerate the mislabeled deliverable before handoff. Supplied mobile PNGs are viewport captures (375 x 812 and 305 x 724), not full-page screenshots. The attempted `1920-form-valid.jpg` capture preceded the settled result paint and should not be used as success-state evidence; `390-form-footer.jpg` visibly contains the settled honest result.

Assets: all 15 image elements reported complete with nonzero natural widths after page traversal. Loaded image set: horizontal logo (header/footer), Stripes (hero/Experience), filled chocolate (hero/product), chocolate bar, drizzle confection, People and Craft photos, three partner marks, and two certification groups. Font CSS and computed family match local Montserrat; individual browser font-load status was not independently exposed by the tool, as recorded in session 01.

Interactions exercised:

- Desktop click/Enter/ArrowDown navigation and Escape; ArrowDown focuses Products. Desktop Gifting dialog keyboard and pointer close return states. Products and People anchors; People heading receives focus from main navigation.
- Mobile Menu opening, bidirectional focus containment, nested submenu, destination dialog and nested Escape; scrolling restores on close.
- Craft Learn With Us dialog and return to a visible cream focus outline; footer Privacy Policy dialog/Escape returns to its trigger.
- Hero discovery link, footer section links and back-to-top, Experience Visit Us contact anchor/topic preselection.
- Form empty submission: three associated errors and first-invalid Name focus. Filled name/message plus malformed email: only email error and Email focus. Valid `review@example.com` with synthetic test text: honest local-only status receives focus; URL stays at `#talk`. Inputs remained local in the reviewed JavaScript path; source contains no fetch, storage, or submission integration.

Limits: no native touch hardware or screen reader used. No automated network interception or JavaScript-disabled browser state was available in the documented tool surface; DC-004 is based on native HTML behavior and frozen source, not a claimed browser reproduction. No OS-level reduced-motion emulation; source remains static without automatic animation and contains the reduced-motion override for smooth scrolling. Full-page screenshot capture was deliberately avoided because of the known tool timeout; viewport captures and scrolling provided actual rendered evidence. Viewport override was reset and the review tab closed afterward.

## Next action

Correct DC-004 and DC-005, make the small DC-006 crop adjustment, and regenerate accurate handoff screenshots. Keep the overall design and source brand treatments. No additional independent invocation was started by this reviewer.
