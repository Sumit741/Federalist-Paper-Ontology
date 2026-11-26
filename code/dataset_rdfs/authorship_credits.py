import csv
from common import *

csv_path = DATA_DIR / "authorship_credits.csv"

graph = init_kg()

with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        record = pfs["fed"][row["record_id"]]
        person = pfs["fed"][row["person_id"]]

        graph.add((record, a, pfs["fed"]["AuthorshipRecord"]))
        graph.add((person, a, pfs["fed"]["Person"]))
        graph.add((record, pfs["fed"]["creditsPerson"], person))


output_file = "authorship_credits.ttl"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
temp = graph.serialize(format="turtle", encoding="utf-8", destination=OUTPUT_DIR / output_file) 
