from copy import deepcopy


class Memento:
    """備忘錄"""
    def set_attributes(self, dictionary):
        """深度拷貝字典中所有屬性"""
        self.__dict__ = deepcopy(dictionary)

    def get_attributes(self):
        """獲取屬性字典"""
        return self.__dict__


class Caretaker:
    """備忘錄管理類別"""
    def __init__(self):
        self._mementos = {}

    def add_memento(self, name, memento):
        self._mementos[name] = memento

    def get_memento(self, name):
        return self._mementos[name]


class Originator:
    """備份發起人"""
    def create_memento(self):
        memento = Memento()
        memento.set_attributes(self.__dict__)
        return memento

    def restore_from_memento(self, memento):
        self.__dict__.update(memento.get_attributes())





