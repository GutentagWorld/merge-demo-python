import pytest
from merge_demo.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_name_is_title_case(client):
    response = client.post("/", data={"username": "john doe"})
    assert response.status_code == 200
    assert b"Hello John Doe!" in response.data
