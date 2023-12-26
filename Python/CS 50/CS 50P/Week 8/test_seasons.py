from seasons import input_date, calculate_mins
import pytest

def test_input_valid():
    assert input_date("1999-12-21") == "1999-12-21"
    assert input_date("2001-11-23") == "2001-11-23"
    assert input_date("2023-12-25") == "2023-12-25"

def test_input_invalid():
    with pytest.raises(SystemExit) as exit_info:
        input_date("January 1, 2003")
    assert exit_info.value.code == "Invalid date"

def test_calculate_mins():
    assert calculate_mins(10) == 14400
