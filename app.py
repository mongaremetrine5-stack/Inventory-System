from flask import Flask, jsonify, request

app = Flask(__name__)

inventory = []

@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory)


@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)
    if not item:
        return {"error": "Item not found"}, 404
    return item


@app.route("/inventory", methods=["POST"])
def add_item():
    data = request.json

    new_item = {
        "id": len(inventory) + 1,
        "barcode": data.get("barcode"),
        "product_name": data.get("product_name"),
        "brand": data.get("brand"),
        "ingredients": data.get("ingredients"),
        "category": data.get("category"),
        "quantity": data.get("quantity", 0),
        "price": data.get("price", 0)
    }

    inventory.append(new_item)
    return {"message": "Item added", "item": new_item}, 201


@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    data = request.json

    item = next((i for i in inventory if i["id"] == item_id), None)
    if not item:
        return {"error": "Item not found"}, 404

    item["quantity"] = data.get("quantity", item["quantity"])
    item["price"] = data.get("price", item["price"])

    return {"message": "Item updated", "item": item}


@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global inventory
    inventory = [i for i in inventory if i["id"] != item_id]

    return {"message": "Item deleted"}


if __name__ == "__main__":
    app.run(debug=True)