from app import app
import pytest


@pytest.fixture
def client():
    return app.test_client()


def test_home_page():
    """
    GIVEN a Flask survey form application
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """

    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Sound of AI Survey Questions" in response.data


def test_submit(client):
    """
    GIVEN a Flask survey form application
    WHEN the form is submitted
    THEN check whether request is sent
    """

    response = client.post('/responsedata',
                           data={
                               'q1': '1',
                               'q2': '1',
                               'q3': '1',
                               'q4': 'I-will-probably-use-it',
                               'q5': 'sample_1',
                           })
    assert response.status_code == 200
