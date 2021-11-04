"""Don't Repeat Yourself"""
import os


# 不好的寫法
def get_path(base_path, file_name):
    ext_name = os.path.splitext(file_name)[1]
    file_path = base_path
    if ext_name.lower() == '.txt':
        file_path += '/txt/'
    elif ext_name.lower() == '.pdf':
        file_path += '/pdf/'
    else:
        file_path += '/other/'
    # 如果目錄不存在，則創建新目錄
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_path += file_name
    return file_path


# 重構後
def get_path_v2(base_path, file_name):
    ext_name = file_name.split('.')[1]
    file_path = base_path + '/' + ext_name + '/'
    # 如果目錄不存在，則創建新目錄
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_path += file_name
    return file_path


