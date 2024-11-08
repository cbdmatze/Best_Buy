class Product:
    
    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize the product with a name, price, and quantity.
        The product is active by default if valid input is provided.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product information: Name can't be empty, price and quantity must be non-negative.")
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Return the current quantity of the product."""
        return self.quantity
    
    def set_quantity(self, quantity: int):
        """Sets the quantity of the product: If it reaches 0, deactivates the product."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
    
    def is_active(self):
        """Check if the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False
    
    def show(self):
        """Returns a string representing the products information."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
    
    def buy(self, quantity: int):
        """
        Processes the purchase of a given quantita of the product.
        Returns the total price for the purchase. if the quantitiy is invalid or 
        exceeds available stock, raises an exception.
        """
        if quantity <= 0:
            raise ValueError("The quantity must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Insufficient stock available.")
        
        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity) # Update the quantity after purchase
        return total_price
