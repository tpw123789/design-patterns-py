from abc import ABCMeta, abstractmethod
import os


class Page:
    """電子書一頁的內容"""
    def __init__(self, page_num):
        self._page_num = page_num

    def get_content(self):
        return f'第{str(self._page_num)}頁的內容....'


class Catalogue:
    """目錄結構"""
    def __init__(self, title):
        self._title = title
        self._chapters = []

    def add_chapter(self, title):
        self._chapters.append(title)

    def show_info(self):
        print(f'書名: {self._title}')
        print('目錄:')
        for chapter in self._chapters:
            print(f'\t{chapter}')


class IBook(metaclass=ABCMeta):
    """電子書文檔的介面類別"""
    @abstractmethod
    def parse_file(self, file_path):
        """解析文檔"""
        pass

    @abstractmethod
    def get_catalogue(self):
        """獲取目錄"""
        pass

    @abstractmethod
    def get_page_count(self):
        """獲取頁數"""
        pass

    @abstractmethod
    def get_page(self, page_num):
        """獲取內容"""
        pass


class TxtBook(IBook):
    """TXT解析類別"""
    def parse_file(self, file_path):
        # 模擬文檔的解析
        print(f'{file_path}檔解析成功')
        self._title = os.path.splitext(file_path)[0]
        self._page_count = 500
        return True

    def get_catalogue(self):
        catalogue = Catalogue(self._title)
        catalogue.add_chapter('第一章 標題')
        catalogue.add_chapter('第二章 標題')
        return catalogue

    def get_page_count(self):
        return self._page_count

    def get_page(self, page_num):
        return Page(page_num)


class EpuBook(IBook):
    """TXT解析類別"""
    def parse_file(self, file_path):
        # 模擬文檔的解析
        print(f'{file_path}檔解析成功')
        self._title = os.path.splitext(file_path)[0]
        self._page_count = 800
        return True

    def get_catalogue(self):
        catalogue = Catalogue(self._title)
        catalogue.add_chapter('第一章 標題')
        catalogue.add_chapter('第二章 標題')
        return catalogue

    def get_page_count(self):
        return self._page_count

    def get_page(self, page_num):
        return Page(page_num)


class Outline:
    """協力廠商PDF解析庫的目錄類別"""
    def __init__(self):
        self._outlines = []

    def add_outline(self, title):
        self._outlines.append(title)

    def get_outlines(self):
        return self._outlines


class PdfPage:
    """PDF頁"""
    def __init__(self, page_num):
        self._page_num =page_num

    def get_page_num(self):
        return self._page_num


class ThirdPdf:
    """協力廠商PDF解析庫"""
    def __init__(self):
        self._page_size = 0
        self._title = ''

    def open(self, file_path):
        print(f'協力廠商庫解析PDF文件:{file_path}')
        self._title = os.path.splitext(file_path)[0]
        self._page_size = 1000
        return True

    def get_title(self):
        return self._title

    def get_outline(self):
        outline = Outline()
        outline.add_outline('第一章 PDF 電子書標題')
        outline.add_outline('第二章 PDF 電子書標題')
        return outline

    def page_size(self):
        return self._page_size

    def page(self, index):
        return PdfPage(index)


class PdfAdapterBook(ThirdPdf, IBook):
    """對協力廠商的PDF解析庫進行包裝"""
    def __init__(self, third_pdf):
        self._third_pdf = third_pdf

    def parse_file(self, file_path):
        """模擬文檔的解析"""
        rtn = self._third_pdf.open(file_path)
        if rtn:
            print(f'{file_path}檔解析成功')
        return rtn

    def get_catalogue(self):
        outline = self.get_outline()
        print('將Outline結構的目錄轉換成Catalogue結構的目錄')
        catalogue = Catalogue(self._third_pdf.get_title())
        for title in outline.get_outlines():
            catalogue.add_chapter(title)
        return catalogue

    def get_page_count(self):
        return self._third_pdf.page_size()

    def get_page(self, page_num):
        page = self.page(page_num)
        print(f'將PdfPage的物件傳換成Page的物件')
        return Page(page.get_page_num())


class Reader:
    """閱讀器"""
    def __init__(self, name):
        self._name = name
        self._file_path = ''
        self._current_book = None
        self._current_page_num = -1

    def _init_book(self, file_path):
        self._file_path = file_path
        ext_name = os.path.splitext(file_path)[1]
        if ext_name.lower() == '.epub':
            self._current_book = EpuBook()
        elif ext_name.lower() == '.txt':
            self._current_book = TxtBook()
        elif ext_name.lower() == '.pdf':
            self._current_book = PdfAdapterBook(ThirdPdf())
        else:
            self._current_book = None

    def open_file(self, file_path):
        self._init_book(file_path)
        if self._current_book is not None:
            rtn = self._current_book.parse_file(file_path)
            if rtn:
                self._current_page_num = 1
            return rtn
        return False

    def close_file(self):
        print(f'關閉 {self._file_path}文件')
        return True

    def show_catalogue(self):
        catalogue = self._current_book.get_catalogue()
        catalogue.show_info()

    def pre_page(self):
        print('往前翻一頁')
        return self.goto_page(self._current_page_num - 1)

    def next_page(self):
        print('往後翻一頁')
        return self.goto_page(self._current_page_num + 1)

    def goto_page(self, page_num):
        if 1 < page_num < self._current_book.get_page_count() - 1:
            self._current_page_num = page_num
        print(f'顯示第{str(self._current_page_num)}頁')
        page = self._current_book.get_page(self._current_page_num)
        page.get_content()
        return page


def test_reader():
    reader = Reader('閱讀器')
    if not reader.open_file('這是TXT書本.txt'):
        return
    reader.show_catalogue()
    reader.pre_page()
    reader.next_page()
    reader.close_file()
    print()
    if not reader.open_file('這是EPUB書本.epub'):
        return
    reader.show_catalogue()
    reader.pre_page()
    reader.next_page()
    reader.close_file()
    print()
    if not reader.open_file('這是PDF書本.pdf'):
        return
    reader.show_catalogue()
    reader.pre_page()
    reader.next_page()
    reader.close_file()


test_reader()












