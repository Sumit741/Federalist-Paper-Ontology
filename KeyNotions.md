# The Federalist: Key Notions

One pattern runs through every module: something happens once (an **Event**), and each source adds its own **Role Record** saying who did what. When sources disagree, the event gets two records. We keep both.

Pattern names are from MODL. "Record" is from the Enslaved ontology (not in MODL).

## Shared

- **Agent**
  - **Rationale:** Anyone who writes, prints, sends, receives or makes a claim. What an agent does is kept in role records, not in the agent.
  - **Connected Pattern:** AgentRole, Name Stub, Identifier
  - **Source Dataset(s):** Gutenberg #1404, Avalon Project, LoC 1788 McLean edition, Hamilton Works v1, Founders Online

- **Person**
  - **Rationale:** A real person: Hamilton, Madison, Jay, Washington, Jefferson. One person can be an author in one event and a sender in another.
  - **Connected Pattern:** AgentRole, Name Stub
  - **Source Dataset(s):** all

- **Organization**
  - **Rationale:** A group that acts: a newspaper, Project Gutenberg, the Avalon Project, the Library of Congress.
  - **Connected Pattern:** AgentRole, Name Stub
  - **Source Dataset(s):** Gutenberg #1404, Avalon Project, LoC 1788 McLean edition

- **Document**
  - **Rationale:** Any written thing: an essay, a letter, a book, a handwritten list. Every document can be a source.
  - **Connected Pattern:** Provenance, Identifier
  - **Source Dataset(s):** all

- **Event**
  - **Rationale:** Something that happened once: a Writing, Publication, Sending or Shipment. It has one date and its places. The kind of event is a type value.
  - **Connected Pattern:** Event, Explicit Typing
  - **Source Dataset(s):** all

- **Role Record**
  - **Rationale:** One source saying that one agent had one role in one event, for example "Avalon says Madison is an author of No. 49". It keeps the source, the date and the label exactly as the source wrote it.
  - **Connected Pattern:** ParticipantRole, Provenance, Record (Enslaved)
  - **Source Dataset(s):** all

- **Source**
  - **Rationale:** The original document a record comes from, who made it, and when. Example: Jefferson's handwritten list.
  - **Connected Pattern:** Provenance
  - **Source Dataset(s):** LoC 1788 McLean edition, Gutenberg #1404, Avalon Project, Hamilton Works v1, Founders Online

- **Copy Activity**
  - **Rationale:** Modern work that copies a source: Gutenberg and Avalon typing up the text, the Library of Congress scanning the book. Whoever did the copying only passes the claim on; they did not make it.
  - **Connected Pattern:** Provenance
  - **Source Dataset(s):** Gutenberg #1404, Avalon Project, LoC 1788 McLean edition

- **Temporal Extent**
  - **Rationale:** A date or a time span. Example span: the Printing Period, 27 Oct 1787 to 28 May 1788.
  - **Connected Pattern:** Temporal Extent
  - **Source Dataset(s):** all

## Module 1: Essays and Authorship

- **Essay**
  - **Rationale:** One of the 85 numbered papers. Part of the Collection. Signed "Publius".
  - **Connected Pattern:** Identifier, Partonymy/Meronymy
  - **Source Dataset(s):** Gutenberg #1404, Avalon Project, LoC 1788 McLean edition

- **Collection**
  - **Rationale:** All 85 essays as one work. Instance: The Federalist.
  - **Connected Pattern:** Aggregation, Bag, Collection
  - **Source Dataset(s):** Gutenberg #1404, Avalon Project, LoC 1788 McLean edition

- **Edition**
  - **Rationale:** One printing or text of the Collection: the 1788 McLean book, the Gutenberg text, the Avalon text. Editions disagree, so each one is a separate source.
  - **Connected Pattern:** Aggregation, Bag, Collection
  - **Source Dataset(s):** Gutenberg #1404, Avalon Project, LoC 1788 McLean edition

- **Volume**
  - **Rationale:** A physical part of an edition. The 1788 edition has two. Jefferson's list is written inside his copy of Vol. 1.
  - **Connected Pattern:** Partonymy/Meronymy
  - **Source Dataset(s):** LoC 1788 McLean edition, Hamilton Works v1

- **Pen Name**
  - **Rationale:** The name the essays were signed with. Value: "Publius". A name, not a person.
  - **Connected Pattern:** Name Stub
  - **Source Dataset(s):** Gutenberg #1404, Avalon Project

- **Writing**
  - **Rationale:** The one event of an essay being written. Who wrote it is in the Author role records.
  - **Connected Pattern:** Event
  - **Source Dataset(s):** Gutenberg #1404, Avalon Project, LoC 1788 McLean edition

- **Author Role Record**
  - **Rationale:** One source saying an agent wrote an essay. This is the authorship claim. A qualifier says how the source said it: Stated, Possibly or Assisting.
  - **Connected Pattern:** ParticipantRole, Provenance
  - **Source Dataset(s):** Gutenberg #1404, Avalon Project, LoC 1788 McLean edition (Jefferson's list)

- **Attribution Qualifier**
  - **Rationale:** How sure a source is about an author. Stated = "MADISON". Possibly = "HAMILTON OR MADISON". Assisting = the helper in "MADISON, with HAMILTON".
  - **Connected Pattern:** Explicit Typing
  - **Source Dataset(s):** Avalon Project, Gutenberg #1404

- **Publication**
  - **Rationale:** The one event of an essay first appearing in a newspaper.
  - **Connected Pattern:** Event
  - **Source Dataset(s):** Gutenberg #1404, Avalon Project

- **Publisher Role Record**
  - **Rationale:** One source saying which newspaper printed an essay, and on what date. Gutenberg and Avalon differ for about 20 essays.
  - **Connected Pattern:** ParticipantRole, Provenance, Temporal Extent
  - **Source Dataset(s):** Gutenberg #1404, Avalon Project

- **Newspaper**
  - **Rationale:** The paper an essay ran in: Independent Journal, New-York Packet, Daily Advertiser. Treated as the publishing organization.
  - **Connected Pattern:** Name Stub
  - **Source Dataset(s):** Gutenberg #1404, Avalon Project

- **Authorship List**
  - **Rationale:** A handwritten list of who wrote each essay. Example: Jefferson's list in his 1788 copy. A Source of type Manuscript List.
  - **Connected Pattern:** Provenance, Explicit Typing
  - **Source Dataset(s):** LoC 1788 McLean edition

- **Attestation Note**
  - **Rationale:** A note saying who wrote another document. On 13 Jan 1829, R. Harrison and Joseph Nourse wrote that the list is in Jefferson's hand. It is a Source for "Jefferson wrote the list".
  - **Connected Pattern:** Provenance
  - **Source Dataset(s):** LoC 1788 McLean edition

- **Computed Result**
  - **Rationale:** An answer we work out instead of reading it from a source: disputed essays, counts, earliest letter. It keeps which records it used.
  - **Connected Pattern:** Provenance
  - **Source Dataset(s):** worked out from the records above

- **Computation**
  - **Rationale:** One run that makes a Computed Result: the records it used, the query, who ran it, when.
  - **Connected Pattern:** Provenance, Event
  - **Source Dataset(s):** worked out from the records above

## Module 2: Letter Network

- **Letter**
  - **Rationale:** A letter about the Federalist. It can reply to another letter. It is also the source for what we record about it.
  - **Connected Pattern:** Identifier, Provenance
  - **Source Dataset(s):** Hamilton Works v1, Founders Online, Teaching American History

- **Sending**
  - **Rationale:** The one event of a letter going from one place to another.
  - **Connected Pattern:** Event, Spatial Extent
  - **Source Dataset(s):** Hamilton Works v1, Founders Online

- **Sender / Recipient Role Record**
  - **Rationale:** An agent as sender (with the sent date) or recipient (with the received date) of a letter.
  - **Connected Pattern:** ParticipantRole, Temporal Extent
  - **Source Dataset(s):** Hamilton Works v1, Founders Online

- **Place**
  - **Rationale:** Where a letter was written and where it went. Often "not recorded".
  - **Connected Pattern:** Spatial Extent
  - **Source Dataset(s):** Hamilton Works v1, Founders Online

## Module 3: What the Letters Say

- **Reference**
  - **Rationale:** Something a letter says about the Federalist, an essay, a volume or a person, with the quoted passage. Its kind is a type value.
  - **Connected Pattern:** Provenance, Explicit Typing
  - **Source Dataset(s):** Hamilton Works v1, Founders Online

- **Shipment**
  - **Rationale:** Copies of a volume sent from one person to another, sometimes through a middleman.
  - **Connected Pattern:** Event
  - **Source Dataset(s):** Hamilton Works v1, Founders Online

- **Shipment Role Record**
  - **Rationale:** An agent as shipper, receiver or middleman in a shipment.
  - **Connected Pattern:** ParticipantRole
  - **Source Dataset(s):** Hamilton Works v1, Founders Online

- **Quantity**
  - **Rationale:** How many copies were shipped, for example "forty copies". A number on the Shipment.
  - **Connected Pattern:** Quantities and Units
  - **Source Dataset(s):** Hamilton Works v1, Founders Online

## Subclasses

- Agent ← Person, Organization ← Newspaper
- Document ← Essay, Collection, Edition, Volume, Letter
- Record (anything with a source) ← Role Record, Reference, Computed Result, Document
- Event ← Computation
- Author, Sender, Recipient are **not** subclasses of Person. They are role types.

## Types (fixed lists)

- Event: Writing, Publication, Sending, Shipment
- Role: Author, Publisher, Sender, Recipient, Shipper, Receiver, Intermediary
- Qualifier: Stated, Possibly, Assisting
- Document: Newspaper Issue, Printed Edition, Manuscript List, Note, Letter
- Reference: Mentions Federalist, Mentions Publius, Mentions Person, Names Authors, Refers To Essay, Opinion, Printing Problem

## Instances and values

- The Federalist: one Collection
- Publius: a Pen Name value
- Printing Period: one Temporal Extent (27 Oct 1787 to 28 May 1788)
- Number of copies: a number on a Shipment

## Key relations

- Writing produces Essay. Publication prints Essay. Sending carries Letter. Shipment ships Volume.
- Event has Role Records. A Role Record has an agent, a role type, a qualifier, a date, the label as written, and is based on a Source.
- Essay is part of Collection. Edition is an edition of Collection. Volume is part of Edition. The list and the note are part of Volume.
- Source is made by an agent (who made the claim), has a date and a document type, and is available from LoC, Gutenberg or Avalon.
- Edition text is made by a Copy Activity, done by an Organization.
- Letter replies to Letter. Sending is from a Place and to a Place.
- Reference is based on a Letter, is about something, and has the passage text.
- Computed Result is made by a Computation. Computation used records, has a method (query), was done by someone, on a date.

## Rules

- One record per source, per agent, per role.
- Joint = one source, two Stated authors. Unsure = one source, two Possibly authors. Helped = one Stated author, one Assisting author.
- Disputed = sources name different authors for one essay, or a source says Possibly. Only Writing events count, so reprints are not disputes.
- Unknown date or place: we answer "not recorded".
- Records point to the original document. LoC, Gutenberg and Avalon only tell us where we got it.

## Key Notions per CQ

| CQ | Key notions |
|----|-------------|
| 1 | Person, Writing, Author Role Record, Essay, Source |
| 2 | Essay, Publication, Publisher Role Record, Newspaper, Temporal Extent, Edition |
| 3 | Essay, Writing, Author Role Record, Attribution Qualifier, Source, Computed Result |
| 4 | Essay, Writing, Author Role Record, Attribution Qualifier, Source, Computed Result |
| 5 | Author Role Record, Source, Authorship List, Agent, Temporal Extent |
| 7 | Essay, Author Role Record, Person, Source, Computed Result |
| 8 | Source, Author Role Record, Person, Essay, Computed Result |
| 11 | Letter, Reference, Collection, Pen Name, Sending, Sender / Recipient Role Record, Person |
| 12 | Person, Sender / Recipient Role Record, Sending, Letter, Temporal Extent |
| 13 | Letter, Temporal Extent |
| 14 | Sending, Letter, Place |
| 15 | Sending, Temporal Extent, Computed Result |
| 16 | Letter, Reference, Person |
| 17 | Letter, Source, Copy Activity |
| 19 | Shipment, Shipment Role Record, Volume, Quantity, Person, Temporal Extent, Letter |
| 20 | Letter, Reference, Essay |
| 21 | Person, Sender / Recipient Role Record, Letter, Reference, Temporal Extent, Computed Result |
| 22 | Author Role Record, Letter, Sending, Sender / Recipient Role Record, Person |
| 23 | Letter, Reference, Collection |
| 24 | Letter, Reference, Volume |
| 25 | Authorship List, Attestation Note, Author Role Record, Person, Temporal Extent |
| 26 | Essay, Publisher Role Record, Edition, Computed Result |
| 27 | Computed Result, Computation, Author Role Record |
| 28 | Author Role Record, Source, Edition, Copy Activity, Organization |
| 29 | Person, Role Record, Computed Result |
| 30 | Essay, Author Role Record, Attribution Qualifier, Source |

CQs 6, 9, 10, 18 were merged into 1, 5, 12, 22.

## New CQs (proposed)

25. Who says an authorship list was written by a given person, and when did they say it?
26. Which essays do the sources disagree on for newspaper or date, and what does each source say? (computed)
27. For the list of disputed essays, which source records was it built from, and when was it computed?
28. Through which modern copy (Gutenberg, Avalon, LoC scan) did we get each author claim, and who made that copy?
29. Which people are credited with essays by any source and also sent or received letters about the Federalist? (computed)
30. Which essays does a source mark as unsure between two authors, and which authors?
