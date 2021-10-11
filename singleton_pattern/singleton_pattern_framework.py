class Singleton1:
    """單例實現方式"""
    _instance = None
    _is_first_init = False

    def __new__(cls, name):
        if not cls._instance:
            Singleton1._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        if not self._is_first_init:
            self._name = name
            Singleton1._is_first_init = True

    def get_name(self):
        return self._name


jack = Singleton1('Jack')
karry = Singleton1('Karry')
print(jack.get_name(), karry.get_name())
print(id(jack), id(karry))
print(jack == karry)

