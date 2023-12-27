from project import ask_property, write_coster, read_last_line
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