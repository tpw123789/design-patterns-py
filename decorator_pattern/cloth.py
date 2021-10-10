from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    """人"""
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def wear(self):
        print('著裝: ')


class Engineer(Person):
    """工程師"""
    def __init__(self, name, skill):
        super().__init__(name)
        self._skill = skill

    def get_skill(self):
        return self._skill

    def wear(self):
        print(f'我是{self._skill}工程師{self._name}', end='，')
        super().wear()


class Teacher(Person):
    """老師"""
    def __init__(self, name, title):
        super().__init__(name)
        self._title = title

    def get_title(self):
        return self._title

    def wear(self):
        print(f'我是{self._name}{self.get_title()}', end='，')
        super().wear()


class ClothingDecorator(Person):
    """服裝裝飾器基類別"""
    def __init__(self, person):
        self._decorator = person

    def wear(self):
        self._decorator.wear()
        self.decorator()

    @abstractmethod
    def decorator(self):
        pass


class CasualPantDecorator(ClothingDecorator):
    """休閒褲裝飾器"""
    def __init__(self, person):
        super().__init__(person)

    def decorator(self):
        print('一條卡其色卡其色褲子')


class BeltDecorator(ClothingDecorator):
    """腰帶裝飾器"""
    def __init__(self, person):
        super().__init__(person)

    def decorator(self):
        print('一條銀色針扣頭的黑色腰帶')


class LeatherShoesDecorator(ClothingDecorator):
    """皮鞋裝飾器"""
    def __init__(self, person):
        super().__init__(person)

    def decorator(self):
        print('一雙深色休閒皮鞋')


class KnittedSweaterDecorator(ClothingDecorator):
    """針織毛衣裝飾器"""
    def __init__(self, person):
        super().__init__(person)

    def decorator(self):
        print('一件紫紅色針織毛衣')


class WhiteShirtDecorator(ClothingDecorator):
    """白色襯衫裝飾器"""
    def __init__(self, person):
        super().__init__(person)

    def decorator(self):
        print('一件白色襯衫')


class GlassesDecorator(ClothingDecorator):
    """眼鏡裝飾器"""
    def __init__(self, person):
        super().__init__(person)

    def decorator(self):
        print('一副黑框眼鏡')


Tony = Engineer('Tony', '軟體')
pant = CasualPantDecorator(Tony)
belt = BeltDecorator(pant)
shoes = LeatherShoesDecorator(belt)
shirt = WhiteShirtDecorator(shoes)
sweater = KnittedSweaterDecorator(shirt)
glasses = GlassesDecorator(sweater)
glasses.wear()
print()

Wells = Teacher('Wells', '教授')
pant = CasualPantDecorator(Wells)
shoes = LeatherShoesDecorator(pant)
shoes.wear()

