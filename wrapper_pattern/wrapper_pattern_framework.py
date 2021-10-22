from abc import ABCMeta, abstractmethod


class Target(metaclass=ABCMeta):
    """目標類別"""
    @abstractmethod
    def function(self):
        pass


class Adaptee:
    """源物件類別"""
    def specific_function(self):
        print('被適配物件的特殊功能')


class Adapter(Adaptee, Target):
    """適配器"""
    def function(self):
        print('進行功能的轉換')



