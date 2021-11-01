from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    """演算法的抽象類別"""
    @abstractmethod
    def algorithm(self, *args, **kwargs):
        """定義演算法"""
        pass


class StrategyA(Strategy):
    """策略A"""
    def algorithm(self, *args, **kwargs):
        print('演算法A的實現...')


class StrategyB(Strategy):
    """策略B"""
    def algorithm(self, *args, **kwargs):
        print('演算法B的實現')


class Context:
    """上下文關係"""
    def interface(self, strategy, *args, **kwargs):
        """交互介面"""
        print('回檔執行前操作')
        strategy.algorithm(strategy)
        print('回檔執行後操作')


context = Context()
context.interface(StrategyA)
context.interface(StrategyB)


