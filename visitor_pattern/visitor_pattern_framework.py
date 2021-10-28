from abc import abstractmethod, ABCMeta


class DataNode(metaclass=ABCMeta):
    """資料結構類別"""
    def accept(self, visitor):
        """接受存取者"""
        visitor.visit(self)


class Visitor(metaclass=ABCMeta):
    """存取者"""
    @abstractmethod
    def visit(self, data):
        """對資料物件的存去操作"""
        pass


class ObjectStructure:
    """資料結構的管理類別，也是資料物件的一個容器，可遍歷容器內所有元素"""
    def __init__(self):
        self._data = []

    def add(self, data_element):
        self._data.append(data_element)

    def action(self, visitor):
        """進行資料存取的操作"""
        for data in self._data:
            data.accept(visitor)




