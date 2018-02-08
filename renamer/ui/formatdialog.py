# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formatdialog.ui'
#
# Created: Tue Dec 29 23:36:05 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FormatDialog(object):
    def setupUi(self, FormatDialog):
        FormatDialog.setObjectName("FormatDialog")
        FormatDialog.resize(388, 270)
        self.button_apply = QtGui.QPushButton(FormatDialog)
        self.button_apply.setGeometry(QtCore.QRect(80, 210, 111, 31))
        self.button_apply.setObjectName("button_apply")
        self.button_cancel = QtGui.QPushButton(FormatDialog)
        self.button_cancel.setGeometry(QtCore.QRect(210, 210, 111, 31))
        self.button_cancel.setObjectName("button_cancel")
        self.label_how_many = QtGui.QLabel(FormatDialog)
        self.label_how_many.setGeometry(QtCore.QRect(90, 120, 111, 20))
        self.label_how_many.setObjectName("label_how_many")
        self.label_at_position = QtGui.QLabel(FormatDialog)
        self.label_at_position.setGeometry(QtCore.QRect(120, 160, 71, 20))
        self.label_at_position.setObjectName("label_at_position")
        self.line_2 = QtGui.QLineEdit(FormatDialog)
        self.line_2.setGeometry(QtCore.QRect(210, 150, 101, 31))
        self.line_2.setObjectName("line_2")
        self.line_1 = QtGui.QLineEdit(FormatDialog)
        self.line_1.setGeometry(QtCore.QRect(210, 110, 101, 31))
        self.line_1.setObjectName("line_1")
        self.line_old = QtGui.QLineEdit(FormatDialog)
        self.line_old.setGeometry(QtCore.QRect(90, 20, 241, 31))
        self.line_old.setObjectName("line_old")
        self.label_old = QtGui.QLabel(FormatDialog)
        self.label_old.setGeometry(QtCore.QRect(50, 30, 31, 20))
        self.label_old.setObjectName("label_old")
        self.label_new = QtGui.QLabel(FormatDialog)
        self.label_new.setGeometry(QtCore.QRect(50, 70, 31, 20))
        self.label_new.setObjectName("label_new")
        self.line_new = QtGui.QLineEdit(FormatDialog)
        self.line_new.setGeometry(QtCore.QRect(90, 60, 241, 31))
        self.line_new.setObjectName("line_new")

        self.retranslateUi(FormatDialog)
        QtCore.QMetaObject.connectSlotsByName(FormatDialog)
        FormatDialog.setTabOrder(self.line_1, self.line_2)
        FormatDialog.setTabOrder(self.line_2, self.button_apply)
        FormatDialog.setTabOrder(self.button_apply, self.button_cancel)
        FormatDialog.setTabOrder(self.button_cancel, self.line_old)
        FormatDialog.setTabOrder(self.line_old, self.line_new)

    def retranslateUi(self, FormatDialog):
        FormatDialog.setWindowTitle(QtGui.QApplication.translate("FormatDialog", "format numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.button_apply.setText(QtGui.QApplication.translate("FormatDialog", "apply", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cancel.setText(QtGui.QApplication.translate("FormatDialog", "cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_how_many.setText(QtGui.QApplication.translate("FormatDialog", "how many digits:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_at_position.setText(QtGui.QApplication.translate("FormatDialog", "at position:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_old.setText(QtGui.QApplication.translate("FormatDialog", "old:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_new.setText(QtGui.QApplication.translate("FormatDialog", "new:", None, QtGui.QApplication.UnicodeUTF8))

