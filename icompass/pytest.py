import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_check_sanitization(client):
    # Positive test case: Input is sanitized
    response = client.post('/v1/sanitized/input/', json={"input": "some input"})
    assert response.status_code == 200
    assert response.json == {"result": "sanitized"}

    # Negative test case: Input is unsanitized (contains SQL injection)
    response = client.post('/v1/sanitized/input/', json={"input": "'; DROP TABLE users; --"})
    assert response.status_code == 200
    assert response.json == {"result": "unsanitized"}

    # Negative test case: Input not provided in the payload
    response = client.post('/v1/sanitized/input/', json={})
    assert response.status_code == 400
    assert response.json == {"error": "Input not provided"}

    # Negative test case: Invalid payload key provided
    response = client.post('/v1/sanitized/input/', json={"invalid_key": "some input"})
    assert response.status_code == 400
    assert response.json == {"error": "Input not provided"}
