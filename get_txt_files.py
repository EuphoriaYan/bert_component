import os
from tqdm import tqdm


def get_all_files(path, files, file_names):
    for f in files:
        f_full = path + f
        if os.path.isdir(f_full):
            folders = os.listdir(f_full)
            cur_path = f_full + '/'
            get_all_files(cur_path, folders, file_names)
        else:
            if f.find(".txt") != -1:
                file_names.append(path + f)


def get_files(path):
    files = os.listdir(path)
    file_names = list()
    get_all_files(path+'/', files, file_names)
    return file_names
