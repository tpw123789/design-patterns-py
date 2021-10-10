class ClassDecorator:
    """類別裝飾器，紀錄一個類別被產生實體的次數"""
    def __init__(self, func):
        self._numCall = 0
        self._func = func

    def __call__(self, *args, **kwargs):
        self._numCall += 1
        obj = self._func(*args, **kwargs)
        print(f'創建{self._func.__name__}的第{self._numCall}個實例: {id(obj)}')
        return obj


@ClassDecorator
class MyClass:
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name


tony = MyClass('Tony')
karry = MyClass('Karry')
print(id(tony))
print(id(karry))
