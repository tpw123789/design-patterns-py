from abc import ABCMeta, abstractmethod


class ReceiveParcel(metaclass=ABCMeta):
    """接收包裹抽象類別"""
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name
    
    @abstractmethod
    def receive(self, parcel_content):
        pass


class TonyReception(ReceiveParcel):
    """Tony接收"""
    def __init__(self, name, phone_num):
        super().__init__(name)
        self._phone_num = phone_num
    
    def get_phone_num(self):
        return self._phone_num
    
    def receive(self, parcel_content):
        print(f'貨物主人: {self.get_name()}，手機號: {self._phone_num}')
        print(f'接收到一個包裹，包裹內容: {parcel_content}')


class WendyReception(ReceiveParcel):
    """Wendy代收"""
    def __init__(self, name, receiver):
        super().__init__(name)
        self._receiver = receiver
    
    def receive(self, parcel_content):
        print(f'我是{self._receiver.get_name()}的朋友，我幫他收快遞!')
        if self._receiver is not None:
            self._receiver.receive(parcel_content)
        print(f'代收人{self.get_name()}')
        

tony = TonyReception('Tony', '8869561515151')
print('Tony收起: ')
tony.receive('包裹')
print()

print('Wendy代收: ')
wendy = WendyReception('Wendy', tony)
wendy.receive('包裹')

