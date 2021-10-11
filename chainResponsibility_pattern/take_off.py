from abc import ABCMeta, abstractmethod


class Person:
    """請假申請人"""
    def __init__(self, name, day_off, reason):
        self._name = name
        self._day_off = day_off
        self._reason = reason
        self._leader = None

    def get_name(self):
        return self._name

    def get_day_off(self):
        return self._day_off

    def get_reason(self):
        return self._reason

    def set_leader(self, leader):
        self._leader = leader

    def request(self):
        print(f'{self._name}申請請假{self._day_off}天。請假事由: {self._reason}')
        if self._leader is not None:
            self._leader.handle_request(self)


class Manager(metaclass=ABCMeta):
    """公司管理人員"""
    def __init__(self, name, title):
        self._name = name
        self._title = title
        self._next_handler = None

    def get_name(self):
        return self._name

    def get_title(self):
        return self._title

    def set_next_handler(self, next_handler):
        self._next_handler = next_handler

    @abstractmethod
    def handle_request(self, person):
        pass


class Supervisor(Manager):
    """主管"""
    def __init__(self, name, title):
        super().__init__(name, title)

    def handle_request(self, person):
        if person.get_day_off() <= 2:
            print(f'同意{person.get_name()}請假，簽字人: {self.get_name()} {self.get_title()}')
        if self._next_handler is not None:
            print(f'{self.get_title()} 傳給下一個人 {self._next_handler.get_title()}')
            self._next_handler.handle_request(person)


class DepartmentManager(Manager):
    """部門總監"""
    def __init__(self, name, title):
        super().__init__(name, title)

    def handle_request(self, person):
        if 5 >= person.get_day_off() > 2:
            print(f'同意{person.get_name()}請假，簽字人: {self.get_name()} {self.get_title()}')
        if self._next_handler is not None:
            print(f'{self.get_title()} 傳給下一個人 {self._next_handler.get_title()}')
            self._next_handler.handle_request(person)


class CEO(Manager):
    """CEO"""
    def __init__(self, name, title):
        super().__init__(name, title)

    def handle_request(self, person):
        if 5 < person.get_day_off() <= 22:
            print(f'同意{person.get_name()}請假，簽字人: {self.get_name()}{self.get_title()}')
        if self._next_handler is not None:
            print(f'{self.get_title()} 傳給下一個人 {self._next_handler.get_title()}')
            self._next_handler.handle_request(person)


class Administrator(Manager):
    """行政人員"""
    def __init__(self, name, title):
        super().__init__(name, title)

    def handle_request(self, person):
        if self._next_handler is not None:
            print(f'{self.get_title()} 傳給下一個人 {self._next_handler.get_title()}')
        else:
            print(f'{person.get_name()}的請假申請已審核，備案處裡。 處理人: {self.get_name()}{self.get_title()}')


directLeader = Supervisor('Eric', '部門經理')
departmentLeader = DepartmentManager('Jack', '總監')
ceo = CEO('Helen', '公司CEO')
administrator = Administrator('Amy', '行政人員')

directLeader.set_next_handler(departmentLeader)
departmentLeader.set_next_handler(ceo)
ceo.set_next_handler(administrator)

sunny = Person('Sunny', 1, '家裡死人')
sunny.set_leader(directLeader)
sunny.request()

print()

tony = Person('Tony', 15, '出國')
tony.set_leader(directLeader)
tony.request()





