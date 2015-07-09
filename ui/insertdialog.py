# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insertdialog.ui'
#
# Created: Wed Jul  8 01:01:09 2015
#      by: pyside-uic 0.2.13 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_InsertDialog(object):
    def setupUi(self, InsertDialog):
        InsertDialog.setObjectName("InsertDialog")
        InsertDialog.resize(388, 270)
        self.button_apply = QtGui.QPushButton(InsertDialog)
        self.button_apply.setGeometry(QtCore.QRect(80, 210, 111, 31))
        self.button_apply.setObjectName("button_apply")
        self.button_cancel = QtGui.QPushButton(InsertDialog)
        self.button_cancel.setGeometry(QtCore.QRect(210, 210, 111, 31))
        self.button_cancel.setObjectName("button_cancel")
        self.label_at_character = QtGui.QLabel(InsertDialog)
        self.label_at_character.setGeometry(QtCore.QRect(50, 120, 111, 20))
        self.label_at_character.setObjectName("label_at_character")
        self.label_insert_what = QtGui.QLabel(InsertDialog)
        self.label_insert_what.setGeometry(QtCore.QRect(50, 160, 71, 20))
        self.label_insert_what.setObjectName("label_insert_what")
        self.line_2 = QtGui.QLineEdit(InsertDialog)
        self.line_2.setGeometry(QtCore.QRect(140, 150, 181, 31))
        self.line_2.setObjectName("line_2")
        self.line_1 = QtGui.QLineEdit(InsertDialog)
        self.line_1.setGeometry(QtCore.QRect(220, 110, 101, 31))
        self.line_1.setObjectName("line_1")
        self.label_old = QtGui.QLabel(InsertDialog)
        self.label_old.setGeometry(QtCore.QRect(50, 30, 31, 20))
        self.label_old.setObjectName("label_old")
        self.label_new = QtGui.QLabel(InsertDialog)
        self.label_new.setGeometry(QtCore.QRect(50, 70, 31, 20))
        self.label_new.setObjectName("label_new")
        self.line_old = QtGui.QLineEdit(InsertDialog)
        self.line_old.setGeometry(QtCore.QRect(90, 20, 241, 31))
        self.line_old.setObjectName("line_old")
        self.line_new = QtGui.QLineEdit(InsertDialog)
        self.line_new.setGeometry(QtCore.QRect(90, 60, 241, 31))
        self.line_new.setObjectName("line_new")

        self.retranslateUi(InsertDialog)
        QtCore.QMetaObject.connectSlotsByName(InsertDialog)
        InsertDialog.setTabOrder(self.line_1, self.line_2)
        InsertDialog.setTabOrder(self.line_2, self.button_apply)
        InsertDialog.setTabOrder(self.button_apply, self.button_cancel)
        InsertDialog.setTabOrder(self.button_cancel, self.line_old)
        InsertDialog.setTabOrder(self.line_old, self.line_new)

    def retranslateUi(self, InsertDialog):
        InsertDialog.setWindowTitle(QtGui.QApplication.translate("InsertDialog", "insert by position", None, QtGui.QApplication.UnicodeUTF8))
        self.button_apply.setText(QtGui.QApplication.translate("InsertDialog", "apply", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cancel.setText(QtGui.QApplication.translate("InsertDialog", "cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_at_character.setText(QtGui.QApplication.translate("InsertDialog", "insert at character:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_insert_what.setText(QtGui.QApplication.translate("InsertDialog", "insert what:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_old.setText(QtGui.QApplication.translate("InsertDialog", "old:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_new.setText(QtGui.QApplication.translate("InsertDialog", "new:", None, QtGui.QApplication.UnicodeUTF8))

