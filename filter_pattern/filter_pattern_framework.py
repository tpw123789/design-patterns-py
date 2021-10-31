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

    def add_filter(self, _filter):
        self._filters.append(_filter)

    def remove_filter(self, _filter):
        self._filters.remove(_filter)

    def do_filter(self, elements):
        for _filter in self._filters:
            elements = _filter.do_filter(elements)
        return elements


class FilterScreen(Filter):
    """過濾網"""
    def do_filter(self, elements):
        for material in elements:
            if material == '豆渣':
                elements.remove(material)
        return elements
