"""
Тесты на PyTest — профессиональный фреймворк
"""

def is_even(number):
    """Проверяет, чётное ли число"""
    return number % 2 == 0

def is_positive(number):
    """Проверяет, положительное ли число"""
    return number > 0

# === ТЕСТЫ ===
# PyTest сам найдёт все функции, начинающиеся с "test_"

def test_even_number():
    """Тест: 42 должно быть чётным"""
    assert is_even(42) == True

def test_odd_number():
    """Тест: 15 должно быть нечётным"""
    assert is_even(15) == False

def test_positive_number():
    """Тест: 100 должно быть положительным"""
    assert is_positive(100) == True

def test_negative_number():
    """Тест: -5 должно быть отрицательным"""
    assert is_positive(-5) == False