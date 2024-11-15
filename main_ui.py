from products_2 import Products, NonStockedProduct, LimitedProduct
from store_2 import Store
from user_interface import start
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree


def main():
    """
    Main function to initialize products, set up store inventory, and start the user interface.
    """

    # Initialize a few products
    macbook_air_m2 = Products("MacBook Air M2", price=1450, quantity=100)
    bose_quietcomfort_earbuds = Products("Bose QuietComfort Earbuds", price=250, quantity=500)
    google_pixel_7 = Products("Google Pixel 7", price=500, quantity=250)
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

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)  # MacBook Air M2
    product_list[1].set_promotion(third_one_free)  # Bose QuietComfort Earbuds
    product_list[3].set_promotion(thirty_percent)  # Windows License (Non-Stocked)

    # Show the product details, including promotions
    for product in product_list:
        print(product.show())

    # Create the store with the product list
    best_buy = Store(product_list)

    # Start the user interface
    start(best_buy)


if __name__ == "__main__":
    main()