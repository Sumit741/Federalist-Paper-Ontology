
import csv
from common import *

csv_path = DATA_DIR / "letter_recipients.csv"

graph = init_kg()

with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        source_id = row["source_id"]
        person_id = row["person_id"]

        letter = pfs["fed"][source_id]
        person = pfs["fed"][person_id]

        graph.add((letter, a, pfs["fed"]["Letter"]))
        graph.add((letter, pfs["fed"]["hasRecipient"], person))
        graph.add((person, a, pfs["fed"]["Person"]))

output_file = "letter_recipients.ttl"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

graph.serialize(
    format="turtle",
    encoding="utf-8",
    destination=OUTPUT_DIR / output_file
)

print(f"Generated: {OUTPUT_DIR / output_file}")
