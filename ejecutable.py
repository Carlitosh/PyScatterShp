#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, uic

import matplotlib.pyplot as plt
import numpy as np
from read_file import atrib,read_shp
from front_end import Ui_MainWindow


# Cargar nuestro archivo .ui
#form_class = uic.loadUiType("front_end.ui")[0]

class scatter_shp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		
		#===============================================================
		self.button_abrir.clicked.connect(self.abrir)
		self.button_procesar.clicked.connect(self.procesar)
		
		
		self.mplwidget.axes.grid(True)
		self.mplwidget.axes.axis((0,300,0,400))
		
		#===============================================================
	
	def abrir(self):
		self.comboBox_x.clear()
		self.comboBox_y.clear()
		
		mapa = QtGui.QFileDialog.getOpenFileName(self, 'Abrir Capa vectorial', 
		'','(*.shp)')
		self.lineEdit_abrir.setText(str(mapa))
		mps = str(self.lineEdit_abrir.text())
		mapa1 = str(mps)
		atributo = atrib(mapa1)
		self.comboBox_x.addItems(atributo)
		self.comboBox_y.addItems(atributo)
		return mapa

	
	#===============================================================
	def procesar(self):		
		
		x = str(self.comboBox_x.currentText())
		y = str(self.comboBox_y.currentText())
		mps = str(self.lineEdit_abrir.text())
		hor = read_shp(mps,x,y)[0]
		vert = read_shp(mps,x,y)[1]
		self.mplwidget.axes.grid(True)
		self.mplwidget.axes.plot(hor,vert,'o')
		#self.mplwidget.axes.set_title('Historical Opening/Closing Prices')
		
		self.mplwidget.axes.set_xlabel(x)
		self.mplwidget.axes.set_ylabel(y)
		self.mplwidget.draw()
		self.mplwidget.axes.grid(True)
		
		
		
	#===============================================================		
	

app = QtGui.QApplication(sys.argv)
ejemplo = scatter_shp(None)
ejemplo.show()
app.exec_()			
	




