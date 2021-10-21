class B:
    def __new__(cls):
        print("new a class object")
        self = 3
        # print(cls)
        return self

    def __init__(self):
        print("class b")
        print(self)


class BaseClass(object):
    def __init__(self):
        pass

    def __new__(cls):
        self = super().__new__(cls)
        return self


from collections import defaultdict
from collections import Counter
a_str = 'abcaaabccabaddeae'
counter = Counter(a_str) # 可直接由初始化的方式統計個數
print(counter)
print(counter.most_common(3)) # 輸出最常出現的3個元素
print(counter['a'])
print(counter['z']) # 對於不存在的key值給出default值0

counter.update('aaeebbc') # 可用update的方式繼續統計個數
print(counter)



