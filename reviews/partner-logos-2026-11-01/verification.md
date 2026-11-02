# Partner logo revision

November 1, 2026. Guy requested replacing Guittard in Connections & collaboration / Our Partners with Chocolate.com and Blue Stripe. The cacao brand's official name is Blue Stripes, verified at [bluestripes.com](https://www.bluestripes.com/); the other source is [chocolate.com](https://chocolate.com/).

Keep Puratos and the supplied Wegmans artwork, yielding four visible marks. Preserve Guittard's files and all downloaded originals. Runtime artwork must be PNG with original colors and geometry; any exact vector conversion is recorded in `assets/trust-export-details.json`. Existing intro and other sections remain unchanged. Logo selection follows the user's request and is not independent verification of business relationships.

Selected source artwork:

- Chocolate.com: [official orange PNG](https://chocolate.com/cdn/shop/t/180/assets/core.sister-link-logo__chocolate.png?v=105910343310861000381777998946), 618 by 96, copied unchanged to `assets/images/partner-chocolate-com.png`.
- Blue Stripes: [current official header SVG](https://www.bluestripes.com/cdn/shop/files/Logo_1216x.svg?v=1752054481), rendered without recoloring, cropping or background removal to the 640 by 422 PNG `assets/images/partner-blue-stripes.png`. Its original white interior shapes remain, with transparent space outside the artwork.

Both selected PNGs were viewed before integration. Hidden-browser checks at 1920, 1440, 768, 390 and 320 CSS pixels confirm exactly four marks in order: Puratos, Wegmans, Chocolate.com and Blue Stripes. All images load; no Guittard remains in the rendered section; no image filter or cropping is applied; every mark uses object-fit contain and remains within the grid with no horizontal overflow. Four desktop columns become two below 1200px and one at 480px or below. Certification layout is unchanged.

Viewed screenshots: [desktop](desktop.png), [tablet](tablet.png), [phone top](phone-top.png), [phone bottom](phone-bottom.png). [Computed layout and asset evidence](browser-checks.json).

Build/static/deterministic checks pass, including source/runtime SHA provenance verification. Local Pages export passes with 18 pages, 76 runtime resources, 118 files, 1,689 references and 144 HTTP cases. The normal local preview was restarted so its asset allowlist includes both new PNGs. No public deployment is included.
