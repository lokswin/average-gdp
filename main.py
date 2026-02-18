from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Any, Iterable

from tabulate import tabulate

from reports import get_report, list_reports


Row = dict[str, Any]


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Build console reports from macroeconomic CSV files.",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="One or more paths to CSV files",
    )
    parser.add_argument(
        "--report",
        required=True,
        help=f"Report name. Available: {', '.join(list_reports())}",
    )
    return parser.parse_args(argv)


def read_csv_rows(paths: Iterable[Path]) -> list[Row]:
    rows: list[Row] = []
    for p in paths:
        with p.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
    return rows


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    paths = [Path(x) for x in args.files]
    missing = [str(p) for p in paths if not p.exists()]
    if missing:
        print(f"ERROR: file(s) not found: {', '.join(missing)}", file=sys.stderr)
        return 2

    try:
        report = get_report(args.report)
    except KeyError:
        print(
            f"ERROR: unknown report '{args.report}'. Available: {', '.join(list_reports())}",
            file=sys.stderr,
        )
        return 2

    rows = read_csv_rows(paths)
    headers, table_rows = report.build(rows)

    # Display as a simple console table. Index is shown like in the example screenshot.
    print(tabulate(table_rows, headers=headers, tablefmt="plain", showindex=True, floatfmt=".2f"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
