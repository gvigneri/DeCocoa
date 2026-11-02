# Chocolate history: four chapters

Historical milestone. Guy subsequently requested the remaining six chapters; see [the complete timeline handoff](chocolate-history-complete.md). The four chapters documented here are preserved.

October 31, 2026. Guy accepted the first sample, then requested three more chapters, four total, using the exact items from his supplied image with small SEO adjustments. This supersedes the initial single-chapter limit and its Amazon-focused caption. The vertical exhibition remains within `/experience-center/#museum-virtual-exhibition`. No publication, WordPress work or additional chapters are included.

## Content decisions

| Reference item | Local chapter | Editorial adjustment |
| --- | --- | --- |
| 1500 BCE–900 CE / Ancient Origins | Ancient Origins / Mesoamerica | Retain the period and subject; focus on Olmec and Maya within this period rather than placing the later Aztec Empire here. Retain the approved cacao, bowl and bean artwork. |
| 900–1500 / The Aztec Empire | 1428–1521 CE / The Aztec Empire | Correct the empire's dates. Preserve the reference themes of sacred cacao, rituals, warriors, special occasions and currency. |
| 1500s / Chocolate Comes to Europe | 1500s / Chocolate Comes to Europe | Preserve the Spanish arrival and luxury-drink subject; use gradual adoption language rather than immediate widespread popularity. |
| 1600s–1700s / A Taste Spreads | 1600s–1700s / A Taste Spreads | Preserve chocolate houses, courts and expanding trade. Add a short description of serving vessels and recipes that supports the visual story. |

The four reference titles and their order are retained. Copy remains editable HTML and descriptive natural language, with no keyword stuffing or search-performance claims. The image is a user-provided editorial reference, not a reliable authority for chronology. These historical periods are chapter ranges, not claims that cacao use began in 1500 BCE or that all customs ended at the chapter boundary.

Sources consulted:

- [Natural History Museum of Utah: Chocolate, its origins](https://nhmu.utah.edu/articles/chocolate-its-origins) supports Mesoamerican cultivation and ceremonial use. Earlier Amazonian evidence remains documented in the historical sample handoff.
- [The Metropolitan Museum of Art: Golden Kingdoms exhibition galleries](https://www.metmuseum.org/exhibitions/listings/2018/golden-kingdoms/exhibition-galleries) dates the Aztec Triple Alliance to 1428–1521.
- [Smithsonian National Museum of American History: cacao currency](https://www.si.edu/object/nmah_835166) supports the cacao-as-currency theme.
- [Alimentarium: Chocolate in Europe](https://www.alimentarium.org/en/fact-sheet/chocolate-europe) supports the European arrival, changing recipes and elite consumption.
- [Historic Royal Palaces: Chocolate fit for a king](https://www.hrp.org.uk/hampton-court-palace/history-and-stories/chocolate-fit-for-a-king/) supports court chocolate culture and chocolate houses.
- [Kate Loveman, The Introduction of Chocolate into England (2013)](https://doi.org/10.1093/jsh/sht050) provides further context for seventeenth-century adoption.

## Artwork and implementation

The original first-chapter production assets remain unchanged. Six new usable images were generated with the built-in image generation tool: an Aztec cacao drinker, a sailing ship, a court chocolate drinker, a cacao sack, a chocolate-pot/cup group, and a spice group. The Aztec figure's initially clipped feather tips were corrected in a separate image-generation edit; both originals are preserved. All new illustrations are interpretive, not verified reconstructions of a named person, vessel, artifact or event.

Three logical layers compose each scene. Existing bowl/beans are reused where appropriate. Each logical group has its own transparent PNG, responsive variants and independent placement. Desktop chapters alternate sides; narrower layouts preserve chronological text-first order. The existing shared theme, navigation, remaining Experience sections and other pages are preserved.

Edit `prototype/chocolate-history.json` for text and responsive placements. `prototype/chocolate-history-artwork.json` is the preparation manifest. `scripts/prepare_chocolate_history_assets.py` supports incremental preparation with `--chapters` and distinct QA output through `--qa-sheet`; it preserves existing production records and detects changed input under an existing filename. Asset dimensions, hashes, source paths and review status are in `assets/chocolate-history-assets.json`. Original new artwork is archived under `brand/source/chocolate-history-2026-10-31/`, excluded from the website export.

Exact new generation/edit prompts are in `chocolate-history-four-chapter-prompts.json`; original sample prompts remain in `chocolate-history-generation-prompts.json`. Rebuild using the existing `scripts/build_homepage.py`. Restart an already-running local preview after adding referenced asset paths so its resource allowlist updates.

Implementation evidence is recorded in `reviews/chocolate-history-2026-10-31/four-chapter-verification.md`. These are implementation checks; no independent review invocation is added to the historical ledger.
