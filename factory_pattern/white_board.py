from abc import ABCMeta, abstractmethod
from enum import Enum


class PenType:
    """畫筆類型"""
    pen_type_line = 1
    pen_type_rect = 2
    pen_type_ellipse = 3


class Pen(metaclass=ABCMeta):
    """畫筆抽象類別"""
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def get_type(self):
        pass

    def get_name(self):
        return self._name


class LinePen(Pen):
    """直線畫筆類別"""
    def __init__(self, name):
        super().__init__(name)

    def get_type(self):
        return PenType.pen_type_line


class RectanglePen(Pen):
    """矩形畫筆類別"""
    def __init__(self, name):
        super().__init__(name)

    def get_type(self):
        return PenType.pen_type_rect


class EllipsePen(Pen):
    """橢圓畫筆類別"""
    def __init__(self, name):
        super().__init__(name)

    def get_type(self):
        return PenType.pen_type_ellipse


class PenFactory:
    """畫筆工廠類別"""
    def __init__(self):
        """
        定義一個字典{PenType: Pen}，確保一個類別類型只有一個物件
        """
        self._pens = {}

    def get_single_obj(self, pen_type):
        """唯一獲得實例物件"""
        return self._pens[pen_type].get_name()

    def create_pen(self, pen_type):
        """創建畫筆"""
        if self._pens.get(pen_type) is None:
            # 如果該物件不存在
            if pen_type == PenType.pen_type_line:
                pen = LinePen('直線畫筆')
            elif pen_type == PenType.pen_type_rect:
                pen = RectanglePen('矩形畫筆')
            else:
                pen = EllipsePen('橢圓畫筆')
            self._pens[pen_type] = pen
        return self._pens[pen_type]


def test_pen_factory():
    factory = PenFactory()
    line_pen = factory.create_pen(PenType.pen_type_line)
    print(f'創建->{line_pen.get_name()}，物件id:{id(line_pen)}，類別:{line_pen.get_type()}')
    line_pen2 = factory.create_pen(PenType.pen_type_line)
    print(f'創建->{line_pen2.get_name()}，物件id:{id(line_pen2)}，類別:{line_pen2.get_type()}')
    rect_pen = factory.create_pen(PenType.pen_type_rect)
    print(f'創建->{rect_pen.get_name()}，物件id:{id(rect_pen)}，類別:{rect_pen.get_type()}')
    ellipse_pen = factory.create_pen(PenType.pen_type_ellipse)
    print(f'創建->{ellipse_pen.get_name()}，物件id:{id(ellipse_pen)}，類別:{ellipse_pen.get_type()}')
    print(factory.get_single_obj(PenType.pen_type_line))


test_pen_factory()


