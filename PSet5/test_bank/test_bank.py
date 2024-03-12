import pytest
from bank import value

def test_hello():
    assert value("hello") == 0


def test_hi():
    assert value("hi") == 20


def test_phrase():
    assert value("what's up?") == 100


def test_hello_phrase():
    assert value("hello, how are you?") == 0


def test_int():
    with pytest.raises(TypeError):
        value(12345)