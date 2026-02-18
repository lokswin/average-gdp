import subprocess
import sys
from pathlib import Path


def test_cli_happy_path(tmp_path: Path):
    f1 = tmp_path / "d1.csv"
    f2 = tmp_path / "d2.csv"

    f1.write_text(
        "country,year,gdp,gdp_growth,inflation,unemployment,population,continent\n"
        "A,2023,10,0,0,0,0,X\n"
        "A,2022,20,0,0,0,0,X\n",
        encoding="utf-8",
    )
    f2.write_text(
        "country,year,gdp,gdp_growth,inflation,unemployment,population,continent\n"
        "B,2023,100,0,0,0,0,X\n"
        "B,2022,0,0,0,0,0,X\n",
        encoding="utf-8",
    )

    r = subprocess.run(
        [sys.executable, "main.py", "--files", str(f1), str(f2), "--report", "average-gdp"],
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True,
        text=True,
        check=False,
    )

    assert r.returncode == 0
    out = r.stdout

    assert "country" in out
    assert "gdp" in out
    # showindex=True prints index column with 0/1 lines; verify content exists
    assert "B" in out and "50.00" in out
    assert "A" in out and "15.00" in out


def test_cli_unknown_report(tmp_path: Path):
    f1 = tmp_path / "d.csv"
    f1.write_text(
        "country,year,gdp,gdp_growth,inflation,unemployment,population,continent\n"
        "A,2023,10,0,0,0,0,X\n",
        encoding="utf-8",
    )

    r = subprocess.run(
        [sys.executable, "main.py", "--files", str(f1), "--report", "nope"],
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True,
        text=True,
        check=False,
    )

    assert r.returncode == 2
    assert "unknown report" in r.stderr.lower()


def test_cli_missing_file():
    r = subprocess.run(
        [sys.executable, "main.py", "--files", "definitely_missing.csv", "--report", "average-gdp"],
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True,
        text=True,
        check=False,
    )
    assert r.returncode == 2
    assert "not found" in r.stderr.lower()
