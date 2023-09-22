from seasons import convert


def test_seasons_convert():
    assert convert("1999-01-01") == "Thirteen million, three thousand, two hundred minutes"
    assert convert("1999-12-31") == "Twelve million, four hundred seventy-nine thousand forty minutes"
