"""Dependency Inversion Principle"""
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    """動物"""
    def __init__(self, name):
        self._name = name

    def eat(self, food):
        if self.check_food(food):
            print(f'{self._name}進食{food.get_name()}')
        else:
            print(f'{self._name}不吃{food.get_name()}')

    @abstractmethod
    def check_food(self, food):
        """檢查哪種食物能吃"""
        pass


class Dog(Animal):
    """狗"""
    def __init__(self):
        super().__init__('狗')

    def check_food(self, food):
        return food.category() == '肉類'


class Swallow(Animal):
    """燕子"""
    def __init__(self):
        super().__init__('燕子')

    def check_food(self, food):
        return food.category() == '昆蟲'


class Food(metaclass=ABCMeta):
    """食物"""
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    @abstractmethod
    def category(self):
        """食物類別"""
        pass

    @abstractmethod
    def nutrient(self):
        """營養成分"""
        pass


class Meat(Food):
    """肉"""
    def __init__(self):
        super().__init__('肉')

    def category(self):
        return '肉類'

    def nutrient(self):
        return '蛋白質、脂肪'


class Worm(Food):
    """蟲子"""
    def __init__(self):
        super().__init__('蟲子')

    def category(self):
        return '昆蟲'

    def nutrient(self):
        return '蛋白質含、微量元素'


def test_food():
    dog = Dog()
    swallow = Swallow()
    meat = Meat()
    worm = Worm()
    dog.eat(meat)
    dog.eat(worm)
    swallow.eat(meat)
    swallow.eat(worm)


test_food()

