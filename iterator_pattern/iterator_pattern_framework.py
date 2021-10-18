

class BaseIterator:
    """反覆運算器"""
    def __init__(self, data):
        self._data = data
        self._curIdx = -1

    def to_begin(self):
        """將指針移至起始點位置"""
        self._curIdx = -1

    def to_end(self):
        """將指針移至起結尾位置"""
        self._curIdx = len(self._data)

    def next(self):
        """移動至下一個元素"""
        if self._curIdx < len(self._data) - 1:
            self._curIdx += 1
            return True
        else:
            return False

    def previous(self):
        """移動到上一個元素"""
        if self._curIdx > 0:
            self._curIdx -= 1
            return True
        else:
            return False

    def current(self):
        """獲取當前的元素"""
        if len(self._data) > self._curIdx >= 0:
            return self._data[self._curIdx]
        else:
            return None


def test_base_iterator():
    print('從前往後遍歷')
    iterator = BaseIterator(range(0, 10))
    while iterator.next():
        customer = iterator.current()
        print(customer, end='\t')
    print()
    print('從後往前遍歷')
    iterator = BaseIterator(range(0, 10))
    iterator.to_end()
    while iterator.previous():
        customer = iterator.current()
        print(customer, end='\t')


test_base_iterator()



