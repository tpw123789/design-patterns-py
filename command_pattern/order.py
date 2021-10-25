from abc import ABCMeta, abstractmethod


class Chef:
    """廚師"""
    def steam_food(self, origin_material):
        print(f'{origin_material}清蒸中...')
        return '清蒸' + origin_material

    def stir_fried_food(self, origin_material):
        print(f'{origin_material}爆炒中...')
        return '香辣炒' + origin_material


class Order(metaclass=ABCMeta):
    """訂單"""
    def __init__(self, name, origin_material):
        self._chef = Chef()
        self._name = name
        self._origin_material = origin_material

    def get_display_name(self):
        return self._name + self._origin_material

    @abstractmethod
    def processing_order(self):
        pass


class SteamedOrder(Order):
    """清蒸"""
    def __init__(self, origin_material):
        super().__init__('清蒸', origin_material)

    def processing_order(self):
        if self._chef is not None:
            return self._chef.steam_food(self._origin_material)
        return ''


class SpicyOrder(Order):
    """香辣炒"""
    def __init__(self, origin_material):
        super().__init__('香辣炒', origin_material)

    def processing_order(self):
        if self._chef is not None:
            return self._chef.stir_fried_food(self._origin_material)
        return ''


class Waiter:
    """服務員"""
    def __init__(self, name):
        self._name = name
        self._order = None

    def receive_order(self, order):
        self._order = order
        print(f'服務員{self._name}: 您的餐{order.get_display_name()}已經準備好，請您慢用!')

    def place_order(self):
        food = self._order.processing_order()
        print(f'服務員{self._name}: 您的餐{food}已經準備好，請您慢用!')


def test_order():
    waiter = Waiter('Anna')
    steamed_order = SteamedOrder('大閘蟹')
    print(f'客戶David:我要一份{steamed_order.get_display_name()}')
    waiter.receive_order(steamed_order)
    waiter.place_order()
    print()
    spicy_order = SpicyOrder('大閘蟹')
    print(f'客戶David:我要一份{spicy_order.get_display_name()}')
    waiter.receive_order(spicy_order)
    waiter.place_order()


test_order()
