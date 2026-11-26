#!/bin/sh
set -eu
project_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
fuseki_jar="$project_dir/.runtime/apache-jena-fuseki-6.3.0/fuseki-server.jar"
if [ ! -f "$fuseki_jar" ]; then
    echo "Extract the official Apache Jena Fuseki 6.3.0 distribution into .runtime/ first." >&2
    exit 1
fi
mkdir -p "$project_dir/.runtime/server"
cd "$project_dir/.runtime/server"
exec java -jar "$fuseki_jar" --localhost --port=3030
