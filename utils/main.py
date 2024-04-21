from abc import ABC, abstractmethod


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
        else:
            raise TypeError

    def __str__(self):
        return f"Название категории: {self.name}, количество продуктов: {len(self)}"

    def __len__(self):
        total = 0
        for goods in self.__goods:
            total += goods.amount
        return total

    #def get_goods(self):
        #for goods in self.__goods:
            #print(f"{goods.product_name}, {goods.price} руб. Остаток: {goods.amount} ")


class AbstractClass(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def price(self):
        pass


class Product(AbstractClass):
    product_name: str
    product_description: str
    price: float
    amount: int
    color: str
    total_products = 0

    def __init__(self, product_name, product_description, price, amount, color):
        self.product_name = product_name
        self.product_description = product_description
        self._price = price
        self.amount = amount
        self.color = color
        Product.total_products += 1

    @staticmethod
    def add_product(name, description, price, amount, color):
        return Product(name, description, price, amount, color)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, cost):
        if cost <= 0:
            print("Стоимость неверная")
        else:
            self._price = cost

    @price.deleter
    def price(self):
        print("Цена удалена")
        self._price = None

    def __str__(self):
        return f"{self.product_name}, {self._price} руб. Остаток: {self.amount}"

    def __add__(self, other):
        if type(self) == type(other):
            return (self.price * self.amount) + (other.price * other.amount)
        else:
            raise TypeError


class MixinLog:
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'Product ({Product.product_name}, {Product.product_description}, {Product.price}, {Product.amount})'


class Smartphone(Product):
    def __init__(self, product_name, product_description, price, amount, color, efficiency, model, memory):
        super().__init__(product_name, product_description, price, amount, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory


class LawnGrass(Product):
    def __init__(self, product_name, product_description, price, amount, color, origin, ger_period):
        super().__init__(product_name, product_description, price, amount, color)
        self.origin = origin
        self.ger_period = ger_period













