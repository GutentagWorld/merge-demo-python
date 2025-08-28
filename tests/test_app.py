import pytest
from merge_demo.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hello_get(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Enter your name:" in response.data


def test_hello_post(client):
    response = client.post("/", data={"username": "Sam"})
    assert response.status_code == 200
    assert b"Hello Sam!" in response.data


def test_favorite_number_not_three(client):
    """
    This test will fail any time the favorite number is 3,
    hypothetically 1/10 tests should fail to simulate a
    flaky test.
    """
    response = client.post("/", data={"username": "Test"})
    assert response.status_code == 200
    # Extract favorite number from response
    import re

    match = re.search(rb"Your favorite number is: (\d+)", response.data)
    assert match is not None, "Favorite number not found in response."
    favorite_number = int(match.group(1))
    assert favorite_number != 3, "Test fails because favorite number is 3."


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
