#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import subprocess


for ui_file in glob.glob('*.ui'):
    py_file = ui_file.replace('.ui', '.py')
    command = ['pyside-uic', ui_file, '-o', py_file]
    subprocess.run(command)
