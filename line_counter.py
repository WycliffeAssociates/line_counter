""" Counts lines in en_tn """

from pathlib import Path
from typing import Dict
import os

BOOK_ABBREVIATIONS = [
    "gen", "exo", "lev", "num", "deu", "jos", "jdg", "rut", "1sa",
    "2sa", "1ki", "2ki", "1ch", "2ch", "ezr", "neh", "est", "job",
    "psa", "pro", "ecc", "sng", "isa", "jer", "lam", "ezk", "dan",
    "hos", "jol", "amo", "oba", "jon", "mic", "nam", "hab", "zep",
    "hag", "zec", "mal", "mat", "mrk", "luk", "jhn", "act", "rom",
    "1co", "2co", "gal", "eph", "php", "col", "1th", "2th", "1ti",
    "2ti", "tit", "phm", "heb", "jas", "1pe", "2pe", "1jn", "2jn",
    "3jn", "jud", "rev" ]

def count_lines() -> Dict[str, int]:
    book_lines = {}
    pathlist = Path(".").glob("**/*.md")
    for path in pathlist:
        topdir = path.parts[0]
        if topdir not in book_lines:
            book_lines[topdir] = 0
        with open(str(path), encoding="utf-8") as md_file:
            content = md_file.read()
            lines = content.count("\n")
            book_lines[topdir] = book_lines[topdir] + lines
    return book_lines

def print_lines(book_lines: Dict[str, int]) -> None:
    total = 0
    for book in BOOK_ABBREVIATIONS:
        if book not in book_lines:
            continue
        total += book_lines[book]
        print(f"{book}: {book_lines[book]:,}")
    print(f"TOTAL: {total:,}")

def main() -> None:
    print_lines(count_lines())


if __name__ == "__main__":
    main()