"""Single Responsibility Principle"""


class TerrestrialAnimal:
    """陸地生物"""
    def __init__(self, name):
        self._name = name

    def running(self):
        print(f'{self._name}陸上跑')


class AquaticAnimal:
    """水中生物"""
    def __init__(self, name):
        self._name = name

    def swimming(self):
        print(f'{self._name}水中游')


TerrestrialAnimal('狗').running()
AquaticAnimal('魚').swimming()
