# Homepage People copy and brand spelling

November 1, 2026. Guy requested DeCocoa capitalization throughout authored site text and supplied a replacement homepage People introduction.

The five active occurrences were updated: hero copy, Craft introduction, DeCocoa DeCOR reference, factory alternative text and Partners introduction. Current working copy/brand records were also normalized; original artwork and archived references remain intact.

The People introduction is exactly the two supplied paragraphs. Its heading, image, mask, CTA and CSS are unchanged. The dedicated Our People page and the other sixteen non-homepage outputs are unchanged byte-for-byte.

Build/static/deterministic checks pass. All 18 generated and all 18 exported pages contain zero instances of the prior mixed-uppercase spelling. The `/DeCocoa/` artifact is refreshed; no deployment or push occurred. [Source/export checks](../../prototype/qa-site-build/people-copy-2026-11-01-checks.json).

Hidden-browser checks at 1920, 1440, 768, 390 and 320px confirm exactly two matching paragraphs, a loaded photograph, unchanged Meet Our People destination, no copy/image-column overlap and no horizontal document overflow. [Measurements](browser-checks.json). Viewed [desktop](people-desktop-1440.jpg) and [phone](people-phone-320.jpg) screenshots. The longer copy fits using the existing responsive layout without a CSS adjustment.

Temporary viewport sizing is reset and the hidden QA tab is closed for handoff. The normal preview remains available at port 4174.
