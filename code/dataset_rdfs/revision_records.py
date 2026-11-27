import csv
from common import *

csv_path = DATA_DIR / "revision_records.csv"
graph = init_kg()
with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        record = pfs["fed"][row["record_id"]]
        source = pfs["fed"][row["source_id"]]
        edition = pfs["fed"][row["edition_id"]]

        graph.add((record, a, pfs["fed"]["RevisionRecords"]))
        graph.add((source, a, pfs["fed"]["Source"]))
        graph.add((edition, a, pfs["fed"]["Edition"]))

        graph.add((record, pfs["fed"]["isRecordedIn"], source))
        graph.add((record, pfs["fed"]["inEdition"], edition))

        if row["essay_id"]:
            essay = pfs["fed"][row["essay_id"]]
            graph.add((essay, a, pfs["fed"]["Essay"]))
            graph.add((record, pfs["fed"]["isAboutEssay"], essay))

        approval = row["was_approved"]

        if approval:
            if approval not in {'true', 'false'}:
                raise ValueError(f"Invalid value for was_approved: {approval}")


            graph.add((record, pfs["fed"]["wasApproved"], Literal(approval, datatype=XSD.boolean)))

        if row["earliest_date"]:
            graph.add((
                record,
                pfs["fed"]["hasEarliestDate"],
                Literal(row["earliest_date"], datatype=XSD.date),
            ))

        if row["latest_date"]:
            graph.add((
                record,
                pfs["fed"]["hasLatestDate"],
                Literal(row["latest_date"], datatype=XSD.date),
            ))


output_file = "revision_records.ttl"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
temp = graph.serialize(format="turtle", encoding="utf-8", destination=OUTPUT_DIR / output_file)