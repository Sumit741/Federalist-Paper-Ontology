import csv  
from common import *

csv_path = DATA_DIR / "publications.csv"

graph = init_kg()

with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        publication = pfs["fed"][row["publication_id"]]
        publication_type = pfs["fed"][row["publication_type"]]

        graph.add((publication, a, publication_type))
        graph.add((publication, pfs["fed"]["label"], Literal(row["title"])))


    output_file = "publications.ttl"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    temp = graph.serialize(format="turtle", encoding="utf-8", destination=OUTPUT_DIR / output_file)