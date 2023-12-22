from fuel import convert, gauge
import pytest

def test_convert_default():
    assert convert("1/2") == 50

def test_convert_error():
    with pytest.raises(ValueError):
        convert("3/2")
        convert("cat/cat")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_gauge_E_F():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(100) == "F"

def test_gauge_default():
    assert gauge(50) == "50%"
    assert gauge(23) == "23%"
