from visitor_pattern.visitor_pattern_framework import Visitor, ObjectStructure, DataNode


class Animal(DataNode):
    """動物類別"""
    def __init__(self, name, is_male, age, weight):
        self._name = name
        self._is_male = is_male
        self._age = age
        self._weight = weight

    def get_name(self):
        return self._name

    def is_male(self):
        return self._is_male

    def get_age(self):
        return self._age

    def get_weight(self):
        return self._weight


class Cat(Animal):
    """貓"""
    def __init__(self, name, is_male, age, weight):
        super().__init__(name, is_male, age, weight)

    def speak(self):
        print('miao~')


class Dog(Animal):
    """狗"""
    def __init__(self, name, is_male, age, weight):
        super().__init__(name, is_male, age, weight)

    def speak(self):
        print('wang~')


class GenderCounter(Visitor):
    """性別統計"""
    def __init__(self):
        self._maleCat = 0
        self._femaleCat = 0
        self._maleDog = 0
        self._femaleDog = 0

    def visit(self, data):
        if isinstance(data, Cat):
            if data.is_male():
                self._maleCat += 1
            else:
                self._femaleCat += 1
        elif isinstance(data, Dog):
            if data.is_male():
                self._maleDog += 1
            else:
                self._femaleDog += 1
        else:
            print('Not support this type.')

    def get_info(self):
        print(f'{self._maleCat}隻公貓，{self._femaleCat}隻母貓，{self._maleDog}隻公狗，{self._femaleDog}隻母狗')


class WeightCounter(Visitor):
    """體重統計"""
    def __init__(self):
        self._catNum = 0
        self._catWeight = 0
        self._dogNum = 0
        self._dogWeight = 0

    def visit(self, data):
        if isinstance(data, Cat):
            self._catNum += 1
            self._catWeight += data.get_weight()
        elif isinstance(data, Dog):
            self._dogNum += 1
            self._dogWeight += data.get_weight()
        else:
            print('Not support this type.')

    def get_info(self):
        print(f'貓的平均體重是: {self._catWeight / self._catNum}，狗的平均體重是: {self._dogWeight / self._dogNum}')


class AgeCounter(Visitor):
    """年齡統計"""
    def __init__(self):
        self._cat_max_age = 0
        self._dog_max_age = 0

    def visit(self, data):
        if isinstance(data, Cat):
            if self._cat_max_age < data.get_age():
                self._cat_max_age = data.get_age()
        elif isinstance(data, Dog):
            if self._dog_max_age < data.get_age():
                self._dog_max_age = data.get_age()
        else:
            print('Not support this type.')

    def get_info(self):
        print(f'貓的最大年齡是: {self._cat_max_age}，狗的最大年齡是: {self._dog_max_age}')


def test_animal():
    animals = ObjectStructure()
    animals.add(Cat('Cat1', True, 1, 5))
    animals.add(Cat('Cat2', True, 0.5, 4.2))
    animals.add(Cat('Cat3', False, 2, 3))
    animals.add(Dog('Dog1', True, 0.5, 8))
    animals.add(Dog('Dog2', False, 3, 21))
    animals.add(Dog('Dog3', True, 1, 52))
    animals.add(Dog('Dog4', False, 2, 25))
    gender_counter = GenderCounter()
    animals.action(gender_counter)
    gender_counter.get_info()
    print()
    weight_counter = WeightCounter()
    animals.action(weight_counter)
    weight_counter.get_info()
    print()
    age_counter = AgeCounter()
    animals.action(age_counter)
    age_counter.get_info()


test_animal()









