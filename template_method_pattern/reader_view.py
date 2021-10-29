from abc import ABCMeta, abstractmethod


class ReaderView(metaclass=ABCMeta):
    """閱讀器視圖"""
    def __init__(self):
        self._cur_page_num = 1

    def get_page(self, page_num):
        self._cur_page_num = page_num
        return '第' + str(page_num) + '頁的內容'

    def pre_page(self):
        """範本方法，往前一頁"""
        content = self.get_page(self._cur_page_num - 1)
        self._display_page(content)

    def next_page(self):
        """範本方法，往後一頁"""
        content = self.get_page(self._cur_page_num + 1)
        self._display_page(content)

    @abstractmethod
    def _display_page(self, content):
        """翻頁效果"""
        pass


class SmoothView(ReaderView):
    """左右平滑的視圖"""
    def _display_page(self,content):
        print('左右平滑:' + content)


class SimulationView(ReaderView):
    """模擬翻頁的視圖"""
    def _display_page(self, content):
        print('模擬翻頁:' + content)


def test_reader():
    smooth_view = SmoothView()
    smooth_view.next_page()
    smooth_view.pre_page()

    simulation_view = SimulationView()
    simulation_view.next_page()
    simulation_view.pre_page()


test_reader()


