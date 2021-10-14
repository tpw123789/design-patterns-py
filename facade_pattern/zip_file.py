from os import path
# 引入path
import logging
# 引入logging


class ZIPModel:
    """ZIP模組，負責ZIP檔案壓縮與解壓縮"""
    def compress(self, src_file_path, dst_file_path):
        print(f'ZIP模組正在進行{src_file_path}檔壓縮')
        print(f'檔案壓縮成功，保存至{dst_file_path}')

    def decompress(self, src_file_path, dst_file_path):
        print(f'ZIP模組正在進行{src_file_path}解壓縮')
        print(f'解壓縮成功，保存至{dst_file_path}')


class RARModel:
    """RAR模組，負責RAR檔的壓縮與解壓縮"""
    def compress(self, src_file_path, dst_file_path):
        print(f'RAR模組正在進行{src_file_path}檔壓縮')
        print(f'檔案壓縮成功，保存至{dst_file_path}')

    def decompress(self, src_file_path, dst_file_path):
        print(f'RAR模組正在進行{src_file_path}解壓縮')
        print(f'解壓縮成功，保存至{dst_file_path}')


class ZModel:
    """7Z模組，負責7Z檔案解壓縮"""
    def compress(self, src_file_path, dst_file_path):
        print(f'7Z模組正在進行{src_file_path}檔壓縮')
        print(f'檔案壓縮成功，保存至{dst_file_path}')

    def decompress(self, src_file_path, dst_file_path):
        print(f'7Z模組正在進行{src_file_path}解壓縮')
        print(f'解壓縮成功，保存至{dst_file_path}')


class CompressionFacade:
    """壓縮系統的外觀類別"""
    def __init__(self):
        self._zipModel = ZIPModel()
        self._rarModel = RARModel()
        self._zModel = ZModel()

    def compress(self, scr_file_path, dst_file_path, file_type):
        """根據不同的壓縮類別"""
        ext_name = "." + file_type
        full_name = dst_file_path + ext_name
        if file_type.lower() == 'zip':
            self._zipModel.compress(scr_file_path, full_name)
        elif file_type.lower() == 'rar':
            self._rarModel.compress(scr_file_path, full_name)
        elif file_type.lower() == '7z':
            self._zModel.compress(scr_file_path, full_name)
        else:
            logging.error('Not support this format: ', str(file_type))
            return False
        return True

    def decompress(self, scr_file_path, dst_file_path):
        """從srcFilePath中獲取尾碼，根據尾碼進行不同格式解壓縮"""
        base_name = path.basename(scr_file_path)
        ext_name = base_name.split('.')[1]
        if ext_name.lower() == 'zip':
            self._zipModel.decompress(scr_file_path, dst_file_path)
        elif ext_name.lower() == 'rar':
            self._rarModel.decompress(scr_file_path, dst_file_path)
        elif ext_name.lower() == '7z':
            self._zModel.decompress(scr_file_path, dst_file_path)
        else:
            logging.error('Not support this format: ', str(ext_name))
            return False
        return True


def test_compression():
    facade = CompressionFacade()
    facade.compress('test.md', '/test', 'zip')
    facade.decompress('test.zip', '/desktop')
    facade.compress('test.md', '/test', 'rar')
    facade.decompress('test.zip', '/desktop')
    facade.compress('test.md', '/test', '7z')
    facade.decompress('test.zip', '/desktop')

test_compression()
