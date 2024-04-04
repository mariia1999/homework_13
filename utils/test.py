import pytest
from main import Product


@pytest.fixture
def product_top():
    return Product('топ', 'для занятия спортом', 599, 10)


def test_init(product_top):
        assert product_top.product_name == 'топ'
        assert product_top.product_description == 'для занятия спортом'
        assert product_top.price == 599
        assert product_top.amount == 10
        assert Product.total_products == 1

