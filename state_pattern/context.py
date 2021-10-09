from abc import ABCMeta, abstractmethod


class Context(metaclass=ABCMeta):
    """狀態模式下的上下文環境類別"""
    def __init__(self):
        self._states = []
        self._cur_state = None
        # 狀態環境發生變化依賴的屬性
        self._state_info = 0

    def add_state(self, state):
        if state not in self._states:
            self._states.append(state)

    def change_state(self, state):
        if state is None:
            return False
        if self._cur_state is None:
            print(f'初始化為{state.get_name()}')
        else:
            print(f'由{self._cur_state.get_name()}變為{state.get_name()}')
        self._cur_state = state
        return True

    def get_state(self):
        return self._cur_state

    def _set_state_info(self, state_info):
        self._state_info = state_info
        for state in self._states:
            if state.is_match(state_info):
                self.change_state(state)

    def _get_state_info(self):
        return self._state_info


class State:
    """狀態的基類別"""
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def is_match(self, state_info):
        """狀態屬性"""
        return False

    @abstractmethod
    def behavior(self, context):
        pass


class Water(Context):
    """水H2O"""
    def __init__(self):
        super().__init__()
        self.add_state(SolidState('固態'))
        self.add_state(LiquidState('液態'))
        self.add_state(GaseousState('氣態'))
        self.set_temperature(25)

    def get_temperature(self):
        return self._get_state_info()

    def set_temperature(self, temperature):
        self._set_state_info(temperature)

    def raise_temperature(self, step):
        self.set_temperature(self.get_temperature() + step)

    def reduce_temperature(self, step):
        self.set_temperature(self.get_temperature() + step)

    def behavior(self):
        state = self.get_state()
        if isinstance(state, State):
            state.behavior(self)


def singleton(cls, *args, **kwargs):
    """建構單例裝飾器"""
    instance = {}

    def _singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton


@singleton
class SolidState(State):
    """固態"""
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info < 0

    def behavior(self, context):
        print(f'溫度{context._get_state_info()}')


@singleton
class LiquidState(State):
    """液態"""
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return 0 <= state_info < 100

    def behavior(self, context):
        print(f'溫度{context._get_state_info()}')


@singleton
class GaseousState(State):
    """氣態"""
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info >= 100

    def behavior(self, context):
        print(f'溫度{context._get_state_info()}')


drink = Water()
drink.behavior()
drink.set_temperature(-4)
drink.behavior()
drink.raise_temperature(18)
drink.behavior()
drink.raise_temperature(101)
drink.behavior()



