class Category:
    name: str
    description: str
    goods: []
    total_categories = 0
    unique_goods = set()

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods
        Category.total_categories += 1

    def add_goods(self, goods):
        self.goods.append(goods)
        Category.unique_goods.add(goods)


class Product:
    product_name: str
    product_description: str
    price: float
    amount: int
    total_products = 0

    def __init__(self, product_name, product_description, price, amount):
        self.product_name = product_name
        self.product_description = product_description
        self.price = price
        self.amount = amount
        Product.total_products += 1








