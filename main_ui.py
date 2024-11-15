from products import Products, NonStockedProduct, LimitedProduct  
from store import Store
from user_interface import start


def main() -> None:
    """
    Main function to initialize products, set up store inventory, and start the user interface.
    """

    # Initialize a few products
    macbook_air_m2 = Products("MacBook Air M2", price=1450, quantity=100)
    bose_quietcomfort_earbuds = Products("Bose QuietComfort Earbuds", price=250, quantity=500)
    google_pixel_7 = Products("Google Pixel 7", price=500, quantity=250)

    # Set up initial stock of inventory
    product_list = [
        macbook_air_m2,
        bose_quietcomfort_earbuds,
        google_pixel_7,
        NonStockedProduct("Windows License", price=125), 
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)  
    ]

    # Show the product details
    for product in product_list:
        print(product.show())  # Add parentheses to call the method

    # Create the store with the product list
    best_buy = Store(product_list)

    # Start the user interface
    start(best_buy)


if __name__ == "__main__":
    main()