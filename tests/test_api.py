import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_get_inventory(client):
    res = client.get("/inventory")
    assert res.status_code == 200


def test_add_item(client):
    res = client.post("/inventory", json={
        "barcode": "123",
        "quantity": 5,
        "price": 100
    })
    assert res.status_code in [201, 404]