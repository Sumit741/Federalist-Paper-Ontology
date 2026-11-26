"""Append Turtle files to the local Federalist dataset, preserving existing data."""
import argparse
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path, nargs="+")
    args = parser.parse_args()
    for path in args.files:
        request = Request(
            "http://localhost:3030/federalist/data?default",
            data=path.read_bytes(),
            headers={"Content-Type": "text/turtle; charset=utf-8"},
            method="POST",
        )
        try:
            with urlopen(request, timeout=60) as response:
                print(f"Loaded {path}: HTTP {response.status}")
        except HTTPError as error:
            parser.exit(1, f"Loading {path} failed: {error.read().decode()}\n")
        except URLError as error:
            parser.exit(1, f"Cannot reach Fuseki. Start code/start_fuseki.sh first. {error}\n")


if __name__ == "__main__":
    main()
