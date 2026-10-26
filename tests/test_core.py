from pilot.core import normalize_label


def test_basic():
    assert normalize_label("Hello World") == "hello-world"


def test_trims_and_collapses_whitespace():
    assert normalize_label("  Many   Spaces\tHere ") == "many-spaces-here"


def test_empty_string():
    assert normalize_label("") == ""
