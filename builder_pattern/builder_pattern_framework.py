from abc import ABCMeta, abstractmethod


class Toy(metaclass=ABCMeta):
    """玩具"""
    def __init__(self, name):
        self._name = name
        self._components = []

    def get_name(self):
        return self._name

    def add_component(self, component, count=1, unit='個'):
        self._components.append([component, count, unit])

    @abstractmethod
    def feature(self):
        pass


class Car(Toy):
    """小車"""
    def feature(self):
        print(f'我是{self._name}....')


class Manor(Toy):
    """莊園"""
    def feature(self):
        print(f'我是{self._name}....')


class ToyBuilder(metaclass=ABCMeta):
    """玩具建構者"""
    @abstractmethod
    def build_product(self):
        pass


class CarBuilder(ToyBuilder):
    """車子建構類別"""
    def build_product(self):
        car = Car('迷你小車')
        print(f'正在建構{car.get_name()}....')
        car.add_component('輪子', 4)
        car.add_component('車身', 1)
        car.add_component('發動機', 1)
        car.add_component('方向盤')
        return car


class ManorBuilder(ToyBuilder):
    """莊園建構類別"""
    def build_product(self):
        manor = Manor('淘淘小莊園')
        print(f'正在建構{manor.get_name()}....')
        manor.add_component('客廳', 1, '間')
        manor.add_component('臥室', 2, '間')
        manor.add_component('書房', 1, '間')
        manor.add_component('廚房', 1, '間')
        manor.add_component('花園', 1, '間')
        manor.add_component('圍牆', 1, '堵')
        return manor


class BuilderManager:
    """建構類別的管理類別"""
    def __init__(self):
        self._car_builder = CarBuilder()
        self._manor_builder = ManorBuilder()

    def build_car(self, num):
        count = 0
        products = []
        while count < num:
            car = self._car_builder.build_product()
            products.append(car)
            count += 1
            print(f'建構完成第{count}輛{car.get_name()}')
        return products

    def build_manor(self, num):
        count = 0
        products = []
        while count < num:
            manor = self._car_builder.build_product()
            products.append(manor)
            count += 1
            print(f'建構完成第{count}輛{manor.get_name()}')
        return products


def test_advanced_builder():
    builder_manager = BuilderManager()
    builder_manager.build_manor(2)
    print()
    builder_manager.build_car(4)


test_advanced_builder()

