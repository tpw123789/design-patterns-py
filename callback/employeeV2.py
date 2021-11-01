from abc import ABCMeta, abstractmethod


class Skill(metaclass=ABCMeta):
    """技能的抽象類別"""
    @abstractmethod
    def performance(self):
        """技能表演"""
        pass


class NewEmployee:
    """公司員工"""
    def __init__(self, name):
        self._name = name

    def do_performance(self, skill):
        print(f'{self._name}的表演:', end='')
        skill.performance()


class Sing(Skill):
    """唱歌"""
    def performance(self):
        print('唱一首歌')


class Joke(Skill):
    """說段子"""
    def performance(self):
        print('說一個搞笑段子')


class Dling(Skill):
    """拉Ukuele"""
    def performance(self):
        print('彈一首Ukuele曲子')


class PerformMagicTricks(Skill):
    """表演魔術"""
    def performance(self):
        print('神秘魔術')


class Skateboarding(Skill):
    """玩滑板"""
    def performance(self):
        print('酷炫滑板')


def test_strategy_skill():
    helen = NewEmployee('Helen')
    helen.do_performance(Sing())
    frank = NewEmployee('Frank')
    frank.do_performance(Dling())
    jacky = NewEmployee('Jacky')
    jacky.do_performance(Joke())
    chork = NewEmployee('Chork')
    chork.do_performance(PerformMagicTricks())
    Kerry = NewEmployee('Kerry')
    Kerry.do_performance(Skateboarding())


test_strategy_skill()
