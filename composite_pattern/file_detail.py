import os
from composite_pattern.composite_pattern_framewrok import Composite, Component


class FileDetail(Component):
    """文件詳情"""
    def __init__(self, name):
        super().__init__(name)
        self._size = 0
    
    def set_size(self, size):
        self._size = size
    
    def get_file_size(self):
        return self._size
    
    def feature(self, indent):
        # 檔案大小單位:KB，精確度:2位小數
        file_size = round(self._size / float(1024), 2)
        print(f'檔案名稱{self._name}，文件大小: {file_size}KB')


class FolderDetail(Composite):
    """資料夾詳情"""
    def __init__(self, name):
        super().__init__(name)
        self._count = 0
    
    def set_count(self, file_num):
        self._count = file_num
    
    def get_count(self):
        return self._count
    
    def feature(self, indent):
        print(f'資料夾名:{self._name}，檔案數量:{self._count}。包含的檔:')
        super().feature(indent)


def scan_dir(root_path, folder_detail):
    """掃描某一資料夾下的所有目錄"""
    # 如果不存在此目錄
    if not os.path.isdir(root_path):
        raise ValueError(f'root_path 不是有效的路徑:{root_path}')
    # folder composite 不能為None
    if folder_detail is None:
        raise ValueError('folder_detail 不能為空!')
    # 列出目錄下所有檔案
    file_names = os.listdir(root_path)
    for file_name in file_names:
        # 根目錄 + 檔案名稱
        file_path = os.path.join(root_path, file_name)
        # 檢查是否為目錄
        if os.path.isdir(file_path):
            # 建立folder composite
            folder = FolderDetail(file_name)
            # 掃描根目錄下的子目錄
            scan_dir(file_path, folder)
            # 將子目錄加入根目錄folder composite
            folder_detail.add_component(folder)

        # 不是目錄，是檔案
        else:
            # 建立file component
            file_detail = FileDetail(file_name)
            # 取得檔案大小，單位:Byte
            file_detail.set_size(os.path.getsize(file_path))
            # 檔案加入file component
            folder_detail.add_component(file_detail)
            # 取得folder composite檔案數量然後+1，再重新設回folder composite
            folder_detail.set_count(folder_detail.get_count() + 1)
        

def test_dir():
    folder = FolderDetail('目前檔案目錄')
    scan_dir('D:\\Workspace\\design-patterns-py\\composite_pattern', folder)
    folder.feature('')


test_dir()

