from abc import ABCMeta, abstractmethod
from observer_pattern.observer_pattern_framework import Observer, Observable


class WaterHeater(Observable):
    def __init__(self):
        super().__init__()
        self._temperature = 25

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, temperature):
        self._temperature = temperature
        print('the temperature is: ', str(self._temperature))
        self.notify_observers()


class WashingMode(Observer):
    """Washing mode"""
    def update(self, observer, num):
        if isinstance(observer, WaterHeater) and 50 <= observer.get_temperature() < 70:
            print('water is already, can wash ~')


class DrinkingMode(Observer):
    """Drinking mode"""
    def update(self, observer, num):
        if isinstance(observer, WaterHeater) and observer.get_temperature() >= 100:
            print('water is already, can drink ~')


heater = WaterHeater()
washing_observer = WashingMode()
drinking_observer = DrinkingMode()
heater.add_observer(washing_observer)
heater.add_observer(drinking_observer)
heater.set_temperature(40)
heater.set_temperature(60)
heater.set_temperature(100)

