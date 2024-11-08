from products import Product
from store import Store

def main():
    # Initialize a few products

    macbook_air_m2 = Product("MacBook Air M2", price=1450, quantity=100)
    bose_quietcomfort_earbuds = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    google_pixel_7 = Product("Google Pixel 7", price=500, quantity=250)

    # Create a list of products
    product_list = [macbook_air_m2, bose_quietcomfort_earbuds, google_pixel_7]
   

    # Create the store
    store = Store(product_list)

    # Get all active products in the store
    products = store.get_all_products()

    # Display total quantity of all products
    print(f"Total quantity in store: {store.get_total_quantity()}")

    # Make an order:
    try:
        total_price = store.order([(products[0], 1), (products[1], 2)])  # Buy 1 MacBook and 2 Bose Earbuds

        print(f"Order total: {total_price} dollars")
    except Exception as e:
        print(f"Error processing order {e}")

if __name__ == "__main__":
    main()