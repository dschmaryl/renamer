from sys import argv, exit
from PySide import QtGui, QtCore

from futils import futils

from ui.mainwindow    import Ui_MainWindow
from ui.insertdialog  import Ui_InsertDialog
from ui.replacedialog import Ui_ReplaceDialog
from ui.stripdialog   import Ui_StripDialog
from ui.formatdialog  import Ui_FormatDialog
from ui.filterdialog  import Ui_FilterDialog



def find_replace(old_name, find_string, replace_string):
    if find_string not in old_name:
        return None
    return old_name.replace(find_string, replace_string)


def insert(old_name, insert_position, insert_string):
    if not insert_string:
        return None
    if not insert_position:
        position_int = 0
    else:
        try:
            position_int = max(0, int(insert_position) - 1)
        except ValueError:
            return None
    return old_name[:position_int] + insert_string + old_name[position_int:]


def strip_chars(old_name, strip_position, strip_length):
    try:
        strip_int = max(0, int(strip_length))
    except ValueError:
        return None
    if not strip_position:
        position_int = 0
    else:
        try:
            position_int = max(0, int(strip_position) - 1)
        except ValueError:
            return None
    return old_name[:position_int] + old_name[position_int + strip_int:]


def format_numbers(old_name, format_length, format_position):
    if not format_length:
        length_int = 2
    else:
        try:
            length_int = min(max(2, int(format_length)), 6)
        except ValueError:
            return None
    format_string = '%0' + str(length_int) + 'd'

    if not format_position:
        position_int = 0
    else:
        try:
            position_int = max(0, int(format_position) - 1)
        except ValueError:
            return None
    piece1 = old_name[:position_int]
    piece2 = old_name[position_int:]
    old_number = ''
    for i in range(length_int):
        if piece2[i].isdigit():
            old_number += piece2[i]
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
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.button_cancel.clicked.connect(self.close)
        self.button_apply.clicked.connect(self.accept)
        self.radioButton_folders.toggled.connect(self.radio_button)
    folders_too = False

    def radio_button(self):
        if self.radioButton_folders.isChecked():
            self.folders_too = True
            print 'set to true'
        else:
            self.folders_too = False

    def get_values(self):
        return self.line_string.text(), self.folders_too



class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.button_filter.clicked.connect(self.apply_filter)
        self.button_insert.clicked.connect(self.dialog_insert)
        self.button_replace.clicked.connect(self.dialog_replace)
        self.button_strip.clicked.connect(self.dialog_strip)
        self.button_format.clicked.connect(self.dia_format)
        self.button_undo.clicked.connect(self.undo_rename)
        self.button_save.clicked.connect(self.save_changes)
        self.button_exit.clicked.connect(self.close)
        self.list_old.itemSelectionChanged.connect(self.select_files)
        self.get_files()


    def get_files(self, filter_string=None):
        self.files = futils.get_dict('./', filter_str=filter_string)
        self.list_new.clear()
        self.list_old.clear()
        for i in self.files:
            self.list_old.addItem(self.files[i]['old'])


    def select_files(self):
        self.selected_items = self.list_old.selectedItems()
        selected_files = [i.text() for i in self.selected_items]
        if len(selected_files) != 0:
            for i in self.files:
                if self.files[i]['old'] in selected_files:
                    self.files[i]['selected'] = True
                else:
                    self.files[i]['selected'] = False


    def refresh_file_list(self):
        self.list_new.clear()

        for i in self.files:
            if self.files[i]['selected'] == True:
                if self.files[i]['new']:
                    self.list_new.addItem(self.files[i]['new'])


    def apply_filter(self):
        d = FilterDialog()
        d.show()
        if d.exec_():
            filter_string, folders_too = d.get_values()
            self.get_files(filter_string)


    def dialog_insert(self):
        self.create_dialog(insert, Ui_InsertDialog)


    def dialog_replace(self):
        self.create_dialog(find_replace, Ui_ReplaceDialog)


    def dialog_strip(self):
        self.create_dialog(strip_chars, Ui_StripDialog)


    def dia_format(self):
        self.create_dialog(format_numbers, Ui_FormatDialog)


    def create_dialog(self, action, ui_form):
        #self.select_files()
        for i in self.files:
            if self.files[i]['selected'] == True:
                preview_file = self.files[i]['old']
                break
        d = Dialog(ui_form, preview_file, action)
        d.show()

        if d.exec_():
            line_1_string, line_2_string = d.get_values()
            for i in self.files:
                if self.files[i]['selected'] == True:
                    self.files[i]['new'] = action(
                        self.files[i]['old'],
                        line_1_string,
                        line_2_string)
            self.refresh_file_list()


    def undo_rename(self):
        if self.saved_files:
            undo_dict = {}
            for i in self.saved_files:
                undo_dict[i] = self.saved_files[i].copy()
                undo_dict[i]['new'] = self.saved_files[i]['old']
                undo_dict[i]['old'] = self.saved_files[i]['new']
            futils.rename_files(undo_dict)
            self.get_files()


    def save_changes(self):
        copy = False
        if self.radioButton_copy.isChecked():
            copy = True
        self.saved_files = futils.rename_files(self.files, copy)
        self.get_files()



if __name__ == "__main__":

    app = QtGui.QApplication(argv)
    mySW = MainWindow()
    mySW.show()
    exit(app.exec_())
