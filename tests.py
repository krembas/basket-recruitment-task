import pytest

from app import create_app


@pytest.fixture
def test_client():
    app = create_app()
    app.debug = True
    return app.test_client()


def test_basket(test_client):
    with test_client.get('/basket') as resp:
        assert resp.status_code == 200
        assert resp.json == {}

    with test_client.put('/basket') as resp:
        assert resp.status_code == 200
        assert resp.json == {}

    with test_client.delete('/basket') as resp:
        assert resp.status_code == 200
        assert resp.json == {}


