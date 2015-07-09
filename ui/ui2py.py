from os import listdir, system
from os.path import isfile

for f in listdir('./'):
    if isfile(f) and '.ui' in f[-3:]:
        ui_name = f
        py_name = f[:-3] + '.py'
        cmd = 'pyside-uic ' + ui_name + ' -o ' + py_name
        system(cmd)
