from abc import ABCMeta, abstractmethod


class Book:
    """書"""
    def get_name(self):
        return 'Harry Potter'


class Reader(metaclass=ABCMeta):
    """存取者，也就是讀者"""
    @abstractmethod
    def read(self, book):
        pass


class Engineer(Reader):
    """工程師"""
    def read(self, book):
        print(f'技術人讀{book.get_name()}一書後的感受: 棒!')


class ProductManager(Reader):
    """產品經理"""
    def read(self, book):
        print(f'產品經理讀{book.get_name()}一書的感受: 棒棒!')


class OtherFriend(Reader):
    """IT圈外"""
    def read(self, book):
        print(f'產品經理讀{book.get_name()}一書的感受: 棒棒棒!')


def test_book():
    book = Book()
    fans = [Engineer(), ProductManager(), OtherFriend()]
    for fan in fans:
        fan.read(book)


test_book()



