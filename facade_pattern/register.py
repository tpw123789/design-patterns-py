class Register:
    """報到登記"""
    def register(self, name):
        print(f'活動中心: {name}同學，報到成功。')


class Payment:
    """繳費中心"""
    def pay(self, name, money):
        print(f'繳費中心: 收到{name}同學{money}元付款，繳費成功。')


class DormitoryManagermentCenter:
    """生活中心(宿舍管理中心)"""
    def provide_living_goods(self, name):
        print(f'生活中心: {name}同學的生活用品已發放。')


class Dormitory:
    """宿舍"""
    def meet_roommate(self, name):
        print(f'宿舍: 大家好，這是剛來新同學{name}。')


class Volunteer:
    """迎新志願者"""
    def __init__(self, name):
        self._name = name
        self._register = Register()
        self._payment = Payment()
        self._life_center = DormitoryManagermentCenter()
        self._dormintory = Dormitory()

    def welcome_freshmen(self, name):
        print(f'你好{name}同學，我是新生報到志願者{self._name}。')
        self._register.register(name)
        self._payment.pay(name, 10000)
        self._life_center.provide_living_goods(name)
        self._dormintory.meet_roommate(name)


volunteer = Volunteer('Frank')
volunteer.welcome_freshmen('Tony')
        


