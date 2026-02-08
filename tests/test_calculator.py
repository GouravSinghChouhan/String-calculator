import pytest
from string_calculator.calculator import add


def test_empty_string_returns_zero():
    assert add("") == 0


def test_single_number_returns_value():
    assert add("1") == 1


def test_two_numbers_comma_separated():
    assert add("1,5") == 6


def test_multiple_numbers():
    assert add("1,2,3,4") == 10


def test_newline_between_numbers():
    assert add("1\n2,3") == 6


def test_custom_delimiter():
    assert add("//;\n1;2") == 3


def test_negative_number_throws_exception():
    with pytest.raises(ValueError, match="Negative numbers not allowed -1"):
        add("-1,2")


def test_multiple_negative_numbers():
    with pytest.raises(ValueError, match="Negative numbers not allowed -1,-3,-7"):
        add("-1,2,-3,4,6,-7")


def test_numbers_greater_than_1000_are_ignored():
    assert add("2, 1001") == 2
