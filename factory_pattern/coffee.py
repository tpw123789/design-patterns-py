from abc import ABCMeta, abstractmethod


class Coffee(metaclass=ABCMeta):
    """咖啡"""
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    @abstractmethod
    def get_taste(self):
        pass


class LatteCoffee(Coffee):
    """拿鐵咖啡"""
    def __init__(self, name):
        super().__init__(name)

    def get_taste(self):
        return '輕柔而香醇'


class MochaCoffee(Coffee):
    """摩卡咖啡"""
    def __init__(self, name):
        super().__init__(name)

    def get_taste(self):
        return '絲滑與醇厚'


class CoffeeMaker:
    """咖啡機"""
    @staticmethod
    def make_coffee(coffee_bean):
        if coffee_bean == '拿鐵咖啡豆':
            coffee = LatteCoffee('拿鐵咖啡')
        elif coffee_bean == '摩卡咖啡豆':
            coffee = MochaCoffee('摩卡咖啡')
        else:
            raise ValueError(f'不支持的參數:{coffee_bean}')
        return coffee


def test_coffee_maker():
    latte = CoffeeMaker.make_coffee('拿鐵咖啡豆')
    print(f'{latte.get_name()}準備好了，口感:{latte.get_taste()}')
    mocha = CoffeeMaker.make_coffee('摩卡咖啡豆')
    print(f'{mocha.get_name()}準備好了，口感:{mocha.get_taste()}')


test_coffee_maker()




