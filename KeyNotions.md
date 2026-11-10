# Key Notions

- Essay
  - Rationale: Identifies a Federalist essay by its McLean number and connects it to authorship records, publication appearances, revisions, and topics.
  - Connected Pattern: Identifier (MODL)
  - Source Dataset(s): McLean edition (1788), Benson list, Kent list, Port Folio list (1807), Gideon edition (1818), Mosteller and Wallace (1964)

- Agent
  - Rationale: Represents a person or organization that wrote, compiled, or printed a source.
  - Connected Pattern: Agent (Enslaved ontology)
  - Source Dataset(s): Kent list, McLean edition (1788), Williams & Whiting edition (1810), Gideon edition (1818)

- Person
  - Rationale: Represents historical individuals independently of their roles as credited authors, claimants, source writers, endorsers, senders, or recipients.
  - Connected Pattern: Agent and agent roles (Enslaved ontology)
  - Source Dataset(s): Benson list, Kent list, Port Folio list (1807), Gideon edition (1818), Madison to Randolph (December 2, 1787), Mosteller and Wallace (1964)

- Organization
  - Rationale: Represents firms or groups that printed or published sources, including J. and A. McLean and Williams & Whiting.
  - Connected Pattern: Agent (Enslaved ontology)
  - Source Dataset(s): McLean edition (1788), Hopkins edition (1802), Williams & Whiting edition (1810)

- Record
  - Rationale: Represents a source-backed assertion about an essay, preserving its source, endorsements, and any dates specific to the assertion. Conflicting assertions remain separate records.
  - Connected Pattern: AgentRecord and Provenance, adapted for essay assertions (Enslaved ontology)
  - Source Dataset(s): Benson list, Kent list, Gideon edition (1818), Dawson edition (1864), J. C. Hamilton edition (1865)

- AuthorshipRecord
  - Rationale: Records a source's attribution to one or more persons, distinguishing credited persons from the claimant and the source's writer. A vague claim may identify no particular essay.
  - Connected Pattern: Record and agent roles, adapted for authorship attribution (Enslaved ontology)
  - Source Dataset(s): Benson list, Kent list, Port Folio list (1807), Gideon edition (1818), Madison to Randolph (December 2, 1787), Mosteller and Wallace (1964)

- JointRecord
  - Rationale: Identifies an authorship record crediting at least two distinct persons, allowing joint attributions to be distinguished from separate conflicting claims.
  - Connected Pattern: Record with a minimum-cardinality restriction, adapted for joint attribution (Enslaved ontology record-based approach)
  - Source Dataset(s): Benson list, including its joint attributions for essays 18–20

- RevisionRecord
  - Rationale: Records a source's assertion that an essay was revised in an edition, including who made or approved the changes. Conflicting accounts of revisions remain separate.
  - Connected Pattern: Record and Provenance, adapted for revision assertions (Enslaved ontology)
  - Source Dataset(s): McLean edition (1788), Hopkins edition (1802), Gideon edition (1818), Dawson edition (1864), J. C. Hamilton edition (1865)

- Source
  - Rationale: Represents the document supporting a record, with its writer, document type, creation and publication dates, survival status, location, and derivation from other sources.
  - Connected Pattern: Provenance (Enslaved ontology, adapted from PROV-O)
  - Source Dataset(s): Benson list, Kent list, Port Folio list (1807), Hamilton's annotated copy, Madison's annotated copy, Gideon edition (1818), Mosteller and Wallace (1964)

- AuthorshipList
  - Rationale: Represents handwritten or printed lists assigning essays to authors, including annotations in personal copies of the collection.
  - Connected Pattern: Source typing, adapted from original source types (Enslaved ontology Provenance module)
  - Source Dataset(s): Benson list, Kent list, Port Folio list (1807), Hamilton's annotated copy, Madison's annotated copy

- Letter
  - Rationale: Represents correspondence used as evidence for authorship claims, with a sender, recipient, and date, including claims that name no specific essay.
  - Connected Pattern: Provenance and agent roles, adapted for correspondence (Enslaved ontology)
  - Source Dataset(s): Madison to Randolph (December 2, 1787)

- Study
  - Rationale: Represents scholarly or statistical analyses whose authorship conclusions can be compared with historical attributions using the same record structure.
  - Connected Pattern: Source typing and Provenance (Enslaved ontology)
  - Source Dataset(s): Mosteller and Wallace (1964)

- Edition
  - Rationale: Represents a book printing of the essays that is both a publication containing essay appearances and a potential source of authorship or revision records.
  - Connected Pattern: Provenance (Enslaved ontology), Collection (MODL)
  - Source Dataset(s): McLean edition (1788), Hopkins edition (1802), Williams & Whiting edition (1810), Gideon edition (1818), Dawson edition (1864), J. C. Hamilton edition (1865)

- Publication
  - Rationale: Represents a newspaper or book edition in which essays appeared, enabling comparison of newspaper and book publication histories.
  - Connected Pattern: Collection (MODL)
  - Source Dataset(s): Original newspaper printings, McLean edition (1788), Hopkins edition (1802), Williams & Whiting edition (1810), Gideon edition (1818)

- Newspaper
  - Rationale: Represents a newspaper publication containing essay appearances, distinguished from a book edition and from its publishing organization.
  - Connected Pattern: Collection and Name Stub (MODL)
  - Source Dataset(s): Original Federalist newspaper printings, including The Daily Advertiser

- Appearance
  - Rationale: Represents a printing in a publication on a date under a printed number. One appearance may cover more than one McLean essay, supporting split essays and numbering changes.
  - Connected Pattern: N-ary relationship reification, adapted for publication appearances (Enslaved ontology relationship-record approach)
  - Source Dataset(s): Original Federalist newspaper printings, McLean edition (1788), Hopkins edition (1802), Williams & Whiting edition (1810), Gideon edition (1818)

- SourceStatus
  - Rationale: Provides controlled terms Lost and Surviving to describe whether a source remains available for inspection.
  - Connected Pattern: Controlled vocabulary (Enslaved ontology)
  - Source Dataset(s): Benson list, Hamilton's annotated copy, Kent list, Madison's annotated copy

- Topic
  - Rationale: Provides controlled subject terms, such as Judiciary and Executive, to retrieve essays by subject and connect them to source-backed authorship attributions.
  - Connected Pattern: Controlled vocabulary (Enslaved ontology)
  - Source Dataset(s): Federalist essay texts in the McLean edition (1788)
