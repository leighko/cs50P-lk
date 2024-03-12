from um import count


def test_count_no_ums():
    assert count("Hello world, it's crazy here.") == 0


def test_count_five_ums_rand_case():
    assert count("Um UM um uM ... um") == 5


def test_count_no_ums_only_nums():
    assert count("123 323 1208") == 0


def test_count_um_in_words():
    assert count("yummy in my tummy scrumptious dumptious") == 0


def test_count_um_with_punct():
    assert count("???um?? hello? um..what? like...um!!?") == 3