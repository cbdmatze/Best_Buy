from products import Products
from store import Store


def main() -> None:
    """
    Main function to initialize products, create a store, display total quantity, and make an order.
    """
    # Initialize a few products
    macbook_air_m2 = Products("MacBook Air M2", price=1450, quantity=100)
    bose_quietcomfort_earbuds = Products("Bose QuietComfort Earbuds", price=250, quantity=500)
    google_pixel_7 = Products("Google Pixel 7", price=500, quantity=250)

    # Create a list of products
    product_list = [macbook_air_m2, bose_quietcomfort_earbuds, google_pixel_7]

    # Create the store
    store = Store(product_list)

    # Get all active products in the store
    products = store.get_all_products()

    # Display total quantity of all products in the store
    total_quantity = store.get_total_quantity()
    print(f"Total quantity in store: {total_quantity}")

    # Make an order:
    try:
        # Buying 1 MacBook and 2 Bose Earbuds
        total_price = store.order([(products[0], 1), (products[1], 2)])
        print(f"Order total: {total_price} dollars")
    except Exception as e:
        print(f"Error processing order: {e}")


if __name__ == "__main__":
    main()
