import csv
from common import *
from pathlib import Path

csv_path = DATA_DIR / "sources.csv"

graph = init_kg()

with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        source_id = row["source_id"]
        source_type = row["source_type"]
        source_status = row["source_status"]
        location = row["location"]
        created_date = row["created_date"]
        published_date = row["published_date"]
        earliest_date = row["earliest_date"]
        latest_date = row["latest_date"]
        based_on_source_id = row["based_on_source_id"]

        source = pfs["fed"][source_id]

        graph.add((source, a, pfs["fed"][source_type]))

        if source_status:
            status = pfs["fed"][source_status]
            graph.add((source, pfs["fed"]["hasSourceStatus"], status))
            graph.add((status, a, pfs["fed"]["SourceStatus"]))

        if location:
            graph.add((source, pfs["fed"]["hasLocation"], Literal(location, datatype=XSD.string)))

        if created_date:
            graph.add((source, pfs["fed"]["hasCreatedDate"], Literal(created_date, datatype=XSD.date)))

        if published_date:
            graph.add((source, pfs["fed"]["hasPublishedDate"], Literal(published_date, datatype=XSD.date)))

        if earliest_date:
            graph.add((source, pfs["fed"]["hasEarliestDate"], Literal(earliest_date, datatype=XSD.date)))

        if latest_date:
            graph.add((source, pfs["fed"]["hasLatestDate"], Literal(latest_date, datatype=XSD.date)))

        if based_on_source_id:
            based_on = pfs["fed"][based_on_source_id]
            graph.add((source, pfs["fed"]["isDirectlyBasedOn"], based_on))
            graph.add((based_on, a, pfs["fed"]["Source"]))


output_file = "sources.ttl"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
temp = graph.serialize(format="turtle", encoding="utf-8", destination=OUTPUT_DIR / output_file)
