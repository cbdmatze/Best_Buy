from store_2 import Store


def start(store):
    """
    Display the main menu for the store and handle user interaction.

    Parameters:
    ----------
    store : Store
        The store object that holds the products and manages orders.
    """
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


def list_products(store):
    """
    Display a list of all active products in the store.

    Parameters:
    ----------
    store : Store
        The store object to list the products from.
    """
    products = store.get_all_products()
    if not products:
        print("No products available in store.")
    else:
        print("\nProducts available in store:")
        for product in products:
            print(product)  # This will use the __str__ method of the Products class


def show_total_quantity(store):
    """
    Display the total quantity of all products in the store.

    Parameters:
    ----------
    store : Store
        The store object to calculate the total quantity from.
    """
    total_quantity = store.get_total_quantity()
    print(f"\nTotal quantity of items in store: {total_quantity}")


def make_order(store):
    """
    Allow the user to make an order by selecting products and quantities.

    Parameters:
    ----------
    store : Store
        The store object that handles the order.
    """
    products = store.get_all_products()
    if not products:
        print("No products available for purchase.")
        return

    shopping_list = []

    # Display available products with numbers
    print("\nAvailable products:")
    for i, product in enumerate(products):
        print(f"{i + 1}. {product}")  # Use __str__ method to display product details

    # Loop to collect products and their quantities
    while True:
        try:
            # Ask user to input the product number or 0 to stop
            product_number = int(input("\nEnter the number of the product you want to buy (or 0 to stop): "))
            
            if product_number == 0:
                break  # Exit the loop if the user enters 0
            
            if 1 <= product_number <= len(products):
                # Get the quantity for the selected product
                quantity = int(input(f"How many units of {products[product_number - 1].name} do you want to buy? "))
                
                # Add product and quantity to the shopping list
                shopping_list.append((products[product_number - 1], quantity))
            else:
                print("Invalid product number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    # If there are items in the shopping list, proceed with the order
    if shopping_list:
        try:
            # Try to process the order
            total_price = store.order(shopping_list)  
            print(f"Order placed successfully! Total price: {total_price} dollars")  # Only print if the order succeeds
        except Exception as e:
            # If an exception occurs, print the error message
            print(f"Error processing order: {e}")
    else:
        print("No items were ordered.")