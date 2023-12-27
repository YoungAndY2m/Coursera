from project import ask_property, write_coster, read_last_line, preference, sorting_hat
from model import Student
import pytest, sys
from pytest import MonkeyPatch as monkeypatch

TEST_ROSTER = "test_roster.csv"

"""
Tests for ask_property
"""
def test_ask_property_name(monkeypatch: monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Alex")
    result = ask_property("name")
    assert result == "Alex"

def test_ask_property_gender(monkeypatch: monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "female")
    result = ask_property("gender")
    assert result == "female"

def test_ask_property_blood(monkeypatch: monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "pure-blood")
    result = ask_property("blood")
    assert result == "pure-blood"

def test_ask_property_description(monkeypatch: monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Bravery")
    result = ask_property("description")
    assert result == "bravery"

"""
Tests for write_coster & read_last_line (constantly changing)
"""
def test_write_coster_read_last_line():
    test_student = Student("Yang Alex", "female", "pure-blood", "bravery")
    write_coster(test_student, TEST_ROSTER)
    assert read_last_line(TEST_ROSTER) == "Yang,Alex,Unknown,female,pure-blood,bravery"

def test_write_coster_read_last_line_unknown():
    test_student = Student("Yang")
    write_coster(test_student, TEST_ROSTER)
    assert read_last_line(TEST_ROSTER) == "Yang,Unknown,Unknown,unknown,Unknown,Unknown"

"""
Tests for preference
"""
def test_preference():
    assert preference(Student("yang alex", "female", "pure-blood", "loyalty")) == ['Slytherin', 'Hufflepuff', 'Ravenclaw', 'Gryffindor']
    assert preference(Student("yang alex", "male", "muggle-born", "loyalty")) == ['Hufflepuff', 'Ravenclaw', 'Gryffindor', 'Slytherin']

def test_preference_unknown():
    assert preference(Student("yang alex")) == ['Ravenclaw', 'Hufflepuff', 'Gryffindor', 'Slytherin']

"""
Tests for sorting_hat
"""
def test_sorting_hat(monkeypatch: monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Yes, of course!")
    result = sorting_hat(Student("yang li", "female", "pure-blood", "loyalty"))
    assert result == "Slytherin"

def test_sorting_hat_all_nos(monkeypatch: monkeypatch):
    no_inputs = ["no", "no", "no", "no"]

    def mock_input(prompt):
        return no_inputs.pop(0)
    
    monkeypatch.setattr('builtins.input', mock_input)
    result = sorting_hat(Student("yang li", "female", "pure-blood", "loyalty"))
    assert result == "Gryffindor"
