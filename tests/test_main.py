from src.main import add, subtract

def test_add_function():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(5, 5) == 10

def test_subtract_function():
    assert subtract(5, 2) == 3
    assert subtract(0, 0) == 0
    assert subtract(5, 5) == 1