import pytest
from app import app

@pytest.fixture
def client():
    """Создание тестового клиента Flask"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Тест главной страницы"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello, DevOps!"

def test_status(client):
    """Тест маршрута /status"""
    response = client.get("/status")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "OK"
    assert "version" in data

def test_data(client):
    """Тест маршрута /data"""
    response = client.get("/data")
    assert response.status_code == 200
    data = response.get_json()
    assert "data" in data
    assert data["count"] == 5

def test_not_found(client):
    """Тест несуществующего маршрута"""
    response = client.get("/nonexistent")
    assert response.status_code == 404