from products_2 import Products, NonStockedProduct, LimitedProduct
from store_2 import Store
from user_interface import start
from promotions import PercentDiscount, SecondHalfPricePromotion, ThirdOneFree


def main():
    """
    Main function to initialize products, set up store inventory, test the magic methods,
    and start the user interface.
    """

    # Initialize a few products for testing the magic methods
    macbook_air_m2 = Products("MacBook Air M2", price=1450, quantity=100)
    bose_quietcomfort_earbuds = Products("Bose QuietComfort Earbuds", price=250, quantity=500)
    google_pixel_7 = LimitedProduct("Google Pixel 7", price=500, quantity=250, maximum=1)
    windows_license = NonStockedProduct("Windows License", price=125)
    shipping = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)

    # Set up initial stock of inventory
    product_list = [
        macbook_air_m2,
        bose_quietcomfort_earbuds,
        google_pixel_7,
        windows_license,
        shipping
    ]

    # Create the store with the product list
    best_buy = Store(product_list)

    # ---------------------- Testing Magic Methods ----------------------
    print("\n--- Magic Methods Testing ---")

    # Test property validation (setting invalid price should raise an error)
    try:
        macbook_air_m2.price = -100  # This should raise a ValueError due to validation
    except ValueError as e:
        print(f"Error: {e}")  # Expected: "Price cannot be negative" or similar

    # Test the __str__ method for product representation
    print(macbook_air_m2)  # Expected: "MacBook Air M2, Price: $1450, Quantity: 100"

    # Test the comparison using > operator
    print(macbook_air_m2 > bose_quietcomfort_earbuds)  # Expected: True, as mac's price is higher

    # Test the __contains__ method to check if a product is in the store
    print(macbook_air_m2 in best_buy)   # Expected: True, as mac is in the store
    print(google_pixel_7 in best_buy)   # Expected: True, as google_pixel_7 is also in the store

    # ---------------------- Setting Up Promotions ----------------------
    print("\n--- Store Inventory with Promotions ---")

    # Create promotion catalog
    second_half_price = SecondHalfPricePromotion("Second Half Price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)  # MacBook Air M2
    product_list[1].set_promotion(third_one_free)     # Bose QuietComfort Earbuds
    product_list[3].set_promotion(thirty_percent)     # Windows License (Non-Stocked)

    # Show the product details, including promotions (using __str__ method)
    for product in product_list:
        print(product)  # Using __str__ method of Products to show product details

    # ---------------------- Start the User Interface ----------------------
    print("\n--- User Interface ---")
    start(best_buy)

if __name__ == "__main__":
    main()
    