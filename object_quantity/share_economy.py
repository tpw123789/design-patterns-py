

class PowerBank:
    """移動電源"""
    def __init__(self, serial_num, electric_quantity):
        self._serial_num = serial_num
        self._electric_quantity = electric_quantity
        self._user = ''

    def get_serial_number(self):
        return self._serial_num

    def get_electric_quantity(self):
        return self._electric_quantity

    def set_user(self, user):
        self._user = user

    def get_user(self):
        return self._user

    def show_info(self):
        print(f'序號:{self._serial_num} 電量:{self._electric_quantity} 使用者:{self._user}')


class ObjectPack:
    """對象的包裝類別，封裝指定的物件是否正在被使用"""
    def __init__(self, obj, in_using=False):
        self._obj = obj
        self._in_using = in_using

    def in_using(self):
        return self._in_using

    def set_using(self, in_using):
        self._in_using = in_using

    def get_obj(self):
        return self._obj


class PowerBankBox:
    """存放移動電源的智慧箱盒"""
    def __init__(self):
        self._pools = dict()
        self._pools['0001'] = ObjectPack(PowerBank('0001', 100))
        self._pools['0002'] = ObjectPack(PowerBank('0002', 100))

    def borrow(self, serial_num):
        """借用移動電源"""
        item = self._pools.get(serial_num)
        result = None
        if item is None:
            print('沒有可用電源!')
        elif not item.in_using():
            # 如果非使用中，設定為使用中
            item.set_using(True)
            # 取得行動電源
            result = item.get_obj()
        else:
            print(f'電源{serial_num}，已被借用!')
        return result

    def give_back(self, serial_num):
        """歸還移動電源"""
        item = self._pools.get(serial_num)
        if item is not None:
            # 設定歸還行動電源為非使用中
            item.set_using(False)
            print(f'{serial_num}電源，已歸還!')


def test_power_bank():
    box = PowerBankBox()
    power_bank1 = box.borrow('0001')
    if power_bank1 is not None:
        power_bank1.set_user('Tony')
        power_bank1.show_info()
    power_bank2 = box.borrow('0002')
    if power_bank2 is not None:
        power_bank2.set_user('Sam')
        power_bank2.show_info()
    power_bank3 = box.borrow('0001')
    box.give_back('0001')
    power_bank3 = box.borrow('0001')
    if power_bank3 is not None:
        power_bank3.set_user('Aimee')
        power_bank3.show_info()


test_power_bank()
