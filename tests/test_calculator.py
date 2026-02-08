from string_calculator.calculator import add


def test_empty_string_returns_zero():
    assert  add("") == 0

def test_single_number_returns_value():
    assert add("1") == 1

def test_two_numbers_comma_separated():
    assert add("1,2") == 3

def test_multiple_numbers():
    assert add("1,2,3,4,5,6") == 21

def test_newline_between_numbers():
    assert add("1\n2,3") == 6