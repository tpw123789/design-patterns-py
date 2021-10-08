from abc import ABCMeta, abstractmethod


class WaterHeater:
    """Observer pattern"""
    def __init__(self):
        self._observers = []
        self._temperature = 25

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, temperature):
        self._temperature = temperature
        print("The temperature is: " + str(self._temperature))
        self.notifies()

    def add_observer(self, observer):
        self._observers.append(observer)

    def notifies(self):
        for o in self._observers:
            o.update(self)


class Observer(metaclass=ABCMeta):
    """抽象類別"""
    @abstractmethod
    def update(self, water_heater):
        pass


class WashingMode(Observer):
    """Washing mode"""
    def update(self, water_heater):
        if 50 <= water_heater.get_temperature() < 70:
            print('water is already, can take a bath now ~')


class DrinkingMode(Observer):
    """Drinking mode"""
    def update(self, water_heater):
        if water_heater.get_temperature() >= 100:
            print('water is already, can drink now ~')


heater = WaterHeater()
washing_observer = WashingMode()
drinking_observer = DrinkingMode()
heater.add_observer(washing_observer)
heater.add_observer(drinking_observer)
heater.set_temperature(40)
heater.set_temperature(60)
heater.set_temperature(100)



