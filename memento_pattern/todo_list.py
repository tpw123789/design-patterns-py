class Engineer:
    """工程師"""
    def __init__(self, name):
        self._name = name
        self._work_items = []

    def add_work_item(self, item):
        self._work_items.append(item)

    def forget(self):
        self._work_items.clear()
        print(f'{self._name}工作太忙，都忘記要做什麼了.....')

    def write_todo_list(self):
        """將工作項記錄到TodoList"""
        todo_list = TodoList()
        for item in self._work_items:
            todo_list.write_work_item(item)
        return todo_list

    def retrospect(self, todo_list):
        """回憶工作項"""
        self._work_items = todo_list.get_work_items()
        print(f'{self._name}想起要做什麼了.....')

    def show_work_item(self):
        if len(self._work_items):
            print(f'{self._name}工作項目:')
            for index in range(0, len(self._work_items)):
                print(f'{str(index + 1)}. {self._work_items[index]};')
        else:
            print(f'{self._name}暫時無工作項.....')


class TodoList:
    """工作項"""
    def __init__(self):
        self._work_items = []

    def write_work_item(self, item):
        self._work_items.append(item)

    def get_work_items(self):
        return self._work_items


class TodoListCaretaker:
    """TodoList管理類別"""
    def __init__(self):
        self._todo_list = None

    def set_todo_list(self, todo_list):
        self._todo_list = todo_list

    def get_todo_list(self):
        return self._todo_list


def test_engineer():
    tony = Engineer('Tony')
    tony.add_work_item('解決線上部分使用者因暱稱太長而無法顯示完全的問題')
    tony.add_work_item('完成PDF的解析')
    tony.add_work_item('在閱讀器中顯示PDF第一頁內容')
    tony.show_work_item()
    caretaker = TodoListCaretaker()
    caretaker.set_todo_list(tony.write_todo_list())
    print()
    tony.forget()
    tony.show_work_item()
    print()
    tony.retrospect(caretaker.get_todo_list())
    tony.show_work_item()


test_engineer()







