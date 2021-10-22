from abc import ABCMeta, abstractmethod


class SocketEntity:
    """介面類別定義"""
    def __init__(self, num_of_pin, type_of_pin):
        self._num_of_pin = num_of_pin
        self._type_of_pin = type_of_pin

    def get_num_of_pin(self):
        return self._num_of_pin

    def set_num_of_pin(self, num_of_pin):
        self._num_of_pin = num_of_pin

    def get_type_of_pin(self):
        return self._type_of_pin

    def set_type_of_pin(self, type_of_pin):
        self._type_of_pin = type_of_pin


class ISocket(metaclass=ABCMeta):
    """插座類型"""
    def get_name(self):
        """插座名稱"""
        pass

    def get_socket(self):
        """獲取介面"""
        pass


class ChineseSocket(ISocket):
    """國標插座"""
    def get_name(self):
        return '國標插座'

    def get_socket(self):
        return SocketEntity(3, '八字扁形')


class BritishSocket(ISocket):
    """英標插座"""
    def get_name(self):
        return '英鏢插座'

    def get_socket(self):
        return SocketEntity(3, 'T字方形')


class AdapterSocket:
    """插座轉換器"""
    def __init__(self, socket):
        self._socket = socket

    def name(self):
        return self._socket.get_name() + '轉換器'

    def socket_interface(self):
        socket = self._socket.get_socket()
        socket.set_type_of_pin('八字扁形')
        # socket.set_num_of_pin(3)
        return socket


def can_charge_for_digital_device(name, socket):
    if socket.get_num_of_pin() == 3 and socket.get_type_of_pin() == '八字扁形':
        is_standard = '符合'
        can_charge = '可以'
    else:
        is_standard = '不符合'
        can_charge = '不可以'
    print(f'[{name}]:\n針腳數量:{socket.get_num_of_pin()}，針腳類型:{socket.get_type_of_pin()};{is_standard}中國標準，{can_charge}給中國內地充電。')


def test_socket():
    chinese_socket = ChineseSocket()
    can_charge_for_digital_device(chinese_socket.get_name(), chinese_socket.get_socket())
    british_socket = BritishSocket()
    can_charge_for_digital_device(british_socket.get_name(), british_socket.get_socket())
    adapt_socket = AdapterSocket(british_socket)
    can_charge_for_digital_device(adapt_socket.name(), adapt_socket.socket_interface())


test_socket()
