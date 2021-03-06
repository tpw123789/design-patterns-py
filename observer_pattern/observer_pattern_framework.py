from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """觀察者的基類別"""
    @abstractmethod
    def update(self, observer, obj):
        pass


class Observable:
    """被觀察者的基類別"""
    def __init__(self):
        self._observer = []

    def add_observer(self, observer):
        self._observer.append(observer)

    def remove_observer(self, observer):
        self._observer.remove(observer)

    def notify_observers(self, obj=0):
        for o in self._observer:
            o.update(self, obj)



