##### Graph stuff
import rdflib
from rdflib import URIRef, Graph, Namespace, Literal
from rdflib import OWL, RDF, RDFS, XSD

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent   # common.py is in code/, so go up one
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"

name_space = "https://w3id.org/federalist-paper-ontology/"

pfs = {
    "fed": Namespace(f"{name_space}"),
    "fedr": Namespace(f"{name_space}resource/"),
    "rdf": RDF,
    "rdfs": RDFS,
    "xsd": XSD,
    "owl": OWL,
}

# rdf:type shortcut
a = pfs["rdf"]["type"]

# Initialization shortcut
def init_kg(prefixes=pfs):
    kg = Graph()
    for prefix in prefixes:
        kg.bind(prefix, prefixes[prefix])
    return kg
