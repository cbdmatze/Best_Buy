from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for product promotions.

    Attributes:
    ----------
    name : str
        The name of the promotion.
    
    Methods:
    -------
    apply_promotion(product, quantity):
        Abstract method to apply the promotion on a product based on the quantity purchased.
    """

    def __init__(self, name):
        """
        Initialize a promotion with a name.

        Parameters:
        ----------
        name : str
            The name of the promotion.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Abstract method to apply the promotion on a product.

        Parameters:
        ----------
        product : Products
            The product to which the promotion is applied.
        quantity : int
            The number of units being purchased.

        Returns:
        -------
        float
            The total price after the promotion is applied.
        """
        pass


class PercentDiscount(Promotion):
    """
    A promotion that applies a percentage discount to the total price.

    Attributes:
    ----------
    name : str
        The name of the promotion.
    percent : float
        The percentage of the discount.

    Methods:
    -------
    apply_promotion(product, quantity):
        Apply the percentage discount to the total price for the specified quantity.
    """

    def __init__(self, name, percent):
        """
        Initialize the percent discount promotion.

        Parameters:
        ----------
        name : str
            The name of the promotion.
        percent : float
            The percentage discount (must be between 0 and 100).
        """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
        Apply the percent discount to the total price.

        Parameters:
        ----------
        product : Products
            The product to which the promotion is applied.
        quantity : int
            The number of units being purchased.

        Returns:
        -------
        float
            The total price after the percentage discount is applied.
        """
        discount_price = product.price * (1 - self.percent / 100)
        return discount_price * quantity


class SecondHalfPricePromotion(Promotion):
    """
    A promotion where the second item is half price for every two items.

    Attributes:
    ----------
    name : str
        The name of the promotion.

    Methods:
    -------
    apply_promotion(product, quantity):
        Apply the 'Second Half Price' promotion to the total price for the specified quantity.
    """

    def __init__(self, name="Second Half Price"):
        """
        Initialize the 'Second Half Price' promotion.

        Parameters:
        ----------
        name : str
            The name of the promotion (default is 'Second Half Price').
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Apply the 'Second Half Price' promotion to the total price.

        For every two items, the second one is half price. If only one item is purchased,
        no promotion is applied.

        Parameters:
        ----------
        product : Products
            The product to which the promotion is applied.
        quantity : int
            The number of units being purchased.

        Returns:
        -------
        float
            The total price after the promotion is applied.
        """
        if quantity == 1:
            # No discount when only one item is purchased
            return product.price
        else:
            # For every two items, the second one is half price
            full_price_items = quantity // 2
            discounted_items = quantity - full_price_items
            total_price = (full_price_items * product.price) + (discounted_items * product.price * 0.5)
            return total_price


class ThirdOneFree(Promotion):
    """
    A promotion where every third item is free.

    Attributes:
    ----------
    name : str
        The name of the promotion.

    Methods:
    -------
    apply_promotion(product, quantity):
        Apply the 'Third One Free' promotion to the total price for the specified quantity.
    """

    def __init__(self, name="Third One Free"):
        """
        Initialize the 'Third One Free' promotion.

        Parameters:
        ----------
        name : str
            The name of the promotion (default is 'Third One Free').
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Apply the 'Third One Free' promotion to the total price.

        For every three items, one is free. This applies to as many multiples of three
        as are purchased.

        Parameters:
        ----------
        product : Products
            The product to which the promotion is applied.
        quantity : int
            The number of units being purchased.

        Returns:
        -------
        float
            The total price after the promotion is applied.
        """
        paid_quantity = quantity - (quantity // 3)
        return paid_quantity * product.price