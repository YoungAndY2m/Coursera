from plates import is_valid

# default
def test_default():
    assert is_valid("CS50") == True
    assert is_valid("CSP50") == True

def test_begin_alphabet():
    assert is_valid("AA") == True
    assert is_valid("A2") == False

def test_number_placement():
    assert is_valid("11") == False
    assert is_valid("CS06") == False
    assert is_valid("sdf222") == True
    assert is_valid("sdf22s") == False


# start with at least two letters
def test_less_than_two():
    assert is_valid("") == False
    assert is_valid("s") == False

# maximum of 6 characters and a minimum of 2 characters
def test_more_than_six():
    assert is_valid("asdfsadfdasf") == False
    assert is_valid("AOFIJDSOSI") == False

# numbers must come at end, first number cannot be a zero
def test_number_at_beginning():
    assert is_valid("11kd") == False
    assert is_valid("k23k") == False

def test_first_zero():
    assert is_valid("kd023") == False
    assert is_valid("dsf000") == False

# No periods, spaces, or punctuation marks
def test_periods():
    assert is_valid("k.dk") == False
    assert is_valid("sdf.") == False

def test_spaces():
    assert is_valid("sdf ") == False
    assert is_valid("s df") == False

def test_punctuation():
    assert is_valid("sd,f") == False
    assert is_valid("sdf?") == False
