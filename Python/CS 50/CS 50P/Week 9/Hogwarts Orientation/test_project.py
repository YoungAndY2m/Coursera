from project import ask_property
import pytest, sys
from io import StringIO

def test_ask_property_valid():
    # name
    user_name = "yang"
    user_input_stream = StringIO(user_name)
    pytest.MonkeyPatch.setattr('sys.stdin', user_input_stream)
    result = ask_property("name")
    assert result == "yang"