# Conference Publications

I created this repository to maintain verified citations and public supporting material for my conference work. Two papers have been accepted for an October 2026 conference at Carnegie Mellon University. I will add the exact titles, author order, venue name, abstracts, DOI/proceedings links, and approved files only after I verify them against the official acceptance and publication records.

## Work completed

- Contributed to two accepted conference papers.
- Organized a release process for citation metadata and public materials.
- Separated verified information from placeholders so incomplete records cannot be presented as final citations.
- Added checks for author lists, dates, venue information, and material-sharing clearance.
- Prepared a structure for future abstracts, posters, slides, and supplementary code when co-author and publisher rules permit release.

## Repository code

- `scripts/validate_metadata.py` checks each publication record for required fields and unresolved placeholders.
- `scripts/build_citations.py` converts verified YAML records into a Markdown publication list.
- `publications/paper-01.yaml` and `paper-02.yaml` hold controlled metadata records.
- `docs/RELEASE_CHECKLIST.md` records the verification and rights checks required before publication.

## Run the metadata checks

```bash
python -m pip install -r requirements.txt
python scripts/validate_metadata.py
python scripts/build_citations.py --output PUBLICATIONS.md
```

The generator intentionally refuses to publish records that still contain unverified placeholder values.

## Release policy

I will not upload accepted manuscripts, figures, reviewer correspondence, private datasets, or co-author material until the applicable conference, publisher, sponsor, institutional, and co-author permissions are confirmed.

## Author and Research Setting

**Hritika Adhikary**  
Collaborative Biomedical Engineering Research  
Two conference papers accepted for presentation at Carnegie Mellon University  
October 2026

## Rights

Copyright (c) 2026 Hritika Adhikary. All rights reserved. See [LICENSE](LICENSE).
