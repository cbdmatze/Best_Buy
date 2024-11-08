from products import Products
from store import Store

def start(store):
    while True:
        print("\nWelcome to Best Buy Tech Store!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        # Get the user's choice
        choice = input("Please enter your choice (1-4): ")

        # Handle the choice
        if choice == "1":
            list_products(store)
        elif choice == "2":
            show_total_quantity(store)
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Thank you for visiting Best Buy!")
            break
        else:
            print("*Invalid choice. Please select a valid option.*")

# Option 1: List all products in store
def list_products(store):
    products = store.get_all_products()
    if not products:
        print("No products available in store.")
    else:
        print("\nProducts available in store:")
        for product in products:
            print(product.show())

# Option 2: Show total amount in store
def show_total_quantity(store):
    total_quantity = store.get_total_quantity()
    print(f"\nTotal quantity of items in store: {total_quantity}")

# Option 2: Make an order
def make_order(store):
    

