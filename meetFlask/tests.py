import json

import pytest

from .meet import create_app


def test_api_put(client):
    """PersonsView:put"""
    res = client.post("/persons",
                     data=json.dumps({"email": "h.l@gmail.com", "name": "h", "lastname": "l",
                                      "password": "hej"}),
                     headers={'content-type': 'application/json'})
    assert res.status_code == 200


@pytest.fixture
def app():
    app = create_app()
    app.debug = True
    app.threaded = True
    return app