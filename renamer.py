#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import os
import pathlib
import sys
import shutil

from PySide import QtGui

from ui.filterdialog import Ui_FilterDialog
from ui.formatdialog import Ui_FormatDialog
from ui.insertdialog import Ui_InsertDialog
from ui.mainwindow import Ui_MainWindow
from ui.replacedialog import Ui_ReplaceDialog
from ui.stripdialog import Ui_StripDialog


def rename_files(files_dict, copy=False):
    rename = shutil.copy2 if copy else os.rename
    renamed_files = {}
    for key, filename in files_dict.items():
        if filename['selected'] and filename['new']:
            old_name = filename['old']
            new_name = filename['new']
            renamed_files[key] = filename
            rename(old_name, new_name)
    return renamed_files


def get_files_dict(filter_str='*'):
    if '*' not in filter_str:
        filter_str = '*' + filter_str + '*'
    files = sorted(glob.glob(filter_str))
    return {files.index(f): {'old': f, 'selected': True} for f in files}


def find_replace(old_name, find_string, replace_string):
    if find_string not in old_name:
        return None
    return old_name.replace(find_string, replace_string, 1)


def insert(old_name, insert_position, insert_string):
    if not insert_string:
        return None
    if insert_position:
        try:
            position_int = max(0, int(insert_position) - 1)
        except ValueError:
            return None
    else:
        position_int = 0
    return old_name[:position_int] + insert_string + old_name[position_int:]


def strip_chars(old_name, strip_position, strip_length):
    try:
        strip_int = max(0, int(strip_length))
    except ValueError:
        return None
    if strip_position:
        try:
            position_int = max(0, int(strip_position) - 1)
        except ValueError:
            return None
    else:
        position_int = 0
    return old_name[:position_int] + old_name[position_int+strip_int:]


def format_numbers(old_name, format_length, format_position):
    if format_length:
        try:
            format_length = min(max(2, int(format_length)), 6)
        except ValueError:
            return None
    else:
        format_length = 2
    if format_position:
        try:
            format_position = max(0, int(format_position) - 1)
        except ValueError:
            return None
    else:
        format_position = 0
    format_string = '%0' + str(format_length) + 'd'
    old_number = ''
    for i in range(format_length):
        if old_name[format_position:][i].isdigit():
            old_number += old_name[format_position:][i]
    try:
        new_number = format_string % int(old_number)
    except ValueError:
        return None
    return old_name.replace(old_number, new_number, 1)


class Dialog(QtGui.QDialog):
    def __init__(self, ui_form, old_name, action, parent=None):
        super(Dialog, self).__init__(parent)
        self.ui = ui_form()
        self.ui.setupUi(self)
        self.ui.line_1.textChanged.connect(self.update_preview)
        self.ui.line_2.textChanged.connect(self.update_preview)
        self.ui.button_cancel.clicked.connect(self.close)
        self.ui.button_apply.clicked.connect(self.accept)
        self.ui.line_old.setText(old_name)
        self.action = action

    def update_preview(self):
        line_1_string = self.ui.line_1.text()
        line_2_string = self.ui.line_2.text()
        old_name = self.ui.line_old.text()
        new_name = self.action(old_name, line_1_string, line_2_string)
        self.ui.line_new.setText(new_name)

    def get_values(self):
        return self.ui.line_1.text(), self.ui.line_2.text()


class FilterDialog(QtGui.QDialog, Ui_FilterDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.button_cancel.clicked.connect(self.close)
        self.button_apply.clicked.connect(self.accept)

    def get_values(self):
        return self.line_string.text()


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.button_filter.clicked.connect(self.apply_filter)
        self.button_insert.clicked.connect(self.dialog_insert)
        self.button_replace.clicked.connect(self.dialog_replace)
        self.button_strip.clicked.connect(self.dialog_strip)
        self.button_format.clicked.connect(self.dialog_format)
        self.button_undo.clicked.connect(self.undo_rename)
        self.button_save.clicked.connect(self.save_changes)
        self.button_exit.clicked.connect(self.close)
        self.list_old.itemSelectionChanged.connect(self.select_files)

        # check to see if a filename or directory was passed as an argument.
        # if so, change to the directory
        if len(sys.argv) == 2:
            self.folder = pathlib.Path(sys.argv[1]).resolve()
            if not self.folder.is_dir():
                self.folder = self.folder.parent
        else:
            self.folder = pathlib.Path('.').resolve()
        os.chdir(str(self.folder))

        self.filter_string = '*'
        self.saved_files = {}
        self.get_files()

    def get_files(self):
        self.files = get_files_dict(filter_str=self.filter_string)
        self.list_new.clear()
        self.list_old.clear()
        for i in self.files:
            self.list_old.addItem(self.files[i]['old'])

    def select_files(self):
        # select files from the file list by highlighting with the mouse
        self.selected_items = self.list_old.selectedItems()
        selected_files = [i.text() for i in self.selected_items]
        if len(selected_files) != 0:
            for key in self.files:
                if self.files[key]['old'] in selected_files:
                    self.files[key]['selected'] = True
                else:
                    self.files[key]['selected'] = False

    def refresh_file_list(self):
        self.list_new.clear()
        for key, filename in self.files.items():
            if filename['selected']:
                self.list_new.addItem(filename['new'])

    def apply_filter(self):
        d = FilterDialog()
        d.show()
        if d.exec_():
            self.filter_string = d.get_values()
            self.get_files()

    def dialog_insert(self):
        self.create_dialog(insert, Ui_InsertDialog)

    def dialog_replace(self):
        self.create_dialog(find_replace, Ui_ReplaceDialog)

    def dialog_strip(self):
        self.create_dialog(strip_chars, Ui_StripDialog)

    def dialog_format(self):
        self.create_dialog(format_numbers, Ui_FormatDialog)

    def create_dialog(self, action, ui_form):
        for key, filename in self.files.items():
            if filename['selected']:
                preview_file = filename['old']
                break
        d = Dialog(ui_form, preview_file, action)
        d.show()
        if d.exec_():
            line_1_string, line_2_string = d.get_values()
            for key, filename in self.files.items():
                if filename['selected']:
                    self.files[key]['new'] = action(
                        filename['old'],
                        line_1_string,
                        line_2_string
                    )
            self.refresh_file_list()

    def undo_rename(self):
        if self.saved_files:
            undo_dict = {}
            for key, filename in self.saved_files.items():
                undo_dict[key] = filename.copy()
                undo_dict[key]['new'] = filename['old']
                undo_dict[key]['old'] = filename['new']
            rename_files(undo_dict)
            self.saved_files = {}
            print('undid', len(undo_dict), 'files')
            self.get_files()
        else:
            print('nothing to undo')

    def save_changes(self):
        copy = True if self.radioButton_copy.isChecked() else False
        self.saved_files = rename_files(self.files, copy)
        count = len(self.saved_files)
        if count > 0:
            print('saved', count, 'files')
        else:
            print('nothing to save')
        self.get_files()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = MainWindow()
    mySW.show()
    sys.exit(app.exec_())
