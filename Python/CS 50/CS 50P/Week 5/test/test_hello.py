from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("yang") == "hello, yang"
    for name in ["1", "2", "3"]:
        assert hello(name) == "hello, " + name