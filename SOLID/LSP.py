"""Liskov Substitution Principle"""
from SOLID.OCP import BirdAnimal, TerrestrialAnimal, AquaticAnimal


class Monkey(TerrestrialAnimal):
    """猴子"""
    def __init__(self, name):
        super().__init__(name)

    def climbing(self):
        print(f'{self._name}在爬樹，動作輕盈...')


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

    def monkey_climbing(self, monkey):
        monkey.climbing()


def test_zoo():
    zoo = Zoo()
    zoo.add_animal(TerrestrialAnimal('狗'))
    zoo.add_animal(AquaticAnimal('魚'))
    zoo.add_animal(BirdAnimal('鳥'))
    zoo.display_activity()
    monkey = Monkey('猴子')
    zoo.add_animal(monkey)
    zoo.display_activity()
    print()
    print('以下猴子:')
    zoo.monkey_climbing(monkey)


test_zoo()
