def singleton_decorator(cls, *args, **kwargs):
    """define a singleton decorator"""
    _instance = {}

    def wrapper_singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return wrapper_singleton


@singleton_decorator
class MyBeautifulGirl:
    """女神"""
    def __init__(self, name):
        self._name = name
        if self._name == name:
            print(f'遇見{name}我一件鍾情')
        else:
            print(f'遇見{name}我置若罔聞')

    def show_my_heart(self):
        print(f'{self._name}是我唯一')


jenny = MyBeautifulGirl('Jenny')
jenny.show_my_heart()
amy = MyBeautifulGirl('amy')
amy.show_my_heart()

