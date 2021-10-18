from collections.abc import Iterable, Iterator


class NumberSequence:
    """生成間隔為step得數位系列"""
    def __init__(self, init, step, max_num=100):
        self._data = init
        self._step = step
        self._max_num = max_num

    def __iter__(self):
        return self

    def __next__(self):
        if self._data < self._max_num:
            tmp = self._data
            self._data += self._step
            return tmp
        else:
            raise StopIteration


def test_number_sequence():
    number_sequence = NumberSequence(0, 5, 20)
    print(isinstance(number_sequence, Iterator))
    print(isinstance(number_sequence, Iterable))
    for n in number_sequence:
        print(n, end='\t')


test_number_sequence()
