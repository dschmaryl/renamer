#!/usr/bin/env python3

import glob
import subprocess


def convert_ui_to_py():
    for ui_file in glob.glob('*.ui'):
        py_file = ui_file.replace('.ui', '.py')
        command = ['pyside-uic', ui_file, '-o', py_file]
        subprocess.run(command)


if __name__ == '__main__':
    convert_ui_to_py()
