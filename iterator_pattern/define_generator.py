from collections.abc import Iterable, Iterator

# 1
gen = (x * x for x in range(10))


# 2
def fibonacci(max_num):
    a = b = 1
    for i in range(max_num):
        yield a
        a, b = b, a + b


def test_next_item():
    item_list = [1, 2, 6]
    item_iter = iter(item_list)
    print(item_iter)


test_next_item()

