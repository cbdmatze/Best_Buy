import pytest
from products_2 import Products


# Test 1: Creating a valid product and assure everything works fine
def test_create_product():
    product = Products(name="Laptop", price=1500.0, quantity=10)
    assert product.name == "Laptop"
    assert product.price == 1500.0
    assert product.quantity == 10
    assert product.is_active() == True  # Product should be active


# Test 2: Creating a product with invalid details (empty name, negative price) raises an exception
def test_invalid_product_creation():
    with pytest.raises(ValueError):
        Products(name="", price=1450.0, quantity=100)  # Empty name should raise ValueError

    with pytest.raises(ValueError):
        Products(name="MacBook Air M2", price=-10.0, quantity=100)  # Negative price should raise ValueError


# Test 3: When product reaches 0 quantity, it becomes inactive
def test_product_becomes_inactive_when_quantity_zero():
    product = Products(name="Phone", price=800.0, quantity=1)
    product.quantity = 0  # Access the quantity property directly
    assert product.is_active() == False  # Product should be inactive when quantity is 0


# Test 4: Product purchase modifies the quantity and returns the correct total price
def test_product_purchase():
    product = Products(name="Headphones", price=100.0, quantity=10)
    total_price = product.buy(3)  # Buy 3 units
    assert total_price == 300.0  # 3 * 100 = 300
    assert product.quantity == 7  # Remaining quantity should be 7


# Test 5: Buying a larger quantity than is available on stock raises an exception
def test_buying_larger_quantity_than_exists():
    product = Products(name="Monitor", price=250.0, quantity=5)
    with pytest.raises(ValueError):
        product.buy(10)  # Trying to buy more than available should raise ValueError
