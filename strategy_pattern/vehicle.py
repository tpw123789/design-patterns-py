from abc import ABCMeta, abstractmethod


class IVehicle(metaclass=ABCMeta):
    """交通工具的抽象類別"""
    @abstractmethod
    def running(self):
        pass


class SharedBicycle(IVehicle):
    """共用單車"""
    def running(self):
        print('騎共用單車', end='')


class ExpressBuss(IVehicle):
    """快速公車"""
    def running(self):
        print('搭快速公車', end='')


class Express(IVehicle):
    """快車"""
    def running(self):
        print('搭快車', end='')


class Subway(IVehicle):
    """地鐵"""
    def running(self):
        print('搭地鐵', end='')


class ClassMate:
    """聚餐同學"""
    def __init__(self, name, vehicle):
        self._name = name
        self._vehicle = vehicle

    def attend_the_dinner(self):
        print(f'{self._name} ', end='')
        self._vehicle.running()
        print('來聚餐')


def test_the_dinner():
    shared_bicycle = SharedBicycle()
    joe = ClassMate('Joe', Subway())
    joe.attend_the_dinner()
    helen = ClassMate('Helen', SharedBicycle())
    helen.attend_the_dinner()
    henry = ClassMate('Henry', ExpressBuss())
    henry.attend_the_dinner()
    ruby = ClassMate('Ruby', Express())
    ruby.attend_the_dinner()


test_the_dinner()
