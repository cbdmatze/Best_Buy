from products import Products

def main():
    """
    Main function to demonstrate product management and purchasing.

    This function creates two product instances (MacBook and Bose earbuds),
    attempts to purchase quantities of each, and displays relevant information
    about the products, including their availability and purchase prices.
    """

    # Create product instances
    macbook = Products("MacBook Air M2", price=1450, quantity=100)
    bose = Products("Bose Quietcomfort Earbuds", price=250, quantity=50)

    # Display initial product information
    print(macbook.show())

    # Attempt to purchase products
    try:
        macbook_purchase_quantity = 5
        total_macbook_price = macbook.buy(macbook_purchase_quantity)
        print(f"Total price for {macbook_purchase_quantity} MacBook: {total_macbook_price}")

        bose_purchase_quantity = 2
        total_bose_price = bose.buy(bose_purchase_quantity)
        print(f"Total price for {bose_purchase_quantity} Bose Earbuds: {total_bose_price}")

    except Exception as e:
        print(f"Error: {e}")

    # Display updated product information
    print(macbook.show())
    print(bose.show())

    # Check product availability
    print(f"Is the MacBook still active? {macbook.is_active()}")

    # Set MacBook quantity to 0 and check availability
    macbook.set_quantity(0)
    print(f"Is the MacBook active after setting quantity to 0? {macbook.is_active()}")
  
