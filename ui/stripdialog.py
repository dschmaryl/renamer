# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stripdialog.ui'
#
# Created: Wed Jul  8 01:01:09 2015
#      by: pyside-uic 0.2.13 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_StripDialog(object):
    def setupUi(self, StripDialog):
        StripDialog.setObjectName("StripDialog")
        StripDialog.resize(388, 270)
        self.button_apply = QtGui.QPushButton(StripDialog)
        self.button_apply.setGeometry(QtCore.QRect(80, 210, 111, 31))
        self.button_apply.setObjectName("button_apply")
        self.button_cancel = QtGui.QPushButton(StripDialog)
        self.button_cancel.setGeometry(QtCore.QRect(210, 210, 111, 31))
        self.button_cancel.setObjectName("button_cancel")
        self.label_start_at = QtGui.QLabel(StripDialog)
        self.label_start_at.setGeometry(QtCore.QRect(80, 120, 111, 20))
        self.label_start_at.setObjectName("label_start_at")
        self.label_how_many = QtGui.QLabel(StripDialog)
        self.label_how_many.setGeometry(QtCore.QRect(90, 160, 91, 20))
        self.label_how_many.setObjectName("label_how_many")
        self.line_2 = QtGui.QLineEdit(StripDialog)
        self.line_2.setGeometry(QtCore.QRect(210, 150, 101, 31))
        self.line_2.setObjectName("line_2")
        self.line_1 = QtGui.QLineEdit(StripDialog)
        self.line_1.setGeometry(QtCore.QRect(210, 110, 101, 31))
        self.line_1.setObjectName("line_1")
        self.label_old = QtGui.QLabel(StripDialog)
        self.label_old.setGeometry(QtCore.QRect(50, 30, 31, 20))
        self.label_old.setObjectName("label_old")
        self.label_new = QtGui.QLabel(StripDialog)
        self.label_new.setGeometry(QtCore.QRect(50, 70, 31, 20))
        self.label_new.setObjectName("label_new")
        self.line_old = QtGui.QLineEdit(StripDialog)
        self.line_old.setGeometry(QtCore.QRect(90, 20, 241, 31))
        self.line_old.setObjectName("line_old")
        self.line_new = QtGui.QLineEdit(StripDialog)
        self.line_new.setGeometry(QtCore.QRect(90, 60, 241, 31))
        self.line_new.setObjectName("line_new")

        self.retranslateUi(StripDialog)
        QtCore.QMetaObject.connectSlotsByName(StripDialog)
        StripDialog.setTabOrder(self.line_1, self.line_2)
        StripDialog.setTabOrder(self.line_2, self.button_apply)
        StripDialog.setTabOrder(self.button_apply, self.button_cancel)
        StripDialog.setTabOrder(self.button_cancel, self.line_old)
        StripDialog.setTabOrder(self.line_old, self.line_new)

    def retranslateUi(self, StripDialog):
        StripDialog.setWindowTitle(QtGui.QApplication.translate("StripDialog", "strip characters", None, QtGui.QApplication.UnicodeUTF8))
        self.button_apply.setText(QtGui.QApplication.translate("StripDialog", "apply", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cancel.setText(QtGui.QApplication.translate("StripDialog", "cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_start_at.setText(QtGui.QApplication.translate("StripDialog", "start at character:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_how_many.setText(QtGui.QApplication.translate("StripDialog", "strip how many:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_old.setText(QtGui.QApplication.translate("StripDialog", "old:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_new.setText(QtGui.QApplication.translate("StripDialog", "new:", None, QtGui.QApplication.UnicodeUTF8))

