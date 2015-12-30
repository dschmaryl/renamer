# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filterdialog.ui'
#
# Created: Tue Dec 29 21:04:34 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FilterDialog(object):
    def setupUi(self, FilterDialog):
        FilterDialog.setObjectName("FilterDialog")
        FilterDialog.resize(366, 210)
        self.button_apply = QtGui.QPushButton(FilterDialog)
        self.button_apply.setGeometry(QtCore.QRect(70, 150, 111, 31))
        self.button_apply.setObjectName("button_apply")
        self.button_cancel = QtGui.QPushButton(FilterDialog)
        self.button_cancel.setGeometry(QtCore.QRect(200, 150, 111, 31))
        self.button_cancel.setObjectName("button_cancel")
        self.label_string = QtGui.QLabel(FilterDialog)
        self.label_string.setGeometry(QtCore.QRect(60, 100, 81, 20))
        self.label_string.setObjectName("label_string")
        self.line_string = QtGui.QLineEdit(FilterDialog)
        self.line_string.setGeometry(QtCore.QRect(150, 90, 171, 31))
        self.line_string.setObjectName("line_string")
        self.radioButton_files = QtGui.QRadioButton(FilterDialog)
        self.radioButton_files.setGeometry(QtCore.QRect(160, 30, 91, 20))
        self.radioButton_files.setChecked(True)
        self.radioButton_files.setObjectName("radioButton_files")
        self.radioButton_folders = QtGui.QRadioButton(FilterDialog)
        self.radioButton_folders.setGeometry(QtCore.QRect(160, 50, 111, 20))
        self.radioButton_folders.setObjectName("radioButton_folders")
        self.label_show = QtGui.QLabel(FilterDialog)
        self.label_show.setGeometry(QtCore.QRect(70, 50, 71, 20))
        self.label_show.setObjectName("label_show")

        self.retranslateUi(FilterDialog)
        QtCore.QMetaObject.connectSlotsByName(FilterDialog)
        FilterDialog.setTabOrder(self.line_string, self.button_apply)
        FilterDialog.setTabOrder(self.button_apply, self.button_cancel)
        FilterDialog.setTabOrder(self.button_cancel, self.radioButton_files)
        FilterDialog.setTabOrder(self.radioButton_files, self.radioButton_folders)

    def retranslateUi(self, FilterDialog):
        FilterDialog.setWindowTitle(QtGui.QApplication.translate("FilterDialog", "filter", None, QtGui.QApplication.UnicodeUTF8))
        self.button_apply.setText(QtGui.QApplication.translate("FilterDialog", "apply", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cancel.setText(QtGui.QApplication.translate("FilterDialog", "cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_string.setText(QtGui.QApplication.translate("FilterDialog", "filter string:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_files.setText(QtGui.QApplication.translate("FilterDialog", "files", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_folders.setText(QtGui.QApplication.translate("FilterDialog", "folders", None, QtGui.QApplication.UnicodeUTF8))
        self.label_show.setText(QtGui.QApplication.translate("FilterDialog", "show only:", None, QtGui.QApplication.UnicodeUTF8))

