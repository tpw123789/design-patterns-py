def singleton_decorator(cls, *args, **kwargs):
    """定義單利裝飾器"""
    instance = {}

    def wrapper_singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper_singleton


@singleton_decorator
class Singleton3:
    """使用單例裝飾器修飾一個類別"""
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


tony = Singleton3('Tony')
karry = Singleton3('Karry')
print(id(tony), id(karry))
print(tony.get_name(), karry.get_name())
print(tony == karry)

