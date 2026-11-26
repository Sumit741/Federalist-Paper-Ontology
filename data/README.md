# Federalist Ontology: data files

These CSVs use separate entity and relationship tables, with three design choices:

- `appearance_essays.csv` replaces the `essay_id` column in `appearances.csv`. This lets one printing hold two essays (newspaper No. 31 became McLean 32 and 33).
- Record IDs carry a prefix, `AR_` (authorship) or `RR_` (revision), so they are unique across both record files.
- A year-only date goes in `earliest_date` / `latest_date` as YYYY-01-01 to YYYY-12-31.

`record_type` holds a manual tag: `JointRecord` when a record has two or more credit rows, `AuthorshipRecord` otherwise.

## Sources used

| Data | Source |
|---|---|
| First printing of each essay (newspaper, date) | Center for the Study of the American Constitution, UW–Madison, "The Federalist Papers" list (archive.csac.history.wisc.edu/678.htm) |
| Newspaper vs. McLean numbering, McLean volume dates, all authorship lists, Hopkins dispute, other editions | Editors' introductory note, *Papers of Alexander Hamilton* vol. 4 (Founders Online, Hamilton/01-04-02-0151-0001). The same note is the source `SyrettCooke1962`. |
| Newspaper reprint dates of 78–85 | Wikipedia "The Federalist Papers" essay table; LSU Federalist table (marks them as *Independent Journal*) |

## Judgment calls to review

1. **Scope of appearances.** Each essay has its first newspaper printing, its McLean printing, and, for 78–85, its *Independent Journal* reprints. Same-week reprints in other papers (Packet, Daily Advertiser, New-York Journal) are not included, because no source gave their dates. `NewYorkJournal` is listed as a publication with no appearances.
1a. **Reprints of 78–85** are attributed to the *Independent Journal* (LSU table; all dates fall on its Wednesday/Saturday schedule). The *Packet* also reprinted them, but its dates are unknown. Multi-part reprints get one appearance per issue, following the definition "one printing in one publication on one date".
1b. **Essay 7** is dated 1787-11-17 (Wisconsin list), not Nov 15 (Gutenberg). Nov 17 was a Saturday, the Journal's day.
2. **Printed numbers.** Newspaper numbers are worked out from the mapping in the Hamilton note (29→35, 30→29, 31→30, 32+33→31, 34→32, 35→33, 36→34, 37–77 → n−1). The reprints of 78–85 are left blank because their printed numbers are unknown; only the Journal's last is known (No. 84).
3. **One record per source per essay**, including the "all the rest by Hamilton" essays. That is why there are about 85 records per list.
4. **Benson list vs. Port Folio vs. Hamilton's copy.** Benson's records are in `BensonList`, the note Coleman reported in 1817. Hamilton's lost copy is known only through the Port Folio notice of 1807, so its records are in `PortFolioList`, which is `based_on` `HamiltonCopy`. `HamiltonCopy` has no records of its own.
5. **Kent list.** Records use Part I *as corrected* (54→64 for Jay, 37–48→37–49 for Madison) and are endorsed by Hamilton, after Part III, dated 1800–1804. The claimant is blank because the informant is unnamed. Part II gets two extra records (`AR_KentPartII_48/49`, claimant Hamilton). They use the corrected numbers; before the corrections they read 68 and 69. The note says the corrections only *resemble* Hamilton's numerals, so treat this reading with care.
6. **Washington's copy** credits essay 1 to Jay and gives 18–20 jointly to Jay, Hamilton and Madison, which makes a three-person JointRecord. Its "37–48 exclusive of last" is entered as 37–47. The Hamilton note calls this source "highly suspect".
7. **Madison's copy vs. the Gideon edition.** Madison's records are in `GideonEdition` (claimant and endorser Madison), which is `based_on` `MadisonCopy`. This follows the R2 test record.
8. **Mosteller & Wallace** has records only for the 12 disputed essays (49–58, 62, 63), all crediting Madison.
9. **Revision records** have no `essay_id`. The sources don't say which essays were changed, only that the edition's text was revised. Splitting them by essay would mean making up data.
10. **Unknown writers** (Port Folio contributor, "Corrector", Washington Gazette, Washington's copy) have no `source_writers` row. Letter writers come from `letter_senders` through `hasSender SubPropertyOf hasWriter`.
11. **Topics** are one per essay, based on the essays' titles. Your group can add more rows.
12. **Printed sources with only a known year** (most editions, the two studies, the 1847 letter) have that year in `earliest_date`/`latest_date`. For a printed source, this window stands for the publication year.
13. **Dates bounded by Hamilton's death.** The Benson list, Hamilton's copy and the Kent list have `latest_date` 1804-07-12 (Hamilton died July 12, 1804) instead of 1804-12-31. Hamilton wrote or reviewed each of them, so none can be later.
14. **Blank status.** `HopkinsLetter1847` has no `source_status`. The Hamilton note only reports J.C. Hamilton quoting it, so whether the original survives is unknown. Under the open-world assumption this still satisfies `hasSourceStatus exactly 1`: the letter has a status, but it isn't recorded.
15. **Edition dates:** These use year windows, except McLean (1788-03-22, volume 1) and Hopkins (1802-12-08, offered for sale). The J.C. Hamilton edition is dated 1865, following the Hamilton note.

## Still needed in the conversion script

- Declare the persons as different individuals, and `Lost` and `Surviving` too.
- Create the `Topic` and `SourceStatus` individuals.
- Map each Edition ID to a single RDF entity that is both a Publication and a Source.
