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





