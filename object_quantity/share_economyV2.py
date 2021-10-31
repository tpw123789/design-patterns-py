from object_quantity.object_quantity_framework import PooledObject, ObjectPool


class PowerBank:
    """移動電源"""
    def __init__(self, serial_num, electric_quantity):
        self._serial_num = serial_num
        self._electric_quantity = electric_quantity
        self._user = ''

    def get_serial_num(self):
        return self._serial_num

    def get_electric_quantity(self):
        return self._electric_quantity

    def set_user(self, user):
        self._user = user

    def get_user(self):
        return self._user

    def show_info(self):
        print(f'序號:{self._serial_num:03d} 電量:{self._electric_quantity} 使用者:{self._user}')


class PowerBankPool(ObjectPool):
    """存放移動電源的智慧箱盒"""
    _serial_num = 0

    @classmethod
    def get_serial_num(cls):
        cls._serial_num += 1
        return cls._serial_num

    def create_pool_object(self):
        power_bank = PowerBank(PowerBankPool.get_serial_num(), 100)
        return PooledObject(power_bank)


def test_object_pool():
    power_bank_pool = PowerBankPool()
    power_bank1 = power_bank_pool.borrow_object()
    if power_bank1 is not None:
        power_bank1.set_user('Tony')
        power_bank1.show_info()
    power_bank2 = power_bank_pool.borrow_object()
    if power_bank2 is not None:
        power_bank2.set_user('Sam')
        power_bank2.show_info()
    power_bank_pool.return_object(power_bank1)
    # object_bank1歸還後，不能再對其進行相關操作
    power_bank3 = power_bank_pool.borrow_object()
    if power_bank3 is not None:
        power_bank3.set_user('Aimee')
        power_bank3.show_info()
    power_bank_pool.return_object(power_bank2)
    power_bank_pool.return_object(power_bank3)
    power_bank_pool.clear()


test_object_pool()



