from products import Product

def main():
    # Create a new product
    macbook = Product("MacBook Air M2", 1450, 100)

    # Display product information
    print(macbook.show())

    # Try buying 5 Macbook
    try:
        total_price = macbook.buy(5)
        print(f"Total price for 5 MacBook: {total_price}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Display updated product information after purchase
    print(macbook.show())

    # Check if the product is still active
    print(f"Is the product active? {macbook.is_active()}")

    # Set quantitiy to 0 and check status
    macbook.set_quantity(0)
    print(f"Is the pruduct active after setting quantity to 0? {macbook.is_active()}")

if __name__ == "__main__":
    main()