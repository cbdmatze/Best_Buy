
from products import Products

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
        """
        Add a new product to the store.

        Parameters:
        ----------
        product : Product
            The product to be added to the store.
        """
        self.products.append(product)

    def remove_product(self, product: Products) -> None:
        """
        Remove a product from the store.

        Parameters:
        ----------
        product : Product
            The product to be removed from the store.

        Raises:
        ------
        ValueError:
            If the product is not found in the store's product list.
        """
        try:
            self.products.remove(product)
        except ValueError:
            print(f"Product {product.name} is not in the store.")
    
    def get_total_quantity(self) -> int:
        """
        Calculate and return the total quantity of all products in the store.

        Returns:
        -------
        int
            The total quantity of all products in the store.
        """
        total_quantity = sum([product.get_quantity() for product in self.products])
        return total_quantity
    
    def get_all_products(self) -> list[Products]:
        """
        Return a list of all active products in the store.

        Returns:
        -------
        list[Product]
            A list of all active Product instances.
        """
        return [product for product in self.products if product.is_active()]
    
    def order(self, shopping_list: list[tuple[Products, int]]) -> float:
        """
        Process the order from a shopping list, which contains tuples of product
        and quantity. Returns the total price of the order.

        Parameters:
        ----------
        shopping_list : list[tuple[Product, int]]
            A list of tuples, where each tuple contains a Product and the quantity to order.

        Returns:
        -------
        float
            The total price of the order.

        Raises:
        ------
        Exception:
            If there's an error in purchasing any of the products.
        """
        total_price = 0
        for product, quantity in shopping_list:
            try:
                # Try buying the given quantity of the product
                total_price += product.buy(quantity)
            except Exception as e:
                print(f"Error with product {product.name}: {e}")
        return total_price