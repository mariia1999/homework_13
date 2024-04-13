import pytest
from main import Category


@pytest.fixture
def category_clothes():
    return Category('одежда', 'для спорта', ["топ", "леггинсы"])


def test_init(category_clothes):
    assert category_clothes.name == 'одежда'
    assert category_clothes.description == 'для спорта'
    assert category_clothes.goods == ["топ", "леггинсы"]
    assert Category.total_categories == 1










