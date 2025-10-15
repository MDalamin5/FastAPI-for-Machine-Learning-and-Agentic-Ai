from calculator import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(4, 3) == 7
    assert add(3, 8) == 11

def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by Zero"):
        divide(10, 0)