## Macro Reports (CLI)

Small CLI utility that reads one or more CSV files with country-level macroeconomic indicators and prints a consolidated report to stdout.

Currently implemented report:
- `average-gdp` — average GDP per country (arithmetic mean of `gdp` across all provided files), sorted descending.

### Requirements
- Python 3.10+
- Runtime deps: `tabulate`
- Parsing/processing: standard library only (`argparse`, `csv`, etc.)

### Usage
```bash
python3 main.py --files economic1.csv economic2.csv --report average-gdp
