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
        print(f'{self._name}增加了{count}{unit}{component}')

    @abstractmethod
    def feature(self):
        pass


class Car(Toy):
    """小車"""
    def feature(self):
        print(f'我是{self._name}，我可以快速奔跑....')


class Manor(Toy):
    """莊園"""
    def feature(self):
        print(f'我是{self._name}，我可以供欣賞，也可以用來遊玩!')


class ToyBuilder:
    """玩具建構者"""
    def build_car(self):
        car = Car('迷你小車')
        print(f'正在建構{car.get_name()}....')
        car.add_component('輪子', 4)
        car.add_component('車身', 1)
        car.add_component('發動機', 1)
        car.add_component('方向盤')
        return car

    def build_manor(self):
        manor = Manor('淘淘小莊園')
        print(f'正在建構{manor.get_name()}....')
        manor.add_component('客廳', 1, '間')
        manor.add_component('臥室', 2, '間')
        manor.add_component('書房', 1, '間')
        manor.add_component('廚房', 1, '間')
        manor.add_component('花園', 1, '間')
        manor.add_component('圍牆', 1, '堵')
        return manor


def test_builder():
    builder = ToyBuilder()
    car = builder.build_car()
    car.feature()
    print()
    manor = builder.build_manor()
    manor.feature()


test_builder()


