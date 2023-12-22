from twttr import shorten

def test_twitter():
    assert shorten("twitter") == "twttr"

def test_aeiou():
    assert shorten("aeiou") == ""

def test_no_change():
    assert shorten("qwrt") == "qwrt"

def test_uppercase():
    assert shorten("AEIOUT") == "T"

def test_number():
    assert shorten("12340987") == "12340987"

def test_punctuation():
    assert shorten("CS, 50") == "CS, 50"

