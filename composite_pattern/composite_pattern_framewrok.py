from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):
    """組件"""
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def is_composite(self):
        return False

    @abstractmethod
    def feature(self, indent):
        """indent: 用於輸出的縮進"""
        pass


class Composite(Component):
    """複合組件"""
    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def add_component(self, component):
        self._components.append(component)

    def remove_component(self, component):
        self._components.remove(component)

    def is_composite(self):
        return True

    def feature(self, indent):
        indent += '\t'
        for component in self._components:
            print(indent, end='')
            component.feature(indent)


