# Certification order and OU-D revision

November 1, 2026. User-requested order: Cacao-Trace, Rainforest Alliance, SQF, HACCP, OU Kosher Dairy. The dairy symbol is OU-D, as described by the [official OU symbol guide](https://oukosher.org/blog/industrial-kosher/all-ou-symbols-explained/). Replace the visible plain OU artwork with authentic OU-D; retain all original files, other four marks, copy and existing responsive behavior.

Source and runtime provenance are recorded in `assets/trust-export-details.json`. This is the user's local draft presentation choice, not independent certification verification. No public deployment is included.

The OU-D source is page 10 (printed page 8) of the official [Behind the Union Symbol, Fall 2017](https://oukosher.org/content/uploads/2017/12/BTU.fall2017-1.pdf). The complete circled U and adjacent D were rendered together from the publication, preserving the original artwork and using a transparent PNG canvas. No letter was added or reconstructed. The source page and 650 by 450 candidate PNG were both viewed before integration. Original PDF and extraction details are retained with the trust assets.

The original five runtime files were hashed before integration in `original-assets.json`; the four retained marks and retired plain OU asset all remain byte-identical after integration. No CSS, JavaScript or section copy changed. The new OU-D class uses the existing responsive cell width and contain sizing without the old plain-OU width cap.

Hidden-browser checks at 1920, 1440, 768, 390 and 320 CSS pixels confirm the exact requested order, all five images loaded, no horizontal overflow, no image filters and object-fit contain. Desktop keeps five columns; phone layouts wrap into two columns with OU-D centered on the last row. Viewed [desktop](desktop.png) and [phone](phone.png) screenshots confirm complete artwork on the Cream surface. Computed evidence is in [browser-checks.json](browser-checks.json).

Build/static/deterministic checks pass for 18 pages. The local Pages export passes with 76 runtime resources, 118 files, 1,691 references and 144 HTTP cases. Git whitespace checks pass. The normal local preview on port 4174 was restarted to include the OU-D file in its runtime asset allowlist. No public deployment was performed.
