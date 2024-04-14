import pytest
from main import Category, Product, Smartphone, LawnGrass


@pytest.fixture
def category_clothes():
    return Category('одежда', 'для спорта', ["топ", "леггинсы"])


def test_init(category_clothes):
    assert category_clothes.name == 'одежда'
    assert category_clothes.description == 'для спорта'
    #assert category_clothes.goods == ["топ", "леггинсы"]
    assert Category.total_categories == 1


@pytest.fixture
def product_top():
    return Product('топ', 'для занятия спортом', 599, 10, 'black')


def test_init_product(product_top):
        assert product_top.product_name == 'топ'
        assert product_top.product_description == 'для занятия спортом'
        assert product_top.price == 599
        assert product_top.amount == 10
        assert Product.total_products == 1


@pytest.fixture
def test_init_smartphone(iphone):
    """тест для инициализации класса Смартфон"""
    assert iphone.product_name == 'Iphone'
    assert iphone.product_description == 'Смартфон'
    assert iphone.price == 100000
    assert iphone.amount == 5
    assert iphone.color == 'space grey'
    assert iphone.efficiency == 'test'
    assert iphone.model == '15 Pro Max'
    assert iphone.memory == 128
    assert Product.total_products == 1


def test_init_grass(grass):
    """тест для инициализации класса трава"""
    assert grass.product_name == 'трава для газона'
    assert grass.product_description == 'для посадки'
    assert grass.price == 200
    assert grass.amount == 100
    assert grass.color == 'green'
    assert grass.origin == 'Germany'
    assert grass.ger_period == 14
    assert Product.total_products == 1


def test__add__(p1, p2):
    assert p1 == Product('watermelon', 'summer', '100', 50, 'red')
    assert p2 == Product('apple', 'russian', 40, 200, 'green')
    assert p1 + p2 == (100 * 50) + (40 * 200)
















