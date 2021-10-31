from abc import ABCMeta, abstractmethod


class Filter(metaclass=ABCMeta):
    """篩檢模式"""
    @abstractmethod
    def do_filter(self, element):
        """過濾方法"""
        pass


class FilterChain(Filter):
    """篩檢程式鍊"""
    def __init__(self):
        self._filters = []

    def add_element(self, element):
        self._filters.append(element)

    def remove_element(self, element):
        self._filters.remove(element)

    def do_filter(self, elements):
        for element in self._filters:
            elements = element.do_filter(elements)
        return elements


class FilterScreen(Filter):
    """過濾網"""
    def do_filter(self, elements):
        for material in elements:
            if material == '豆渣':
                elements.remove(material)
        return elements
