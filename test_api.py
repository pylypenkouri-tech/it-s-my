"""
API тесты для JSONPlaceholder
Тестируем реальный веб-сервис
"""
import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users():
    """Тест 1: GET запрос - получение списка пользователей"""
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    users = response.json()
    assert len(users) > 0
    assert users[0]["name"] == "Leanne Graham"

def test_get_user_by_id():
    """Тест 2: GET запрос - получение конкретного пользователя"""
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"

def test_create_post():
    """Тест 3: POST запрос - создание нового поста"""
    new_post = {
        "title": "My First API Test",
        "body": "This is a test post",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    created_post = response.json()
    assert created_post["title"] == "My First API Test"

def test_not_found():
    """Тест 4: GET запрос - несуществующий ресурс (404)"""
    response = requests.get(f"{BASE_URL}/users/99999")
    assert response.status_code == 404