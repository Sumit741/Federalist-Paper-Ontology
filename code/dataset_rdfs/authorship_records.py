import csv
from common import *

csv_path = DATA_DIR / "authorship_records.csv"
graph = init_kg()

with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        record = pfs["fed"][row["record_id"]]
        record_type = pfs["fed"][row["record_type"]]
        essay = pfs["fed"][row["essay_id"]]
        source = pfs["fed"][row["source_id"]]

        graph.add((record, a, record_type))
        graph.add((record, pfs["fed"]["isAboutEssay"], essay))
        graph.add((record, pfs["fed"]["isRecordedIn"], source))


        graph.add((essay, a, pfs["fed"]["Essay"]))
        graph.add((source, a, pfs["fed"]["Source"]))


        # Add a claimant only when one is recorded.
        if row["claimant_id"]:
            claimant = pfs["fed"][row["claimant_id"]]

            graph.add((record, pfs["fed"]["hasClaimant"], claimant))
            graph.add((claimant, a, pfs["fed"]["Person"]))

        # Add dates only when they are recorded.
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


output_file = "authorship_records.ttl"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
temp = graph.serialize(format="turtle", encoding="utf-8", destination=OUTPUT_DIR / output_file)