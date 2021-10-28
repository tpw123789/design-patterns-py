from abc import ABCMeta, abstractmethod


class Flyweight(metaclass=ABCMeta):
    """享元類別"""
    @abstractmethod
    def operation(self, extrinsic_state):
        pass


class FlyweightImpl(Flyweight):
    """享元類別的具體實現類別"""
    def __init__(self, color):
        self._color = color

    def operation(self, extrinsic_state):
        print(f'{extrinsic_state}取得{self._color}色顏料')


class FlyweightFactory:
    """享元工廠"""
    def __init__(self):
        self._flyweight = {}

    def get_flyweight(self, key):
        pigment = self._flyweight.get(key)
        if pigment is None:
            pigment = FlyweightImpl(key)
        return pigment


def test_flyweight():
    factory = FlyweightFactory()
    pigment_red = factory.get_flyweight('紅')
    pigment_red.operation('中華隊')
    pigment_yellow = factory.get_flyweight('黃')
    pigment_yellow.operation('中華隊')
    pigment_blue = factory.get_flyweight('藍')
    pigment_blue.operation('中華隊')
    pigment_blue2 = factory.get_flyweight('藍')
    pigment_blue2.operation('夢之隊')


test_flyweight()

