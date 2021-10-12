from proxy_pattern.proxy_pattern_framework import Subject, ProxySubject, RealSubject


class TonyReception(Subject):
    """Tony接收"""
    def __init__(self, name, phone_num, content):
        super().__init__(name)
        self._phone_num = phone_num
        self._content = content

    def get_phone_num(self):
        return self._phone_num

    def request(self):
        print(f'貨物主人: {self.get_name()}，手機號碼: {self._phone_num}')
        print(f'接收到一個包裹，包裹內容: {str(self._content)}')


class WendyReception(ProxySubject):
    """Wendy代收"""
    def __init__(self, name, receiver):
        super().__init__(name=name, real_subject=receiver)

    def pre_request(self):
        print(f'我是{self._real_subject.get_name()}的朋友，我來幫代收包裹!')

    def after_request(self):
        print(f'代收人: {self.get_name()}')


if __name__ == '__main__':
    tony = TonyReception('Tony', '886988455652', '禮物')
    print('Tony接收: ')
    tony.request()
    print()
    print('Wendy 代收: ')
    wendy = WendyReception('Wendy', tony)
    wendy.request()

