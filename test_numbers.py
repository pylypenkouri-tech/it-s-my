"""
Мой первый проект по автоматизации тестирования
Автор: pylypenkouri-tech
"""

# ============ ФУНКЦИИ (что мы тестируем) ============

def is_even(number):
    """Проверяет, чётное ли число"""
    return number % 2 == 0

def is_positive(number):
    """Проверяет, положительное ли число"""
    return number > 0

# ============ ТЕСТЫ (проверки) ============

def test_even_number():
    """Тест: 42 должно быть чётным"""
    assert is_even(42) == True, "42 должно быть чётным!"

def test_odd_number():
    """Тест: 15 должно быть нечётным"""
    assert is_even(15) == False, "15 должно быть нечётным!"

def test_positive_number():
    """Тест: 100 должно быть положительным"""
    assert is_positive(100) == True, "100 должно быть положительным!"

def test_negative_number():
    """Тест: -5 должно быть отрицательным"""
    assert is_positive(-5) == False, "-5 должно быть отрицательным!"

# ============ ЗАПУСК ТЕСТОВ ============

print("🧪 Запуск автотестов...")
print("=" * 40)

tests = [
    ("Тест 1: 42 - чётное", test_even_number),
    ("Тест 2: 15 - нечётное", test_odd_number),
    ("Тест 3: 100 - положительное", test_positive_number),
    ("Тест 4: -5 - отрицательное", test_negative_number),
]

passed = 0
failed = 0

for name, test_func in tests:
    try:
        test_func()
        print(f"✅ {name} - ПРОЙДЕН")        
        passed += 1
    except AssertionError as e:
        print(f"❌ {name} - ПРОВАЛЕН: {e}")
        failed += 1

print("=" * 40)
print(f"📊 Итого: {passed} пройдено, {failed} провалено")

if failed == 0:
    print("🎉 Все тесты прошли успешно!")
else:
    print("⚠️ Есть проваленные тесты, нужно чинить код!")
