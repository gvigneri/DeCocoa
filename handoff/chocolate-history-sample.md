# Chocolate history: first chapter

Historical sample record. Guy subsequently approved extending to four reference-based chapters; see [current handoff](chocolate-history-four-chapters.md). The original artwork remains, while the opening caption now follows Ancient Origins from the supplied image.

Date: October 31, 2026.

Guy requested one sample first, after choosing a vertical visual exhibition and allowing overlapping chapters to be consolidated after factual review. This milestone is one local chapter, not the complete timeline. It belongs in the existing Experience Center Museum & Virtual Exhibition section at `/experience-center/#museum-virtual-exhibition`. WordPress remains deferred. This sample has not been published.

## Editorial direction and evidence

The sample opens with **Around 3300 BCE**, **Upper Amazon · Present-day Ecuador**, and **Chocolate begins with cacao**. The caption is brief and uses archaeological evidence without claiming an exact origin date for all cacao use or reconstructing a particular recipe.

The source panorama's opening date is not repeated. Zarrillo et al. report cacao starch, theobromine residues, and ancient DNA from Santa Ana-La Florida in southeast Ecuador dating to approximately 5,300 years ago. The sample links to the original research. This is an interpretive visual introduction, not a depiction of an identified historic event.

- [Original study, Nature Ecology & Evolution (2018)](https://www.nature.com/articles/s41559-018-0697-x)
- [Research team's university report, UBC (October 29, 2018)](https://news.ubc.ca/2018/10/sweet-discovery-new-ubc-study-pushes-back-the-origins-of-chocolate/)
- [Nature research highlight explicitly giving around 3300 BC](https://www.nature.com/articles/d41586-018-07226-y)

The supplied reference is `C:/Users/guyta/Downloads/ChatGPT Image Oct 31, 2026, 11_59_25 AM.jpg`; it provided atmosphere and narrative direction only. Its text, cultural scenes, brand packaging, and typography were not copied into the sample. The supplied implementation brief is `C:/Users/guyta/Downloads/DeCocoa-Vertical-Chocolate-Timeline-Brief.md`. The user's later one-chapter scope takes precedence over the brief's full-timeline instruction.

## Original artwork

Three independent logical groups were generated with the built-in image-generation tool, each explicitly requesting true alpha transparency. The original outputs remain unchanged in the generated-images directory. Optimized production PNGs and mobile variants live in `assets/images/chocolate-history/01-origins/`.

- Cacao pods and leaves: meaningful botanical illustration; one intact pod and one open pod with pale pulp.
- Earthenware bowl: decorative, generic interpretive vessel. It is not a verified archaeological replica and has no invented cultural markings.
- Cacao beans: decorative cluster.

[Exact generation prompts](chocolate-history-generation-prompts.json) and [asset dimensions, alpha bounds, hashes, variant sizes and roles](../assets/chocolate-history-assets.json) record the provenance. Resizing and conservative alpha-padding crops preserve the originals and do not alter their depicted content. Main artwork retains its entire generated canvas because low-alpha pixels reach its boundaries.

## Editing

Edit `prototype/chocolate-history.json` for the heading, caption, era label, source link, CTA, and per-layer placement. The template and dedicated stylesheet keep layout and animation separate. Existing site navigation and page content remain available. Run the existing `python scripts/build_homepage.py` command to regenerate the pages.

The next milestone, after Guy reviews the sample, is to settle its art treatment and spacing, then fact-check and consolidate the remaining proposed chapters. No remaining chapter artwork has been produced or represented as delivered.

Verification is recorded separately in `reviews/chocolate-history-2026-10-31/verification.md` once the sample checks are complete.
