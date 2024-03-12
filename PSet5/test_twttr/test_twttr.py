import pytest

from twttr import shorten


def test_shorten():
    assert shorten("abcdeiou") == "bcd"


def test_symbols():
    assert shorten("?./#$&#(@*)") == "?./#$&#(@*)"


def test_num_str():
    assert shorten("2343") == "2343"


def test_num():
    with pytest.raises(TypeError):
        shorten(1296)