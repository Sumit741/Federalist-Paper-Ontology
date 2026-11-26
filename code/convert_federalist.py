import argparse
import csv
from datetime import date
from pathlib import Path
from urllib.parse import quote

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, OWL, XSD


# --------------------------------------------------
# Prefixes — same namespace as schema.ttl
# --------------------------------------------------

FED = Namespace(
    "https://w3id.org/federalist-paper-ontology/"
)

pfs = {
    "fed": FED,
    "rdf": RDF,
    "rdfs": RDFS,
    "owl": OWL,
    "xsd": XSD,
}

a = RDF.type


# --------------------------------------------------
# Main entity files
#
# filename:
#   ID column, type column, permitted classes
#
# None means every row has the same fixed class.
# --------------------------------------------------

FILES = {
    "agents.csv": (
        "agent_id",
        "agent_type",
        {"Person", "Organization"},
    ),

    "essays.csv": (
        "essay_id",
        None,
        {"Essay"},
    ),

    "sources.csv": (
        "source_id",
        "source_type",
        {
            "Source",
            "AuthorshipList",
            "Study",
            "Letter",
            "Edition",
        },
    ),

    "authorship_records.csv": (
        "record_id",
        "record_type",
        {"AuthorshipRecord", "JointRecord"},
    ),

    "publications.csv": (
        "publication_id",
        "publication_type",
        {"Publication", "Newspaper", "Edition"},
    ),

    "appearances.csv": (
        "appearance_id",
        None,
        {"Appearance"},
    ),

    "revision_records.csv": (
        "record_id",
        None,
        {"RevisionRecord"},
    ),
}


# --------------------------------------------------
# Literal values
#
# CSV column:
#   ontology property, datatype
# --------------------------------------------------

VALUES = {
    "name": ("hasName", XSD.string),
    "mclean_number": ("hasMcLeanNumber", XSD.positiveInteger),
    "location": ("hasLocation", XSD.string),
    "created_date": ("hasCreatedDate", XSD.date),
    "published_date": ("hasPublishedDate", XSD.date),
    "earliest_date": ("hasEarliestDate", XSD.date),
    "latest_date": ("hasLatestDate", XSD.date),
    "date": ("hasDate", XSD.date),
    "printed_number": ("hasPrintedNumber", XSD.positiveInteger),
    "was_approved": ("wasApproved", XSD.boolean),
}


# --------------------------------------------------
# Relationships recorded in the main files
#
# Each mapping:
#   CSV column, property, expected target class
# --------------------------------------------------

LINKS = {
    "sources.csv": [
        ("based_on_source_id", "isDirectlyBasedOn", "Source"),
    ],

    "authorship_records.csv": [
        ("essay_id", "isAboutEssay", "Essay"),
        ("source_id", "isRecordedIn", "Source"),
        ("claimant_id", "hasClaimant", "Person"),
    ],

    "appearances.csv": [
        ("publication_id", "inPublication", "Publication"),
    ],

    "revision_records.csv": [
        ("essay_id", "isAboutEssay", "Essay"),
        ("source_id", "isRecordedIn", "Source"),
        ("edition_id", "inEdition", "Edition"),
    ],
}


# --------------------------------------------------
# Relationship files
#
# Each mapping:
#   filename,
#   subject ID column, expected subject class,
#   property,
#   target ID column, expected target class
# --------------------------------------------------

LINK_FILES = [
    (
        "appearance_essays.csv",
        "appearance_id", "Appearance",
        "ofEssay",
        "essay_id", "Essay",
    ),
    (
        "authorship_credits.csv",
        "record_id", "AuthorshipRecord",
        "creditsPerson",
        "person_id", "Person",
    ),
    (
        "source_writers.csv",
        "source_id", "Source",
        "hasWriter",
        "agent_id", "Agent",
    ),
    (
        "letter_senders.csv",
        "source_id", "Letter",
        "hasSender",
        "person_id", "Person",
    ),
    (
        "letter_recipients.csv",
        "source_id", "Letter",
        "hasRecipient",
        "person_id", "Person",
    ),
    (
        "record_endorsements.csv",
        "record_id", "Record",
        "endorsedBy",
        "person_id", "Person",
    ),
    (
        "revision_makers.csv",
        "record_id", "RevisionRecord",
        "madeBy",
        "person_id", "Person",
    ),
]


# --------------------------------------------------
# Initialize an empty RDF graph
# --------------------------------------------------

def init_kg(prefixes=pfs):
    graph = Graph()

    for prefix, namespace in prefixes.items():
        graph.bind(prefix, namespace)

    return graph


# --------------------------------------------------
# Read and check a CSV
# --------------------------------------------------

def read_csv(path, required):
    with path.open(
        encoding="utf-8-sig",
        newline="",
    ) as file:

        reader = csv.DictReader(file)

        missing = (
            set(required)
            - set(reader.fieldnames or [])
        )

        if missing:
            raise ValueError(
                f"{path.name}: missing columns {sorted(missing)}"
            )

        rows = []

        for number, row in enumerate(reader, start=2):
            if None in row:
                raise ValueError(
                    f"{path.name}, row {number}: extra CSV values"
                )

            if any(value is None for value in row.values()):
                raise ValueError(
                    f"{path.name}, row {number}: missing CSV cells"
                )

            row = {
                key: value.strip()
                for key, value in row.items()
            }

            # Ignore completely empty rows.
            if not any(row.values()):
                continue

            # Required IDs and types cannot be blank.
            if any(not row[column] for column in required):
                raise ValueError(
                    f"{path.name}, row {number}: empty required value"
                )

            rows.append(row)

        return rows


# --------------------------------------------------
# Turn an ID into an RDF identifier
#
# Example:
# Hamilton → fed:Hamilton
# --------------------------------------------------

def entity(identifier):
    return FED[quote(identifier, safe="_-~.")]


# --------------------------------------------------
# Create typed literal values
# --------------------------------------------------

def make_literal(value, datatype):
    if datatype == XSD.date:
        parsed = date.fromisoformat(value)

        if parsed.isoformat() != value:
            raise ValueError(
                f"Date must use YYYY-MM-DD: {value}"
            )

    elif datatype == XSD.positiveInteger:
        value = int(value)

        if value <= 0:
            raise ValueError(
                "Essay and printed numbers must be positive"
            )

    elif datatype == XSD.boolean:
        if value.lower() not in {"true", "false"}:
            raise ValueError(
                f"Approval must be true or false: {value}"
            )

        value = value.lower() == "true"

    return Literal(value, datatype=datatype)


# --------------------------------------------------
# Convert the dataset
# --------------------------------------------------

def convert(data_dir, schema_path, output):
    # Read schema.ttl to check subclass relationships.
    # The schema is not copied into the data output.
    schema = Graph().parse(
        schema_path,
        format="turtle",
    )

    graph = init_kg()
    tables = {}

    # --------------------------------------------------
    # First pass: declare all entities.
    # --------------------------------------------------

    for filename, settings in FILES.items():
        id_column, type_column, allowed = settings

        required = [id_column]

        if type_column:
            required.append(type_column)

        rows = read_csv(
            data_dir / filename,
            required,
        )

        tables[filename] = rows
        seen = set()

        for row in rows:
            identifier = row[id_column]

            if identifier in seen:
                raise ValueError(
                    f"{filename}: duplicate ID {identifier}"
                )

            seen.add(identifier)

            if type_column:
                kind = row[type_column]
            else:
                kind = next(iter(allowed))

            if kind not in allowed:
                raise ValueError(
                    f"{filename}: unsupported type {kind}"
                )

            graph.add((
                entity(identifier),
                a,
                FED[kind],
            ))

    # --------------------------------------------------
    # Check referenced IDs and their classes.
    #
    # Person is accepted where Agent is expected because
    # schema.ttl states Person SubClassOf Agent.
    # --------------------------------------------------

    def reference(identifier, expected):
        node = entity(identifier)

        for kind in graph.objects(node, a):
            if kind == FED[expected]:
                return node

            superclasses = schema.transitive_objects(
                kind,
                RDFS.subClassOf,
            )

            if FED[expected] in superclasses:
                return node

        raise ValueError(
            f"{identifier}: missing entity or expected {expected}"
        )

    # --------------------------------------------------
    # Second pass: add values and relationships.
    # --------------------------------------------------

    for filename, rows in tables.items():
        id_column = FILES[filename][0]

        for row in rows:
            subject = entity(row[id_column])

            # Literal values: names, dates, numbers, etc.
            for column, settings in VALUES.items():
                prop, datatype = settings

                if row.get(column):
                    graph.add((
                        subject,
                        FED[prop],
                        make_literal(row[column], datatype),
                    ))

            # Publication titles are descriptive labels.
            if row.get("title"):
                graph.add((
                    subject,
                    RDFS.label,
                    Literal(row["title"]),
                ))

            # Source status is a controlled-vocabulary entity.
            if row.get("source_status"):
                status = row["source_status"]

                if status not in {"Lost", "Surviving"}:
                    raise ValueError(
                        f"Unknown source status: {status}"
                    )

                graph.add((
                    FED[status],
                    a,
                    FED.SourceStatus,
                ))

                graph.add((
                    subject,
                    FED.hasSourceStatus,
                    FED[status],
                ))

            # Relationships from columns in the main files.
            for column, prop, expected in LINKS.get(filename, []):
                if row.get(column):
                    graph.add((
                        subject,
                        FED[prop],
                        reference(row[column], expected),
                    ))

    # --------------------------------------------------
    # Read relationship files.
    # Repeated subject IDs allow multiple linked entities.
    # --------------------------------------------------

    for settings in LINK_FILES:
        (
            filename,
            subject_column,
            subject_class,
            prop,
            target_column,
            target_class,
        ) = settings

        rows = read_csv(
            data_dir / filename,
            [subject_column, target_column],
        )

        for row in rows:
            subject = reference(
                row[subject_column],
                subject_class,
            )

            target = reference(
                row[target_column],
                target_class,
            )

            graph.add((
                subject,
                FED[prop],
                target,
            ))

    # --------------------------------------------------
    # Read essay topics.
    # --------------------------------------------------

    topic_rows = read_csv(
        data_dir / "essay_topics.csv",
        ["essay_id", "topic_id"],
    )

    for row in topic_rows:
        topic = entity(row["topic_id"])

        graph.add((
            topic,
            a,
            FED.Topic,
        ))

        graph.add((
            reference(row["essay_id"], "Essay"),
            FED.hasTopic,
            topic,
        ))

        if row.get("topic_label"):
            graph.add((
                topic,
                RDFS.label,
                Literal(row["topic_label"]),
            ))

    # --------------------------------------------------
    # Save the completed graph.
    # --------------------------------------------------

    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    graph.serialize(
        destination=str(output),
        format="turtle",
    )

    print(f"Saved {len(graph)} triples to {output}")


# --------------------------------------------------
# Run from the terminal
# --------------------------------------------------

if __name__ == "__main__":
    project = Path(__file__).resolve().parent.parent

    parser = argparse.ArgumentParser(
        description="Convert Federalist CSV files into Turtle"
    )

    parser.add_argument(
        "--data",
        type=Path,
        default=project / "data",
    )

    parser.add_argument(
        "--schema",
        type=Path,
        default=project / "schema.ttl",
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=project / "./federalist_data.ttl",
    )

    args = parser.parse_args()

    try:
        convert(
            args.data,
            args.schema,
            args.output,
        )

    except (ValueError, OSError) as error:
        parser.exit(
            1,
            f"Conversion failed: {error}\n",
        )