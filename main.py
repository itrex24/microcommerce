products = [
    {"ID": 1, "name": "Keyboard", "price": 90, "stock": 10},
    {"ID": 2, "name": "Mouse", "price": 50, "stock": 2},
    {"ID": 3, "name": "Monitor", "price": 300,"stock": 5},
    {"ID": 4, "name": "Desk", "price": 120,"stock": 15},
    {"ID": 5, "name": "Chair", "price": 250,"stock": 3},
]

def all_products():
    for entry in products:
        print(f"ID: {entry['ID']} | {entry['name']} | £{entry['price']} | Stock: {entry['stock']}")



def get_product_id_input():
    while True:
        try:
            return int(input("Enter product ID: "))
        except ValueError:
            print("you must enter an integer")

def lookup_product(target_id):
    for entry in products:
        if entry["ID"] == target_id:
            return entry
    return None

def product_search():
    chosen_id = get_product_id_input()
    product_found = lookup_product(chosen_id)

    if product_found:
        print(product_found)
    else:
        print("\nCouldn't find it. Here are the available products:\n")
        all_products()

product_search()
