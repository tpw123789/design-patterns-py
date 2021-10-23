from abc import ABCMeta, abstractmethod


class Person:
    """人類別"""
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def show_myself(self):
        print(f'姓名:{self.name}，年齡:{self.age}歲，體重:{self.weight:0.2f}kg，身高:{self.height:0.2f}m。')


class ICompare(metaclass=ABCMeta):
    """比較演算法"""
    @abstractmethod
    def comparable(self, person1, person2):
        """
        if person1 > person2 return: > 0
        if person1 == person2 return: 0
        if person1 < person2 return: < 0
        """
        pass


class CompareByAge(ICompare):
    """透過年齡排序"""
    def comparable(self, person1, person2):
        return person1.age - person2.age


class CompareByHeight(ICompare):
    """透過身高排序"""
    def comparable(self, person1, person2):
        return person1.height - person2.height


class CompareByHeightAndWeight(ICompare):
    """透過身高體重加權排序"""
    def comparable(self, person1, person2):
        value1 = person1.height * 0.6 + person1.weight * 0.4
        value2 = person2.height * 0.6 + person2.weight * 0.4
        return value1 - value2


class SortPerson:
    """Person的排序類別"""
    def __init__(self, compare):
        self._compare = compare

    def sort(self, person_list):
        """氣泡排序演算法"""
        n = len(person_list)
        for i in range(n - 1):
            for j in range(n - 1):
                if self._compare.comparable(person_list[j], person_list[j + 1]) > 0:
                    tmp = person_list[j]
                    person_list[j] = person_list[j + 1]
                    person_list[j + 1] = tmp


def test_sort_person():
    person_list = [
        Person('Tony', 2, 54.5, 0.82),
        Person('Jack', 31, 74.5, 1.80),
        Person('Nick', 54, 44.5, 1.59),
        Person('Eric', 23, 62.0, 1.78),
        Person('Helen', 16, 45.7, 1.6),
    ]
    print('依身高排序:')
    height_sorter = SortPerson(CompareByHeight())
    height_sorter.sort(person_list)
    for person in person_list:
        person.show_myself()

    print()
    print('依年齡排序:')
    age_sorter = SortPerson(CompareByAge())
    age_sorter.sort(person_list)
    for person in person_list:
        person.show_myself()

    print()
    print('依身高體體重排序:')
    age_sorter = SortPerson(CompareByHeightAndWeight())
    age_sorter.sort(person_list)
    for person in person_list:
        person.show_myself()


test_sort_person()


