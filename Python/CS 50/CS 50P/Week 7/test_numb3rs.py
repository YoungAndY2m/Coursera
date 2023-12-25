import pytest
from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("127.10.12.3") == True

def test_max():
    assert validate("255.255.255.255") == True

def test_invalid():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False

def test_first_range():
    assert validate("75.456.23.26") == False

def test_str():
    assert validate("cat") == False
    assert validate("cat.cat.cat.cat") == False
