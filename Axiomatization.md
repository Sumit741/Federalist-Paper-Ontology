# Federalist Papers Ontology

![Overall Federalist Papers schema](Schema%20Diagram/Final_Schem_diagram/Final_Schem_diagram.png)

## Publication Module

![Publication Module schema diagram](Schema%20Diagram/Public_module/Public_module.png)

### Axioms

- `Appearance SubClassOf inPublication only Publication`\
  If appearance is in something, then that is a publication.

- `Newspaper SubClassOf Publication`\
  Newspaper is a type of publication.

- `Edition SubClassOf Publication`\
  Edition is a type of publication.

- `Appearance SubClassOf hasDate max 1 xsd:date`\
  Each appearance has at most one date.

- `Appearance SubClassOf hasPrintedNumber max 1 xsd:positiveInteger`\
  Each appearance has at most one printed number.

- `Essay SubClassOf inverse ofEssay some Appearance`\
  Every essay has at least one appearance.

- `Newspaper DisjointWith Edition`\
  A publication cannot be both a newspaper and an edition.

## Essay Module

![Essay Module schema diagram](Schema%20Diagram/Essay_module/Essay_module.png)

### Axioms

- `Essay SubClassOf hasTopic only Topic`\
  Anything linked to an essay with hasTopic must be a Topic, such as judiciary or executive.

- `Essay SubClassOf hasMcLeanNumber exactly 1 xsd:positiveInteger`\
  An essay has one McLeanNumber value that is a positive integer.

## Agent Module

![Agent Module schema diagram](Schema%20Diagram/Agent_module/Agent_module.png)

### Axioms

- `Person SubClassOf Agent`\
  Person is a type of Agent.

- `Organization SubClassOf Agent`\
  Organization is a type of Agent.

- `Agent SubClassOf hasName exactly 1 xsd:string`\
  An agent has exactly one name.

## Source Module

![Source Module schema diagram](Schema%20Diagram/Source_module/Source_module.png)

### Axioms

- `Source SubClassOf hasLatestDate max 1 xsd:date`\
  Each source has at most one latest date.

- `Source SubClassOf hasEarliestDate max 1 xsd:date`\
  Each source has at most one earliest date.

- `Source SubClassOf hasPublishedDate max 1 xsd:date`\
  Each source has at most one published date.

- `Source SubClassOf hasCreatedDate max 1 xsd:date`\
  Each source has at most one created date.

- `Source SubClassOf hasSourceStatus exactly 1 SourceStatus`\
  Every source has exactly one source status, such as Lost or Surviving.

- `Source SubClassOf hasLocation max 1 xsd:string`\
  Each source has at most one location recorded as text.

- `AuthorshipList SubClassOf Source`\
  AuthorshipList is a type of Source.

- `Edition SubClassOf Source`\
  Edition is a type of Source.

- `Study SubClassOf Source`\
  Study is a type of Source.

- `Letter SubClassOf Source`\
  A letter is a type of Source.

- `Letter SubClassOf hasRecipient only Person`\
  Anyone listed as a letter’s recipient must be a person.

- `Letter SubClassOf hasSender only Person`\
  Anyone listed as a letter’s sender must be a person.

- `Source SubClassOf isDirectlyBasedOn max 1 Source`\
  Every source is directly based on at most one source.

- `Source SubClassOf hasWriter some Agent`\
  Every source has at least one agent who wrote it.

- `Source SubClassOf hasWriter only Agent`\
  Anything listed as a source’s writer must be an agent.

- `hasSender SubPropertyOf hasWriter`\
  If someone is listed as a letter’s sender, they are also its writer.

## Record Module

![Record Module schema diagram](Schema%20Diagram/Record_module/Record_module.png)

### Axioms

- `Record SubClassOf hasEarliestDate max 1 xsd:date`\
  Each record has at most one earliest date.

- `Record SubClassOf hasLatestDate max 1 xsd:date`\
  Each record has at most one latest date.

- `Record SubClassOf endorsedBy only Person`\
  Anyone who endorses a record must be a person.

- `Record SubClassOf isRecordedIn exactly 1 Source`\
  Every record is recorded in exactly one source.

- `Record SubClassOf isAboutEssay only Essay`\
  Anything a record refers to through isAboutEssay must be an Essay.

- `AuthorshipRecord SubClassOf Record`\
  AuthorshipRecord is a type of Record.

- `AuthorshipRecord SubClassOf creditsPerson some Person`\
  Every authorship record credits at least one person as an author.

- `AuthorshipRecord SubClassOf hasClaimant max 1 Person`\
  Each authorship record has at most one person making the claim.

- `JointRecord SubClassOf AuthorshipRecord`\
  JointRecord is a type of AuthorshipRecord.

## Revision Record Module

![Revision Record Module schema diagram](Schema%20Diagram/Revision_record_module/Revision_record_module.png)

### Axioms

- `RevisionRecord SubClassOf wasApproved max 1 xsd:boolean`\
  Each revision record has at most one boolean approval value.

- `inEdition some Edition SubClassOf RevisionRecord`\
  Anything that is linked to Edition with inEdition is a RevisionRecord.

- `RevisionRecord SubClassOf madeBy only Person`\
  Anyone linked from a revision record through madeBy must be a person.

- `RevisionRecord SubClassOf Record`\
  RevisionRecord is a type of Record.
