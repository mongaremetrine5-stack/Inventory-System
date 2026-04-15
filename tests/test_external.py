from unittest.mock import patch
from external_api import fetch_product

@patch("external_api.requests.get")
def test_fetch(mock_get):
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Milk",
            "brands": "Test",
            "ingredients_text": "Milk",
            "categories": "Dairy"
        }
    }

    result = fetch_product("123")
    