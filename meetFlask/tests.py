import json

import pytest

from .meet import create_app

email = "h.l@gmail.com"


def test_api_post(client):
    """PersonsView:put"""
    global email
    res = client.post("/persons",
                     data=json.dumps({"email": email, "name": "h", "lastname": "l",
                                      "password": "hej"}),
                     headers={'content-type': 'application/json'})
    assert res.status_code == 200


# def test_api_patch(client):
#     """PersonsView:patch"""
#     global email
#     res = client.patch("/persons/" + email,
#                        data=json.dumps({"name": "j"}),
#                        headers={'content-type': 'application/json'})
#     assert res.status_code == 200
#     assert res.json == {"result": "OK"}


def test_api_get(client):
    """PersonsView:get"""
    global email
    res = client.get("/persons/" + email)
    assert res.status_code == 200
    res = client.get("/persons/" + email + "lol")
    assert res.status_code == 404


def test_api_delete(client):
    """PersonsView:delete"""
    global email
    res = client.delete("/persons/" + email)
    assert res.status_code == 200
    assert res.json == {"result": "OK"}


@pytest.fixture
def app():
    app = create_app()
    app.debug = True
    app.threaded = True
    return app