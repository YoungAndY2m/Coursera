import pytest
from working import convert

def test_default():
    assert convert("9:05 AM to 5:12 PM") == "09:05 to 17:12"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_error_hr():
    with pytest.raises(ValueError):
        convert("12 AM to 17 PM")
        convert("20 AM to 17 PM")

def test_error_min():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:99 PM")

def test_error_omit_to():
    with pytest.raises(ValueError):
        convert("9:12 AM - 5:12 PM")
        convert("9 AM - 5 PM")
