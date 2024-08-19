import pytest
from src.product_category import Product, Category

def test_create_product():
    product = Product(name="Phone", description="A smartphone", price=699.99, quantity=5)
    assert product.name == "Phone"
    assert product.description == "A smartphone"
    assert product.price == 699.99
    assert product.quantity == 5

def test_create_category():
    category = Category(name="Electronics", description="Electronic items")
    assert category.name == "Electronics"
    assert category.description == "Electronic items"
    assert len(category.products) == 0
    assert Category.total_categories == 1

def test_category_with_products():
    product1 = Product(name="Phone", description="A smartphone", price=699.99, quantity=5)
    product2 = Product(name="Tablet", description="A tablet", price=399.99, quantity=3)
    category = Category(name="Gadgets", description="Various gadgets", products=[product1, product2])
    assert len(category.products) == 2
    assert Category.total_products == 2

