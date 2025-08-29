import pytest
from merge_demo.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# def test_favorite_number_not_three(client):
#     """
#     This test will fail any time the favorite number is 3,
#     hypothetically 1/10 tests should fail to simulate a
#     flaky test.
#     """
#     response = client.post("/", data={"username": "Test"})
#     assert response.status_code == 200
#     # Extract favorite number from response
#     import re

#     match = re.search(rb"Your favorite number is: (\d+)", response.data)
#     assert match is not None, "Favorite number not found in response."
#     favorite_number = int(match.group(1))
#     assert favorite_number != 3, "Test fails because favorite number is 3."


# def test_favorite_number_less_than_four(client):
#     """
#     This test will fail any time the favorite number is less than four,
#     hypothetically 3/10 tests should fail to simulate a
#     flaky test.
#     """
#     response = client.post("/", data={"username": "Test"})
#     assert response.status_code == 200
#     # Extract favorite number from response
#     import re

#     match = re.search(rb"Your favorite number is: (\d+)", response.data)
#     assert match is not None, "Favorite number not found in response."
#     favorite_number = int(match.group(1))
#     assert favorite_number < 4, "Test fails because favorite number is not less than 4."
