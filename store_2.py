from products_2 import Products

class Store:
    """
    A class to represent a store that holds and manages multiple products.

    Attributes:
    ----------
    products : list
        A list of Product instances available in the store.

    Methods:
    -------
    add_product(product: Product) -> None:
        Adds a new product to the store.
    remove_product(product: Product) -> None:
        Removes an existing product from the store.
    get_total_quantity() -> int:
        Returns the total quantity of all products in the store.
    get_all_products() -> list:
        Returns a list of all active products in the store.
    order(shopping_list: list[tuple[Product, int]]) -> float:
        Processes the order for multiple products, returning the total cost.
    """

    def __init__(self, products: list[Products]):
        """
        Initialize the store with a list of Product instances.

        Parameters:
        ----------
        products : list
            A list of Product instances to initialize the store.
        """
        self.products = products
    
    def add_product(self, product: Products) -> None:
        """Add a new product to the store."""
        self.products.append(product)

    def remove_product(self, product: Products) -> None:
        """Remove a product from the store."""
        try:
            self.products.remove(product)
        except ValueError:
            print(f"Product {product.name} is not in the store.")
    
    def get_total_quantity(self) -> int:
        """Return the total quantity of all products in the store."""
        return sum([product.quantity for product in self.products])
    
    def get_all_products(self) -> list:
        """Return a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]
    
    def order(self, shopping_list: list[tuple[Products, int]]) -> float:
        """Process the order and return the total price."""
        total_price = 0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
            except Exception as e:
                print(f"Error with product {product.name}: {e}")
        return total_price

    def __str__(self):
        """Return a string representation of the store's products."""
        return "\n".join([str(product) for product in self.products])

    def __contains__(self, product):
        """Check if a product is in the store."""
        return product in self.products

    def __add__(self, other_store):
        """Combine two stores into a new one by adding their products."""
        if isinstance(other_store, Store):
            combined_products = self.products + other_store.products
            return Store(combined_products)
        return NotImplemented