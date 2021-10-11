from chainResponsibility_pattern.responsibility_pattern_framework import Responsible, Request


class Person:
    """請求者(請假人)"""
    def __init__(self, name):
        self._name = name
        self._leader = None

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_leader(self, leader):
        self._leader = leader

    def get_leader(self):
        return self._leader

    def send_request(self, request):
        print(f'{self._name}申請請假{request.get_day_off()}，事由: {request.get_reason()}')
        if self._leader is not None:
            self._leader.handle_request(request)


class Supervisor(Responsible):
    """主管"""
    def __init__(self, name, title):
        super().__init__(name, title)

    def _handle_request_impl(self, request):
        if request.get_day_off() <= 2:
            print(f'同意{request.get_name()}請假，簽字人: {self.get_name()}{self.get_title()}')
        else:
            print('Next one')


class DepartmentManager(Responsible):
    """部門總監"""
    def __init__(self, name, title):
        super().__init__(name, title)

    def _handle_request_impl(self, request):
        if 2 < request.get_day_off() <= 5:
            print(f'同意{request.get_name()}請假，簽字人: {request.get_name()}{self.get_title()}')
        else:
            print('Next one')


class CEO(Responsible):
    """CEO"""
    def __init__(self, name, title):
        super().__init__(name, title)

    def _handle_request_impl(self, request):
        if 5 < request.get_day_off() <= 22:
            print(f'同意{request.get_name()}請假，簽字人: {request.get_name()}{self.get_title()}')
        else:
            print('Next one')


class Administrator(Responsible):
    """行政人員"""
    def __init__(self, name, title):
        super().__init__(name, title)

    def _handle_request_impl(self, request):
        print(f'同意{request.get_name()}請假，簽字人: {request.get_name()}{self.get_title()}')


directLeader = Supervisor('Eric', '部門經理')
departmentLeader = DepartmentManager('Jack', '總監')
ceo = CEO('Helen', '公司CEO')
administrator = Administrator('Amy', '行政人員')

directLeader.set_next_handler(departmentLeader)
departmentLeader.set_next_handler(ceo)
ceo.set_next_handler(administrator)

sunny = Person('Sunny')
sunny.set_leader(directLeader)
sunny.send_request(Request('Sunny', 1, '家裡死人'))

print()

tony = Person('Tony')
tony.set_leader(directLeader)
tony.send_request(Request('Tony', 20, '出國'))


