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

def add_product():
    while True:
        new_product_name = input("Specify name (or type 'quit' to exit): ").strip()
        if new_product_name.lower() == 'quit': 
            break
        if not new_product_name:
            print("Name cannot be empty, Please try again")
            continue

        name_exists = any(item.get("name", "").lower() == new_product_name.lower() for item in products)

        if name_exists:
            print(f"The product '{new_product_name}' already exists. Please choose a different name")
        else:
            while True:
                try:
                    new_product_price = int(input("Specify price: "))
                except ValueError:
                    print("Invalid input!")
                    continue

                if new_product_price <= 0:
                    print("Price must be greater than zero")
                    continue

                break

            while True:
                try:
                    new_product_stock = int(input("Specify stock: "))
                except ValueError:
                    print("Invalid input!")
                    continue

                if new_product_stock < 0:
                    print("Stock cannot be negative")
                    continue

                break
                
            existing_ids = [item["ID"] for item in products if "ID" in item]
            next_id = max(existing_ids) + 1 if existing_ids else 1
            new_entry = {
                "ID": next_id,
                "name": new_product_name,
                "price": new_product_price,
                "stock": new_product_stock
            }

            products.append(new_entry)
            print("New product added")
            break

    
while True:
    menu = """
    =========================
          MICROCOMMERCE      
    =========================
    1. View all products
    2. Search for a product
    3. Purchase a product
    4. Add a product
    5. Exit
    =========================
    """
    print(menu)
    menu_input = input("Enter your choice: ")
    if menu_input   == "1":
        all_products()
    elif menu_input == "2":
        product_search()
    elif menu_input == "3":
        purchase_product()
    elif menu_input == "4":
        add_product()
    elif menu_input == "5":
        print("Thank you")
        break
    else:
        print("Invalid option")
    