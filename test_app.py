import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Enter your name:' in response.data

def test_hello_post(client):
    response = client.post('/', data={'username': 'Sam'})
    assert response.status_code == 200
    assert b'Hello Sam!' in response.data
