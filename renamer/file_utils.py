#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import os
import shutil


def get_files_dict(filter_str='*'):
    if '*' not in filter_str:
        filter_str = '*' + filter_str + '*'
    files = sorted(glob.glob(filter_str))
    return {files.index(f): {'old': f, 'selected': True} for f in files}


def rename_files(files_dict, copy=False):
    '''
    'files_dict' should be a dictionary like the following:

    files_dict = {
        file_one: {
            'old': old_name,
            'new': new_name,
            'selected': boolean
        },
        file_two: {
            ...
        },
        ...
    }
    '''
    rename = shutil.copy2 if copy else os.rename
    renamed_files = {}

    for key, filename in files_dict.items():
        if filename['selected'] and filename['new']:
            old_name = filename['old']
            new_name = filename['new']
            renamed_files[key] = filename
            rename(old_name, new_name)

    return renamed_files
