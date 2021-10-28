import logging


class Pigment:
    """顏料"""
    def __init__(self, color):
        self._color = color
        self._user = ''

    def get_color(self):
        return self._color

    def set_user(self, user):
        self._user = user
        return self

    def show_info(self):
        print(f'{self._user}取得{self._color}色顏料')


class PigmentFactory:
    """顏料工廠類別"""
    def __init__(self):
        self._pigment_set = {
            "紅": Pigment('紅'),
            "黃": Pigment('黃'),
            "藍": Pigment('藍'),
            "綠": Pigment('綠'),
            "紫": Pigment('紫')
        }

    def get_pigment(self, color):
        pigment = self._pigment_set.get(color)
        if pigment is None:
            logging.error(f'沒有{color}顏色的顏料!')
        return pigment


def test_pigment():
    factory = PigmentFactory()
    pigment_red = factory.get_pigment('紅')
    pigment_red.set_user('中華隊')
    pigment_red.show_info()
    pigment_blue = factory.get_pigment('藍')
    pigment_blue.set_user('中華隊')
    pigment_blue.show_info()
    pigment_yellow = factory.get_pigment('黃')
    pigment_yellow.set_user('中華隊')
    pigment_yellow.show_info()
    pigment_yellow = factory.get_pigment('黃')
    pigment_yellow.set_user('夢之隊')
    pigment_yellow.show_info()


test_pigment()

