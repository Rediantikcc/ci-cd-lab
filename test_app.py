from app import app


def test_health_check():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_not_found():
    client = app.test_client()
    response = client.get("/unknown")
    assert response.status_code == 404
