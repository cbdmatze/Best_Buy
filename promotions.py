from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        # Apply percent discount to the total price
        discount_price = product.price * (1 - self.percent / 100)
        return discount_price * quantity


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        # For every two items, the second one is half price
        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        # For every three items, one is for free
        paid_quantity = quantity - (quantity // 3)
        return paid_quantity * product.price