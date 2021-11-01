class Employee:
    """公司員工"""
    def __init__(self, name):
        self._name = name

    def do_performance(self, skill):
        print(f'{self._name}的表演: ', end='')
        skill()


def sing():
    """唱歌"""
    print('唱一首歌')


def dling():
    """拉Ukulele"""
    print('拉一首Ukulele曲子')


def joke():
    """說段子"""
    print('說一個搞笑段子')


def performance_magic_tricks():
    """表演魔術"""
    print('神秘魔術')


def skateboarding():
    """玩滑板"""
    print('酷炫滑板')


def test_skill():
    helen = Employee('Helen')
    helen.do_performance(sing)
    frank = Employee('Frank')
    frank.do_performance(dling)
    jacky = Employee('Jacky')
    jacky.do_performance(joke)
    chork = Employee('Chork')
    chork.do_performance(performance_magic_tricks)
    kerry = Employee('Kerry')
    kerry.do_performance(skateboarding)


test_skill()
