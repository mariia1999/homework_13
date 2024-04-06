class Category:
    name: str
    description: str
    goods: []
    total_categories = 0
    unique_goods = set()

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__goods = []
        Category.total_categories += 1

    def add_unique_goods(self, goods):
        self.__goods.append(goods)
        Category.unique_goods.add(goods)

    def add_goods(self, goods):
        if isinstance(goods, Product):
            self.__goods.append(goods)

    def get_goods(self):
        for goods in self.__goods:
            print(f"{goods.product_name}, {goods.price} руб. Остаток: {goods.amount} ")


class Product:
    product_name: str
    product_description: str
    price: float
    amount: int
    total_products = 0

    def __init__(self, product_name, product_description, price, amount):
        self.product_name = product_name
        self.product_description = product_description
        self._price = price
        self.amount = amount
        Product.total_products += 1

    @staticmethod
    def add_product(name, description, price, amount):
        return Product(name, description, price, amount)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, cost):
        if cost <= 0:
            print("Стоимость неверная")
        else:
            self._price = cost








