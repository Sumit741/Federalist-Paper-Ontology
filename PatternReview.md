# Pattern review for the Federalist Papers ontology

This review connects the supplied readings and MODL patterns to the current competency questions. Pattern selections and Federalist modeling proposals below are interpretations for this project, not claims that the papers prescribe this exact ontology.

## Materials reviewed

| Material | Coverage | Main contribution |
|---|---|---|
| [Modular Ontology Modeling: A Tutorial](/Users/sumit/Downloads/2020-mom-tutorial.pdf), Shimizu, Hitzler and Krisnadhi | All 19 PDF pages; especially the workflow and worked recipe example | Derive key notions from questions and available data; adapt patterns into modules; document and axiomatize them before assembling the ontology. |
| [The Enslaved Ontology: Peoples of the Historic Slave Trade](/Users/sumit/Downloads/enslaved-ontology%20%281%29.pdf), Shimizu et al. | All 9 PDF pages; especially Sections 2–3 and Figures 2–9 | Represent source-dependent historical records, agents, participation roles and provenance while retaining conflicting accounts. |
| [Modular Ontology Modeling](/Users/sumit/Downloads/sw-prepress_sw--1--1-sw222886_sw--1-sw222886%20%282%29.pdf), Shimizu, Hammar and Hitzler, DOI 10.3233/SW-222886 | All 31 PDF pages; especially Section 3, Table 1, and Section 5.5 | Explain MOMo's diagram-first workflow, module boundaries, systematic axiomatization, scoped restrictions, and supporting tooling. |
| [Template-Based Content ODP Instantiation](/Users/sumit/Downloads/template-based-instantiation%20%281%29.pdf), Hammar and Presutti | All 12 PDF pages; especially Sections 3–4 | Copy and adapt relevant pattern structures into local terms rather than requiring their entire import hierarchy. Discuss benefits, limitations and a small preliminary evaluation. |
| [Hyvönen datasets for ontology project](/Users/sumit/Downloads/Hyvo%CC%88nen%20datasets%20for%20ontology%20project.md) | Complete supplied note | Comparative leads for record, role, event, place and provenance modeling in historical datasets. This is a research note, not one of the supplied papers. |
| [MODL repository](https://github.com/kastle-lab/modular-ontology-design-library/tree/b14ada02bc21faa3c00bb8e1ddbbb14344266db5/modl) | README, documentation text, pattern annotations and logical definitions in all 31 pattern folders, top-level catalog, and the included 12-page MODL paper | Concrete pattern templates, schema diagrams and OWL serializations. Core diagrams were also rendered and visually inspected. |

Repository snapshot: `b14ada02bc21faa3c00bb8e1ddbbb14344266db5`. This review inspects the pattern definitions; it does not certify that the repository passes an OWL parser, profile checker or reasoner. The supplied dataset note's endpoint, license and dataset-size claims were not independently rechecked, nor were all publications linked from that note read.

## Shared lessons from the papers

1. Start with use cases, actual source material and competency questions. A useful ontology must capture information the sources can supply.
2. Identify key notions, then choose patterns for those notions. A notion need not have the same name as a library pattern, and some notions need a custom module.
3. Use a pattern as a template: preserve its useful structure, adapt names and restrictions, and document departures.
4. Develop a schema diagram and explanation for each module. A diagram alone does not specify cardinality, existence, disjointness or other logical constraints.
5. Select axioms deliberately. Scoped restrictions often avoid unintended commitments when properties are reused across modules.
6. Assemble modules through explicit connections, review their combined axioms and check coverage of the competency questions.
7. Preserve the origin of module designs with documentation and OPLa annotations. External ontology alignments can be maintained separately from the local model.

The tutorial presents an eight-step walkthrough; the later MOMo paper expands the workflow into ten steps in Table 1. These are compatible presentations at different levels of detail.

The Enslaved paper is especially relevant because it treats historical source reports as records rather than assuming that all imported statements are established facts. Its provenance model also distinguishes the source, the responsible agent, and the activity producing the modeled information.

The template-instantiation paper supports local adaptation, but also identifies costs: automatic interoperability through shared pattern IRIs is reduced, and copied structures require maintenance. Its five-participant evaluation offers preliminary evidence, not a universal proof of superiority. The later MOMo paper evaluates CoModIDE with 21 participants; this evaluates the tool in the reported tasks, not the quality of every ontology built with MOMo.

## Pattern choices for our key notions

| Federalist notion | Pattern or approach | Application and adaptation | Relevant question numbers |
|---|---|---|---|
| Agent | Stub / Name Stub, with optional Identifier | People and organizations, including conventions if needed; roles remain separate from agents. | 1, 5, 11–12, 16, 19, 21–22 |
| AgentRole | Agent-Role plus Participant-Role | An agent's source-qualified Author, Sender, Recipient, Shipper, Receiver or Intermediary participation in an event. | 1, 3–5, 7–8, 11–12, 19, 21–22 |
| Event | Event | Writing, Publication, Sending and Shipment; connect the relevant documents, roles, time and places. | 1–4, 7–8, 11–15, 19, 21–22 |
| Document | Custom document module, with Stub, Identifier and Explicit Typing | Essay, Letter, Collection, Edition, Volume, AuthorshipList, Newspaper and Study. MODL has no dedicated Document pattern folder in this snapshot. | All source-dependent questions |
| Record | Record plus Provenance, adapted using the Enslaved approach | A structured account or assertion based on a source document, describing an event, role or textual reference. | 1–5, 7–8, 14, 17, 19–24 |
| Computation | Provenance; optionally Data Transformation | An execution that uses records and generates a derived result. Algorithm and execution environment are optional refinements. MODL has no pattern folder named Computation. | 3–4, 7–8, 15, 21 |
| Reference | Reification plus Record / Provenance | A letter-to-target relation with a type, evidence passage and source context. This needs a Federalist-specific module; there is no dedicated Reference folder. | 11, 16, 20–21, 23–24 |
| TemporalExtent | Temporal Extent, simplified to the source granularity | Exact dates, intervals and uncertain dates. Distinguish event date, assertion date and extraction date. | 2, 5, 12–15, 19, 21 |
| Place | Stub initially; Spatial Object if geometry is needed | Named historical sending and receiving places. Detailed polygons and trajectories are unnecessary for the current questions. | 14 |
| Quantity | Quantity | Number of copies of a specified volume in a shipment; use an integer count where appropriate. | 19 |
| Passage | Custom evidence component using part/whole and Identifier ideas | A quote and locator in the specific text or edition used as evidence. Passage occurs in the questions but is missing from the key-notion list. | 20, 23–24; useful for 5 and 21 |

Pattern links: [Agent-Role](https://github.com/kastle-lab/modular-ontology-design-library/tree/b14ada02bc21faa3c00bb8e1ddbbb14344266db5/modl/agent-role), [Participant-Role](https://github.com/kastle-lab/modular-ontology-design-library/tree/b14ada02bc21faa3c00bb8e1ddbbb14344266db5/modl/participant-role), [Event](https://github.com/kastle-lab/modular-ontology-design-library/tree/b14ada02bc21faa3c00bb8e1ddbbb14344266db5/modl/event), [Record](https://github.com/kastle-lab/modular-ontology-design-library/tree/b14ada02bc21faa3c00bb8e1ddbbb14344266db5/modl/record), [Provenance](https://github.com/kastle-lab/modular-ontology-design-library/tree/b14ada02bc21faa3c00bb8e1ddbbb14344266db5/modl/provenance), [Reification](https://github.com/kastle-lab/modular-ontology-design-library/tree/b14ada02bc21faa3c00bb8e1ddbbb14344266db5/modl/reification), [Temporal Extent](https://github.com/kastle-lab/modular-ontology-design-library/tree/b14ada02bc21faa3c00bb8e1ddbbb14344266db5/modl/temporal-extent), [Quantity](https://github.com/kastle-lab/modular-ontology-design-library/tree/b14ada02bc21faa3c00bb8e1ddbbb14344266db5/modl/quantity), [Data Transformation](https://github.com/kastle-lab/modular-ontology-design-library/tree/b14ada02bc21faa3c00bb8e1ddbbb14344266db5/modl/data-transformation).

## Refinements to discuss before creating OWL

### Separate an event from its records

The current statement, "Every Event, AgentRole and Reference is a Record based on a source Document," needs an explicit interpretation. The papers do not require actual events to be records. The MODL Record diagram instead shows a Record that `records` a thing, and an EventRecord that is a kind of Record.

A proposed interpretation is:

- An Event identifies the historical occurrence being discussed.
- An EventRecord describes that occurrence according to a source.
- A role record describes an agent's reported participation in that occurrence.
- A Reference record describes a textual mention or assertion with its evidence.

The current role node can remain a source-qualified role record if that meaning is documented. Avoid automatically turning every reported Author role into an unqualified assertion of actual authorship.

For example, using hypothetical sources and agents:

```text
Essay N <-- concernsEssay -- Writing N

Source S1 <-- isDirectlyBasedOn -- AuthorRoleRecord R1
R1 -- forEvent --> Writing N
R1 -- attributedAuthor --> Agent A

Source S2 <-- isDirectlyBasedOn -- AuthorRoleRecord R2
R2 -- forEvent --> Writing N
R2 -- attributedAuthor --> Agent B
```

This represents two source-qualified attributions. It does not establish that A and B jointly wrote the essay. The property names in this example are proposed local names, not copied MODL vocabulary.

Keeping one Writing event per essay can serve as a project convention that groups the source attributions. It is not an axiom supplied by MODL, and it needs reconsideration if drafts or separate writing episodes enter scope. Publication occurrences should remain distinct from the records reporting them, so conflicting publication dates do not become an unexplained list of dates on a single event.

### Distinguish three different kinds of time

1. The historical occurrence: when an essay was published or a letter was sent.
2. The source assertion: when someone made an attribution.
3. The research activity: when a record was extracted or a computation executed.

An Author role's temporal extent is not automatically the date of the later source claiming authorship. Similarly, a letter's written date, sending date and received date need not coincide. Question 12's receipt-date follow-up needs a received-date assertion or a Receiving/Delivery event beyond the present Sending model.

### Define the scope of computed answers

- **Disputed authorship:** compare attribution sets within an identified group of relevant sources. A missing author is not a denial; a partial list need not contradict a fuller list. Document what counts as a conflict.
- **Joint authorship:** group roles by essay and source/assertion context, then count distinct agents. Two different sources naming different single authors do not demonstrate joint authorship.
- **Agreement across every source:** define the source set and required coverage. Agreement among sources with recorded claims differs from an attribution explicitly present in every selected source.
- **Essay counts:** count distinct essays credited to each agent by the selected source; repeated mentions must not inflate totals.
- **Letters during printing:** define whether the query means within the overall project date window or overlapping particular recorded printing/publication intervals. Publication instants alone do not describe continuous printing activity.
- **Earliest evidence:** identify the earliest dated letter in the available corpus. This does not prove when a person first knew the authors' identities. Undated or uncertain letters must remain visible as limitations.

These are query/computation policies, not results that plain OWL axioms automatically calculate. If results are persisted, connect each result to its Computation and the input records, source set and query or algorithm used.

### Make evidence passages and reference targets explicit

Reference records should identify the containing Letter, reference type, target, and supporting Passage. Passages should identify the exact source text/edition and a locator such as page, paragraph or character span, with quoted text where available.

For `NamesAuthors`, link the actual attribution content: which agent is named as author of which essay or collection. Merely marking a letter as `NamesAuthors` does not connect it to the particular authorship claims needed by Questions 21–22.

For the shipment question, distinguish a Volume or Edition from the physical copies sent. A small ShipmentItem component can connect a shipment, volume/edition and Quantity without requiring an individual node for every copy. The quantity should attach to that item, particularly if one shipment includes more than one volume.

### Decide how types will be represented

The current labels `Event(Writing)`, `AgentRole(Author)` and `Reference(Opinion)` do not yet specify whether Writing, Author and Opinion are OWL subclasses or controlled-vocabulary individuals.

Explicit Typing is suitable when categories change independently of the schema. Subclasses are suitable when a category needs its own logical restrictions. Choose and document the approach for each category; do not use the same IRI as both an ordinary type individual and a class without an intentional design.

### Preserve unknowns without inventing facts

"Not recorded" and "no evidence" should normally be query or presentation outputs for the examined corpus. They should not become fictitious Place or Agent entities. Optional or uncertain dates should not be replaced by invented exact dates to satisfy copied pattern restrictions.

## Repository details that affect reuse

These observations come from the pinned repository files, rather than from the conceptual pattern descriptions alone.

| File or pattern | Observation | Consequence for this project |
|---|---|---|
| Agent-Role | The OWL contains a scoped-domain restriction making anything with `hasTemporalExtent` to a TemporalExtent an AgentRole. | If we unify that property across events, documents and roles, we could unintentionally classify them all as roles. Adapt the restriction before composing modules. |
| Participant-Role | The documentation lists an exactly-one performer restriction on AgentRole; the standalone participant-role OWL does not include that same performer cardinality. | Verify intended role cardinalities explicitly instead of assuming the prose and standalone file match. |
| Record | Record is a subclass of EntityWithProvenance; EventRecord is a subclass of Record. The OWL requires every Record to derive from an EventRecord and have temporal/type information. | Keep the record/entity distinction, but adapt the required provenance chain to our actual source documents. |
| Reification | The file places `hasContext some Context` on `owl:Thing`. | Copying it literally requires every individual to have context. Scope the requirement to the reified assertion if that is the intended meaning. |
| Quantity | The numeric range is `xsd:double`. | Adapt copy counts to an appropriate integer datatype; retain the quantity structure when it adds value. |
| Role Dependent Name | The file contains an `Error1` superclass and models `hasNameAsString` as an object property to a class named `:xsd:string`. | Use the idea cautiously for Publius; repair the datatype/name modeling before reuse. A simple source-qualified name module may suffice. |
| Reporting Event | The connection annotation says ActualEventView is an InformationObject; the OWL makes InformationObject a subclass of ActualEventView. | Check intended direction and granularity before adapting this more elaborate alternative. |
| Aggregation | The connection annotation describes BagItem `itemOf` Bag, while the restriction uses Bag `itemOf` BagItem. | Use clearly named local relations such as `hasMember` and `isMemberOf`. |

These checks reinforce the papers' recommendation to adapt and document patterns. They are a source inspection, not an exhaustive defect report or a formal consistency result.

## Complete pattern inventory and Federalist relevance

The checked snapshot contains 31 pattern directories. The older MODL paper and documentation describe a smaller earlier collection; the repository also contains later additions.

| Pattern folder | What it contributes | Federalist relevance |
|---|---|---|
| agent-role | Contextual, time-bounded agent roles | Core |
| aggregation | Unordered membership in a collection | Essays in collections; copies in a batch |
| causal-event | Source-qualified causal relations and resulting states | Defer; current questions do not ask about causation |
| data-transformation | Computational executions, algorithms, inputs and outputs | Optional detail for Computation |
| description-situation | Descriptions and the situations they characterize | Alternative if richer contextual interpretations become necessary |
| event | Occurrences, participants, extents and subevents | Core |
| explicit-typing | Extensible vocabulary types | Role, event, document and reference categories |
| hierarchical-cell-features | Spatial cells, features and attributes | Defer |
| identifier | Identifiers and identifier types | Essay numbers, archival IDs and source identifiers |
| name-stub | Names with a string representation | Agent and document naming |
| observation | Observations, properties, results and times | Optional analogy for scholarly observations; not required initially |
| part-whole | Different kinds of part relations | Passage/document and volume structure, with appropriate relation choices |
| part-whole-contextualized | Reified part/whole relations | Useful if membership itself varies by source or edition |
| participant-role | Agent participation in an event | Core |
| provenance | Derivation, attribution and generating activities | Core |
| quantity | Magnitudes, kinds, values and units | Shipment copy counts |
| record | Records about entities, with provenance and time | Core, after adaptation |
| recurrent-event | Series of repeating events | Defer; multiple publications need not be a recurrent series |
| reification | Relations represented as entities with context | Reference and authorship assertions |
| reporting-event | Reporting acts and views of actual events | Optional alternative for detailed reporting histories |
| role-dependent-name | Names used in particular roles | Potential extension for Publius; implementation needs review |
| sequence | Ordered items | Optional essay order or correspondence order; replies can branch |
| spatial-extent | Geometric extents | Defer unless spatial queries require geometry |
| spatial-object | Features and geometries | Optional refinement of Place |
| spatiotemporal-extent | Movement described through time/place fixes | Defer unless routes become part of the questions |
| state-transition | States, actions and transitions | Defer |
| stub | Minimal extensible placeholders | Simple Agent, Place and other supporting notions |
| taxonomy-alignment | Connections between vocabulary concepts | Optional future source-vocabulary alignment |
| temporal-extent | Points and intervals | Core, simplified for historical source precision |
| trajectory | Ordered fixes and connecting segments | Optional future shipment routes |
| tree | Hierarchical data | Optional document hierarchy; not a general correspondence-network model |

## Proposed development order

1. Draft Record and Provenance together, including how records refer to source documents and evidence passages.
2. Draft AgentRole / ParticipantRole and Event together, demonstrating two conflicting source attributions without asserting joint authorship.
3. Draft the Document and Reference modules, including essay identity, edition/volume distinctions and evidence locators.
4. Attach time, place and shipment quantities at the level justified by real examples.
5. Define computation inputs, source coverage and missing-data behavior for the computed questions.
6. Draw the composed model, determine scoped axioms and check each question against sample data before producing OWL.

The three existing question modules organize research tasks. The ontology can implement them using shared conceptual modules for documents, records/provenance, events, roles, references, time/place, quantities and computations. A research-question group need not correspond to exactly one ontology file.

The supplied Hyvönen note provides comparison leads: it emphasizes person/record separation in WarSampo and AcademySampo, manuscript-source provenance in MMM, time-dependent roles in ParliamentSampo, and correspondence modeling in LetterSampo. These are leads from the note; their underlying schemas and papers require separate inspection before claiming a verified alignment to the Federalist model.
