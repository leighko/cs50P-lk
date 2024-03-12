from plates import is_valid


def test_plate_num():
    assert is_valid("34dkfj") == False


def test_plate_punct():
    assert is_valid("!/#$") == False


def test_plate_too_few():
    assert is_valid("f") == False


def test_plate_too_many():
    assert is_valid("sdlfjdlkjf") == False


def test_plate_wrong_num_indexes():
    assert is_valid("dkf3d") == False

def test_plate_zero():
    assert is_valid("eif023") == False