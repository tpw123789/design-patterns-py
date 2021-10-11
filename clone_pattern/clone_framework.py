from copy import copy, deepcopy


class Clone:
    """Clone 基類別"""
    def clone(self):
        """淺拷貝clone物件"""
        return copy(self)

    def deep_clone(self):
        """深拷貝clone物件"""
        return deepcopy(self)


class Person(Clone):
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


if __name__ == '__main__':
    tony = Person('Tony', 10)
    tony.show_myself()
    tony.coding()
    tony.reading()
    tony.sleeping()

    tony1 = tony.clone()
    tony1.show_myself()
    tony1.coding()
    tony1.reading()
    tony1.sleeping()
