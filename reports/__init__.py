from __future__ import annotations

from typing import Any, Protocol

from .average_gdp import AverageGdpReport


class Report(Protocol):
    name: str

    def build(self, rows: list[dict[str, Any]]) -> tuple[list[str], list[list[Any]]]:
        """Return (headers, rows) for tabulate()."""
        raise NotImplementedError


_REGISTRY: dict[str, Report] = {
    "average-gdp": AverageGdpReport(),
}


def get_report(name: str) -> Report:
    return _REGISTRY[name]


def list_reports() -> list[str]:
    return sorted(_REGISTRY.keys())


def register(report: Report) -> None:
    """Register a new report at runtime (extensibility hook)."""
    _REGISTRY[report.name] = report
