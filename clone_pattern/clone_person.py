from copy import copy, deepcopy


class Person:
    """人"""
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def show_myself(self):
        print(f'I am {self._name}, {self._age} years old')

    def coding(self):
        print(f'{self._name} coding now.')

    def reading(self):
        print('I am reading now.')

    def sleeping(self):
        print('I am sleeping now.')

    def clone(self):
        return copy(self)


henry = Person('Henry', 25)
henry.show_myself()
henry.coding()
henry.reading()
henry.sleeping()

peter = henry.clone()
peter.show_myself()
peter.coding()

print(id(henry), id(peter))
