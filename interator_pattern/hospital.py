class Customer:
    """客戶"""
    def __init__(self, name):
        self._name = name
        self._num = 0
        self._clinic = None
    
    def get_name(self):
        return self._name
    
    def register(self, system):
        system.push_customer(self)
    
    def set_num(self, num):
        self._num = num
    
    def get_num(self):
        return self._num
    
    def set_clinic(self, clinic):
        self._clinic = clinic
    
    def get_clinic(self):
        return self._clinic


class NumeralIterator:
    """反覆運算器"""
    def __init__(self, data):
        self._data = data
        # 移動到首個元素為第0個位置，所以初始值為-1
        self._curIdx = -1
    
    def next(self):
        """移動至下一個元素"""
        # 如果當前號碼尚未移動到最後一個位置
        if self._curIdx < len(self._data) - 1:
            # 移動到下一位置
            self._curIdx += 1
            return True
        else:
            return False
    
    def current(self):
        """獲取當前元素"""
        # data至少有一個元素且當前位置>=0，當前位置若為-1表示尚未移動過
        if len(self._data) > self._curIdx >= 0:
            return self._data[self._curIdx] 
        else:
            return None
    

class NumeralSystem:
    """排號系統"""
    _clinics = ('1號急診室', '2號急診室', '3號急診室')
    
    def __init__(self, name):
        self._customers = []
        self._curNum = 0
        self._name = name
    
    def push_customer(self, customer):
        # 新增客人，當前號碼+1
        self._curNum += 1
        # 設定客人的號碼，1號開始
        customer.set_num(self._curNum)
        # 急診室號碼
        click = NumeralSystem._clinics[(self._curNum - 1) % len(NumeralSystem._clinics)]
        # 設定急診室號碼
        customer.set_clinic(click)
        # 客人物件 加入list
        self._customers.append(customer)
        print(f'{customer.get_name()} 您好!您已在 {self._name} 成功掛號，序號: {customer.get_num():04d}，請耐心等待!')

    def get_iterator(self):
        return NumeralIterator(self._customers)


def test_hospital():
    numeral_system = NumeralSystem('掛號台')
    lily = Customer('Lily')
    lily.register(numeral_system)
    pony = Customer('Pony')
    pony.register(numeral_system)
    nick = Customer('Nick')
    nick.register(numeral_system)
    tony = Customer('Tony')
    tony.register(numeral_system)
    print()
    iterator = numeral_system.get_iterator()
    while iterator.next():
        customer = iterator.current()
        print(f'下一位病人{customer.get_num():04d}({customer.get_name()})請到 {customer.get_clinic()} 就診。')


test_hospital()


