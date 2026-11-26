import csv
from common import *

csv_path = DATA_DIR / "essay_topics.csv"

graph = init_kg()

with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        essay_id = row["essay_id"]
        topic_id = row["topic_id"]

        essay = pfs["fed"][essay_id]
        topic = pfs["fed"][topic_id]

        graph.add((essay, a, pfs["fed"]["Essay"]))
        graph.add((essay, pfs["fed"]["hasTopic"], topic))
        graph.add((topic, a, pfs["fed"]["Topic"]))

output_file = "essay_topics.ttl"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

graph.serialize(
    format="turtle",
    encoding="utf-8",
    destination=OUTPUT_DIR / output_file
)

print(f"Generated: {OUTPUT_DIR / output_file}")