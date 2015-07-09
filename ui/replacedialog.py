# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'replacedialog.ui'
#
# Created: Wed Jul  8 01:01:09 2015
#      by: pyside-uic 0.2.13 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ReplaceDialog(object):
    def setupUi(self, ReplaceDialog):
        ReplaceDialog.setObjectName("ReplaceDialog")
        ReplaceDialog.resize(388, 270)
        self.button_apply = QtGui.QPushButton(ReplaceDialog)
        self.button_apply.setGeometry(QtCore.QRect(80, 210, 111, 31))
        self.button_apply.setObjectName("button_apply")
        self.button_cancel = QtGui.QPushButton(ReplaceDialog)
        self.button_cancel.setGeometry(QtCore.QRect(210, 210, 111, 31))
        self.button_cancel.setObjectName("button_cancel")
        self.label_find = QtGui.QLabel(ReplaceDialog)
        self.label_find.setGeometry(QtCore.QRect(100, 120, 31, 20))
        self.label_find.setObjectName("label_find")
        self.label_replace = QtGui.QLabel(ReplaceDialog)
        self.label_replace.setGeometry(QtCore.QRect(80, 160, 51, 20))
        self.label_replace.setObjectName("label_replace")
        self.line_2 = QtGui.QLineEdit(ReplaceDialog)
        self.line_2.setGeometry(QtCore.QRect(140, 150, 181, 31))
        self.line_2.setObjectName("line_2")
        self.line_1 = QtGui.QLineEdit(ReplaceDialog)
        self.line_1.setGeometry(QtCore.QRect(140, 110, 181, 31))
        self.line_1.setObjectName("line_1")
        self.label_old = QtGui.QLabel(ReplaceDialog)
        self.label_old.setGeometry(QtCore.QRect(50, 30, 31, 20))
        self.label_old.setObjectName("label_old")
        self.label_new = QtGui.QLabel(ReplaceDialog)
        self.label_new.setGeometry(QtCore.QRect(50, 70, 31, 20))
        self.label_new.setObjectName("label_new")
        self.line_old = QtGui.QLineEdit(ReplaceDialog)
        self.line_old.setGeometry(QtCore.QRect(90, 20, 241, 31))
        self.line_old.setObjectName("line_old")
        self.line_new = QtGui.QLineEdit(ReplaceDialog)
        self.line_new.setGeometry(QtCore.QRect(90, 60, 241, 31))
        self.line_new.setObjectName("line_new")

        self.retranslateUi(ReplaceDialog)
        QtCore.QMetaObject.connectSlotsByName(ReplaceDialog)
        ReplaceDialog.setTabOrder(self.line_1, self.line_2)
        ReplaceDialog.setTabOrder(self.line_2, self.button_apply)
        ReplaceDialog.setTabOrder(self.button_apply, self.button_cancel)
        ReplaceDialog.setTabOrder(self.button_cancel, self.line_old)
        ReplaceDialog.setTabOrder(self.line_old, self.line_new)

    def retranslateUi(self, ReplaceDialog):
        ReplaceDialog.setWindowTitle(QtGui.QApplication.translate("ReplaceDialog", "find and replace", None, QtGui.QApplication.UnicodeUTF8))
        self.button_apply.setText(QtGui.QApplication.translate("ReplaceDialog", "apply", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cancel.setText(QtGui.QApplication.translate("ReplaceDialog", "cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_find.setText(QtGui.QApplication.translate("ReplaceDialog", "find:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_replace.setText(QtGui.QApplication.translate("ReplaceDialog", "replace:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_old.setText(QtGui.QApplication.translate("ReplaceDialog", "old:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_new.setText(QtGui.QApplication.translate("ReplaceDialog", "new:", None, QtGui.QApplication.UnicodeUTF8))

