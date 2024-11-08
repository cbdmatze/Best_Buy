from products import Products

def main():
    # Create a new product
    macbook = Products("MacBook Air M2", price=1450, quantity=100)
    bose = Products("Bose Quietcomfort Earbuds", price=250, quantity=50)

    # Display product information
    print(macbook.show())

    # Try buying 5 Macbook
    try:
        macbook_purchase_quantity = 5
        total_purchase_price_macbook = macbook.buy(macbook_purchase_quantity)
        print(f"Total price for {macbook_purchase_quantity} MacBook: {total_purchase_price_macbook}")

        bose_purchase_quantity = 2
        total_purchase_price_bose = bose.buy(bose_purchase_quantity)
        print(f"Total price for {bose_purchase_quantity} Bose Earbuds: {total_purchase_price_bose}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Display updated product information after purchase
    print(macbook.show())
    print(bose.show())

    # Check if the product is still active
    print(f"Is the product active? {macbook.is_active()}")

    # Set quantitiy to 0 and check status
    macbook.set_quantity(0)
    print(f"Is the pruduct active after setting quantity to 0? {macbook.is_active()}")

if __name__ == "__main__":
    main()