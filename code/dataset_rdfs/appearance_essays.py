import csv
from common import *

csv_path = DATA_DIR / "appearance_essays.csv"

graph = init_kg()

with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        appearance_id = row["appearance_id"]
        essay_id = row["essay_id"]

        appearance = pfs["fed"][appearance_id]
        essay = pfs["fed"][essay_id]

        graph.add((appearance, a, pfs["fed"]["Appearance"]))
        graph.add((essay, a, pfs["fed"]["Essay"]))
        graph.add((appearance, pfs["fed"]["ofEssay"], essay))


    output_file = "appearance_essays.ttl"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    temp = graph.serialize(format="turtle", encoding="utf-8", destination=OUTPUT_DIR / output_file)