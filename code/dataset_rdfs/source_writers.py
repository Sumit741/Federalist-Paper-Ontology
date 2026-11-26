import csv
from common import *

csv_path = DATA_DIR / "source_writers.csv"

graph = init_kg()

with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        source_id = row["source_id"]
        agent_id = row["agent_id"]
        
        source = pfs["fed"][source_id]
        graph.add((source, a, pfs["fed"]["Source"]))

        agent = pfs["fed"][agent_id]
        graph.add((source, pfs["fed"]["hasWriter"], agent))
        graph.add((agent, a, pfs["fed"]["Agent"]))

output_file = "source_writers.ttl"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
temp = graph.serialize(format="turtle", encoding="utf-8", destination=OUTPUT_DIR / output_file)
