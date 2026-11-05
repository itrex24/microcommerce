products = [
    {"ID": 1, "name": "Keyboard", "price": 90, "stock": 10},
    {"ID": 2, "name": "Mouse", "price": 50, "stock": 0},
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

def get_quantity_input():
    while True:
        try:
            return int(input("How much stock do you want to buy? "))
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
        print("Couldn't find it. Here are the available products:")
        all_products()

def purchase_product():
    chosen_id = get_product_id_input()
    product_found = lookup_product(chosen_id)

    if not product_found:
        print("Couldn't find it. Here are the available products:")
        all_products()
        return

    stock_wanted = get_quantity_input()

    if stock_wanted <= 0:
        print("stock wanted must be above 0")
        return

    if product_found["stock"] < stock_wanted:
        print(f"Not enough stock. We only have {product_found['stock']} available.")
        return

    total_price = stock_wanted * product_found["price"]

    product_found["stock"] -= stock_wanted
    print(f"Purchase successful! You bought {stock_wanted} {product_found['name']}(s). Total is {total_price}")
    print(product_found)

purchase_product()
