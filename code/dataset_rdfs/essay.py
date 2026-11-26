
import csv
from common import *

csv_path = DATA_DIR / "essays.csv"

graph = init_kg()

with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        essay_id = row["essay_id"]
        mclean_number = int(row["mclean_number"])

        essay = pfs["fed"][essay_id]

        graph.add((essay, a, pfs["fed"]["Essay"]))

        graph.add((
            essay,
            pfs["fed"]["hasMcLeanNumber"],
            Literal(mclean_number, datatype=XSD.positiveInteger)
        ))

output_file = "essays.ttl"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

graph.serialize(
    format="turtle",
    encoding="utf-8",
    destination=OUTPUT_DIR / output_file
)

print(f"Total triples: {len(graph)}")
print(f"Generated: {OUTPUT_DIR / output_file}")
