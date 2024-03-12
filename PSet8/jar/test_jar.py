from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar._size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.deposit(4) == 4
    jar.deposit(4)
    assert jar._size == 8


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    assert jar.withdraw(3) == 7
    jar.withdraw(2)
    assert jar._size == 5