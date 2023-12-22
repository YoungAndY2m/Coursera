from calculator import square
from hello import hello
import pytest

# def main():
#     test_square()

# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared is not 4")
#     assert square(3) == 9

# if __name__ == "__main__":
#     main()

# pytest package
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

def test_hello():
    # no return value -> return None == sth. WRONG
    # have return value -> return sth = sth. CORRECT
    assert hello("yang") == "hello, yang"
    assert hello() == "hello, world"
    for name in ["1", "2", "3"]:
        assert hello(name) == "hello, " + name
