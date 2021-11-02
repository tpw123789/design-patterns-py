"""Open Close Principle"""
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    """動物"""
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def moving(self):
        pass


class TerrestrialAnimal(Animal):
    """陸生生物"""
    def __init__(self, name):
        super().__init__(name)

    def moving(self):
        print(f'{self._name}在陸上跑...')


class AquaticAnimal(Animal):
    """水中生物"""
    def __init__(self, name):
        super().__init__(name)

    def moving(self):
        print(f'{self._name}在水中游...')


class BirdAnimal(Animal):
    """鳥類"""
    def __init__(self, name):
        super().__init__(name)

    def moving(self):
        print(f'{self._name}在空中飛...')


class Zoo:
    """動物園"""
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def display_activity(self):
        print('觀察每一種動物活動方式:')
        for animal in self._animals:
            animal.moving()


def test_zoo():
    zoo = Zoo()
    zoo.add_animal(TerrestrialAnimal('狗'))
    zoo.add_animal(AquaticAnimal('魚'))
    zoo.add_animal(BirdAnimal('鳥'))
    zoo.display_activity()


# test_zoo()
