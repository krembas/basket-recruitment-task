import pytest

from app import create_app


@pytest.fixture
def test_client():
    app = create_app()
    app.debug = True
    return app.test_client()


def test_basket(test_client):
    # test empty basket
    with test_client.get('/basket') as resp:
        assert resp.status_code == 200
        assert resp.json == {'items': []}


    # test adding items to basket
    data = {'items': [{'id': '1', 'qty': 1}, {'id': '2', 'qty': 2}]}
    with test_client.put('/basket', json=data) as resp:
        assert resp.status_code == 200
    with test_client.get('/basket') as resp:
        assert resp.status_code == 200
        assert resp.json == data

    # test removing products from basket
    data = {'items': [{'id': '1', 'qty': -1}]}
    with test_client.put('/basket', json=data) as resp:
        assert resp.status_code == 200
    with test_client.get('/basket') as resp:
        assert resp.status_code == 200
        assert resp.json == {'items': [{'id': '2', 'qty': 2}]}

    # test emptying basket
    with test_client.delete('/basket') as resp:
        assert resp.status_code == 204
    with test_client.get('/basket') as resp:
        assert resp.status_code == 200
        assert resp.json == {'items': []}

    # test basket accounting
    with test_client.get('/basket/account') as resp:
        assert resp.status_code == 200
        assert resp.json == {'total_price': '1.23'}
