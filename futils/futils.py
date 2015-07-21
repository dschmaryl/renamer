from os import listdir, rename, walk
from os.path import isfile, join
from shutil  import copy2


def rename_files(files, copy=False):
    if copy:
        rename_func = copy2
    else:
        rename_func = rename
    renamed_files = {}
    for i in files:
        if files[i]['new'] and files[i]['selected'] == True:
            old_name = files[i]['old']
            new_name = files[i]['new']
            renamed_files[i] = files[i]
            rename_func(old_name, new_name)
    return renamed_files


def list_files(folder='./', filter_str=None, recursive=False):
    files = []
    if recursive:
        for (p, d, fs) in walk(folder):
            if p == './':
                for f in fs:
                    if not filter_str or filter_str in f:
                        files.append(p+f)
            else:
                for f in fs:
                    if not filter_str or filter_str in f:
                        files.append(p+'/'+f)
    else:
        for f in listdir(folder):
            if isfile(join(folder,f)):
                if not filter_str or filter_str in f:
                    files.append(f)
    return files


def dict_files(file_list):
    file_dict = {}
    for f in file_list:
        file_dict[file_list.index(f)] = {
            'old': f,
            'new': '',
            'selected': True
        }
    return file_dict


def get_dict(folder='./', **kwargs):
    return dict_files(list_files(folder, **kwargs))
