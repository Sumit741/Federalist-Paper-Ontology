import csv
from common import *

csv_path = DATA_DIR / "agents.csv"

graph = init_kg()
# test triple

with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        agent_id = row["agent_id"]
        agent_name = row["name"]
        agent_type = row["agent_type"]

        agent = pfs["fed"][agent_id]
        graph.add((agent, a, pfs["fed"][agent_type]))
        graph.add((agent, pfs["fed"]["hasName"], Literal(agent_name)))



output_file = "agents.ttl"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
temp = graph.serialize(format="turtle", encoding="utf-8", destination=OUTPUT_DIR / output_file)
