import requests

def fetch_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    try:
        res = requests.get(url)
        data = res.json()

        if data["status"] != 1:
            return None

        product = data["product"]

        return {
            "product_name": product.get("product_name"),
            "brand": product.get("brands"),
            "ingredients": product.get("ingredients_text"),
            "category": product.get("categories")
        }

    except:
        return None