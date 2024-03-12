from working import convert, reformat
import pytest


def test_convert_valid_long_zeros():
    assert convert("12:00 am to 9:00 pm") == "00:00 to 21:00"


def test_convert_valid_short_zeros():
    assert convert("4 am to 8 pm") == "04:00 to 20:00"


def test_convert_valid_short_nonzeros():
    assert convert("4:06 am to 8 pm") == "04:06 to 20:00"


def test_convert_valid_long_nonzeros():
    assert convert("4:34 am to 8:59 pm") == "04:34 to 20:59"


def test_convert_invalid_hour1():
    with pytest.raises(ValueError):
        convert("15:00 am to 9:00 pm") 


def test_convert_invalid_hour2():
    with pytest.raises(ValueError):
        convert("12:00 am to 19:00 pm")


def test_convert_invalid_minute1():
    with pytest.raises(ValueError):
        convert("12:65 am to 9:00 pm")


def test_convert_invalid_minute2():
    with pytest.raises(ValueError):
        convert("12:00 am to 9:98 pm")


def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("12:00 am - 9:00 pm")


def test_convert_capital_hour1():
    assert convert("1:00 AM to 9:00 pm") == "01:00 to 21:00"


def test_convert_capital_hour2():
    assert convert("8:00 am to 10:00 PM") == "08:00 to 22:00"


def test_convert_mixedcase_hour1():
    assert convert("12:00 Am to 9:00 pm") == "00:00 to 21:00"


def test_convert_mixedcase_hour2():
    assert convert("12:00 am to 9:00 pM") == "00:00 to 21:00"


def test_convert_swap_am_pm():
    assert convert("12:00 pm to 9:00 am") == "12:00 to 09:00"


def test_convert_swap_am_pm():
    assert convert("5:45 pm to 6:27 am") == "17:45 to 06:27"