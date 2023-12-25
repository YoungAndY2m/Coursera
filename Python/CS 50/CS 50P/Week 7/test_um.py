from um import count
import pytest

def test_one():
    assert count("um?") == 1
    assert count("um") == 1
    
def test_default():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_zero():
    assert count("asfjasld;fksjk") == 0
    assert count("umumum, yummy") == 0
    assert count("UMUMUM") == 0
    assert count("MUUM") == 0
