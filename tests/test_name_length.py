import pytest
from merge_demo.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_name_too_long_rejected(client):
    """
    Test that a name longer than 20 characters is rejected with an error message.
    """
    long_name = "A" * 21
    response = client.post("/", data={"username": long_name})
    assert response.status_code == 200
    assert b"Name must be less than 20 characters." in response.data
    # Should not greet the user
    assert b"Hello" not in response.data or long_name.encode() not in response.data


def test_name_accepted_when_20_or_less(client):
    """
    Test that a name of exactly 20 characters is accepted.
    """
    valid_name = "B" * 20
    response = client.post("/", data={"username": valid_name})
    assert response.status_code == 200
    assert b"Hello" in response.data
    assert valid_name.encode() in response.data
