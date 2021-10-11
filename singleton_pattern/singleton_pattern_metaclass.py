class Singleton2(type):
    """單例實現方式2"""
    def __init__(cls, what, bases=None, dict=None):
        super().__init__(what, bases, dict)
        # 初始化全域變數為None
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, *kwargs)
        return cls._instance


class CustomClass(metaclass=Singleton2):
    """用戶自訂類別"""
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


tony = CustomClass('Tony')
karry = CustomClass('Karry')
print(tony.get_name(), karry.get_name())
print(id(tony), id(karry))
print(tony == karry)

