"""Interface Segregation Principle"""
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    """脊椎動物"""
    def __init__(self, name):
        self._name = name

    def get_names(self):
        return self._name

    @abstractmethod
    def feature(self):
        pass

    @abstractmethod
    def moving(self):
        pass


class IRunnable(metaclass=ABCMeta):
    """奔跑的介面"""
    @abstractmethod
    def running(self):
        pass


class IFlyable(metaclass=ABCMeta):
    """飛行的介面"""
    @abstractmethod
    def flying(self):
        pass


class INatatory(metaclass=ABCMeta):
    """游泳介面"""
    @abstractmethod
    def swimming(self):
        pass


class MammalAnimal(Animal, IRunnable):
    """哺乳動物"""
    def __init__(self, name):
        super().__init__(name)

    def feature(self):
        print(f'{self._name}的生理特徵: 恆溫，胎生，哺乳')

    def running(self):
        print('在陸上跑...')

    def moving(self):
        print(f'{self._name}的活動方式:', end='')
        self.running()


class BirdAnimal(Animal, IFlyable):
    """鳥類動物"""
    def __init__(self, name):
        super().__init__(name)

    def feature(self):
        print(f'{self._name}的生理特徵: 恆溫，卵生，前肢成翅')

    def flying(self):
        print('在天空飛...')

    def moving(self):
        print(f'{self._name}的活動方式:', end='')
        self.flying()


class FishAnimal(Animal, INatatory):
    """魚類"""

    def __init__(self, name):
        super().__init__(name)

    def feature(self):
        print(f'{self._name}的生理特徵: 流線型體型，用鰓呼吸')

    def swimming(self):
        print('在水中游...')

    def moving(self):
        print(f'{self._name}的活動方式:', end='')
        self.swimming()


class Bat(MammalAnimal, IFlyable):
    """蝙蝠"""
    def __init__(self, name):
        super().__init__(name)

    def running(self):
        print('行為功能已經退化')

    def flying(self):
        print('在天空飛...', end='')

    def moving(self):
        print(f'{self._name}的活動方式:', end='')
        self.flying()
        self.running()


class Swan(BirdAnimal, IRunnable, INatatory):
    """天鵝"""
    def __init__(self, name):
        super().__init__(name)

    def running(self):
        print('在陸上跑...', end='')

    def swimming(self):
        print('在水中游...', end='')

    def moving(self):
        print(f'{self._name}的活動方式:', end='')
        self.running()
        self.swimming()
        self.flying()


class CrucianCarp(FishAnimal):
    """鯽魚"""
    def __init__(self, name):
        super().__init__(name)


def test_animal():
    bat = Bat('蝙蝠')
    bat.feature()
    bat.moving()
    swan = Swan('天鵝')
    swan.feature()
    swan.moving()
    crucian_carp = CrucianCarp('鯽魚')
    crucian_carp.feature()
    crucian_carp.moving()


test_animal()

