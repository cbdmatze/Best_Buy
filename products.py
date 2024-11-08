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
        Returns a string representing the product's details.
    buy(quantity: int):
        Processes the purchase of a given quantity, reduces stock, and returns the total price.
    """

    def __init__(self, name: str, price: float, quantity: int):
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

    def get_quantity(self) -> int:
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
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

    def is_active(self) -> bool:
        """Return True if the product is active, otherwise False."""
        return self.active

    def activate(self) -> None:
        """Activate the product."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivate the product."""
        self.active = False

    def show(self) -> str:
        """Return a string representation of the product's details."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Process the purchase of a given quantity of the product. If the quantity is
        valid, deduct it from stock and return the total price. If the quantity is invalid
        or exceeds available stock, raise an exception.

        Parameters:
        ----------
        quantity : int
            The number of items to purchase. Must be positive and less than or equal to stock.

        Returns:
        -------
        total_price : float
            The total price of the purchased items.

        Raises:
        ------
        ValueError:
            If the quantity is less than or equal to 0 or exceeds available stock.
        """
        if quantity <= 0:
            raise ValueError("The quantity must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Insufficient stock available.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)  # Update the quantity after purchase
        return total_price