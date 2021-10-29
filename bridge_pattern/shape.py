from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    """形狀"""
    def __init__(self, color):
        self._color = color

    @abstractmethod
    def get_shape_type(self):
        pass

    def get_shape_info(self):
        return self._color.get_color() + '的' + self.get_shape_type()


class Rectangle(Shape):
    """矩形"""
    def __init__(self, color):
        super().__init__(color)

    def get_shape_type(self):
        return '矩形'


class Ellipse(Shape):
    """橢圓"""
    def __init__(self, color):
        super().__init__(color)

    def get_shape_type(self):
        return '橢圓'


class Color(metaclass=ABCMeta):
    """顏色"""
    @abstractmethod
    def get_color(self):
        pass


class Red(Color):
    """紅色"""
    def get_color(self):
        return '紅色'


class Green(Color):
    """綠色"""
    def get_color(self):
        return '綠色'


def test_shape():
    red_rect = Rectangle(Red())
    print(red_rect.get_shape_info())
    green_rect = Rectangle(Green())
    print(green_rect.get_shape_info())
    red_ellipse = Ellipse(Red())
    print(red_ellipse.get_shape_info())
    green_ellipse = Ellipse(Green())
    print(green_ellipse.get_shape_info())


test_shape()
