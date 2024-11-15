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
    is_active():
        Checks if the product is active.
    activate():
        Activates the product.
    deactivate():
        Deactivates the product.
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
            raise ValueError("Invalid product information: Name can't be empty, price and quantity must be non-negrative.")
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def set_promotion(self, promotion):
        """Assign a promotion to the product."""
        self.promotion = promotion
    
    def get_promotion(self):
        """Retrun the current promotion apolied to the product."""
        return self.promotion
    
    @property
    def quantity(self):
        """Property for quantity of the product."""
        return self._quantity
    
    @quantity.setter
    def quantity(self, quantity):
        """Set the quantity and deactivate the product if quantity reaches zero."""
        if quantity < 0:
            raise ValueError("Quantity cannot be neagative.")
        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()

    @property
    def price(self):
        """Property for the price of the product."""
        return self._price
    
    @price.setter
    def price(self, price):
        """Set the price for the product."""
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self._price = price
    
    def is_active(self):
        """Return True if the product is active, otherwise False."""
        return self.active
    
