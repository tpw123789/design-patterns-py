

def is_even_num(num):
    return num % 2 == 0


def is_greater_than_ten(num):
    return num > 10


def get_result_num(func, elements):
    new_list = []
    for item in elements:
        if func(item):
            new_list.append(item)
    return new_list


def test_callback():
    elements = [2, 3, 6, 9, 12, 15, 18]
    list1 = get_result_num(is_even_num, elements)
    list2 = get_result_num(is_greater_than_ten, elements)
    print('所有的偶數:', list1)
    print('大於10的數:', list2)


test_callback()

