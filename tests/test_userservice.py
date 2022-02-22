from flask import Flask
from src.userservice import configure_routes


def test_users():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = "/users"
    response = client.get(url)
    assert response.status == "200 OK"
    assert b"Hans" in response.data


def test_preferred_hobbies():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = "/preferred-hobbies"
    response = client.get(url)
    assert response.status == "200 OK"
    assert b"watching tellie" in response.data