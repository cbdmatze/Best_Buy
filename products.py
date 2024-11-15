from promotions import Promotion

class Products:
    """
    A class to represent a product in the store.

    Attributes:
    ----------
    name : str
        The name of the product.
    price : float
        The price of the product.
    quantity : int
        The current available stock of the product.
    active : bool
        Status of the product (active/inactive).
    promotion : Promotion or None
        The promotion applied to the product, if any.

    Methods:
    -------
    get_quantity():
        Returns the current quantity of the product.
    set_quantity(quantity: int):
        Sets the product's quantity, and deactivates it if the quantity reaches 0.
    is_active():
        Checks if the product is active.
    activate():
        Activates the product.
    deactivate():
        Deactivates the product.
    show():
        Returns a string representing the product's details, including promotions.
    buy(quantity: int):
        Processes the purchase of a given quantity, applies promotions (if any), reduces stock, and returns the total price.
    """

    def __init__(self, name, price, quantity):
        """
        Initialize a Product object with the given name, price, and quantity.
        The product is considered active by default unless invalid input is provided.

        Parameters:
        ----------
        name : str
            The name of the product.
        price : float
            The price of the product. Must be non-negative.
        quantity : int
            The quantity of the product in stock. Must be non-negative.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product information: Name can't be empty, price and quantity must be non-negative.")
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None  # New promotion attribute

    def set_promotion(self, promotion):
        """Assign a promotion to the product."""
        self.promotion = promotion

    def get_promotion(self):
        """Return the current promotion applied to the product."""
        return self.promotion

    def get_quantity(self):
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity of the product. If the quantity is set to 0, the product
        is deactivated.

        Parameters:
        ----------
        quantity : int
            The new quantity of the product. Must be non-negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Return True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Return a string representation of the product's details, including promotions."""
        promo_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo_info}"

    def buy(self, quantity):
        """
        Process the purchase of a given quantity of the product. If the quantity is
        valid, deduct it from stock and return the total price after applying promotions (if any).
        If the quantity is invalid or exceeds available stock, raise an exception.

        Parameters:
        ----------
        quantity : int
            The number of items to purchase. Must be positive and less than or equal to stock.

        Returns:
        -------
        total_price : float
            The total price of the purchased items, with any promotions applied.

        Raises:
        ------
        ValueError:
            If the quantity is less than or equal to 0 or exceeds available stock.
        """
        if quantity <= 0:
            raise ValueError("The quantity must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Insufficient stock available.")

        # Apply promotion if it exists
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        # Deduct the purchased quantity from the stock
        self.set_quantity(self.quantity - quantity)
        return total_price


# Class for Non-Stocked Products
class NonStockedProduct(Products):
    """
    A class for non-stocked products (e.g., digital products like software licenses):
    These products always have a quantity of zero.
    """
    def __init__(self, name, price):
        super().__init__(name, price, 0)  # Quantity is always 0
    
    def set_quantity(self, quantity):
        """Non-stocked products cannot have a quantity other than 0."""
        raise ValueError("Non-stocked products cannot have a quantity.")
    
    def show(self):
        """Return a string representation of the non-stocked product."""
        promo_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name} (Non-Stocked), Price: {self.price}{promo_info}"


# Class for Limited Products
class LimitedProduct(Products):
    """
    A class for products that have a limit on how many can be purchased in a single order.
    For example, shipping fee can only be added once.
    """
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum  # Maximum allowed to purchase in a single order
    
    def buy(self, quantity):
        """Override the buy method to enforce a maximum purchase limit."""
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} units of {self.name} in a single order.")
        return super().buy(quantity)
    
    def show(self):
        """Return a string representation of the limited product."""
        promo_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name} (Limited, Max: {self.maximum} per order), Price: {self.price}, Quantity: {self.quantity}{promo_info}"