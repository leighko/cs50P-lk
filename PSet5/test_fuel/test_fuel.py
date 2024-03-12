from fuel import convert, gauge
import pytest


def test_convert_fract():
    assert convert("3/4") == 75


def test_convert_str():
    with pytest.raises(UnboundLocalError):
        convert("abcd")


def test_gauge():
    assert gauge(75) == "75%"


def test_gauge_str():
    with pytest.raises(TypeError):
        gauge("75")