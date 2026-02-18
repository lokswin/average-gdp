from reports.average_gdp import AverageGdpReport


def test_average_gdp_report_sort_and_values():
    rows = [
        {"country": "A", "gdp": "10"},
        {"country": "A", "gdp": "20"},
        {"country": "B", "gdp": "100"},
        {"country": "B", "gdp": "0"},
    ]
    headers, table = AverageGdpReport().build(rows)

    assert headers == ["country", "gdp"]

    assert table[0][0] == "B"
    assert table[1][0] == "A"
    assert abs(table[0][1] - 50.0) < 1e-9
    assert abs(table[1][1] - 15.0) < 1e-9
