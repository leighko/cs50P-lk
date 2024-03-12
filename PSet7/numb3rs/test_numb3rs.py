from numb3rs import validate


def test_validate_hundred():
    assert validate("100.100.100.100") == True


def test_validate_uppermost():
    assert validate("255.255.255.255") == True


def test_validate_zeros():
    assert validate("0.0.0.0") == True


def test_validate_thousand():
    assert validate("1000.1.2.1000") == False


def test_validate_too_big():
    assert validate("512.512.512.512") == False


def test_validate_str():
    assert validate("cat") == False


def test_validate_toomanyinputs():
    assert validate("1.2.3.4.5") == False