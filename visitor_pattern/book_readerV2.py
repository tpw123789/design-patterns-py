from visitor_pattern.visitor_pattern_framework import DataNode, Visitor, ObjectStructure


class Book(DataNode):
    """Harry Potter"""
    def get_name(self):
        return 'Harry Potter'


class Book2(DataNode):
    """Twilight"""
    def get_name(self):
        return 'Twilight'


class Engineer(Visitor):
    """工程師"""
    def visit(self, book):
        print(f'技術人讀{book.get_name()}一書後的感受: 棒!')


class ProductManager(Visitor):
    """產品經理"""
    def visit(self, book):
        print(f'產品經理{book.get_name()}一書後的感受: 棒!')


class OtherFriends(Visitor):
    """圈外朋友"""
    def visit(self, book):
        print(f'圈外朋友{book.get_name()}一書後的感受: 棒!')


def test_visit_book():
    book = Book()
    book2 = Book2()
    obj_manager = ObjectStructure()
    obj_manager.add(book)
    obj_manager.add(book2)
    obj_manager.action(Engineer())
    obj_manager.action(ProductManager())
    obj_manager.action(OtherFriends())


test_visit_book()


