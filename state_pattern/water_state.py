from abc import ABCMeta, abstractmethod


class Water:
    """水"""
    def __init__(self, state):
        self._temperature = 25
        self._state = state

    def set_state(self, state):
        self._state = state

    def change_state(self, state):
        if self._state:
            print(f'由{self._state.get_name()}變成{state.get_name()}')
        else:
            print(f'初始化為{state.get_name()}')
        self._state = state

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, temperature):
        self._temperature = temperature
        if self._temperature <= 0:
            self.change_state(SolidState('固態'))
        elif self._temperature <= 100:
            self.change_state(LiquidState('液態'))
        else:
            self.change_state(GaseousState('氣態'))

    def raise_temperature(self, step):
        self.set_temperature(self._temperature + step)

    def reduce_temperature(self, step):
        self.set_temperature(self._temperature - step)

    def behaviour(self):
        self._state.behaviour(self)


class State(metaclass=ABCMeta):
    """狀態類別"""
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    @abstractmethod
    def behaviour(self, water):
        """不同狀態下的行為"""
        pass


class SolidState(State):
    def __init__(self, name):
        super().__init__(name)

    def behaviour(self, water):
        print(f'固態 當前溫度{str(water.get_temperature())}度')


class LiquidState(State):
    def __init__(self, name):
        super().__init__(name)

    def behaviour(self, water):
        print(f'液態 當前溫度{str(water.get_temperature())}度')


class GaseousState(State):
    def __init__(self, name):
        super().__init__(name)

    def behaviour(self, water):
        print(f'氣態 當前溫度{str(water.get_temperature())}度')


drinkState = LiquidState('液態')
drink = Water(drinkState)
drink.behaviour()
drink.set_temperature(-4)
drink.behaviour()
drink.raise_temperature(18)
drink.behaviour()
drink.raise_temperature(110)
drink.behaviour()

