import csv
from datetime import date

from common import *

graph = init_kg()
csv_path = DATA_DIR / "appearances.csv"

with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        appearance = pfs["fed"][row["appearance_id"]]
        publication = pfs["fed"][row["publication_id"]]

        graph.add((appearance, a, pfs["fed"]["Appearance"]))
        graph.add((publication, a, pfs["fed"]["Publication"]))
        graph.add((appearance, pfs["fed"]["inPublication"], publication))

        # Leave unknown dates and printed numbers unrecorded.
        appearance_date = row["date"]
        if appearance_date:
            date.fromisoformat(appearance_date)
            graph.add((appearance, pfs["fed"]["hasDate"],
                       Literal(appearance_date, datatype=XSD.date)))

        printed_number = row["printed_number"]
        if printed_number:
            number = int(printed_number)
            if number <= 0:
                raise ValueError("Printed numbers must be positive integers")
            graph.add((appearance, pfs["fed"]["hasPrintedNumber"],
                       Literal(number, datatype=XSD.positiveInteger)))
            
output_file = "appearances.ttl"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
temp = graph.serialize(format="turtle", encoding="utf-8", destination=OUTPUT_DIR / output_file)

