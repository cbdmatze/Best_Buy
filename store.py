from products import Products

class Store:

    def __init__(self, products):
        # Initialize the store with a list of prudocts
        self.products = products
    
    def add_product(self, product):
        # Add a new product to the store
        self.products.append(product)

    def remoce_product(self, product):
        # Remove a product from the store 
        self.products.remove(product)

    def get_total_quantity(self):
        total_quantity = sum([product.get_quantity() for product in self.products])
        return total_quantity
    
    def get_all_products(self):
        # Return a list from all active products in the store
        return [product for product in self.products if product.is_active()]
    
    def order(self, shopping_list):
        # Process the order from a list of tuples (product, quantity)
        total_price = 0
        for product, quantity in shopping_list:
            try:
                # Try buying the given quantity of the product
                total_price += product.buy(quantity)
            except Exception as e:
                print(f"Error with product {product.name}: {e}")
        return total_price
