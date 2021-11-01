import requests
from threading import Thread


class DownloadThread(Thread):
    """下載檔案的執行緒"""
    # 每次寫文件的緩衝大小
    CHUNK_SIZE = 1024 * 512

    def __init__(self, filename, url, save_path, callback_progress, callback_finished):
        super().__init__()
        self._filename = filename
        self._url = url
        self._save_path = save_path
        self._callback_progress = callback_progress
        self._callback_finished = callback_finished

    def run(self):
        read_size = 0
        req = requests.get(self._url, stream=True)
        total_size = int(req.headers.get('Content-Length'))
        print(f'[下載{self._filename}] 文件大小:{total_size}')
        with open(self._save_path, mode='wb') as file:
            for chunk in req.iter_content(chunk_size=self.CHUNK_SIZE):
                if chunk:
                    file.write(chunk)
                    read_size += self.CHUNK_SIZE
                    self._callback_progress(self._filename, read_size, total_size)
        self._callback_finished(self._filename)


def test_download():
    def download_progress(filename, read_size, total_size):
        """定義下載進度的回乎函數"""
        percent = (read_size / total_size) * 100
        print(f'[下載{filename}] 下載進度:{percent:.2f}%')

    def download_finished(filename):
        """定義下載完成的回乎函數"""
        print(f'[下載{filename}]檔下載完成!')

    print('開始下載CSV_file......')
    download_url1 = 'https://plvr.land.moi.gov.tw//Download?type=zip&fileName=lvr_landcsv.zip'
    download1 = DownloadThread('檔案1', download_url1, './csv_file.zip', download_progress, download_finished)
    download1.start()
    print('開始下載XML_file......')
    download_url2 = 'https://plvr.land.moi.gov.tw//Download?type=zip&fileName=lvr_landxml.zip'
    download2 = DownloadThread('檔案2', download_url2, './xml_file.zip', download_progress, download_finished)
    download2.start()
    print('執行其他的任務....')


test_download()





