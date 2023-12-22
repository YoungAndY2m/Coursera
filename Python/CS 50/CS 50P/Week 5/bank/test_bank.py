from bank import value

def test_default_0():
    assert value("hello, you") == 0

def test_all_upper_0():
    assert value("HELLO, you") == 0

def test_cap_0():
    assert value("Hello") == 0

def test_default_20():
    assert value("Hey, you") == 20

def test_all_upper_20():
    assert value("HEY, you") == 20

def test_cap_20():
    assert value("Howdy") == 20

def test_default_100():
    assert value("You") == 100

def test_all_upper_20():
    assert value("YOU~") == 100

def test_cap_20():
    assert value("What's up!") == 100

