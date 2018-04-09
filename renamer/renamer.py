#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pathlib
import sys

from PySide import QtGui

from ui.filterdialog import Ui_FilterDialog
from ui.formatdialog import Ui_FormatDialog
from ui.insertdialog import Ui_InsertDialog
from ui.mainwindow import Ui_MainWindow
from ui.replacedialog import Ui_ReplaceDialog
from ui.stripdialog import Ui_StripDialog

from file_utils import get_files_dict, rename_files
from rename_funcs import find_replace, format_numbers, insert, strip_chars


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
        for filename in self.files.values():
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
        copy = self.radioButton_copy.isChecked()
        self.saved_files = rename_files(self.files, copy)
        count = len(self.saved_files)
        if count > 0:
            print('saved', count, 'files')
        else:
            print('nothing to save')
        self.get_files()


if __name__ == "__main__":
    # check to see if a directory or file was passed as an argument;
    # if so, change to the directory or the directory containing the file.
    if len(sys.argv) == 2:
        folder = pathlib.Path(sys.argv[1]).resolve()
        if not folder.is_dir():
            folder = folder.parent
        os.chdir(str(folder))

    app = QtGui.QApplication(sys.argv)
    mySW = MainWindow()
    mySW.show()
    sys.exit(app.exec_())
