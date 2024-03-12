from seasons import is_date_input_valid
from datetime import date
import pytest

def test_date_valid():
    assert is_date_input_valid("2023-11-4") == date(2023, 11, 4)


def test_date_invalid():
    with pytest.raises(SystemExit):
        is_date_input_valid("haha")