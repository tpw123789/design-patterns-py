class MyBeautifulGirl:
    """女"""
    _instance = None
    _is_first_init = False

    def __new__(cls, name):
        if not cls._instance:
            MyBeautifulGirl._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, name):
        if not self._is_first_init:
            self._name = name
            print(f'遇見{name}，一見鍾情')
            MyBeautifulGirl._is_first_init = True
        else:
            print(f'遇見{name}，我置若罔聞')

    def show_my_heart(self):
        print(f'{self._name}，你是唯一')


jenny = MyBeautifulGirl('Jenny')
jenny.show_my_heart()

amy = MyBeautifulGirl('Amy')
amy.show_my_heart()


