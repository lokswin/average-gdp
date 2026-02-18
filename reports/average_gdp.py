from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from collections import defaultdict


@dataclass(frozen=True)
class AverageGdpReport:
    """Average GDP by country across all provided rows/files."""

    name: str = "average-gdp"

    def build(self, rows: list[dict[str, Any]]) -> tuple[list[str], list[list[Any]]]:
        gdp_by_country: dict[str, list[float]] = defaultdict(list)

        for r in rows:
            country = str(r.get("country", "")).strip()
            if not country:
                continue
            gdp_by_country[country].append(float(r["gdp"]))

        averaged: list[tuple[str, float]] = [
            (country, sum(values) / len(values)) for country, values in gdp_by_country.items()
        ]
        averaged.sort(key=lambda x: x[1], reverse=True)

        table_rows: list[list[Any]] = [[country, avg] for country, avg in averaged]
        return ["country", "gdp"], table_rows
