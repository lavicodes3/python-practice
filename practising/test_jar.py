import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(3)
    assert jar.capacity == 3
    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6
    jar.deposit(3)
    assert jar.size == 9
    with pytest.raises(ValueError):
        jar.deposit(4)  

def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(3)
    assert jar.size == 3
    jar.withdraw(2)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(2)
