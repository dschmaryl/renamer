# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu May 17 17:39:31 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 506)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_oold = QtGui.QLabel(self.centralwidget)
        self.label_oold.setGeometry(QtCore.QRect(30, 10, 101, 20))
        self.label_oold.setObjectName("label_oold")
        self.list_old = QtGui.QListWidget(self.centralwidget)
        self.list_old.setGeometry(QtCore.QRect(20, 30, 281, 311))
        self.list_old.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.list_old.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.list_old.setObjectName("list_old")
        self.label_new = QtGui.QLabel(self.centralwidget)
        self.label_new.setGeometry(QtCore.QRect(320, 10, 81, 20))
        self.label_new.setObjectName("label_new")
        self.list_new = QtGui.QListWidget(self.centralwidget)
        self.list_new.setGeometry(QtCore.QRect(310, 30, 281, 311))
        self.list_new.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.list_new.setObjectName("list_new")
        self.button_insert = QtGui.QPushButton(self.centralwidget)
        self.button_insert.setGeometry(QtCore.QRect(30, 410, 111, 31))
        self.button_insert.setObjectName("button_insert")
        self.button_save = QtGui.QPushButton(self.centralwidget)
        self.button_save.setGeometry(QtCore.QRect(340, 450, 111, 31))
        self.button_save.setObjectName("button_save")
        self.button_replace = QtGui.QPushButton(self.centralwidget)
        self.button_replace.setGeometry(QtCore.QRect(30, 450, 111, 31))
        self.button_replace.setObjectName("button_replace")
        self.button_exit = QtGui.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(470, 450, 111, 31))
        self.button_exit.setObjectName("button_exit")
        self.button_undo = QtGui.QPushButton(self.centralwidget)
        self.button_undo.setGeometry(QtCore.QRect(170, 360, 111, 31))
        self.button_undo.setObjectName("button_undo")
        self.button_strip = QtGui.QPushButton(self.centralwidget)
        self.button_strip.setGeometry(QtCore.QRect(170, 410, 111, 31))
        self.button_strip.setObjectName("button_strip")
        self.button_format = QtGui.QPushButton(self.centralwidget)
        self.button_format.setGeometry(QtCore.QRect(170, 450, 111, 31))
        self.button_format.setObjectName("button_format")
        self.button_filter = QtGui.QPushButton(self.centralwidget)
        self.button_filter.setGeometry(QtCore.QRect(30, 360, 111, 31))
        self.button_filter.setObjectName("button_filter")
        self.radioButton_move = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_move.setGeometry(QtCore.QRect(460, 360, 91, 20))
        self.radioButton_move.setChecked(True)
        self.radioButton_move.setObjectName("radioButton_move")
        self.radioButton_copy = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_copy.setGeometry(QtCore.QRect(460, 380, 111, 20))
        self.radioButton_copy.setObjectName("radioButton_copy")
        self.label_rename_by = QtGui.QLabel(self.centralwidget)
        self.label_rename_by.setGeometry(QtCore.QRect(360, 380, 71, 20))
        self.label_rename_by.setObjectName("label_rename_by")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.button_filter, self.button_undo)
        MainWindow.setTabOrder(self.button_undo, self.button_insert)
        MainWindow.setTabOrder(self.button_insert, self.button_strip)
        MainWindow.setTabOrder(self.button_strip, self.button_replace)
        MainWindow.setTabOrder(self.button_replace, self.button_format)
        MainWindow.setTabOrder(self.button_format, self.radioButton_move)
        MainWindow.setTabOrder(self.radioButton_move, self.radioButton_copy)
        MainWindow.setTabOrder(self.radioButton_copy, self.button_save)
        MainWindow.setTabOrder(self.button_save, self.button_exit)
        MainWindow.setTabOrder(self.button_exit, self.list_old)
        MainWindow.setTabOrder(self.list_old, self.list_new)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "renamer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_oold.setText(QtGui.QApplication.translate("MainWindow", "old names:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_new.setText(QtGui.QApplication.translate("MainWindow", "new names:", None, QtGui.QApplication.UnicodeUTF8))
        self.button_insert.setText(QtGui.QApplication.translate("MainWindow", "insert by position", None, QtGui.QApplication.UnicodeUTF8))
        self.button_save.setText(QtGui.QApplication.translate("MainWindow", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.button_replace.setText(QtGui.QApplication.translate("MainWindow", "find and replace", None, QtGui.QApplication.UnicodeUTF8))
        self.button_exit.setText(QtGui.QApplication.translate("MainWindow", "exit", None, QtGui.QApplication.UnicodeUTF8))
        self.button_undo.setText(QtGui.QApplication.translate("MainWindow", "undo last", None, QtGui.QApplication.UnicodeUTF8))
        self.button_strip.setText(QtGui.QApplication.translate("MainWindow", "strip characters", None, QtGui.QApplication.UnicodeUTF8))
        self.button_format.setText(QtGui.QApplication.translate("MainWindow", "format numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.button_filter.setText(QtGui.QApplication.translate("MainWindow", "filter list", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_move.setText(QtGui.QApplication.translate("MainWindow", "moving files", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_copy.setText(QtGui.QApplication.translate("MainWindow", "creating copies", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rename_by.setText(QtGui.QApplication.translate("MainWindow", "rename by:", None, QtGui.QApplication.UnicodeUTF8))

