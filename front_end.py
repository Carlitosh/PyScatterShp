# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front_end.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(532, 568)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.button_procesar = QtGui.QPushButton(self.centralwidget)
        self.button_procesar.setGeometry(QtCore.QRect(420, 130, 75, 23))
        self.button_procesar.setObjectName(_fromUtf8("button_procesar"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 160, 521, 411))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.mplwidget = MatplotlibWidget(self.groupBox)
        self.mplwidget.setGeometry(QtCore.QRect(20, 20, 491, 371))
        self.mplwidget.setObjectName(_fromUtf8("mplwidget"))
        self.lineEdit_abrir = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_abrir.setGeometry(QtCore.QRect(120, 40, 311, 20))
        self.lineEdit_abrir.setObjectName(_fromUtf8("lineEdit_abrir"))
        self.comboBox_x = QtGui.QComboBox(self.centralwidget)
        self.comboBox_x.setGeometry(QtCore.QRect(60, 100, 241, 22))
        self.comboBox_x.setObjectName(_fromUtf8("comboBox_x"))
        self.comboBox_y = QtGui.QComboBox(self.centralwidget)
        self.comboBox_y.setGeometry(QtCore.QRect(60, 130, 241, 22))
        self.comboBox_y.setObjectName(_fromUtf8("comboBox_y"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 100, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.button_abrir = QtGui.QPushButton(self.centralwidget)
        self.button_abrir.setGeometry(QtCore.QRect(440, 40, 75, 23))
        self.button_abrir.setObjectName(_fromUtf8("button_abrir"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Scatter Shp", None))
        self.button_procesar.setText(_translate("MainWindow", "Procesar", None))
        self.groupBox.setTitle(_translate("MainWindow", "Grafico", None))
        self.label.setText(_translate("MainWindow", "X", None))
        self.label_2.setText(_translate("MainWindow", "Y", None))
        self.button_abrir.setText(_translate("MainWindow", "Abrir .Shp", None))
        self.label_3.setText(_translate("MainWindow", "Abrir .shp de puntos", None))

from matplotlibwidget import MatplotlibWidget
