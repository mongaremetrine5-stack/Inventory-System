import requests

BASE_URL = "http://127.0.0.1:5000"

def menu():
    while True:
        print("\n1. View Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            print(requests.get(f"{BASE_URL}/inventory").json())

        elif choice == "2":
            barcode = input("Barcode: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))

            print(requests.post(f"{BASE_URL}/inventory", json={
                "barcode": barcode,
                "quantity": quantity,
                "price": price
            }).json())

        elif choice == "3":
            id = input("ID: ")
            quantity = int(input("New quantity: "))

            print(requests.patch(f"{BASE_URL}/inventory/{id}", json={
                "quantity": quantity
            }).json())

        elif choice == "4":
            id = input("ID: ")
            print(requests.delete(f"{BASE_URL}/inventory/{id}").json())

        elif choice == "5":
            break

menu()