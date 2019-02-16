# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontwin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import os
import osgeo
from osgeo import ogr,osr
import operator
import sys
import gdal
import ogr
import io
import osgeo
import os
from osgeo import gdalnumeric
from osgeo import gdal_array 
from osgeo.gdalconst import *
import operator
import math
import numpy as np
from math import sqrt
gdal.AllRegister()

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
    unionfile_path=''
    gridfile_path=''
    outputfile_path=''
    hei_name=''
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(631, 428)
        MainWindow.setStyleSheet(_fromUtf8("QDialog{\n"
"color:navy; background-color: white;\n"
"\n"
"                     \n"
"}\n"
"QRadioButton{\n"
"color:navy;\n"
"}\n"
"QLabel{\n"
"color: navy; \n"
"                        \n"
"                        selection-color: yellow;\n"
"                        selection-background-color: blue;\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
" border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 140, 191, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.Browse1 = QtGui.QPushButton(self.centralwidget)
        self.Browse1.setGeometry(QtCore.QRect(510, 140, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Browse1.setFont(font)
        self.Browse1.setObjectName(_fromUtf8("Browse1"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 140, 211, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 30, 401, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.WRF_btn = QtGui.QPushButton(self.centralwidget)
        self.WRF_btn.setGeometry(QtCore.QRect(260, 350, 171, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.WRF_btn.setFont(font)
        self.WRF_btn.setObjectName(_fromUtf8("WRF_btn"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 190, 191, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 190, 211, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.Browse2 = QtGui.QPushButton(self.centralwidget)
        self.Browse2.setGeometry(QtCore.QRect(510, 190, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Browse2.setFont(font)
        self.Browse2.setObjectName(_fromUtf8("Browse2"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 240, 191, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(280, 240, 211, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.Browse3 = QtGui.QPushButton(self.centralwidget)
        self.Browse3.setGeometry(QtCore.QRect(510, 240, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Browse3.setFont(font)
        self.Browse3.setObjectName(_fromUtf8("Browse3"))
        self.heichoice1 = QtGui.QRadioButton(self.centralwidget)
        self.heichoice1.setGeometry(QtCore.QRect(150, 290, 171, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.heichoice1.setFont(font)
        self.heichoice1.setObjectName(_fromUtf8("heichoice1"))
        self.heichoice2 = QtGui.QRadioButton(self.centralwidget)
        self.heichoice2.setGeometry(QtCore.QRect(400, 297, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.heichoice2.setFont(font)
        self.heichoice2.setObjectName(_fromUtf8("heichoice2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuShapefile_Generator = QtGui.QMenu(self.menubar)
        self.menuShapefile_Generator.setObjectName(_fromUtf8("menuShapefile_Generator"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLine_Generator = QtGui.QAction(MainWindow)
        self.actionLine_Generator.setObjectName(_fromUtf8("actionLine_Generator"))
        self.FrontalArea = QtGui.QAction(MainWindow)
        self.FrontalArea.setObjectName(_fromUtf8("FrontalArea"))
        self.actionNeed_Help = QtGui.QAction(MainWindow)
        self.actionNeed_Help.setObjectName(_fromUtf8("actionNeed_Help"))
        self.actionAbout_WRF_UME = QtGui.QAction(MainWindow)
        self.actionAbout_WRF_UME.setObjectName(_fromUtf8("actionAbout_WRF_UME"))
        self.actionBuiding_s_Elevation = QtGui.QAction(MainWindow)
        self.actionBuiding_s_Elevation.setObjectName(_fromUtf8("actionBuiding_s_Elevation"))
        self.menuShapefile_Generator.addAction(self.actionLine_Generator)
        self.menuShapefile_Generator.addAction(self.FrontalArea)
        self.menuShapefile_Generator.addAction(self.actionBuiding_s_Elevation)
        self.menuHelp.addAction(self.actionNeed_Help)
        self.menuHelp.addAction(self.actionAbout_WRF_UME)
        self.menubar.addAction(self.menuShapefile_Generator.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionNeed_Help.triggered.connect(self.myfunc_Needhelp)
        self.actionAbout_WRF_UME.triggered.connect(self.myfunc_AboutWRF)
        self.actionLine_Generator.triggered.connect(self.myfunc_WGL)
        self.actionBuiding_s_Elevation.triggered.connect(self.myfunc_ELEV)
        QtCore.QObject.connect(self.Browse1,QtCore.SIGNAL("clicked()"),self.footprint_browse)
        QtCore.QObject.connect(self.Browse2,QtCore.SIGNAL("clicked()"),self.grid_browse)
        QtCore.QObject.connect(self.Browse3,QtCore.SIGNAL("clicked()"),self.output_browse)
        self.FrontalArea.triggered.connect(self.myfunc_CFA)
        QtCore.QObject.connect(self.WRF_btn,QtCore.SIGNAL("clicked()"),self.myfunc_WRF)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Select the Union Shapefile:", None))
        self.Browse1.setText(_translate("MainWindow", "Browse", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">WRF-UME EXTRACTOR</span></p></body></html>", None))
        self.WRF_btn.setText(_translate("MainWindow", "WRF Parameters", None))
        self.label_3.setText(_translate("MainWindow", "Select the Grid Shapefile:", None))
        self.Browse2.setText(_translate("MainWindow", "Browse", None))
        self.label_4.setText(_translate("MainWindow", "Select the output files location:", None))
        self.Browse3.setText(_translate("MainWindow", "Browse", None))
        self.heichoice1.setText(_translate("MainWindow", "Building\'s Elevated Height", None))
        self.heichoice2.setText(_translate("MainWindow", "Buildings Height", None))
        self.menuShapefile_Generator.setTitle(_translate("MainWindow", "Others", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionLine_Generator.setText(_translate("MainWindow", "Wind Lines Creation", None))
        self.FrontalArea.setText(_translate("MainWindow", "Frontal Area", None))
        self.actionNeed_Help.setText(_translate("MainWindow", "Need Help", None))
        self.actionAbout_WRF_UME.setText(_translate("MainWindow", "About WRF-UME", None))
        self.actionBuiding_s_Elevation.setText(_translate("MainWindow", "Buiding\'s Elevation", None))


    def footprint_browse(self):
        print ('selecting folder containing building union shapefile ')
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home',filter= '*.shp')
        #Ui_MainWindow.footprint_path = self.fname.replace('\\','/')
        Ui_MainWindow.unionfile_path = self.fname.replace('\\','/')
        self.lineEdit.setText(self.fname)
        print(Ui_MainWindow.unionfile_path)

    def grid_browse(self):
        print ('selecting folder containing Grid shape file ')
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home',filter= '*.shp')
        Ui_MainWindow.gridfile_path = self.fname.replace('\\','/')
        self.lineEdit_2.setText(self.fname)
        print(Ui_MainWindow.gridfile_path)

    def output_browse(self):
        print ('selecting folder containing output text file')
        #self.fname = QtGui.QFileDialog.getSaveFileName(None, 'Save file','/home',filter = '*.txt')
        self.fname = QtGui.QFileDialog.getExistingDirectory(None, "Select Directory for saving output files")
        Ui_MainWindow.outputfile_path = self.fname.replace('\\','/')
        self.lineEdit_3.setText(self.fname)
        print(Ui_MainWindow.outputfile_path)

    def myfunc_Needhelp(self):
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog_Needhelp()
        ui.setupUi(Dialog)
        Dialog.exec_()

    def myfunc_AboutWRF(self):
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog_AboutWRF()
        ui.setupUi(Dialog)
        Dialog.exec_()

    def myfunc_WGL(self):
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog_WGL()
        ui.setupUi(Dialog)
        Dialog.exec_()

    def myfunc_CFA(self):
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog_CFA()
        ui.setupUi(Dialog)
        Dialog.exec_()

    def myfunc_ELEV(self):
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog_ELEV()
        ui.setupUi(Dialog)
        Dialog.exec_()

    def myfunc_WRF(self):
        if self.heichoice1.isChecked()== True:
            Ui_MainWindow.hei_name='Height'
        if self.heichoice2.isChecked()== True:
            Ui_MainWindow.hei_name='buildh'
        Dialog = QtGui.QDialog()
        ui1 = Ui_Dialog_WRF()
        ui1.setupUi(Dialog)
        Dialog.exec_()

class Ui_Dialog_WRF(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(654, 479)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        Dialog.setStyleSheet(_fromUtf8("QDialog{\n"
"color:navy; background-color: white;\n"
"\n"
"                     \n"
"}\n"
"QLabel{\n"
"color: navy; \n"
"                        \n"
"                        selection-color: yellow;\n"
"                        selection-background-color: blue;\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
" border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"#
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
""))
        self.frontal_area_btn = QtGui.QPushButton(Dialog)
        self.frontal_area_btn.setGeometry(QtCore.QRect(390, 60, 231, 21))
        self.frontal_area_btn.setObjectName(_fromUtf8("frontal_area_btn"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 0, 401, 51))
        self.label.setObjectName(_fromUtf8("label"))
        self.hwratio_btn = QtGui.QPushButton(Dialog)
        self.hwratio_btn.setGeometry(QtCore.QRect(390, 380, 231, 21))
        self.hwratio_btn.setObjectName(_fromUtf8("hwratio_btn"))
        self.svf_btn = QtGui.QPushButton(Dialog)
        self.svf_btn.setGeometry(QtCore.QRect(20, 420, 231, 21))
        self.svf_btn.setObjectName(_fromUtf8("svf_btn"))
        self.FAD_btn = QtGui.QPushButton(Dialog)
        self.FAD_btn.setGeometry(QtCore.QRect(390, 100, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.FAD_btn.setFont(font)
        self.FAD_btn.setObjectName(_fromUtf8("FAD_btn"))
        self.Planareadensity = QtGui.QPushButton(Dialog)
        self.Planareadensity.setGeometry(QtCore.QRect(20, 260, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Planareadensity.setFont(font)
        self.Planareadensity.setObjectName(_fromUtf8("Planareadensity"))
        self.Roofareadensity = QtGui.QPushButton(Dialog)
        self.Roofareadensity.setGeometry(QtCore.QRect(20, 340, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Roofareadensity.setFont(font)
        self.Roofareadensity.setObjectName(_fromUtf8("Roofareadensity"))
        self.Planareafraction = QtGui.QPushButton(Dialog)
        self.Planareafraction.setGeometry(QtCore.QRect(20, 220, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Planareafraction.setFont(font)
        self.Planareafraction.setObjectName(_fromUtf8("Planareafraction"))
        self.Meanbuildingheight = QtGui.QPushButton(Dialog)
        self.Meanbuildingheight.setGeometry(QtCore.QRect(20, 60, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Meanbuildingheight.setFont(font)
        self.Meanbuildingheight.setObjectName(_fromUtf8("Meanbuildingheight"))
        self.SDBV = QtGui.QPushButton(Dialog)
        self.SDBV.setGeometry(QtCore.QRect(20, 100, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SDBV.setFont(font)
        self.SDBV.setObjectName(_fromUtf8("SDBV"))
        self.MBH = QtGui.QPushButton(Dialog)
        self.MBH.setGeometry(QtCore.QRect(20, 140, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.MBH.setFont(font)
        self.MBH.setObjectName(_fromUtf8("MBH"))
        self.PAR = QtGui.QPushButton(Dialog)
        self.PAR.setGeometry(QtCore.QRect(20, 300, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PAR.setFont(font)
        self.PAR.setObjectName(_fromUtf8("PAR"))
        self.CAR = QtGui.QPushButton(Dialog)
        self.CAR.setGeometry(QtCore.QRect(20, 380, 231, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CAR.setFont(font)
        self.CAR.setObjectName(_fromUtf8("CAR"))
        self.GORL = QtGui.QPushButton(Dialog)
        self.GORL.setGeometry(QtCore.QRect(390, 140, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GORL.setFont(font)
        self.GORL.setObjectName(_fromUtf8("GORL"))
        self.GODH = QtGui.QPushButton(Dialog)
        self.GODH.setGeometry(QtCore.QRect(390, 180, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GODH.setFont(font)
        self.GODH.setObjectName(_fromUtf8("GODH"))
        self.RRL = QtGui.QPushButton(Dialog)
        self.RRL.setGeometry(QtCore.QRect(390, 220, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RRL.setFont(font)
        self.RRL.setObjectName(_fromUtf8("RRL"))
        self.RDH = QtGui.QPushButton(Dialog)
        self.RDH.setGeometry(QtCore.QRect(390, 260, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RDH.setFont(font)
        self.RDH.setObjectName(_fromUtf8("RDH"))
        self.MRL = QtGui.QPushButton(Dialog)
        self.MRL.setGeometry(QtCore.QRect(390, 300, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.MRL.setFont(font)
        self.MRL.setObjectName(_fromUtf8("MRL"))
        self.MDH = QtGui.QPushButton(Dialog)
        self.MDH.setGeometry(QtCore.QRect(390, 340, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.MDH.setFont(font)
        self.MDH.setObjectName(_fromUtf8("MDH"))
        self.Volumetric_height_btn = QtGui.QPushButton(Dialog)
        self.Volumetric_height_btn.setGeometry(QtCore.QRect(20, 180, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Volumetric_height_btn.setFont(font)
        self.Volumetric_height_btn.setObjectName(_fromUtf8("Volumetric_height_btn"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.Meanbuildingheight, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Mean_Building_Height)
        QtCore.QObject.connect(self.SDBV, QtCore.SIGNAL(_fromUtf8("clicked()")), self.SD_Building_Height)
        QtCore.QObject.connect(self.Planareafraction, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cal_PAF)
        QtCore.QObject.connect(self.Planareadensity, QtCore.SIGNAL(_fromUtf8("clicked()")), self.myfunc_PAFD) 
        QtCore.QObject.connect(self.MBH, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Area_weighted_MBH)
        QtCore.QObject.connect(self.Volumetric_height_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Volumetric_Height)
        QtCore.QObject.connect(self.CAR, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Complete_Aspect_Ratio)
        QtCore.QObject.connect(self.frontal_area_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.myfunc_FAID)
        QtCore.QObject.connect(self.PAR, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Building_Surface_PAR)
        QtCore.QObject.connect(self.MDH, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Macdonald_Displacement_height)
        QtCore.QObject.connect(self.MRL, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Macdonald_Roughness_length)
        QtCore.QObject.connect(self.RDH, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Raupach_Displacement_Height)
        QtCore.QObject.connect(self.RRL, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Raupach_Roughness_length)
        QtCore.QObject.connect(self.GODH, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Grimmond_Displacement_Height)
        QtCore.QObject.connect(self.GORL, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Grimmond_Roughness_Length)
        QtCore.QObject.connect(self.svf_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.myfunc_SVF)
        QtCore.QObject.connect(self.hwratio_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.myfunc_HWR)
        QtCore.QObject.connect(self.Roofareadensity, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Roof_Area_Density)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Urban Canopy Parameters", None))
        self.frontal_area_btn.setToolTip(_translate("Dialog", "<html><head/><body><p>Clicked this button to compute Frontal Area.</p><p><br/></p></body></html>", None))
        self.frontal_area_btn.setText(_translate("Dialog", "Frontal Area Index", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">WRF Factors</span></p></body></html>", None))
        self.hwratio_btn.setToolTip(_translate("Dialog", "<html><head/><body><p>Click this button to calculate Height/Width Ratio</p><p><br/></p></body></html>", None))
        self.hwratio_btn.setText(_translate("Dialog", "Height/Width Ratio", None))
        self.svf_btn.setToolTip(_translate("Dialog", "<html><head/><body><p>Click this button to calculate Sky View Factor</p></body></html>", None))
        self.svf_btn.setText(_translate("Dialog", "Sky View Factor", None))
        self.FAD_btn.setText(_translate("Dialog", "Frontal Area Density ", None))
        self.Planareadensity.setText(_translate("Dialog", "Plan Area Density", None))
        self.Roofareadensity.setText(_translate("Dialog", "Roof Area Density", None))
        self.Planareafraction.setText(_translate("Dialog", "Plan Area Fraction", None))
        self.Meanbuildingheight.setText(_translate("Dialog", "Mean Building Height", None))
        self.SDBV.setText(_translate("Dialog", "Standard Deviation of Building Height", None))
        self.MBH.setText(_translate("Dialog", "Area Weighted Mean Building Height", None))
        self.PAR.setText(_translate("Dialog", "Building Surface to Plan Area Ratio", None))
        self.CAR.setText(_translate("Dialog", "Complete Aspect Ratio", None))
        self.GORL.setText(_translate("Dialog", "Grimmond and Oke Roughness Length ", None))
        self.GODH.setText(_translate("Dialog", "Grimmond and Oke Displacement Height", None))
        self.RRL.setText(_translate("Dialog", "Raupach  Roughness Length ", None))
        self.RDH.setText(_translate("Dialog", "Raupach  Displacement Height ", None))
        self.MRL.setText(_translate("Dialog", "Macdonald  Roughness Length ", None))
        self.MDH.setText(_translate("Dialog", "Macdonald Displacement Height  ", None))
        self.Volumetric_height_btn.setText(_translate("Dialog", "Volumetric Height", None))

    def Mean_Building_Height(self):
        driver = ogr.GetDriverByName('ESRI Shapefile')
        unionfile = str(Ui_MainWindow.unionfile_path)
        unionSource = driver.Open(unionfile,1)
        #unionSource = driver.Open('F:\\codes\\codes\\reprojected\\7buildingunion2.shp',1)
        unionLayer = unionSource.GetLayer()
        #GridSource = driver.Open('F:\\codes\\codes\\reprojected\\7buildgrid.shp',1)
        gridfile=str(Ui_MainWindow.gridfile_path)
        output = str(Ui_MainWindow.outputfile_path)
        GridSource=driver.Open(gridfile,1)
        GridLayer = GridSource.GetLayer()
        UnionFeat = unionLayer.GetFeature(0)
        UnionGeom = UnionFeat.GetGeometryRef()
        list1 = unionLayer.GetExtent()
        list2 = UnionGeom.GetEnvelope()
        text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Mean Building height :')
        if ok:
            name=str(text)
        ldefn = GridLayer.GetLayerDefn()
        sch= []
        check=0
        n=0
        for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
            field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
            sch.append(field) 
        n=0
        for n in range(len(sch)):
           if(name==str(sch[n])):
               check=1
               print('Field Already exists')
        if (check==0):
            new_field = ogr.FieldDefn(name, ogr.OFTReal)
            GridLayer.CreateField(new_field)
            print('New Field Created')
        noc = (list1[1]-list1[0])/(list2[1]-list2[0])
        nor = (list1[3]-list1[2])/(list2[3]-list2[2])
        prod=noc*nor
        #new_field = ogr.FieldDefn("Mean", ogr.OFTReal)
        #new_field.SetWidth(32)
        #new_field.SetPrecision(2)
        #GridLayer.CreateField(new_field)        
        BuildId = []
        BuildGdId = []
        BuildHt = []
        Mean=[]
        print (Ui_MainWindow.hei_name)
        for i in range(unionLayer.GetFeatureCount()):
            
            feature=unionLayer.GetFeature(i)
            #print (feature)
            var1=feature.GetField('FIDGrid')
            BuildGdId.append(var1)
            var2=feature.GetField('FIDBuild')
            BuildId.append(var2)
            var3=feature.GetField(Ui_MainWindow.hei_name)
            BuildHt.append(var3)
        name_of_file = 'Mean Building Height'
        completeName = os.path.join(output, name_of_file+".txt") 
        f_Mean = open(completeName , "w")
        #f_Mean = open('Mean Building Height.txt','w')
        count =0
        #print('print someyhing')
        while (count < prod):
            i=0
            buildheight = []
            no_of_build=0
            for i in range(unionLayer.GetFeatureCount()):
                if (BuildGdId[i]==count and BuildId[i] > -1):
                    buildheight.append(BuildHt[i])
                    no_of_build=no_of_build+1
            count = count+1
            if(no_of_build==0):
                Mean.append(0)
                f_Mean.write('The mean of buildings height in Grid {} is 0.\n'.format(count))                
            else:                    
                build_height_sum=float(sum(buildheight))
                mean2=float(build_height_sum )/float( no_of_build)
                mean=round(mean2,6)
                f_Mean.write('The mean of buildings height in Grid {} is {}.\n'.format(count,mean))
                Mean.append(mean)
        #print('Mean Buildings Height computed')
        f_Mean.close()
        i=0
        for i in range(GridLayer.GetFeatureCount()):            
            GridFeat = GridLayer.GetFeature(i)
            GridFeat.SetField(name,Mean[i])
            GridLayer.SetFeature(GridFeat)
        print('Mean Building Completed')

    def SD_Building_Height(self):
        driver = ogr.GetDriverByName('ESRI Shapefile')
        unionfile = str(Ui_MainWindow.unionfile_path)
        unionSource = driver.Open(unionfile,1)
        unionLayer = unionSource.GetLayer()
        gridfile=str(Ui_MainWindow.gridfile_path)
        output = str(Ui_MainWindow.outputfile_path)
        GridSource=driver.Open(gridfile,1)
        GridLayer = GridSource.GetLayer()
        UnionFeat = unionLayer.GetFeature(0)
        UnionGeom = UnionFeat.GetGeometryRef()
        list1 = unionLayer.GetExtent()
        list2 = UnionGeom.GetEnvelope()
        text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Standard deviation of building heigth:')
        if ok:
            name=str(text)
        text2, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Mean Building height:')        
        if ok:
            name2=str(text)
        sch= []
        check=0
        n=0
        for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
            field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
            sch.append(field) 
        n=0
        for n in range(len(sch)):
           if(name==str(sch[n])):
               check=1
               print('Field Already exists')
        if (check==0):
            new_field = ogr.FieldDefn(name, ogr.OFTReal)
            GridLayer.CreateField(new_field)
            print('New Field Created')
        noc = (list1[1]-list1[0])/(list2[1]-list2[0])
        nor = (list1[3]-list1[2])/(list2[3]-list2[2])
        prod=noc*nor
        BuildId = []
        BuildGdId = []
        BuildHt = []
        Std_Devi=[]
        Mean=[]
        #new_field = ogr.FieldDefn("Std_Devi", ogr.OFTReal)
        #new_field.SetWidth(32)
        #new_field.SetPrecision(2)
        #GridLayer.CreateField(new_field)        
        for i in range(unionLayer.GetFeatureCount()):
            
            feature=unionLayer.GetFeature(i)
            #print (feature)
            var1=feature.GetField('FIDGrid')
            BuildGdId.append(var1)
            var2=feature.GetField('FIDBuild')
            BuildId.append(var2)
            
            var3=feature.GetField(Ui_MainWindow.hei_name)
            BuildHt.append(var3)
        for i in range(GridLayer.GetFeatureCount()):
            gridfeature=GridLayer.GetFeature(i)
            var4=gridfeature.GetField(name2)###mmman#####################################
            Mean.append(var4)         
        name_of_file = 'Standard Deviation'
        completeName = os.path.join(output, name_of_file+".txt") 
        f_std_devi = open(completeName , "w")
        #f_std_devi = open('Standard Deviation.txt','w')   
        count =0

        while (count <prod):
            i=0
            buildheight = []
            no_of_build=0
            for i in range(unionLayer.GetFeatureCount()):
                if (BuildGdId[i]==count and BuildId[i] > -1):
                    buildheight.append(BuildHt[i])
                    no_of_build=no_of_build+1
            count = count+1
            build_height_sum=float(sum(buildheight))
            if(no_of_build==0):
                Std_Devi.append(0)
                f_std_devi.write('The Standard Deviation in Grid {} is 0.\n'.format(count))

            else:
                mean2=float(build_height_sum / no_of_build)
                #mean=round(mean2,6)
                
                differences = [x - mean2 for x in buildheight]
                sq_differences = [d ** 2 for d in differences]
                ssd = sum(sq_differences)
                variance = ssd / no_of_build
                sd2 = sqrt(variance)
                sd=round(sd2,6)
                Std_Devi.append(sd)
                f_std_devi.write('The Standard Deviation in Grid {} is {}.\n'.format(count,sd))
        #sys.stdout.close()
        #print('Standard Deviation Computed')
        f_std_devi.close()    
        i=0
        for i in range(GridLayer.GetFeatureCount()):
                GridFeat = GridLayer.GetFeature(i)
                GridFeat.SetField(name,Std_Devi[i])
                GridLayer.SetFeature(GridFeat) 
        print('Standard Deviation Completed')           

    def Area_weighted_MBH(self):
        driver = ogr.GetDriverByName('ESRI Shapefile')
        unionfile = str(Ui_MainWindow.unionfile_path)
        unionSource = driver.Open(unionfile,1)
        unionLayer = unionSource.GetLayer()
        output = str(Ui_MainWindow.outputfile_path)
        gridfile=str(Ui_MainWindow.gridfile_path)
        GridSource=driver.Open(gridfile,1)
        GridLayer = GridSource.GetLayer()
        UnionFeat = unionLayer.GetFeature(0)
        UnionGeom = UnionFeat.GetGeometryRef()
        list1 = unionLayer.GetExtent()
        list2 = UnionGeom.GetEnvelope()
        text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Area weighted mean building height:')
        if ok:
            name=str(text)
        sch= []
        check=0
        n=0
        for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
            field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
            sch.append(field) 
        n=0
        for n in range(len(sch)):
           if(name==str(sch[n])):
               check=1
               print('Field Already exists')
        if (check==0):
            new_field = ogr.FieldDefn(name, ogr.OFTReal)
            GridLayer.CreateField(new_field)
            print('New Field Created')
        noc = (list1[1]-list1[0])/(list2[1]-list2[0])
        nor = (list1[3]-list1[2])/(list2[3]-list2[2])
        prod=noc*nor
        BuildId = []
        BuildGdId = []
        BuildHt = []
        BuildAr=[]
        Ar_MBH=[]
        #new_field = ogr.FieldDefn("Ar_MBH", ogr.OFTReal)
        #new_field.SetWidth(32)
        #new_field.SetPrecision(2)
        #GridLayer.CreateField(new_field)        

        for i in range(unionLayer.GetFeatureCount()):
            
            feature=unionLayer.GetFeature(i)
            #print (feature)
            var1=feature.GetField('FIDGrid')
            BuildGdId.append(var1)
            var2=feature.GetField('FIDBuild')
            BuildId.append(var2)
            
            var3=feature.GetField(Ui_MainWindow.hei_name)
            BuildHt.append(var3)
            var4=feature.GetField('buildarea')
            BuildAr.append(var4)
        name_of_file = 'Area Weighted Mean Building Height'
        completeName = os.path.join(output, name_of_file+".txt") 
        f_MBH = open(completeName , "w")
        #f_MBH = open('Area Weighted Mean Building Height.txt','w')            
        count=0
        while(count<prod):
            #print('######################3333')
            buildhei=[]
            buildarea=[]
            i=0
            for i in range(unionLayer.GetFeatureCount()):
                if (BuildGdId[i]==count and BuildId[i] > -1):
                    buildhei.append(BuildHt[i])
                    buildarea.append(BuildAr[i])
            areaheight = [buildarea[i]*buildhei[i] for i in range(len(buildarea))]
            #print(areaheight)
            if(sum(buildarea)==0):
                Ar_MBH.append(0)
                f_MBH.write('The Weighted Area Mean Height in Grid {} is 0\n'.format(count))
            else:
                weight_area_height=float(sum(areaheight))/float(sum(buildarea))
                Ar_MBH.append(weight_area_height)
                f_MBH.write('The Weighted Area Mean Height in Grid {} is {}\n'.format(count,weight_area_height))
            count+=1
        f_MBH.close()
        i=0
        for i in range(GridLayer.GetFeatureCount()):
                GridFeat = GridLayer.GetFeature(i)
                GridFeat.SetField(name,Ar_MBH[i])
                GridLayer.SetFeature(GridFeat) 
        print('Area Weighted Mean Building Height Completed')    
   
    def Volumetric_Height(self):
        driver = ogr.GetDriverByName('ESRI Shapefile')
        unionfile = str(Ui_MainWindow.unionfile_path)
        unionSource = driver.Open(unionfile,1)
        #unionSource = driver.Open('F:\\codes\\codes\\reprojected\\7buildingunion2.shp',1)
        unionLayer = unionSource.GetLayer()
        #GridSource = driver.Open('F:\\codes\\codes\\reprojected\\7buildgrid.shp',1)
        gridfile=str(Ui_MainWindow.gridfile_path)
        output = str(Ui_MainWindow.outputfile_path)
        GridSource=driver.Open(gridfile,1)
        GridLayer = GridSource.GetLayer()
        UnionFeat = unionLayer.GetFeature(0)
        UnionGeom = UnionFeat.GetGeometryRef()
        list1 = unionLayer.GetExtent()
        list2 = UnionGeom.GetEnvelope()
        text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Volumetric height:')
        if ok:
            name=str(text)
        sch= []
        check=0
        n=0
        for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
            field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
            sch.append(field) 
        n=0
        for n in range(len(sch)):
           if(name==str(sch[n])):
               check=1
               print('Field Already exists')
        if (check==0):
            new_field = ogr.FieldDefn(name, ogr.OFTReal)
            GridLayer.CreateField(new_field)
            print('New Field Created')
        noc = (list1[1]-list1[0])/(list2[1]-list2[0])
        nor = (list1[3]-list1[2])/(list2[3]-list2[2])
        prod=noc*nor
        BuildId = []
        BuildGdId = []
        BuildHt = []
        BuildAr=[]
        Vol_Hei=[]
        #new_field = ogr.FieldDefn("Vol_Hei", ogr.OFTReal)
        #new_field.SetWidth(32)
        #new_field.SetPrecision(2)
        #GridLayer.CreateField(new_field)        
        for i in range(unionLayer.GetFeatureCount()):
            
            feature=unionLayer.GetFeature(i)
            #print (feature)
            var1=feature.GetField('FIDGrid')
            BuildGdId.append(var1)
            var2=feature.GetField('FIDBuild')
            BuildId.append(var2)
            
            var3=feature.GetField(Ui_MainWindow.hei_name)
            BuildHt.append(var3)
            var4=feature.GetField('buildarea')
            BuildAr.append(var4)
        name_of_file = 'Volumetric Avedrage Height'
        completeName = os.path.join(output, name_of_file+".txt") 
        f_Vol= open(completeName , "w")
        #f_Vol = open('Volumetric Avedrage Height.txt','w')            
        count=0
        while(count<prod):
            buildhei=[]
            buildarea=[]
            i=0
            for i in range(unionLayer.GetFeatureCount()):
                if (BuildGdId[i]==count and BuildId[i] > -1):
                    buildhei.append(BuildHt[i])
                    buildarea.append(BuildAr[i])
            areaheight = [buildarea[i]*buildhei[i] for i in range(len(buildarea))]
            volheight = [areaheight[a]*buildhei[a] for a in range(len(buildarea))]
            #print(areaheight)
            if(sum(buildarea)==0):
                Vol_Hei.append(0)
                f_Vol.write('The Volumetric Average Height in Grid {} is 0\n'.format(count))
            else:
                volumetric_height=float(sum(volheight))/float(sum(areaheight))
                Vol_Hei.append(volumetric_height)
                f_Vol.write('The Volumetric Average Height in Grid {} is {}\n'.format(count,volumetric_height))
            count+=1
        f_Vol.close()
        i=0
        for i in range(GridLayer.GetFeatureCount()):
                GridFeat = GridLayer.GetFeature(i)
                GridFeat.SetField(name,Vol_Hei[i])
                GridLayer.SetFeature(GridFeat)
        print('Volumetric Avedrage Height Completed')

    def Roof_Area_Density(self):
        driver = ogr.GetDriverByName('ESRI Shapefile')
        unionfile = str(Ui_MainWindow.unionfile_path)
        unionSource = driver.Open(unionfile,1)
        unionLayer = unionSource.GetLayer()
        gridfile=str(Ui_MainWindow.gridfile_path)
        GridSource=driver.Open(gridfile,1)
        GridLayer = GridSource.GetLayer()
        output = str(Ui_MainWindow.outputfile_path)
        GridFeat = unionLayer.GetFeature(0)
        GridGeom = GridFeat.GetGeometryRef()
        list1 = unionLayer.GetExtent()
        list2 = GridGeom.GetEnvelope()
        noc = (list1[1]-list1[0])/(list2[1]-list2[0])
        nor = (list1[3]-list1[2])/(list2[3]-list2[2])
        prod=noc*nor
        #new_field = ogr.FieldDefn("Roof_Ar_Den", ogr.OFTReal)
        #new_field.SetWidth(32)
        #new_field.SetPrecision(2)
        #GridLayer.CreateField(new_field)
        BuildId = []
        BuildGdId = []
        BuildHt = []
        BuildAr = []
        BuildSumAr = []
        BlankSumAr = []
        BuildMaxGdHt = []
        BuildMinGdHt = []
        BuildRoofAreaDen = []
        #print (layer.GetFeatureCount())
        for i in range(unionLayer.GetFeatureCount()):
            
            feature=unionLayer.GetFeature(i)
            #print (feature)
            var1=feature.GetField('FIDGrid')
            BuildGdId.append(var1)
            var2=feature.GetField('FIDBuild')
            BuildId.append(var2)
            
            var3=feature.GetField('buildh')
            BuildHt.append(var3)
            var4=feature.GetField('buildarea')
            BuildAr.append(var4)

        count = 0
        while (count < prod):
            buildsum = 0
            blanksum = 0
            i=0
            for i in range(unionLayer.GetFeatureCount()):
                if (BuildGdId[i]==count and BuildId[i] > -1):
                    buildsum=buildsum+BuildAr[i]
                    
            count = count+1
            BuildSumAr.append(buildsum)

        count =0
        while (count <prod):
            i=0
            buildheight = []
            buildheight2 = []
            for i in range(unionLayer.GetFeatureCount()):
                if (BuildGdId[i]==count and BuildId[i] > -1):
                    buildheight.append(BuildHt[i])            
            count = count+1
            if(len(buildheight)==0):
                BuildMaxGdHt.append(0)

            else:
                BuildMaxGdHt.append(max(buildheight))
        
        text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Input Increment in height:')
        if ok:
            name=str(text)

        #inc = raw_input("Please Input Increment in height ")
        inc=int(name)        
        name_of_file = 'Roof Area Density'
        completeName = os.path.join(output, name_of_file+".txt") 
        f_roof = open(completeName , "w")
        #f_roof=open('Roof Area Density.txt','w')
        temp=inc
        count = 0
        while(count<prod):
            inc=temp
            BuildRoofAreaDen = []
        #    print "$$$$$$$$$$$$$$$$"
            while(inc <= max(BuildMaxGdHt)):
                 buildsum2=0
                 blanksum2=0
                 i=0
                 roofareaden=0
                 for i in range(unionLayer.GetFeatureCount()):
                    if(BuildGdId[i]==count and BuildId[i] > -1 and BuildHt[i] >= inc):
                        buildsum2=buildsum2+BuildAr[i]
                    elif(BuildGdId[i]==count and BuildId[i] == -1):
                        blanksum2=blanksum2+BuildAr[i]
                 inc = inc+temp
                 if(buildsum2>0 and blanksum2>0):
                     roofareaden=float(buildsum2)/float(temp*buildsum2*inc)
                     BuildRoofAreaDen.append(roofareaden)
                 else:
                     BuildRoofAreaDen.append(0)
            temp2 =0
        #    print (len(BuildRoofAreaDen))
            for i in range(len(BuildRoofAreaDen)):
                temp2=temp2+temp
                f_roof.write(" Roof area Density for Grid {0} at height {1} is {2}\n".format( count, temp2 ,BuildRoofAreaDen[i]))
            count=count+1
        f_roof.close()
        print('Roof Area Density Completed')
        

    def cal_PAF(self):        
        driver = ogr.GetDriverByName('ESRI Shapefile')
        unionfile = str(Ui_MainWindow.unionfile_path)
        unionSource = driver.Open(unionfile,1)
        unionLayer = unionSource.GetLayer()
        gridfile=str(Ui_MainWindow.gridfile_path)
        GridSource=driver.Open(gridfile,1)
        GridLayer = GridSource.GetLayer()
        output = str(Ui_MainWindow.outputfile_path)
        UnionFeat = unionLayer.GetFeature(0)
        UnionGeom = UnionFeat.GetGeometryRef()
        list1 = unionLayer.GetExtent()
        list2 = UnionGeom.GetEnvelope()
        text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Plan area fraction:')
        if ok:
            name=str(text)
        sch= []
        check=0
        n=0
        for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
            field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
            sch.append(field) 
        n=0
        for n in range(len(sch)):
           if(name==str(sch[n])):
               check=1
               print('Field Already exists')
        if (check==0):
            new_field = ogr.FieldDefn(name, ogr.OFTReal)
            GridLayer.CreateField(new_field)
            print('New Field Created')
        noc = (list1[1]-list1[0])/(list2[1]-list2[0])
        nor = (list1[3]-list1[2])/(list2[3]-list2[2])
        prod=noc*nor
        BuildId = []
        BuildGdId = []
        BuildHt = []
        BuildAr = []
        BuildSumAr = []
        BlankSumAr = []
        BuildMaxGdHt = []
        BuildMinGdHt = []
        #new_field = ogr.FieldDefn("PAF", ogr.OFTReal)
        #new_field.SetWidth(32)
        #new_field.SetPrecision(2)
        #GridLayer.CreateField(new_field)
        #print (layer.GetFeatureCount())
        name_of_file = 'Plan Area fraction'
        completeName = os.path.join(output, name_of_file+".txt") 
        f_PAF = open(completeName , "w")
        #sys.stdout = open('Plan Area Fraction.txt','w')
        for i in range(unionLayer.GetFeatureCount()):
            
            feature=unionLayer.GetFeature(i)
            #print (feature)
            var1=feature.GetField('FIDGrid')
            BuildGdId.append(var1)
            var2=feature.GetField('FIDBuild')
            BuildId.append(var2)
            
            var3=feature.GetField(Ui_MainWindow.hei_name)
            BuildHt.append(var3)
            var4=feature.GetField('buildarea')
            BuildAr.append(var4)
        count = 0
        while (count < prod):
            buildsum = 0
            blanksum = 0
            i=0
            for i in range(unionLayer.GetFeatureCount()):
                if (BuildGdId[i]==count and BuildId[i] > -1):
                    buildsum=buildsum+BuildAr[i]
                    
                elif (BuildGdId[i]==count and BuildId[i]==-1):
                    blanksum=blanksum+BuildAr[i]

                    
            count = count+1
            BuildSumAr.append(buildsum)
            BlankSumAr.append(blanksum)
        #    print("Total building area  for grid {0} is {1}".format((count-1), BuildSumAr[count-1]))
        #    print("Total blank area  for grid {0} is {1}".format((count-1), BlankSumAr[count-1]))
        length=len(BlankSumAr)
        x=0
        PlAr = 0
        plan_area_fr = []
        for x in range(length):
            
            if (BuildSumAr[x]>0  and BlankSumAr[x]>0 ):
                PlAr= float(BuildSumAr[x]) / float(BlankSumAr[x]+BuildSumAr[x])
                plan_area_fr.append(PlAr)
            else:
                plan_area_fr.append('0')
            f_PAF.write("Plan area Fraction for grid {0} is {1} \n".format((x+1),plan_area_fr[x]))
    
        i=0
        for i in range(GridLayer.GetFeatureCount()):
                GridFeat = GridLayer.GetFeature(i)
                GridFeat.SetField(name,plan_area_fr[i])
                GridLayer.SetFeature(GridFeat)    
        f_PAF.close()        
        print("Plan Area Fraction Completed")


    def Building_Surface_PAR(self):
        driver = ogr.GetDriverByName('ESRI Shapefile')
        unionfile = str(Ui_MainWindow.unionfile_path)
        unionSource = driver.Open(unionfile,1)
        unionLayer = unionSource.GetLayer()
        gridfile=str(Ui_MainWindow.gridfile_path)
        output = str(Ui_MainWindow.outputfile_path)
        GridSource=driver.Open(gridfile,1)
        GridLayer = GridSource.GetLayer()
        GridFeat = unionLayer.GetFeature(0)
        GridGeom = GridFeat.GetGeometryRef()
        list1 = unionLayer.GetExtent()
        list2 = GridGeom.GetEnvelope()
        text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Building surface to plan area ratio :')
        if ok:
            name=str(text)
        sch= []
        check=0
        n=0
        for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
            field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
            sch.append(field) 
        n=0
        for n in range(len(sch)):
           if(name==str(sch[n])):
               check=1
               print('Field Already exists')
        if (check==0):
            new_field = ogr.FieldDefn(name, ogr.OFTReal)
            GridLayer.CreateField(new_field)
            print('New Field Created')
        noc = (list1[1]-list1[0])/(list2[1]-list2[0])
        nor = (list1[3]-list1[2])/(list2[3]-list2[2])
        prod=noc*nor
        BuildId = []
        BuildGdId = []
        BuildHt = []
        BuildAr = []
        BuildPr = []
        BuildGr = []
        BuildSumArAR= []
        BlankSumArAT= []
        BuildLb=[]
        #new_field = ogr.FieldDefn("BSA/PAR", ogr.OFTReal)
        #new_field.SetWidth(32)
        #new_field.SetPrecision(2)
        #GridLayer.CreateField(new_field)        

        for i in range(unionLayer.GetFeatureCount()):
            feature=unionLayer.GetFeature(i)
            var1=feature.GetField('FIDGrid')
            BuildGdId.append(var1)
            var2=feature.GetField('FIDBuild')
            BuildId.append(var2)
            var3=feature.GetField(Ui_MainWindow.hei_name)
            BuildHt.append(var3)
            var4=feature.GetField('buildarea')
            BuildAr.append(var4)
            var5=feature.GetField('perimeter')
            BuildPr.append(var5)
            var6=feature.GetField('area')
            BuildGr.append(var6)
        name_of_file = 'Building Surface'
        completeName = os.path.join(output, name_of_file+".txt") 
        f_bsa = open(completeName , "w")
        #f_bsa = open('Building Surface.txt','w')            
        count = 0
        while (count < prod):
            buildsum = 0
            blanksum=0
            i=0
            Aw=0
            At=0
            Ar=0
            lb=0
            for i in range(unionLayer.GetFeatureCount()):
                if (BuildGdId[i]==count and BuildId[i] > -1):
                    buildsum=buildsum+BuildAr[i]
                    Aw=Aw+BuildHt[i]*BuildPr[i]
                    At=BuildGr[i]
                    Ar=Ar+BuildAr[i]
                    lb=float(Aw+Ar)/float(At)
            
                elif(BuildGdId[i]==count and BuildId[i] == -1):
                    blanksum=blanksum+BuildAr[i]
            

            count = count+1
            BuildSumArAR.append(buildsum)
            BlankSumArAT.append(blanksum)
            BuildLb.append(lb)
        i=0
        #print len(BuildLb)
        for i in range(len(BuildLb)):
            f_bsa.write('Building Surface Area to Plan Area Ratio,lamda b for grid {0} is {1} \n'.format(i+1,BuildLb[i]))
        i=0
        for i in range(GridLayer.GetFeatureCount()):
                GridFeat = GridLayer.GetFeature(i)
                GridFeat.SetField(name,BuildLb[i])
                GridLayer.SetFeature(GridFeat)
        f_bsa.close()
        print('Building Surface to Plan Area Ratio Completed')
           
    def Complete_Aspect_Ratio(self):
        driver = ogr.GetDriverByName('ESRI Shapefile')
        unionfile = str(Ui_MainWindow.unionfile_path)
        unionSource = driver.Open(unionfile,1)
        unionLayer = unionSource.GetLayer()
        gridfile=str(Ui_MainWindow.gridfile_path)
        output = str(Ui_MainWindow.outputfile_path)
        GridSource=driver.Open(gridfile,1)
        GridLayer = GridSource.GetLayer()
        GridFeat = unionLayer.GetFeature(0)
        GridGeom = GridFeat.GetGeometryRef()
        list1 = unionLayer.GetExtent()
        list2 = GridGeom.GetEnvelope()
        text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Complete Aspect ratio:')
        if ok:
            name=str(text)
        sch= []
        check=0
        n=0
        for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
            field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
            sch.append(field) 
        n=0
        for n in range(len(sch)):
           if(name==str(sch[n])):
               check=1
               print('Field Already exists')
        if (check==0):
            new_field = ogr.FieldDefn(name, ogr.OFTReal)
            GridLayer.CreateField(new_field)
            print('New Field Created')
        noc = (list1[1]-list1[0])/(list2[1]-list2[0])
        nor = (list1[3]-list1[2])/(list2[3]-list2[2])
        prod=noc*nor
        BuildId = []
        BuildGdId = []
        BuildHt = []
        BuildAr = []
        BuildPr = []
        BuildGr = []
        BuildSumArAR= []
        BlankSumArAT= []
        #BuildLb=[]
        BuildLc=[]
        #new_field = ogr.FieldDefn("CAR", ogr.OFTReal)
        #new_field.SetWidth(32)
        #new_field.SetPrecision(2)
        #GridLayer.CreateField(new_field)        

        #print (layer.GetFeatureCount())
        for i in range(unionLayer.GetFeatureCount()):            
            feature=unionLayer.GetFeature(i)
            var1=feature.GetField('FIDGrid')
            BuildGdId.append(var1)
            var2=feature.GetField('FIDBuild')
            BuildId.append(var2)
            var3=feature.GetField(Ui_MainWindow.hei_name)
            BuildHt.append(var3)
            var4=feature.GetField('buildarea')
            BuildAr.append(var4)
            var5=feature.GetField('perimeter')
            BuildPr.append(var5)
            var6=feature.GetField('area')
            BuildGr.append(var6)
        name_of_file = 'Complete Aspect Ratio'
        completeName = os.path.join(output, name_of_file+".txt") 
        f_car = open(completeName , "w")
        #f_car = open('Complete Aspect Ratio.txt','w')            
        count = 0
        while (count <= prod):
            buildsum = 0
            blanksum=0
            i=0
            Aw=0
            At=0
            Ar=0
            #lb=0
            lc=0
            for i in range(unionLayer.GetFeatureCount()):
                if (BuildGdId[i]==count and BuildId[i] > -1):
                    buildsum=buildsum+BuildAr[i]
                    Aw=Aw+BuildHt[i]*BuildPr[i]
                    At=BuildGr[i]
                    Ar=Ar+BuildAr[i]
                    #lb=float(Aw+Ar)/float(At)
                    lc=float(Aw/At)+float(1)

                elif(BuildGdId[i]==count and BuildId[i] == -1):
                    blanksum=blanksum+BuildAr[i]
            

            count = count+1
            BuildSumArAR.append(buildsum)
            BlankSumArAT.append(blanksum)
            #BuildLb.append(lb)
            BuildLc.append(lc)       

        i=0
        #print len(BuildLb)
        for i in range(len(BuildLc)):
            #print('Building Surface Area to Plan Area Ratio,lamda b for grid {0} is {1} \n'.format(i+1,BuildLb[i]))
            f_car.write('Complete Aspect Ratio,lamda c for grid {0} is {1} \n'.format(i+1,BuildLc[i]))
        i=0
        for i in range(GridLayer.GetFeatureCount()):
                GridFeat = GridLayer.GetFeature(i)
                GridFeat.SetField(name,BuildLc[i])
                GridLayer.SetFeature(GridFeat)
        f_car.close()
        print('Complete Aspect Ratio Completed')

    def Macdonald_Displacement_height(self):
        driver = ogr.GetDriverByName('ESRI Shapefile')
        unionfile = str(Ui_MainWindow.unionfile_path)
        unionSource = driver.Open(unionfile,1)
        unionLayer = unionSource.GetLayer()
        gridfile=str(Ui_MainWindow.gridfile_path)
        output = str(Ui_MainWindow.outputfile_path)
        GridSource=driver.Open(gridfile,1)
        GridLayer = GridSource.GetLayer()
        GridFeat = unionLayer.GetFeature(0)
        GridGeom = GridFeat.GetGeometryRef()
        list1 = unionLayer.GetExtent()
        list2 = GridGeom.GetEnvelope()
        text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Macdonald displacement height:')
        if ok:
            name=str(text)
        sch= []
        text2, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name of Plan Area Fraction:')        
        if ok:
            name2=str(text2)
        text3, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name of Mean Building Height:')        
        if ok:
            name3=str(text3)
        check=0
        n=0
        for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
            field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
            sch.append(field) 
        n=0
        for n in range(len(sch)):
           if(name==str(sch[n])):
               check=1
               print('Field Already exists')
        if (check==0):
            new_field = ogr.FieldDefn(name, ogr.OFTReal)
            GridLayer.CreateField(new_field)
            print('New Field Created')
        noc = (list1[1]-list1[0])/(list2[1]-list2[0])
        nor = (list1[3]-list1[2])/(list2[3]-list2[2])
        prod=noc*nor
        build=[]
        hieght=[]
        BuildId = []
        BuildGdId = []
        plan_ar_fr=[]
        PAF=[]
        Mean=[]
        mean_build_hei=[]
        count = 0
        dis_len=[]
        #new_field = ogr.FieldDefn("Dis_len", ogr.OFTReal)
        #new_field.SetWidth(32)
        #new_field.SetPrecision(2)
        #GridLayer.CreateField(new_field)        
        for i in range(unionLayer.GetFeatureCount()):
            feature=unionLayer.GetFeature(i)
            buildheight2=feature.GetField(Ui_MainWindow.hei_name )
            build.append(buildheight2)
            var1=feature.GetField('FIDGrid')
            BuildGdId.append(var1)
            var2=feature.GetField('FIDBuild')
            BuildId.append(var2)
        for i in range(GridLayer.GetFeatureCount()):
            gridfeature=GridLayer.GetFeature(i)
            var3=gridfeature.GetField(name2)####'PAF'###############################################
            PAF.append(var3)
            var4=gridfeature.GetField(name3)######'Mean'############################################
            Mean.append(var4)
        name_of_file = 'Macdonald Displacement Height'
        completeName = os.path.join(output, name_of_file+".txt") 
        f_mcdis= open(completeName , "w")
        #f_mcdis=open('Macdonald Displacement Height.txt','w')            
        count=0    
        while(count<prod):
            lp=PAF[count]  #value needed building plan area fraction
            p=lp-1
            A=4.43
            r=A**(-lp)
            q=p*r
            zd=Mean[count]*(q+1)
            dis_len.append(zd)
            f_mcdis.write('Macdonald Displacement Height for Grid {0} is {1}\n'.format(count,zd))
            count+=1
        f_mcdis.close()    
        i=0
        for i in range(GridLayer.GetFeatureCount()):
                GridFeat = GridLayer.GetFeature(i)
                GridFeat.SetField(name,dis_len[i])
                GridLayer.SetFeature(GridFeat)
        print('Macdonald Displacement Height Completed')

    def Macdonald_Roughness_length(self):
        driver = ogr.GetDriverByName('ESRI Shapefile')
        unionfile = str(Ui_MainWindow.unionfile_path)
        unionSource = driver.Open(unionfile,1)
        #unionSource = driver.Open('F:\\codes\\codes\\reprojected\\7buildingunion2.shp',1)
        unionLayer = unionSource.GetLayer()
        #GridSource = driver.Open('F:\\codes\\codes\\reprojected\\7buildgrid.shp',1)
        gridfile=str(Ui_MainWindow.gridfile_path)
        output = str(Ui_MainWindow.outputfile_path)
        GridSource=driver.Open(gridfile,1)
        GridLayer = GridSource.GetLayer()
        GridFeat = unionLayer.GetFeature(0)
        GridGeom = GridFeat.GetGeometryRef()
        list1 = unionLayer.GetExtent()
        list2 = GridGeom.GetEnvelope()
        text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Macdonald Roughness Length:')
        if ok:
            name=str(text)
        sch= []
        text2, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name of Mean Building Height:')        
        if ok:
            name2=str(text2)
        check=0
        n=0
        text3, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name of Frontal Area Index:')        
        if ok:
            name3=str(text3)
        text4, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name of Macdonald Displacement Height:')        
        if ok:
            name4=str(text4)
        for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
            field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
            sch.append(field)
        n=0
        for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
            field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
            sch.append(field) 
        n=0
        for n in range(len(sch)):
           if(name==str(sch[n])):
               check=1
               print('Field Already exists')
        if (check==0):
            new_field = ogr.FieldDefn(name, ogr.OFTReal)
            GridLayer.CreateField(new_field)
            print('New Field Created')
        noc = (list1[1]-list1[0])/(list2[1]-list2[0])
        nor = (list1[3]-list1[2])/(list2[3]-list2[2])
        prod=noc*nor
        build=[]
        hieght=[]
        BuildId = []
        BuildGdId = []
        plan_ar_fr=[]
        FAIND=[]
        Mean=[]
        dis_len=[]
        count = 0
        rou_len=[]
        #new_field = ogr.FieldDefn("Rou_len", ogr.OFTReal)
        #new_field.SetWidth(32)
        #new_field.SetPrecision(2)
        #GridLayer.CreateField(new_field)        
        for i in range(unionLayer.GetFeatureCount()):
            feature=unionLayer.GetFeature(i)
            buildheight2=feature.GetField(Ui_MainWindow.hei_name)
            build.append(buildheight2)
            var1=feature.GetField('FIDGrid')
            BuildGdId.append(var1)
            var2=feature.GetField('FIDBuild')
            BuildId.append(var2)

        i=0
        for i in range(GridLayer.GetFeatureCount()):
            gridfeature=GridLayer.GetFeature(i)    
            var4=gridfeature.GetField(name2)#####'Mean'#################################
            Mean.append(var4)
            var3=gridfeature.GetField(name3)#####'GridFAND'#############################
            FAIND.append(var3)
            var5=gridfeature.GetField(name4)###'Dis_len'################################
            dis_len.append(var5)

        name_of_file = 'Macdonald Roughness Length'
        completeName = os.path.join(output, name_of_file+".txt") 
        f_mclen = open(completeName , "w")
        #f_mclen=open('Macdonald Roughness Length.txt','w')
        cd=1.2
        k=0.4
        B=1.0
        u=(k**2)
                    
        count=0    

        while(count<prod):
            lf=FAIND[count]  #value needed frontal area density
            if(lf==0):
                Zo=0
                rou_len.append(Zo)
                f_mclen.write('Macdonald Roughness Length for Grid {0} is 0.\n'.format(count))
            else:
                x=1-(dis_len[count]/Mean[count])
                var23=(cd/u)
                v=(0.5*B*var23*x*lf)
                y=(v**(-0.5))
                w=math.exp(y)
                z=(x *w)
                Zo=Mean[count]*z
                rou_len.append(Zo)
                f_mclen.write('Macdonald Roughness Length for Grid {0} is {1}.\n'.format(count,Zo))
            count+=1
            
        f_mclen.close()
        i=0
        for i in range(GridLayer.GetFeatureCount()):
                GridFeat = GridLayer.GetFeature(i)
                GridFeat.SetField(name,rou_len[i])
                GridLayer.SetFeature(GridFeat)
        print('Macdonald Roughness Length Completed')

    def Raupach_Displacement_Height(self):
        driver = ogr.GetDriverByName('ESRI Shapefile')
        unionfile = str(Ui_MainWindow.unionfile_path)
        unionSource = driver.Open(unionfile,1)
        #unionSource = driver.Open('F:\\codes\\codes\\reprojected\\7buildingunion2.shp',1)
        unionLayer = unionSource.GetLayer()
        #GridSource = driver.Open('F:\\codes\\codes\\reprojected\\7buildgrid.shp',1)
        gridfile=str(Ui_MainWindow.gridfile_path)
        output = str(Ui_MainWindow.outputfile_path)
        GridSource=driver.Open(gridfile,1)
        GridLayer = GridSource.GetLayer()
        GridFeat = unionLayer.GetFeature(0)
        GridGeom = GridFeat.GetGeometryRef()
        list1 = unionLayer.GetExtent()
        list2 = GridGeom.GetEnvelope()
        text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Rapauch displacement height:')
        if ok:
            name=str(text)
        sch= []
        check=0
        text2, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name of Mean Building Height:')        
        if ok:
            name2=str(text2)

        text3, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name of Plan Area Fraction:')        
        if ok:
            name3=str(text3)
        n=0
        for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
            field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
            sch.append(field) 
        n=0
        for n in range(len(sch)):
           if(name==str(sch[n])):
               check=1
               print('Field Already exists')
        if (check==0):
            new_field = ogr.FieldDefn(name, ogr.OFTReal)
            GridLayer.CreateField(new_field)
            print('New Field Created')
        noc = (list1[1]-list1[0])/(list2[1]-list2[0])
        nor = (list1[3]-list1[2])/(list2[3]-list2[2])
        prod=noc*nor
        build=[]
        hieght=[]
        BuildId = []
        BuildGdId = []
        PAF=[]
        Mean=[]
        ra_dis=[]
        #new_field = ogr.FieldDefn("Ra_Dis", ogr.OFTReal)
        #new_field.SetWidth(32)
        #new_field.SetPrecision(2)
        #GridLayer.CreateField(new_field)        
        for i in range(unionLayer.GetFeatureCount()):
            feature=unionLayer.GetFeature(i)
            buildheight2=feature.GetField(Ui_MainWindow.hei_name)
            build.append(buildheight2)
            var1=feature.GetField('FIDGrid')
            BuildGdId.append(var1)
            var2=feature.GetField('FIDBuild')
            BuildId.append(var2)

        i=0
        for i in range(GridLayer.GetFeatureCount()):
            gridfeature=GridLayer.GetFeature(i)    
            var4=gridfeature.GetField(name2)############'Mean'#############
            Mean.append(var4)
            var5=gridfeature.GetField(name3)##########'PAF'##############
            PAF.append(var5)
        name_of_file = 'Raupach Displacement height'
        completeName = os.path.join(output, name_of_file+".txt") 
        f_radis= open(completeName , "w")
        #f_radis=open('Raupach Displacement height.txt','w')
        count=0    
        while(count<prod):
            p1=float((7.5)*2*PAF[count])
            if(p1==0):
                p8=0
                ra_dis.append(p8)
                f_radis.write("Rad for grid {0} is {1}".format(count,p8))
            else:            
                p2=p1**0.5
                p3=p1-1
                p4=math.exp(p3)
                p5=float(p4)*float(1/p1)
                p6=p5+1
                p7=Mean[count]
                p8=p6/p7
                f_radis.write("Rad for grid {0} is {1}".format(count,p8))
                ra_dis.append(p8)
            count+=1
        f_radis.close()       
        i=0
        for i in range(GridLayer.GetFeatureCount()):
                GridFeat = GridLayer.GetFeature(i)
                GridFeat.SetField(name,ra_dis[i])
                GridLayer.SetFeature(GridFeat)
        print('Raupach Displacement height Completed')

    def Raupach_Roughness_length(self):
        driver = ogr.GetDriverByName('ESRI Shapefile')
        unionfile = str(Ui_MainWindow.unionfile_path)
        unionSource = driver.Open(unionfile,1)
        #unionSource = driver.Open('F:\\codes\\codes\\reprojected\\7buildingunion2.shp',1)
        unionLayer = unionSource.GetLayer()
        #GridSource = driver.Open('F:\\codes\\codes\\reprojected\\7buildgrid.shp',1)
        gridfile=str(Ui_MainWindow.gridfile_path)
        GridSource=driver.Open(gridfile,1)
        GridLayer = GridSource.GetLayer()
        output = str(Ui_MainWindow.outputfile_path)
        GridFeat = unionLayer.GetFeature(0)
        GridGeom = GridFeat.GetGeometryRef()
        list1 = unionLayer.GetExtent()
        list2 = GridGeom.GetEnvelope()
        text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Rapauch roughness length:')        
        if ok:
            name=str(text)

        sch= []
        check=0
        text2, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Mean Building Height:')        
        if ok:
            name2=str(text2)

        text3, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Frontal Area Index:')        
        if ok:
            name3=str(text3)
        text4, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Rapauch Displacement Height:')        
        if ok:
            name4=str(text4)
        n=0
        for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
            field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
            sch.append(field) 
        n=0
        for n in range(len(sch)):
           if(name==str(sch[n])):
               check=1
               print('Field Already exists')
        if (check==0):
            new_field = ogr.FieldDefn(name, ogr.OFTReal)
            GridLayer.CreateField(new_field)
            print('New Field Created')
        noc = (list1[1]-list1[0])/(list2[1]-list2[0])
        nor = (list1[3]-list1[2])/(list2[3]-list2[2])
        prod=noc*nor
        build=[]
        hieght=[]
        BuildId = []
        BuildGdId = []
        plan_ar_fr=[]
        FAIND=[]
        Mean=[]
        rou_len=[]
        raf_ralen=[]
        ra_dis=[]
        count = 0
        #new_field = ogr.FieldDefn("Ra_rou", ogr.OFTReal)
        #new_field.SetWidth(32)
        #new_field.SetPrecision(2)
        #GridLayer.CreateField(new_field)        
        for i in range(unionLayer.GetFeatureCount()):
            feature=unionLayer.GetFeature(i)
            buildheight2=feature.GetField(Ui_MainWindow.hei_name)
            build.append(buildheight2)
            var1=feature.GetField('FIDGrid')
            BuildGdId.append(var1)
            var2=feature.GetField('FIDBuild')
            BuildId.append(var2)

        i=0
        for i in range(GridLayer.GetFeatureCount()):
            gridfeature=GridLayer.GetFeature(i)    
            var4=gridfeature.GetField(name2)#######'Mean'###################################
            Mean.append(var4)
            var3=gridfeature.GetField(name3)#####'GridFAND'#####################################
            FAIND.append(var3)
            var5=gridfeature.GetField(name4)########'Ra_Dis'##################################
            ra_dis.append(var5)

        name_of_file = 'Raupach Roughness Length'
        completeName = os.path.join(output, name_of_file+".txt") 
        f_ralen= open(completeName , "w")
        #f_ralen=open('Raupach Roughness Length.txt','w')

        count=0    
        while(count<prod):
            w1=0.003+0.3*FAIND[i]
            if(w1==0 or Mean[count]==0):
                w8=0
                rou_len.append(w8)
            else:
                w2=w1**0.5
                #print(w2)
                w3=min(w2,0.3)
                #print(w3)
                w4=(-0.4)*w3+0.193
                #print('w4',w4)
                w5=math.exp(w4)
                #print('w6',w5)
                w6=1-float(ra_dis[count])/float(Mean[count])
                #print('w6',w6)
                w7=w5*w6
                #print('w7',w7)
                w8=Mean[count]*w7
                rou_len.append(w8)
            f_ralen.write('Raupach Roughness Length for Grid {0} is {1}\n'.format(count,w8))
            count+=1
        f_ralen.close()
        i=0
        for i in range(GridLayer.GetFeatureCount()):
                GridFeat = GridLayer.GetFeature(i)
                GridFeat.SetField(name,rou_len[i])
                GridLayer.SetFeature(GridFeat)   
        print('Raupach Roughness Length Completed')         

    def Grimmond_Displacement_Height(self):
        driver = ogr.GetDriverByName('ESRI Shapefile')
        unionfile = str(Ui_MainWindow.unionfile_path)
        unionSource = driver.Open(unionfile,1)
        unionLayer = unionSource.GetLayer()
        gridfile=str(Ui_MainWindow.gridfile_path)
        output = str(Ui_MainWindow.outputfile_path)
        GridSource=driver.Open(gridfile,1)
        GridLayer = GridSource.GetLayer()
        GridFeat = unionLayer.GetFeature(0)
        GridGeom = GridFeat.GetGeometryRef()
        list1 = unionLayer.GetExtent()
        list2 = GridGeom.GetEnvelope()
        text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Grimmond and Oke \n Displacement height:')
        if ok:
            name=str(text)
        sch= []
        text2, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name of Mean Buildings Height:')        
        if ok:
            name2=str(text2)
        check=0
        n=0
        for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
            field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
            sch.append(field) 
        n=0
        for n in range(len(sch)):
           if(name==str(sch[n])):
               check=1
               print('Field Already exists')
        if (check==0):
            new_field = ogr.FieldDefn(name, ogr.OFTReal)
            GridLayer.CreateField(new_field)
            print('New Field Created')
        noc = (list1[1]-list1[0])/(list2[1]-list2[0])
        nor = (list1[3]-list1[2])/(list2[3]-list2[2])
        prod=noc*nor
        build=[]
        hieght=[]
        BuildId = []
        BuildGdId = []
        Mean=[]
        mean_build_hei=[]
        count = 0
        grim_hei=[]
        for i in range(unionLayer.GetFeatureCount()):
            feature=unionLayer.GetFeature(i)
            buildheight2=feature.GetField(Ui_MainWindow.hei_name)
            build.append(buildheight2)
            var1=feature.GetField('FIDGrid')
            BuildGdId.append(var1)
            var2=feature.GetField('FIDBuild')
            BuildId.append(var2)
        for i in range(GridLayer.GetFeatureCount()):
            gridfeature=GridLayer.GetFeature(i)
            var3=gridfeature.GetField(name2)
            Mean.append(var3)
        name_of_file = 'Grimmond & Oke Displacement Height'
        completeName = os.path.join(output, name_of_file+".txt") 
        f_grodis= open(completeName , "w")
        #f_mcdis=open('Macdonald Displacement Height.txt','w')            
        count=0    
        while(count<prod):
            gimok=0.1*Mean[count]
            grim_hei.append(gimok)
            f_grodis.write('Grimmond & Oke Displacement Height for Grid {0} is {1}\n'.format(count,gimok))
            count+=1
        f_grodis.close()    
        i=0
        for i in range(GridLayer.GetFeatureCount()):
                GridFeat = GridLayer.GetFeature(i)
                GridFeat.SetField(name,grim_hei[i])
                GridLayer.SetFeature(GridFeat)
        print('Grimmond & Oke Displacement Height Completed')

    def Grimmond_Roughness_Length(self):
        driver = ogr.GetDriverByName('ESRI Shapefile')
        unionfile = str(Ui_MainWindow.unionfile_path)
        unionSource = driver.Open(unionfile,1)
        unionLayer = unionSource.GetLayer()
        gridfile=str(Ui_MainWindow.gridfile_path)
        output = str(Ui_MainWindow.outputfile_path)
        GridSource=driver.Open(gridfile,1)
        GridLayer = GridSource.GetLayer()
        GridFeat = unionLayer.GetFeature(0)
        GridGeom = GridFeat.GetGeometryRef()
        list1 = unionLayer.GetExtent()
        list2 = GridGeom.GetEnvelope()
        text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for Grimmond and Oke \n Roughness Length:')
        if ok:
            name=str(text)
        sch= []
        text2, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name of Mean Buildings Height:')        
        if ok:
            name2=str(text2)
        check=0
        n=0
        for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
            field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
            sch.append(field) 
        n=0
        for n in range(len(sch)):
           if(name==str(sch[n])):
               check=1
               print('Field Already exists')
        if (check==0):
            new_field = ogr.FieldDefn(name, ogr.OFTReal)
            GridLayer.CreateField(new_field)
            print('New Field Created')
        noc = (list1[1]-list1[0])/(list2[1]-list2[0])
        nor = (list1[3]-list1[2])/(list2[3]-list2[2])
        prod=noc*nor
        build=[]
        hieght=[]
        BuildId = []
        BuildGdId = []
        Mean=[]
        mean_build_hei=[]
        count = 0
        grim_hei=[]
        for i in range(GridLayer.GetFeatureCount()):
            gridfeature=GridLayer.GetFeature(i)
            var3=gridfeature.GetField(name2)
            Mean.append(var3)
        name_of_file = 'Grimmond & Oke Roughness Length'
        completeName = os.path.join(output, name_of_file+".txt") 
        f_grolen= open(completeName , "w")
        #f_mcdis=open('Macdonald Displacement Height.txt','w')            
        count=0    
        while(count<prod):
            gimok=0.5*float(Mean[count])
            grim_hei.append(gimok)
            f_grolen.write('Grimmond & Oke Roughness Length for Grid {0} is {1}\n'.format(count,gimok))
            count+=1
        f_grolen.close()    
        i=0
        for i in range(GridLayer.GetFeatureCount()):
                GridFeat = GridLayer.GetFeature(i)
                GridFeat.SetField(name,grim_hei[i])
                GridLayer.SetFeature(GridFeat)
        print('Grimmond & Oke Roughness Length Completed')

        
    def myfunc_PAFD(self):
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog_PAFD()
        ui.setupUi(Dialog)
        Dialog.exec_()

    def myfunc_SVF(self):
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog_SVF()
        ui.setupUi(Dialog)
        Dialog.exec_()        

    def myfunc_HWR(self):
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog_HWR()
        ui.setupUi(Dialog)
        Dialog.exec_()        

    def myfunc_FAID(self):
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog_FAID()
        ui.setupUi(Dialog)
        Dialog.exec_()

class Ui_Dialog_FAID(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(641, 374)
        Dialog.setStyleSheet(_fromUtf8("QDialog{\n"
"color:navy; background-color: white;\n"
"\n"
"                     \n"
"}\n"
"QRadioButton{\n"
"color:navy;\n"
"}\n"
"QLabel{\n"
"color: navy; \n"
"                        \n"
"                        selection-color: yellow;\n"
"                        selection-background-color: blue;\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
" border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
""))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 20, 231, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 210, 261, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.Browse4 = QtGui.QPushButton(Dialog)
        self.Browse4.setGeometry(QtCore.QRect(490, 210, 84, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Browse4.setFont(font)
        self.Browse4.setObjectName(_fromUtf8("Browse4"))
        self.ok_btn = QtGui.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(230, 330, 84, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.cancel_btn = QtGui.QPushButton(Dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(330, 331, 84, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 170, 261, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 191, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 191, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(200, 90, 261, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.Browse1 = QtGui.QPushButton(Dialog)
        self.Browse1.setGeometry(QtCore.QRect(490, 90, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Browse1.setFont(font)
        self.Browse1.setObjectName(_fromUtf8("Browse1"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 191, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Browse3 = QtGui.QPushButton(Dialog)
        self.Browse3.setGeometry(QtCore.QRect(490, 170, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Browse3.setFont(font)
        self.Browse3.setObjectName(_fromUtf8("Browse3"))
        self.Browse2 = QtGui.QPushButton(Dialog)
        self.Browse2.setGeometry(QtCore.QRect(490, 130, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Browse2.setFont(font)
        self.Browse2.setObjectName(_fromUtf8("Browse2"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 130, 261, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 170, 151, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 326, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(160, 290, 161, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.Wind_Select = QtGui.QComboBox(Dialog)
        self.Wind_Select.setGeometry(QtCore.QRect(340, 250, 281, 20))
        self.Wind_Select.setObjectName(_fromUtf8("Wind_Select"))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Resolution = QtGui.QSpinBox(Dialog)
        self.Resolution.setGeometry(QtCore.QRect(340, 290, 42, 22))
        self.Resolution.setMaximum(20)
        self.Resolution.setObjectName(_fromUtf8("Resolution"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QObject.connect(self.Browse1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.footprint_browse)
        QtCore.QObject.connect(self.Browse2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.wind_browse)
        QtCore.QObject.connect(self.Browse3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.grid_browse)
        QtCore.QObject.connect(self.Browse4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.output_browse)
        QtCore.QObject.connect(self.ok_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.myfunc_FAID)
        self.Resolution.valueChanged[str].connect(self.input_resolution)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Compute Frontal Area", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Frontal Area Index</span></p></body></html>", None))
        self.Browse4.setText(_translate("Dialog", "Browse", None))
        self.ok_btn.setText(_translate("Dialog", "Ok", None))
        self.cancel_btn.setText(_translate("Dialog", "Cancel", None))
        self.label_3.setText(_translate("Dialog", "Select the Wind Lines Shapefile:", None))
        self.label_4.setText(_translate("Dialog", "Select the footprint Building Shapefile:", None))
        self.Browse1.setText(_translate("Dialog", "Browse", None))
        self.label_5.setText(_translate("Dialog", "Select the output files location:", None))
        self.Browse3.setText(_translate("Dialog", "Browse", None))
        self.Browse2.setText(_translate("Dialog", "Browse", None))
        self.label_7.setText(_translate("Dialog", "Select the location of grid file..", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Select the direction for which Shape file is to be created:</span></p></body></html>", None))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Enter wind line resolution:</span></p></body></html>", None))
        self.Wind_Select.setToolTip(_translate("Dialog", "<html><head/><body><p>Select the angle for the direction of wind </p></body></html>", None))
        self.Wind_Select.setItemText(0, _translate("Dialog", "Angles start from south & proceeds anticlockwise.", None))
        self.Wind_Select.setItemText(1, _translate("Dialog", "0 Degrees", None))
        self.Wind_Select.setItemText(2, _translate("Dialog", "45 Degrees", None))
        self.Wind_Select.setItemText(3, _translate("Dialog", "90 Degrees", None))
        self.Wind_Select.setItemText(4, _translate("Dialog", "135 Degrees", None))
        self.Wind_Select.setItemText(5, _translate("Dialog", "180 Degrees", None))
        self.Wind_Select.setItemText(6, _translate("Dialog", "225 Degrees", None))
        self.Wind_Select.setItemText(7, _translate("Dialog", "270 Degrees", None))
        self.Wind_Select.setItemText(8, _translate("Dialog", "315 Degrees", None))

    def footprint_browse(self):
        print ('selecting folder containing building footprint')
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home',filter= '*.shp')
        self.footprint_path = self.fname.replace('\\','/')
        self.lineEdit.setText(self.fname)
        print(self.footprint_path)

    def wind_browse(self):
        print ('selecting folder that will contain wind direction shape file')
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home',filter= '*.shp')
        self.wind_path = self.fname.replace('\\','/')
        self.lineEdit_2.setText(self.fname)
        print(self.wind_path)

    def grid_browse(self):
        print ('selecting folder containing Grid shape file ')
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home',filter= '*.shp')
        self.grid_path = self.fname.replace('\\','/')
        self.lineEdit_4.setText(self.fname)
        print(self.grid_path)

    def output_browse(self):
        print ('selecting folder containing output text file')
        #self.fname = QtGui.QFileDialog.getSaveFileName(None, 'Save file','/home',filter = '*.txt')
        self.fname = QtGui.QFileDialog.getExistingDirectory(None, "Select Directory for saving output files")
        self.output_path = self.fname.replace('\\','/')
        self.lineEdit_3.setText(self.fname)
        print(self.output_path)

    def input_resolution(self):
        self.reso_val = self.Resolution.value()

    def myfunc_FAID(self):
        self.Index_ = self.Wind_Select.currentIndex()
        if self.Index_ == 1:
            Driver1 = ogr.GetDriverByName('ESRI Shapefile')
            Grid =str(self.grid_path)
            GridSource = Driver1.Open(Grid,1)
            GridLayer = GridSource.GetLayer()
            length = GridLayer.GetFeatureCount()
            frontalAreaList = list([0.0 for x in range(length)])
            Footprint = str(self.footprint_path)
            BuildingSource = Driver1.Open(Footprint,0)
            BuildingLayer = BuildingSource.GetLayer()
            wind = str(self.wind_path)
            WindSource = Driver1.Open(wind,0)
            WindLayer = WindSource.GetLayer()
            output = str(self.output_path)
            layer_defn = GridLayer.GetLayerDefn()
            #print self.Wind_select.currentText()
            text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for frontal area index :')
            if ok:
                name=str(text)
            ldefn = GridLayer.GetLayerDefn()
            sch= []
            check=0
            n=0
            for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
                field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
                sch.append(field) 
            n=0
            for n in range(len(sch)):
               if(name==str(sch[n])):
                   check=1
                   print('Field Already exists')
            if (check==0):
                new_field = ogr.FieldDefn(name, ogr.OFTReal)
                GridLayer.CreateField(new_field)
                print('New Field Created')
            FrontalArea = 0
            GridFrontalArea = []
            length = GridLayer.GetFeatureCount()
            GridFeat = GridLayer.GetFeature(0)
            GridGeom = GridFeat.GetGeometryRef()
            list1 = GridLayer.GetExtent()
            list2 = GridGeom.GetEnvelope()
            noc = (list1[1]-list1[0])/(list2[1]-list2[0])
            nor = (list1[3]-list1[2])/(list2[3]-list2[2])
            i=0
            f=0
            l=0
            k= -noc
            height_list2 = []
            height_list3 = [] 
            height_list1 = []
            area=0
            name_of_file = 'Frontal Area Index Grid 0 DEG'
            completeName = os.path.join(output, name_of_file+".txt") 
            faid0 = open(completeName , "w")
            #sys.stdout = open('running.txt','w')

            for Grid in range(0,length):
                

                BuildingSeq = []
                WindSeq = []
                polyIntersectSeq = []   
                polySeq = []
                if f<=nor-1:
                    k=k+noc
                    f=f+1
                    
                else:
                    k=l+1
                    f= 1
                    l=l+1
                     
              
               
                GridFeat = GridLayer.GetFeature(int(abs(k)))
               
                GridGeom = GridFeat.GetGeometryRef()
                area=GridGeom.GetArea()
                BuildingLayer.SetSpatialFilter(GridGeom)
                WindLayer.SetSpatialFilter(GridGeom)

                GridList= list(GridGeom.GetEnvelope())
                # print GridList
                lineSpacing = self.reso_val
                
                for line in range(0,WindLayer.GetFeatureCount()):
                     
                    windFeature = WindLayer.GetNextFeature()
                    windGeometry = windFeature.GetGeometryRef()
                   
                    
                    for poly in range(0,BuildingLayer.GetFeatureCount()):
                        polyFeature = BuildingLayer.GetNextFeature()
                        if not polyFeature:
                            continue
                        polyGeom = polyFeature.GetGeometryRef()
                        Intersect = windGeometry.Intersection(polyGeom)
                        
                        if Intersect.IsEmpty()==False:
                            abc = list(Intersect.GetEnvelope())
                            # print abc
                            # print "Entering intersect"
                            if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                            # polyIntersectSeq.append(Intersect.GetPoints())
                            # polySeq.append(polyFeature.GetFID())
                                height_list1.append(polyFeature.GetField('height'))
                                # print "Entering GridCompare"
                        # else:
                        #     o=0
                        #     height_list1.append(o)
                    BuildingLayer.ResetReading()
                    if height_list1:
                        m = max(height_list1)
                    else:
                        m=0  
                    #print m 
                    #print "H1 is "
                    #print height_list1   
                    #print                 
                    height_list2.append(m)
                    del height_list1[:]
                    #print ("Height_list2 earlier",height_list2)
                for x in range(0,len(height_list2)):
                    if len(height_list3) == 0:
                        FrontalArea = FrontalArea+ lineSpacing*(height_list2[x])
                        # print 'hello : Length '
                        # p print "len"rint len(height_list3)

                    else:
                    
                        if (height_list2[x]-height_list3[x])>0:
                            j = height_list2[x]-height_list3[x]
                            # print"@@@@@@@"
                            FrontalArea= FrontalArea+ lineSpacing*(j)
                            # print k
                        else:
                            j=0
                            FrontalArea= FrontalArea+ lineSpacing*(j)
                #print "H2 is "
                #print height_list2
                #print "h3 is "
                #print height_list3
                FrontalArId= float(FrontalArea)*float(1/area)            
                faid0.write("The Frontal area Index for Grid {0} is {1} \n " .format(GridFeat.GetFID(),FrontalArId))
                frontalAreaList[GridFeat.GetFID()] = FrontalArea
                GridFeat.SetField(name,FrontalArId)
                GridLayer.SetFeature(GridFeat)
                #print
                
                FrontalArea=0
                i=i+1 
                
                if(i>=nor):
                    del height_list3[:]
                    del height_list2[:]
                    i=0
                   
                else:
                    del height_list3[:]
                    height_list3= list(height_list2) 
                    del height_list2[:]
                    
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
            faid0.close()
            print('Frontal Area Index Completed')

        if self.Index_ == 2:
            Driver1 = ogr.GetDriverByName('ESRI Shapefile')
            Grid =str(self.grid_path)
            GridSource = Driver1.Open(Grid,1)
            GridLayer = GridSource.GetLayer()
            Footprint = str(self.footprint_path)
            BuildingSource = Driver1.Open(Footprint,0)
            BuildingLayer = BuildingSource.GetLayer()
            wind = str(self.wind_path)
            WindSource = Driver1.Open(wind,0)
            output = str(self.output_path)
            WindLayer = WindSource.GetLayer()
            layer_defn = GridLayer.GetLayerDefn()


            text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for frontal area index :')
            if ok:
                name=str(text)
            ldefn = GridLayer.GetLayerDefn()
            sch= []
            check=0
            n=0
            for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
                field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
                sch.append(field) 
            n=0
            for n in range(len(sch)):
               if(name==str(sch[n])):
                   check=1
                   print('Field Already exists')
            if (check==0):
                new_field = ogr.FieldDefn(name, ogr.OFTReal)
                GridLayer.CreateField(new_field)
                print('New Field Created')

            GridLayer.CreateField(new_field)
            FrontalArea = 0
            GridFrontalArea = []
            length = GridLayer.GetFeatureCount()
            lineSpacing= self.reso_val
            ListTop = []
            ListBottom = []
            ListRight = []
            ListLeft = []
            windLeft = []
            windRight = []
            windBottomLeft = []
            windBottomRight = []
            listFrontalArea = list([0.0 for x in range(length)])
            GridFeat =  GridLayer.GetFeature(0)

            GridGeom = GridFeat.GetGeometryRef()
            list1 = GridLayer.GetExtent()
            list2 = GridGeom.GetEnvelope()
            col = int((list1[1]-list1[0])/(list2[1]-list2[0]))
            row = int((list1[3]-list1[2])/(list2[3]-list2[2]))
            # print "COl"
            # print col
            # print "row"
            # print row
            name_of_file = 'Frontal Area Index 45 DEG'
            completeName = os.path.join(output, name_of_file+".txt") 
            faid45 = open(completeName , "w")
            #sys.stdout = open('running.txt','w')
            k=1
            q=0
            
            for Grid in range(0,GridLayer.GetFeatureCount()):
                if(Grid == k*col-1):
                    k=k+1
                    continue
                if(Grid == (row-1)*col):
                    break

                GridFeat1 = GridLayer.GetFeature(int(Grid))
                GridGeom1 = GridFeat1.GetGeometryRef()
                GridList= list(GridGeom1.GetEnvelope())
                # print("Grid Points",GridList)
                # print
                WindLayer.SetSpatialFilter(GridGeom1)
                BuildingLayer.SetSpatialFilter(GridGeom1)
                
                
                for wind_line in range(0,WindLayer.GetFeatureCount()):

                    maxx=0
                    feature =  WindLayer.GetNextFeature()

                    interWind = feature.GetGeometryRef()
                    windLeft.append(feature.GetFID())
                    for buildings in range(0,BuildingLayer.GetFeatureCount()):
                         currentPolyFeat = BuildingLayer.GetNextFeature()
                         currentPolyGeom = currentPolyFeat.GetGeometryRef()

                         FirstIntersect =interWind.Intersection(currentPolyGeom)
                         if FirstIntersect != None and FirstIntersect.IsEmpty()==False:
                            abc = list(FirstIntersect.GetEnvelope())

                            
                            # if ((GridList[0] > abc[0] or GridList[1] < abc[0]) and (GridList[1]< abc[1] or GridList[0]> abc[1])) and ((GridList[2] < abc[2] or GridList[3] > abc[2]) and (GridList[3]> abc[3] or GridList[2]< abc[3])):
                               
                            #    continue
                         # if ( (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[3] < GridList[2]) and (abc[3] > GridList[3]))) or (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[2] < GridList[2]) and (abc[2] > GridList[3]))) ):                            
                            if ( (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                curmaxOfLine = currentPolyFeat.GetField("Height")
                                if(curmaxOfLine > maxx):
                                    maxx = curmaxOfLine
                    ListLeft.append(maxx)
                    
                    BuildingLayer.ResetReading()
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
                WindLayer.ResetReading()
                BuildingLayer.ResetReading()

                
                
                # print ("ListLeft",ListLeft)
              
                    

                GridFeat2 = GridLayer.GetFeature(int(Grid+1))
                GridGeom2 = GridFeat2.GetGeometryRef()
                GridList= list(GridGeom2.GetEnvelope())
                WindLayer.SetSpatialFilter(GridGeom2)
                BuildingLayer.SetSpatialFilter(GridGeom2)
                for wind_line in range(0,WindLayer.GetFeatureCount()):  
                    maxx = 0
                    feature = WindLayer.GetNextFeature() 
                    # print("windline no . ",feature.GetFID())
                    interWind = feature.GetGeometryRef()                 
                    windRight.append(feature.GetFID())
                    for buildings in range(0,BuildingLayer.GetFeatureCount()):
                         currentPolyFeat = BuildingLayer.GetNextFeature()
                         # print("Building is . ",currentPolyFeat.GetField('Id'))
                         currentPolyGeom = currentPolyFeat.GetGeometryRef()
                         FirstIntersect = interWind.Intersection(currentPolyGeom)
                         if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                            abc = list(FirstIntersect.GetEnvelope())
                            # print("Wind intersect ",abc)
                            # if ((GridList[0] > abc[0] or GridList[1] < abc[0]) and (GridList[1]< abc[1] or GridList[0]> abc[1])) and ((GridList[2] < abc[2] or GridList[3] > abc[2]) and (GridList[3]> abc[3] or GridList[2]< abc[3])):
                               
                            #    continue
                            if ( (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):                            
                                curmaxOfLine = currentPolyFeat.GetField("Height")
                                if(curmaxOfLine > maxx):
                                    maxx = curmaxOfLine

                    ListRight.append(maxx)
                    BuildingLayer.ResetReading()
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
                WindLayer.ResetReading()
                BuildingLayer.ResetReading()
                # print ("ListRight",ListRight)


                GridFeat3 = GridLayer.GetFeature(int(Grid+col))
                GridGeom3 = GridFeat3.GetGeometryRef()
                GridList= list(GridGeom3.GetEnvelope())
                WindLayer.SetSpatialFilter(GridGeom3)
                BuildingLayer.SetSpatialFilter(GridGeom3)
                for wind_line in range(0,WindLayer.GetFeatureCount()):
                    maxx = 0
                    feature = WindLayer.GetNextFeature()  
                    interWind = feature.GetGeometryRef()
                    windBottomLeft.append(feature.GetFID())
                  
                    for buildings in range(0,BuildingLayer.GetFeatureCount()):
                         currentPolyFeat = BuildingLayer.GetNextFeature()
                                                   
                         currentPolyGeom = currentPolyFeat.GetGeometryRef()
                         FirstIntersect = interWind.Intersection(currentPolyGeom)
                         if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                            abc = list(FirstIntersect.GetEnvelope())
                            
                            # if ((GridList[0] > abc[0] or GridList[1] < abc[0]) and (GridList[1]< abc[1] or GridList[0]> abc[1])) :
                               
                            #    continue
                            if ( (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                curmaxOfLine = currentPolyFeat.GetField("Height")
                                if(curmaxOfLine > maxx):
                                    maxx = curmaxOfLine
                    ListTop.append(maxx)
                    BuildingLayer.ResetReading()
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
                WindLayer.ResetReading()
                BuildingLayer.ResetReading()
                # print ("ListBottomLeft",ListTop)

                GridFeat4 = GridLayer.GetFeature(int(Grid+col+1))
                GridGeom4 = GridFeat4.GetGeometryRef()
                GridList= list(GridGeom4.GetEnvelope())          
                WindLayer.SetSpatialFilter(GridGeom4)
                BuildingLayer.SetSpatialFilter(GridGeom4)
                for wind_line in range(0,WindLayer.GetFeatureCount()):
                    maxx = 0
                    feature = WindLayer.GetNextFeature()  
                    interWind = feature.GetGeometryRef()
                    windBottomRight.append(feature.GetFID())
                    for buildings in range(0,BuildingLayer.GetFeatureCount()):
                         currentPolyFeat = BuildingLayer.GetNextFeature()
                         currentPolyGeom = currentPolyFeat.GetGeometryRef()
                         FirstIntersect = interWind.Intersection(currentPolyGeom)
                         if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                            abc = list(FirstIntersect.GetEnvelope())
                            
                            # if ((GridList[0] > abc[0] or GridList[1] < abc[0]) and (GridList[1]< abc[1] or GridList[0]> abc[1])) :
                               
                            #    continue
                            if ( (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                curmaxOfLine = currentPolyFeat.GetField("Height")
                                if(curmaxOfLine > maxx):
                                    maxx = curmaxOfLine
                    ListBottom.append(maxx)
                    BuildingLayer.ResetReading()
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
                WindLayer.ResetReading()
                BuildingLayer.ResetReading()
                # print ("ListBottomRight",ListBottom)

                #for GridRight
                for i in range(0,len(windLeft)):
                    for j in range(0,len(windRight)):
                        if windLeft[i]==windRight[j]:
                            if ListLeft[i]<ListRight[j]:
                                ListRight[j]= ListRight[j]-ListLeft[i]
                            else:
                                ListRight[j]=0
                # print ("ListRight",ListRight)
                #GridBottomLeft
                for i in range(0,len(windLeft)):
                    for j in range(0,len(windBottomLeft)):
                        if windLeft[i]==windBottomLeft[j]:
                            if ListTop[j]>ListLeft[i]:
                                ListTop[j]= ListTop[j]-ListLeft[i]
                            else:
                                ListTop[j]=0
                # print ("ListBottomLeft",ListTop)
                #GridBottomRight
                for i in range(0,len(windRight)):
                    for j in range(0,len(windBottomRight)):
                        if windRight[i]==windBottomRight[j]:
                            if ListBottom[j]>ListRight[i]:
                                ListBottom[j]= ListBottom[j]-ListRight[i]
                            else:
                                ListBottom[j]=0
                # print ("ListBottomRight",ListBottom)


                for i in range(0,len(windBottomLeft)):
                    for j in range(0,len(windBottomRight)):
                        if windBottomLeft[i]==windBottomRight[j]:
                            if ListTop[i]<ListBottom[j]:
                                ListBottom[j]= ListBottom[j]-ListTop[i]
                            else:
                                ListBottom[j]=0
                # print ("ListBottomRight",ListBottom)
                
                if(listFrontalArea[Grid] == 0):
                    listFrontalArea[Grid] = sum(ListLeft)* lineSpacing ;
                if(listFrontalArea[Grid+1] == 0):
                    listFrontalArea[Grid+1] = sum(ListRight)* lineSpacing ;
                if(listFrontalArea[Grid+col] == 0):
                    listFrontalArea[Grid+col] = sum(ListTop)* lineSpacing ;
                if(listFrontalArea[Grid+col+1] == 0):
                    listFrontalArea[Grid+col+1] = sum(ListBottom)* lineSpacing ;

                
                del windLeft[:]
                del windRight[:]
                del windBottomRight[:]
                del windBottomLeft[:]


                del ListLeft[:]
                del ListRight[:]
                del ListTop[:]
                del ListBottom[:]
            for i in range(0,len(listFrontalArea)):
                FrontalArId= float(listFrontalArea[i])*float(1/area)            
                faid45.write("The Frontal area Index for Grid {0} is {1} \n " .format(GridFeat.GetFID(),FrontalArId))
                Grid_feature = GridLayer.GetFeature(i)
                Grid_feature.SetField(name,FrontalArId)
                GridLayer.SetFeature(Grid_feature)

            # print "Answer List is"
            # print listFrontalArea
            #cfg45.write ("The total frontal area is {0} \n".format(sum(listFrontalArea)))
            # for gridFrontal in range(0,len(listFrontalArea)):
            #     Grid_feature = GridLayer.GetFeature(gridFrontal)
                
            #     Grid_feature.SetField('GridFA',listFrontalArea[gridFrontal])
            #     GridLayer.SetFeature(Grid_feature)
            faid45.close()
            print('Frontal Area Index Completed')

        if self.Index_ == 3:
            Driver1 = ogr.GetDriverByName('ESRI Shapefile')
            Grid =str(self.grid_path)
            # print(Grid)
            GridSource = Driver1.Open(Grid,1)
            GridLayer = GridSource.GetLayer()
            length = GridLayer.GetFeatureCount()
            frontalAreaList = list([0.0 for x in range(length)])
            Footprint = str(self.footprint_path)
            BuildingSource = Driver1.Open(Footprint,0)
            BuildingLayer = BuildingSource.GetLayer()
            wind = str(self.wind_path)
            WindSource = Driver1.Open(wind,0)
            WindLayer = WindSource.GetLayer()
            layer_defn = GridLayer.GetLayerDefn()
            # new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
            #new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
            # GridLayer.CreateField(new_field)
            #GridLayer.CreateField(new_field)
            text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for frontal area index :')
            if ok:
                name=str(text)
            ldefn = GridLayer.GetLayerDefn()
            sch= []
            check=0
            n=0
            for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
                field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
                sch.append(field) 
            n=0
            for n in range(len(sch)):
               if(name==str(sch[n])):
                   check=1
                   print('Field Already exists')
            if (check==0):
                new_field = ogr.FieldDefn(name, ogr.OFTReal)
                GridLayer.CreateField(new_field)
                print('New Field Created')
            FrontalArea = 0
            GridFrontalArea = []
            length = GridLayer.GetFeatureCount()
            GridFeat = GridLayer.GetFeature(0)
            GridGeom = GridFeat.GetGeometryRef()
            list1 = GridLayer.GetExtent()
            list2 = GridGeom.GetEnvelope()
            noc = (list1[1]-list1[0])/(list2[1]-list2[0])
            nor = (list1[3]-list1[2])/(list2[3]-list2[2])
            i=0
            height_list2 = []
            height_list3 = [] 
            height_list1 = [] 
            name_of_file = 'Frontal Area Index 90 DEG'
            completeName = os.path.join(output, name_of_file+".txt") 
            faid90 = open(completeName , "w")
            #sys.stdout = open('running.txt','w')

            for Grid in range(0,length):
                

                BuildingSeq = []
                WindSeq = []
                polyIntersectSeq = []   
                polySeq = []
                GridFeat = GridLayer.GetNextFeature()
                # print "Grid id "
                # print GridFeat.GetField('ID')
                GridGeom = GridFeat.GetGeometryRef()
                # print('The Building intersection and WindLine intersection sequence in the grid ',GridFeat.GetFID(),'is')
                BuildingLayer.SetSpatialFilter(GridGeom)
                WindLayer.SetSpatialFilter(GridGeom)
                GridList= list(GridGeom.GetEnvelope())
    
                lineSpacing = self.reso_val
                
                for line in range(0,WindLayer.GetFeatureCount()):
                     
                    windFeature = WindLayer.GetNextFeature()
                    windGeometry = windFeature.GetGeometryRef()
                    # newGem = windGeometry.Buffer(lineSpacing);
                  
                    # # abc =  newGem.GetEnvelope()
                    # BuildingLayer.SetSpatialFilter(newGem)
                    for poly in range(0,BuildingLayer.GetFeatureCount()):
                        polyFeature = BuildingLayer.GetNextFeature()
                        if not polyFeature:
                            continue
                        polyGeom = polyFeature.GetGeometryRef()
                        Intersect = windGeometry.Intersection(polyGeom)
                        if Intersect.IsEmpty()==False:
                            abc = list(Intersect.GetEnvelope())
                            if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                                height_list1.append(polyFeature.GetField('Height'))
                    BuildingLayer.ResetReading()
                    
                    if height_list1:
                        m = max(height_list1)
                    else:
                        m=0  
                                         
                    height_list2.append(m)
                    del height_list1[:]
                
                for x in range(0,len(height_list2)):
                    if len(height_list3) == 0:
                        FrontalArea = FrontalArea+ lineSpacing*(height_list2[x])
                      

                    else:
                        
                        if (height_list2[x]-height_list3[x])>0:
                            k = height_list2[x]-height_list3[x]
                            
                        else:
                            k=0
                        FrontalArea= FrontalArea+ lineSpacing*(k)
                # print height_list2
                # print height_list3
                FrontalArId= float(FrontalArea)*float(1/area)            
                faid90.write("The Frontal area Index for Grid {0} is {1} \n " .format(GridFeat.GetFID('ID'),FrontalArId))
                frontalAreaList[GridFeat.GetFID()] = FrontalArea
                GridFeat.SetField(name,FrontalArId)
                GridLayer.SetFeature(GridFeat)
                FrontalArea=0
                i+=1 
                if(i>=noc):
                    del height_list3[:]
                    del height_list2[:]
                    i=0
                    
                else:
                    del height_list3[:]
                    height_list3= list(height_list2) 
                    del height_list2[:]
                    
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
            faid90.close()
            print('Frontal Area Index Completed')

        if self.Index_ == 4:
            Driver1 = ogr.GetDriverByName('ESRI Shapefile')
            Grid =str(self.grid_path)
            GridSource = Driver1.Open(Grid,1)
            GridLayer = GridSource.GetLayer()
            Footprint = str(self.footprint_path)
            BuildingSource = Driver1.Open(Footprint,0)
            BuildingLayer = BuildingSource.GetLayer()
            wind = str(self.wind_path)
            output = str(self.output_path)
            WindSource = Driver1.Open(wind,0)
            WindLayer = WindSource.GetLayer()
            layer_defn = GridLayer.GetLayerDefn()
            # new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
            #new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
            # GridLayer.CreateField(new_field)
            #GridLayer.CreateField(new_field)
            text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for frontal area index :')
            if ok:
                name=str(text)
            ldefn = GridLayer.GetLayerDefn()
            sch= []
            check=0
            n=0
            for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
                field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
                sch.append(field) 
            n=0
            for n in range(len(sch)):
               if(name==str(sch[n])):
                   check=1
                   print('Field Already exists')
            if (check==0):
                new_field = ogr.FieldDefn(name, ogr.OFTReal)
                GridLayer.CreateField(new_field)
                print('New Field Created')
            FrontalArea = 0
            GridFrontalArea = []
            length = GridLayer.GetFeatureCount()
            lineSpacing= self.reso_val
            ListTop = []
            ListBottom = []
            ListRight = []
            ListLeft = []
            windLeft = []
            windRight = []
            windBottomLeft = []
            windBottomRight = []

            GridFeat =  GridLayer.GetFeature(0)

            GridGeom = GridFeat.GetGeometryRef()
            list1 = GridLayer.GetExtent()
            list2 = GridGeom.GetEnvelope()
            col = int((list1[1]-list1[0])/(list2[1]-list2[0]))
            row = int((list1[3]-list1[2])/(list2[3]-list2[2]))
            # print "COl"
            # print col
            # print "row"
            # print row
            name_of_file = 'Frontal Area Index 135 DEG'
            completeName = os.path.join(output, name_of_file+".txt") 
            faid135 = open(completeName , "w")
            #sys.stdout = open('running.txt','w')
            k=row
            q=0
            t= (row-1) *col
            listFrontalArea = list([0.0 for x in range(int(col*row))])
            for Grid in range(0,GridLayer.GetFeatureCount()):
                if(t == (k*col) -1):
                    k=k-1
                    t= t- (col+row-1)
                    continue
                if(k == 1):
                    break
                GridFeat1 = GridLayer.GetFeature(t)
                # print("left : ",GridFeat1.GetField('Id'))
                GridGeom1 = GridFeat1.GetGeometryRef()
                GridList= list(GridGeom1.GetEnvelope())
                WindLayer.SetSpatialFilter(GridGeom1)
                BuildingLayer.SetSpatialFilter(GridGeom1)
                
                for wind_line in range(0,WindLayer.GetFeatureCount()):
                    maxx=0
                    feature =  WindLayer.GetNextFeature() 
                    interWind = feature.GetGeometryRef() 
                    windLeft.append(feature.GetFID())
                    for buildings in range(0,BuildingLayer.GetFeatureCount()):
                         currentPolyFeat = BuildingLayer.GetNextFeature()
                         currentPolyGeom = currentPolyFeat.GetGeometryRef()
                         FirstIntersect =interWind.Intersection(currentPolyGeom)
                         if FirstIntersect != None and FirstIntersect.IsEmpty()==False:
                             abc = list(FirstIntersect.GetEnvelope())
                             # print "List is ",abc
                             
                             if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                    
                                        curmaxOfLine = currentPolyFeat.GetField("Height")
                                        # print "cur max ",curmaxOfLine
                                        if(curmaxOfLine >= maxx):
                                              maxx = curmaxOfLine
                    ListLeft.append(maxx)

                    
                    BuildingLayer.ResetReading()
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
                WindLayer.ResetReading()
                BuildingLayer.ResetReading()
                # print ("ListLeft",ListLeft)
                
                    

                GridFeat2 = GridLayer.GetFeature(int(t+1))
                GridGeom2 = GridFeat2.GetGeometryRef()
                GridList= list(GridGeom2.GetEnvelope())
                # print(GridFeat2.GetField('Id'))
                WindLayer.SetSpatialFilter(GridGeom2)
                BuildingLayer.SetSpatialFilter(GridGeom2)
                for wind_line in range(0,WindLayer.GetFeatureCount()):  
                    maxx = 0
                    feature = WindLayer.GetNextFeature() 
                    interWind = feature.GetGeometryRef()                 
                    windRight.append(feature.GetFID())
                    for buildings in range(0,BuildingLayer.GetFeatureCount()):
                         currentPolyFeat = BuildingLayer.GetNextFeature()
                         currentPolyGeom = currentPolyFeat.GetGeometryRef()
                         FirstIntersect =interWind.Intersection(currentPolyGeom)
                         if FirstIntersect != None and FirstIntersect.IsEmpty()==False:
                                 abc = list(FirstIntersect.GetEnvelope())
                                 if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                    
                                        curmaxOfLine = currentPolyFeat.GetField("Height")
                                        # print "cur max ",curmaxOfLine
                                        if(curmaxOfLine >= maxx):
                                              maxx = curmaxOfLine
                    ListRight.append(maxx)
                    BuildingLayer.ResetReading()
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
                WindLayer.ResetReading()
                BuildingLayer.ResetReading()
                


                GridFeat3 = GridLayer.GetFeature(int(t-col))
                GridGeom3 = GridFeat3.GetGeometryRef()
                GridList= list(GridGeom3.GetEnvelope())
                # print(GridFeat3.GetField('Id'))
                WindLayer.SetSpatialFilter(GridGeom3)
                BuildingLayer.SetSpatialFilter(GridGeom3)
                for wind_line in range(0,WindLayer.GetFeatureCount()):
                    maxx = 0
                    feature = WindLayer.GetNextFeature()  
                    interWind = feature.GetGeometryRef()
                    windBottomLeft.append(feature.GetFID())
                  
                    for buildings in range(0,BuildingLayer.GetFeatureCount()):
                         currentPolyFeat = BuildingLayer.GetNextFeature()
                                                   
                         currentPolyGeom = currentPolyFeat.GetGeometryRef()
                         FirstIntersect =interWind.Intersection(currentPolyGeom)
                         if FirstIntersect != None and FirstIntersect.IsEmpty()==False:
                                 abc = list(FirstIntersect.GetEnvelope())
                                 if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                    
                                        curmaxOfLine = currentPolyFeat.GetField("Height")
                                        # print "cur max ",curmaxOfLine
                                        if(curmaxOfLine >= maxx):
                                              maxx = curmaxOfLine
                    ListTop.append(maxx)
                    BuildingLayer.ResetReading()
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
                WindLayer.ResetReading()
                BuildingLayer.ResetReading()
                

                GridFeat4 = GridLayer.GetFeature(int(t-col+1))
                GridGeom4 = GridFeat4.GetGeometryRef()
                GridList= list(GridGeom4.GetEnvelope())  
                # print(GridFeat4.GetField('Id'))        
                WindLayer.SetSpatialFilter(GridGeom4)
                BuildingLayer.SetSpatialFilter(GridGeom4)
                for wind_line in range(0,WindLayer.GetFeatureCount()):
                    maxx = 0
                    feature = WindLayer.GetNextFeature()  
                    interWind = feature.GetGeometryRef()
                    windBottomRight.append(feature.GetFID())
                    for buildings in range(0,BuildingLayer.GetFeatureCount()):
                         currentPolyFeat = BuildingLayer.GetNextFeature()
                         currentPolyGeom = currentPolyFeat.GetGeometryRef()
                         FirstIntersect =interWind.Intersection(currentPolyGeom)
                         if FirstIntersect != None and FirstIntersect.IsEmpty()==False:
                                 abc = list(FirstIntersect.GetEnvelope())
                                 if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                    
                                        curmaxOfLine = currentPolyFeat.GetField("Height")
                                        # print "cur max ",curmaxOfLine
                                        if(curmaxOfLine >= maxx):
                                              maxx = curmaxOfLine
                    ListBottom.append(maxx)
                    BuildingLayer.ResetReading()
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
                WindLayer.ResetReading()
                BuildingLayer.ResetReading()
                
                # print 
                #for GridRight
                for i in range(0,len(windLeft)):
                    for j in range(0,len(windRight)):
                        if windLeft[i]==windRight[j]:
                            if ListLeft[i]<ListRight[j]:
                                ListRight[j]= ListRight[j]-ListLeft[i]
                            else:
                                ListRight[j]=0
                # print ("ListRight",ListRight)
                #GridBottomLeft
                for i in range(0,len(windLeft)):
                    for j in range(0,len(windBottomLeft)):
                        if windLeft[i]==windBottomLeft[j]:
                            if ListTop[j]>ListLeft[i]:
                                ListTop[j]= ListTop[j]-ListLeft[i]
                            else:
                                ListTop[j]=0
                # print ("Listtop",ListTop)
                for i in range(0,len(windRight)):
                    for j in range(0,len(windBottomRight)):
                        if windRight[i]==windBottomRight[j]:
                            if ListBottom[j]>ListRight[i]:
                                ListBottom[j]= ListBottom[j]-ListRight[i]
                            else:
                                ListBottom[j]=0
                

                for i in range(0,len(windBottomLeft)):
                    for j in range(0,len(windBottomRight)):
                        if windBottomLeft[i]==windBottomRight[j]:
                            if ListTop[i]<ListBottom[j]:
                                ListBottom[j]= ListBottom[j]-ListTop[i]
                            else:
                                ListBottom[j]=0
                # print ("ListBottomRight",ListBottom)
                if(listFrontalArea[t] == 0):
                    listFrontalArea[t] = math.fsum(ListLeft)* lineSpacing ;
                if(listFrontalArea[t+1] == 0):
                    listFrontalArea[t+1] = math.fsum(ListRight)* lineSpacing ;
                if(listFrontalArea[t-col] == 0):
                    listFrontalArea[t-col] = sum(ListTop)* lineSpacing ;
                if(listFrontalArea[t-col+1] == 0):
                    listFrontalArea[t-col+1] = sum(ListBottom)* lineSpacing ;

                t=t+1
                
                del windLeft[:]
                del windRight[:]
                del windBottomRight[:]
                del windBottomLeft[:]


                del ListLeft[:]  
                del ListRight[:]
                del ListTop[:]
                del ListBottom[:]
            for i in range(0,len(listFrontalArea)):
                FrontalArId= float(listFrontalArea[i])*float(1/area)            
                faid135.write("The Frontal area Index for Grid {0} is {1} \n " .format(GridFeat.GetFID(),FrontalArId))
                Grid_feature = GridLayer.GetFeature(i)
                Grid_feature.SetField(name,FrontalArId)
                GridLayer.SetFeature(Grid_feature)
            
            faid135.close()
            print('Frontal Area Index Completed')

            # print "Answer List is"
            # print listFrontalArea
            #print "The total frontal area is", sum(listFrontalArea)
            # for gridFrontal in range(0,len(listFrontalArea)):

        if self.Index_ == 5:
            Driver1 = ogr.GetDriverByName('ESRI Shapefile')
            Grid =str(self.grid_path)
            # print(Grid)
            GridSource = Driver1.Open(Grid,1)
            GridLayer = GridSource.GetLayer()
            length = GridLayer.GetFeatureCount()
            frontalAreaList = list([0.0 for x in range(length)])
            Footprint = str(self.footprint_path)
            BuildingSource = Driver1.Open(Footprint,0)
            BuildingLayer = BuildingSource.GetLayer()
            wind = str(self.wind_path)
            output = str(self.output_path)
            WindSource = Driver1.Open(wind,0)
            WindLayer = WindSource.GetLayer()
            layer_defn = GridLayer.GetLayerDefn()
            # new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
            #new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
            # GridLayer.CreateField(new_field)
            #GridLayer.CreateField(new_field)
            text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for frontal area index :')
            if ok:
                name=str(text)
            ldefn = GridLayer.GetLayerDefn()
            sch= []
            check=0
            n=0
            for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
                field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
                sch.append(field) 
            n=0
            for n in range(len(sch)):
               if(name==str(sch[n])):
                   check=1
                   print('Field Already exists')
            if (check==0):
                new_field = ogr.FieldDefn(name, ogr.OFTReal)
                GridLayer.CreateField(new_field)
                print('New Field Created')
            FrontalArea = 0
            GridFrontalArea = []
            length = GridLayer.GetFeatureCount()
            GridFeat = GridLayer.GetFeature(0)
            GridGeom = GridFeat.GetGeometryRef()
            list1 = GridLayer.GetExtent()
            list2 = GridGeom.GetEnvelope()
            noc = (list1[1]-list1[0])/(list2[1]-list2[0])
            nor = (list1[3]-list1[2])/(list2[3]-list2[2])
            i=0
            f=0
            l=1
            k= (nor) * noc 
            height_list2 = []
            height_list3 = [] 
            height_list1 = [] 
            #sys.stdout = open('running.txt','w')
            name_of_file = 'Frontal Area Index 180 DEG'
            completeName = os.path.join(output, name_of_file+".txt") 
            faid180 = open(completeName , "w")

            for Grid in range(0,length):
                

                BuildingSeq = []
                WindSeq = []
                polyIntersectSeq = []   
                polySeq = []
                
                if f<=nor-1:
                    k=k-noc
                    
               
                GridFeat = GridLayer.GetFeature(int(abs(k)))
               
                GridGeom = GridFeat.GetGeometryRef()
                GridList = list(GridGeom.GetEnvelope())
                BuildingLayer.SetSpatialFilter(GridGeom)
                WindLayer.SetSpatialFilter(GridGeom)

    
                lineSpacing = self.reso_val
                
                for line in range(0,WindLayer.GetFeatureCount()):
                     
                    windFeature = WindLayer.GetNextFeature()
                    windGeometry = windFeature.GetGeometryRef()
                    
                    
                    for poly in range(0,BuildingLayer.GetFeatureCount()):
                        polyFeature = BuildingLayer.GetNextFeature()
                        if not polyFeature:
                            continue
                        polyGeom = polyFeature.GetGeometryRef()
                        Intersect = windGeometry.Intersection(polyGeom)
                        if Intersect.IsEmpty()==False:
                            abc = list(Intersect.GetEnvelope())
                            # print abc
                            # print "Entering intersect"
                            if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                            
                                height_list1.append(polyFeature.GetField('height'))
                       
                    BuildingLayer.ResetReading()
                    if height_list1:
                        m = max(height_list1)
                    else:
                        m=0  
                                 
                    height_list2.append(m)
                    del height_list1[:]
                
                for x in range(0,len(height_list2)):
                    if len(height_list3) == 0:
                        FrontalArea = FrontalArea+ lineSpacing*(height_list2[x])
                       

                    else:
                    
                        if (height_list2[x]-height_list3[x])>0:
                            j = height_list2[x]-height_list3[x]
                          
                        else:
                            j=0
                        FrontalArea= FrontalArea+ lineSpacing*(j)
                # print "H2 is "
                # print height_list2
                # print "h3 is "
                # print height_list3
                FrontalArId= float(FrontalArea)*float(1/area)            
                faid180.write("The Frontal area Index for Grid {0} is {1} \n " .format(GridFeat.GetFID(),FrontalArId))
                frontalAreaList[GridFeat.GetFID()] = FrontalArea
                GridFeat.SetField(name,FrontalArId)
                GridLayer.SetFeature(GridFeat)
                # print
                print
                FrontalArea=0
                
                f+=1
                if(f > nor-1):
                    del height_list3[:]
                    del height_list2[:]
                    f=1
                    k=nor*noc -noc +l
                    l=l+1
                  
                else:
                    del height_list3[:]
                    height_list3= list(height_list2) 
                    del height_list2[:]
                   
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
            faid180.close()
            print('Frontal Area Index Completed')

                

        if self.Index_ == 6:
            Driver1 = ogr.GetDriverByName('ESRI Shapefile')
            Grid =str(self.grid_path)
            GridSource = Driver1.Open(Grid,1)
            GridLayer = GridSource.GetLayer()
            Footprint = str(self.footprint_path)
            BuildingSource = Driver1.Open(Footprint,0)
            BuildingLayer = BuildingSource.GetLayer()
            wind = str(self.wind_path)
            output = str(self.output_path)
            WindSource = Driver1.Open(wind,0)
            WindLayer = WindSource.GetLayer()
            layer_defn = GridLayer.GetLayerDefn()
            # new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
            #src = 'GridFA '+str(self.Wind_select.currentText())
            #new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
            #GridLayer.CreateField(new_field)
            text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for frontal area index :')
            if ok:
                name=str(text)
            ldefn = GridLayer.GetLayerDefn()
            sch= []
            check=0
            n=0
            for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
                field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
                sch.append(field) 
            n=0
            for n in range(len(sch)):
               if(name==str(sch[n])):
                   check=1
                   print('Field Already exists')
            if (check==0):
                new_field = ogr.FieldDefn(name, ogr.OFTReal)
                GridLayer.CreateField(new_field)
                print('New Field Created')
            FrontalArea = 0
            GridFrontalArea = []
            length = GridLayer.GetFeatureCount()
            lineSpacing= self.reso_val
            ListTop = []
            ListBottom = []
            ListRight = []
            ListLeft = []
            windLeft = []
            windRight = []
            windBottomLeft = []
            windBottomRight = []

            GridFeat =  GridLayer.GetFeature(0)

            GridGeom = GridFeat.GetGeometryRef()
            list1 = GridLayer.GetExtent()
            list2 = GridGeom.GetEnvelope()
            col = int((list1[1]-list1[0])/(list2[1]-list2[0]))
            row = int((list1[3]-list1[2])/(list2[3]-list2[2]))
            # print "COl"
            # print col
            # print "row"
            # print row
            name_of_file = 'Frontal Area Index 2255 DEG'
            completeName = os.path.join(output, name_of_file+".txt") 
            faid225 = open(completeName , "w")
            #sys.stdout = open('running.txt','w')
            k=row
            q=0
            t= (row *col)-1
            listFrontalArea = list([0.0 for x in range(int(col*row))])
            for Grid in range(0,GridLayer.GetFeatureCount()):
                if(t == (k*col) -col):
                    k=k-1
                    t= t-1
                    continue
                if(k == 1):
                    break
                GridFeat1 = GridLayer.GetFeature(t)
                GridGeom1 = GridFeat1.GetGeometryRef()
                GridList= list(GridGeom1.GetEnvelope())
                WindLayer.SetSpatialFilter(GridGeom1)
                BuildingLayer.SetSpatialFilter(GridGeom1)
                # print "Grid is ", GridFeat1.GetFID()
                for wind_line in range(0,WindLayer.GetFeatureCount()):
                    maxx=0
                    feature =  WindLayer.GetNextFeature() 
                    interWind = feature.GetGeometryRef() 
                    windLeft.append(feature.GetFID())
                    for buildings in range(0,BuildingLayer.GetFeatureCount()):
                         currentPolyFeat = BuildingLayer.GetNextFeature()
                         currentPolyGeom = currentPolyFeat.GetGeometryRef()
                    #      FirstIntersect = interWind.Intersection(currentPolyGeom)
                    #      if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                    #            curmaxOfLine = currentPolyFeat.GetField("Height")
                    #            if(curmaxOfLine > maxx):
                    #                 maxx = curmaxOfLine
                    # ListLeft.append(maxx)
                         FirstIntersect =interWind.Intersection(currentPolyGeom)
                         if FirstIntersect != None and FirstIntersect.IsEmpty()==False:
                                abc = list(FirstIntersect.GetEnvelope())
                                # print "List is ", abc
                                if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[3]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[2]<GridList[3] )):
                                     
                                  # if ( (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                        curmaxOfLine = currentPolyFeat.GetField("Height")
                                        # print "cur max ",curmaxOfLine
                                        if(curmaxOfLine >= maxx):
                                              maxx = curmaxOfLine
                    ListLeft.append(maxx)
                    BuildingLayer.ResetReading()
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
                WindLayer.ResetReading()
                BuildingLayer.ResetReading()
                # print ("ListLeft",ListLeft)
                
                    

                GridFeat2 = GridLayer.GetFeature(int(t-1))
                GridGeom2 = GridFeat2.GetGeometryRef()
                GridList= list(GridGeom2.GetEnvelope())
                WindLayer.SetSpatialFilter(GridGeom2)
                BuildingLayer.SetSpatialFilter(GridGeom2)
                for wind_line in range(0,WindLayer.GetFeatureCount()):  
                    maxx = 0
                    feature = WindLayer.GetNextFeature() 
                    interWind = feature.GetGeometryRef()                 
                    windRight.append(feature.GetFID())
                    for buildings in range(0,BuildingLayer.GetFeatureCount()):
                         currentPolyFeat = BuildingLayer.GetNextFeature()
                         currentPolyGeom = currentPolyFeat.GetGeometryRef()
                         FirstIntersect = interWind.Intersection(currentPolyGeom)
                         if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                                abc = list(FirstIntersect.GetEnvelope())
                                if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[3]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[2]<GridList[3] )):
                                     
                                  # if ( (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                        curmaxOfLine = currentPolyFeat.GetField("Height")
                                        # print "cur max ",curmaxOfLine
                                        if(curmaxOfLine >= maxx):
                                              maxx = curmaxOfLine
                    ListRight.append(maxx)
                    BuildingLayer.ResetReading()
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
                WindLayer.ResetReading()
                BuildingLayer.ResetReading()
                # print ("ListRight",ListRight)


                GridFeat3 = GridLayer.GetFeature(int(t-col))
                GridGeom3 = GridFeat3.GetGeometryRef()
                GridList= list(GridGeom3.GetEnvelope())
                WindLayer.SetSpatialFilter(GridGeom3)
                BuildingLayer.SetSpatialFilter(GridGeom3)
                for wind_line in range(0,WindLayer.GetFeatureCount()):
                    maxx = 0
                    feature = WindLayer.GetNextFeature()  
                    interWind = feature.GetGeometryRef()
                    windBottomLeft.append(feature.GetFID())
                  
                    for buildings in range(0,BuildingLayer.GetFeatureCount()):
                         currentPolyFeat = BuildingLayer.GetNextFeature()
                                                   
                         currentPolyGeom = currentPolyFeat.GetGeometryRef()
                         FirstIntersect = interWind.Intersection(currentPolyGeom)
                         if FirstIntersect != None and FirstIntersect.IsEmpty() == False:

                                abc = list(FirstIntersect.GetEnvelope())
                                if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[3]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[2]<GridList[3] )):
                                      
                                  # if ( (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                        curmaxOfLine = currentPolyFeat.GetField("Height")
                                        # print "cur max ",curmaxOfLine
                                        if(curmaxOfLine >= maxx):
                                              maxx = curmaxOfLine
                    ListTop.append(maxx)
                    BuildingLayer.ResetReading()
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
                WindLayer.ResetReading()
                BuildingLayer.ResetReading()
                # print ("ListBottomLeft",ListTop)

                GridFeat4 = GridLayer.GetFeature(int(t-col-1))
                GridGeom4 = GridFeat4.GetGeometryRef() 
                GridList= list(GridGeom4.GetEnvelope())         
                WindLayer.SetSpatialFilter(GridGeom4)
                BuildingLayer.SetSpatialFilter(GridGeom4)
                for wind_line in range(0,WindLayer.GetFeatureCount()):
                    maxx = 0
                    feature = WindLayer.GetNextFeature()  
                    interWind = feature.GetGeometryRef()
                    windBottomRight.append(feature.GetFID())
                    for buildings in range(0,BuildingLayer.GetFeatureCount()):
                         currentPolyFeat = BuildingLayer.GetNextFeature()
                         currentPolyGeom = currentPolyFeat.GetGeometryRef()
                         FirstIntersect = interWind.Intersection(currentPolyGeom)
                         if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                                abc = list(FirstIntersect.GetEnvelope())
                                if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[3]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[2]<GridList[3] )):
                                      
                                  # if ( (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                        curmaxOfLine = currentPolyFeat.GetField("Height")
                                        # print "cur max ",curmaxOfLine
                                        if(curmaxOfLine >= maxx):
                                              maxx = curmaxOfLine
                    ListBottom.append(maxx)
                    BuildingLayer.ResetReading()
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
                WindLayer.ResetReading()
                BuildingLayer.ResetReading()
                # print ("ListBottomRight",ListBottom)

                #for GridRight
                for i in range(0,len(windLeft)):
                    for j in range(0,len(windRight)):
                        if windLeft[i]==windRight[j]:
                            if ListLeft[i]<ListRight[j]:
                                ListRight[j]= ListRight[j]-ListLeft[i]
                            else:
                                ListRight[j]=0
                # print ("ListRight",ListRight)
                #GridBottomLeft
                for i in range(0,len(windLeft)):
                    for j in range(0,len(windBottomLeft)):
                        if windLeft[i]==windBottomLeft[j]:
                            if ListTop[j]>ListLeft[i]:
                                ListTop[j]= ListTop[j]-ListLeft[i]
                            else:
                                ListTop[j]=0
                # print ("ListBottomLeft",ListTop)
                #GridBottomRight
                for i in range(0,len(windRight)):
                    for j in range(0,len(windBottomRight)):
                        if windRight[i]==windBottomRight[j]:
                            if ListBottom[j]>ListRight[i]:
                                ListBottom[j]= ListBottom[j]-ListRight[i]
                            else:
                                ListBottom[j]=0
                # print ("ListBottomRight",ListBottom)


                for i in range(0,len(windBottomLeft)):
                    for j in range(0,len(windBottomRight)):
                        if windBottomLeft[i]==windBottomRight[j]:
                            if ListTop[i]<ListBottom[j]:
                                ListBottom[j]= ListBottom[j]-ListTop[i]
                            else:
                                ListBottom[j]=0
                # print ("ListBottomRight",ListBottom)
                
                if(listFrontalArea[t] == 0):
                    listFrontalArea[t] = sum(ListLeft)* lineSpacing ;
                if(listFrontalArea[t-1] == 0):
                    listFrontalArea[t-1] = sum(ListRight)* lineSpacing ;
                if(listFrontalArea[t-col] == 0):
                    listFrontalArea[t-col] = sum(ListTop)* lineSpacing ;
                if(listFrontalArea[t-col-1] == 0):
                    listFrontalArea[t-col-1] = sum(ListBottom)* lineSpacing ;

                t=t-1
                
                del windLeft[:]
                del windRight[:]
                del windBottomRight[:]
                del windBottomLeft[:]


                del ListLeft[:]
                del ListRight[:]
                del ListTop[:]
                del ListBottom[:]
            for i in range(0,len(listFrontalArea)):
                FrontalArId= float(listFrontalArea[i])*float(1/area)            
                faid225.write("The Frontal area Index for Grid {0} is {1} \n " .format(GridFeat.GetFID(),FrontalArId))
                Grid_feature = GridLayer.GetFeature(i)
                Grid_feature.SetField(name,FrontalArId)
                GridLayer.SetFeature(Grid_feature)

            
            #print "The total frontal area is", sum(listFrontalArea)
            # for gridFrontal in range(0,len(listFrontalArea)):
            #     Grid_feature = GridLayer.GetFeature(gridFrontal)
            #     Grid_feature.SetField('GridFA',listFrontalArea[gridFrontal])
            #     GridLayer.SetFeature(Grid_feature)
            faid225.close()
            print('Frontal Area Index Completed')

        if self.Index_ == 7:
            Driver1 = ogr.GetDriverByName('ESRI Shapefile')
            Grid =str(self.grid_path)
            # print(Grid)
            GridSource = Driver1.Open(Grid,1)
            GridLayer = GridSource.GetLayer()
            length = GridLayer.GetFeatureCount()
            frontalAreaList = list([0.0 for x in range(length)])
            Footprint = str(self.footprint_path)
            BuildingSource = Driver1.Open(Footprint,0)
            BuildingLayer = BuildingSource.GetLayer()
            wind = str(self.wind_path)
            WindSource = Driver1.Open(wind,0)
            WindLayer = WindSource.GetLayer()
            layer_defn = GridLayer.GetLayerDefn()
            # new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
            #new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
            #GridLayer.CreateField(new_field)
            output = str(self.output_path)
            text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for frontal area index :')
            if ok:
                name=str(text)
            ldefn = GridLayer.GetLayerDefn()
            sch= []
            check=0
            n=0
            for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
                field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
                sch.append(field) 
            n=0
            for n in range(len(sch)):
               if(name==str(sch[n])):
                   check=1
                   print('Field Already exists')
            if (check==0):
                new_field = ogr.FieldDefn(name, ogr.OFTReal)
                GridLayer.CreateField(new_field)
                print('New Field Created')
            name_of_file = 'Frontal Area Index 270 DEG'
            completeName = os.path.join(output, name_of_file+".txt") 
            faid270 = open(completeName , "w")
            
            FrontalArea = 0
            GridFrontalArea = []
            length = GridLayer.GetFeatureCount()
            GridFeat = GridLayer.GetFeature(0)
            GridGeom = GridFeat.GetGeometryRef()
            list1 = GridLayer.GetExtent()
            list2 = GridGeom.GetEnvelope()
            noc = (list1[1]-list1[0])/(list2[1]-list2[0])
            nor = (list1[3]-list1[2])/(list2[3]-list2[2])
            i=0
            f=0
            z=2
            k=noc
            height_list2 = []
            height_list3 = [] 
            height_list1 = [] 
            #sys.stdout = open('running.txt','w')

            for Grid in range(0,length):
                

                BuildingSeq = []
                WindSeq = []
                polyIntersectSeq = []   
                polySeq = []
                if f<=noc-1:
                    k=k-1
                    
                else:
                    k=(noc*z)-1
                    z=z+1
                    f=0
                
                GridFeat = GridLayer.GetFeature(int(abs(k)))
                
                GridGeom = GridFeat.GetGeometryRef()
                # print('The Building intersection and WindLine intersection sequence in the grid ',GridFeat.GetFID(),'is')
                BuildingLayer.SetSpatialFilter(GridGeom)
                WindLayer.SetSpatialFilter(GridGeom)
                GridList= list(GridGeom.GetEnvelope())                        
                lineSpacing = self.reso_val
                
                for line in range(0,WindLayer.GetFeatureCount()):
                     
                    windFeature = WindLayer.GetNextFeature()
                    windGeometry = windFeature.GetGeometryRef()
                   
                    
                    for poly in range(0,BuildingLayer.GetFeatureCount()):
                        polyFeature = BuildingLayer.GetNextFeature()
                        if not polyFeature:
                            continue
                        polyGeom = polyFeature.GetGeometryRef()
                        Intersect = windGeometry.Intersection(polyGeom)
                        if Intersect.IsEmpty()==False:
                            abc = list(Intersect.GetEnvelope())
                            if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                                height_list1.append(polyFeature.GetField('height'))
                        
                    BuildingLayer.ResetReading()
                    if height_list1:
                        m = max(height_list1)
                    else:
                        m=0  
                                  
                    height_list2.append(m)
                    del height_list1[:]
                
                for x in range(0,len(height_list2)):
                    if len(height_list3) == 0:
                        FrontalArea = FrontalArea+ lineSpacing*(height_list2[x])
                       

                    else:
                    
                        if (height_list2[x]-height_list3[x])>0:
                            j = height_list2[x]-height_list3[x]
                         
                        else:
                            j=0
                        FrontalArea= FrontalArea+ lineSpacing*(j)
                # print "H2 is "
                # print height_list2
                # print "h3 is "
                # print height_list3
                FrontalArId= float(FrontalArea)*float(1/area)            
                faid270.write("The Frontal area Index for Grid {0} is {1} \n " .format(GridFeat.GetFID(),FrontalArId))
                frontalAreaList[GridFeat.GetFID()] = FrontalArea
                GridFeat.SetField(name,FrontalArId)
                GridLayer.SetFeature(GridFeat)
                # print
                FrontalArea=0
                i=i+1 
                f+=1
                if(i>=noc):
                    del height_list3[:]
                    del height_list2[:]
                    i=0
                    
                else:
                    del height_list3[:]
                    height_list3= list(height_list2) 
                    del height_list2[:]
                  
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
            faid270.close()
            print('Frontal Area Index Completed')

        if self.Index_ == 8:
            Driver1 = ogr.GetDriverByName('ESRI Shapefile')
            Grid =str(self.grid_path)
            GridSource = Driver1.Open(Grid,1)
            GridLayer = GridSource.GetLayer()
            length = GridLayer.GetFeatureCount()
            frontalAreaList = list([0.0 for x in range(length)])
            Footprint = str(self.footprint_path)
            BuildingSource = Driver1.Open(Footprint,0)
            BuildingLayer = BuildingSource.GetLayer()
            wind = str(self.wind_path)
            WindSource = Driver1.Open(wind,0)
            WindLayer = WindSource.GetLayer()
            layer_defn = GridLayer.GetLayerDefn()
            output = str(self.output_path)
            text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for frontal area index :')
            if ok:
                name=str(text)
            ldefn = GridLayer.GetLayerDefn()
            sch= []
            check=0
            n=0
            for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
                field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
                sch.append(field) 
            n=0
            for n in range(len(sch)):
               if(name==str(sch[n])):
                   check=1
                   print('Field Already exists')
            if (check==0):
                new_field = ogr.FieldDefn(name, ogr.OFTReal)
                GridLayer.CreateField(new_field)
                print('New Field Created')
            name_of_file = 'Frontal Area Index 315 DEG'
            completeName = os.path.join(output, name_of_file+".txt") 
            faid315 = open(completeName , "w")
            FrontalArea = 0
            GridFrontalArea = []
            length = GridLayer.GetFeatureCount()
            GridFeat = GridLayer.GetFeature(0)
            GridGeom = GridFeat.GetGeometryRef()
            list1 = GridLayer.GetExtent()
            list2 = GridGeom.GetEnvelope()
            noc = (list1[1]-list1[0])/(list2[1]-list2[0])
            nor = (list1[3]-list1[2])/(list2[3]-list2[2])
            i=0
            f=0
            l=0
            k= -noc
            height_list2 = []
            height_list3 = [] 
            height_list1 = []
            area=0
            for Grid in range(0,length):
                

                BuildingSeq = []
                WindSeq = []
                polyIntersectSeq = []   
                polySeq = []
                if f<=nor-1:
                    k=k+noc
                    f=f+1
                    
                else:
                    k=l+1
                    f= 1
                    l=l+1
                                 
                GridFeat = GridLayer.GetFeature(int(abs(k)))
               
                GridGeom = GridFeat.GetGeometryRef()
                area=GridGeom.GetArea()
                BuildingLayer.SetSpatialFilter(GridGeom)
                WindLayer.SetSpatialFilter(GridGeom)

                GridList= list(GridGeom.GetEnvelope())
                # print GridList
                lineSpacing = self.reso_val
                
                for line in range(0,WindLayer.GetFeatureCount()):
                     
                    windFeature = WindLayer.GetNextFeature()
                    windGeometry = windFeature.GetGeometryRef()
                   
                    
                    for poly in range(0,BuildingLayer.GetFeatureCount()):
                        polyFeature = BuildingLayer.GetNextFeature()
                        if not polyFeature:
                            continue
                        polyGeom = polyFeature.GetGeometryRef()
                        Intersect = windGeometry.Intersection(polyGeom)
                        
                        if Intersect.IsEmpty()==False:
                            abc = list(Intersect.GetEnvelope())
                            # print abc
                            # print "Entering intersect"
                            if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                            # polyIntersectSeq.append(Intersect.GetPoints())
                            # polySeq.append(polyFeature.GetFID())
                                height_list1.append(polyFeature.GetField('height'))
                                # print "Entering GridCompare"
                        # else:
                        #     o=0
                        #     height_list1.append(o)
                    BuildingLayer.ResetReading()
                    if height_list1:
                        m = max(height_list1)
                    else:
                        m=0  
                    #print m 
                    #print "H1 is "
                    #print height_list1   
                    #print                 
                    height_list2.append(m)
                    del height_list1[:]
                    #print ("Height_list2 earlier",height_list2)
                for x in range(0,len(height_list2)):
                    if len(height_list3) == 0:
                        FrontalArea = FrontalArea+ lineSpacing*(height_list2[x])
                        # print 'hello : Length '
                        # p print "len"rint len(height_list3)

                    else:
                    
                        if (height_list2[x]-height_list3[x])>0:
                            j = height_list2[x]-height_list3[x]
                            # print"@@@@@@@"
                            FrontalArea= FrontalArea+ lineSpacing*(j)
                            # print k
                        else:
                            j=0
                            FrontalArea= FrontalArea+ lineSpacing*(j)
                #print "H2 is "
                #print height_list2
                #print "h3 is "
                #print height_list3
                FrontalArId= float(FrontalArea)*float(1/area)            
                faid315.write("The Frontal area Index for Grid {0} is {1} \n " .format(GridFeat.GetFID(),FrontalArId))
                frontalAreaList[GridFeat.GetFID()] = FrontalArea
                GridFeat.SetField(name,FrontalArId)
                GridLayer.SetFeature(GridFeat)
                FrontalArea=0
                i=i+1 
                
                if(i>=nor):
                    del height_list3[:]
                    del height_list2[:]
                    i=0
                   
                else:
                    del height_list3[:]
                    height_list3= list(height_list2) 
                    del height_list2[:]
                    
                BuildingLayer.SetSpatialFilter(None)
                WindLayer.SetSpatialFilter(None)
            faid315.close()
            print('Frontal Area Index Completed')    

class Ui_Dialog_AboutWRF(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 495)
        Dialog.setStyleSheet(_fromUtf8("QDialog{\n"
"color:navy; background-color: white;\n"
"\n"
"                     \n"
"}\n"
"QLabel{\n"
"color: navy; \n"
"                        \n"
"                        selection-color: yellow;\n"
"                        selection-background-color: blue;\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
" border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
""))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 10, 551, 131))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "About WRF-UME ", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline; color:#5500ff;\">ABOUT WRF-UME</span></p><p align=\"center\"><span style=\" font-size:11pt; font-style:italic; color:#00aaff;\">This toolkit is helpfull for calculation of various WRF-UME parameters</span></p><p align=\"center\"><span style=\" font-size:11pt; font-style:italic; color:#00aaff;\">of different buildings as well as in grid form.</span></p></body></html>", None))

class Ui_Dialog_Needhelp(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 480)
        Dialog.setStyleSheet(_fromUtf8("QDialog{\n"
"color:navy; background-color: white;\n"
"\n"
"                     \n"
"}\n"
"QLabel{\n"
"color: navy; \n"
"                        \n"
"                        selection-color: yellow;\n"
"                        selection-background-color: blue;\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
" border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
""))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 30, 491, 81))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "UME-WRF Help", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#5500ff;\">!!!HELP!!!</span></p><p align=\"center\"><span style=\" font-size:10pt; font-style:italic; color:#00aaff;\"></span></p></body></html>", None))

class Ui_Dialog_ELEV(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(648, 330)
        Dialog.setStyleSheet(_fromUtf8("QDialog{\n"
"color:navy; background-color: white;\n"
"\n"
"                     \n"
"}\n"
"QLabel{\n"
"color: navy; \n"
"                        \n"
"                        selection-color: yellow;\n"
"                        selection-background-color: blue;\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
" border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
""))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 40, 46, 13))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 10, 441, 61))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Browse2 = QtGui.QPushButton(Dialog)
        self.Browse2.setGeometry(QtCore.QRect(530, 140, 84, 23))
        self.Browse2.setObjectName(_fromUtf8("Browse2"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 140, 291, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 110, 171, 71))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.Browse3 = QtGui.QPushButton(Dialog)
        self.Browse3.setGeometry(QtCore.QRect(530, 190, 84, 23))
        self.Browse3.setObjectName(_fromUtf8("Browse3"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 190, 291, 21))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 160, 171, 71))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(210, 90, 291, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 191, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Browse1 = QtGui.QPushButton(Dialog)
        self.Browse1.setGeometry(QtCore.QRect(530, 90, 84, 23))
        self.Browse1.setObjectName(_fromUtf8("Browse1"))
        self.height = QtGui.QPushButton(Dialog)
        self.height.setGeometry(QtCore.QRect(320, 280, 84, 23))
        self.height.setObjectName(_fromUtf8("height"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.Browse2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.DTM_browse)
        QtCore.QObject.connect(self.Browse3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.nDSM_browse)
        QtCore.QObject.connect(self.Browse1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.footprint_browse)
        QtCore.QObject.connect(self.height, QtCore.SIGNAL(_fromUtf8("clicked()")), self.myfunc_ELEV)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Wind Line Creator", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Building\'s Elevation</span></p></body></html>", None))
        self.Browse2.setToolTip(_translate("Dialog", "<html><head/><body><p>Choose shape file for DTM file </p></body></html>", None))
        self.Browse2.setText(_translate("Dialog", "Browse", None))
        self.label_7.setText(_translate("Dialog", "Select the DTM file..", None))
        self.Browse3.setToolTip(_translate("Dialog", "<html><head/><body><p>Choose shape file for nDSM file</p></body></html>", None))
        self.Browse3.setText(_translate("Dialog", "Browse", None))
        self.label_8.setText(_translate("Dialog", "Select the nDSM file..", None))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p>Select the building\'s shape-file location:</p><p><br/></p></body></html>", None))
        self.Browse1.setToolTip(_translate("Dialog", "<html><head/><body><p>Choose shape file to generate the Output wind direction</p></body></html>", None))
        self.Browse1.setText(_translate("Dialog", "Browse", None))
        self.height.setToolTip(_translate("Dialog", "<html><head/><body><p>Select elevation</p></body></html>", None))
        self.height.setText(_translate("Dialog", "Add Height", None))

    def footprint_browse(self):
        print ('selecting folder containing building footprint')
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home',filter= '*.shp')
        self.footprint_path = self.fname.replace('\\','/')
        self.loc_1.setText(self.fname)
        print(self.footprint_path)

    def DTM_browse(self):
        print ('selecting folder containing DTM file')
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home',filter= '*.img')
        self.DTM_path = self.fname.replace('\\','/')
        self.loc_5.setText(self.fname)
        print(self.DTM_path)

    def nDSM_browse(self):
        print ('selecting folder containing nDSM file')
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home',filter= '*.img')
        self.nDSM_path = self.fname.replace('\\','/')
        self.loc_6.setText(self.fname)
        print(self.nDSM_path)

    def myfunc_ELEV(self):
        self.DTM_path = str(self.DTM_path)
        self.dtm_gdata = gdal.Open(self.DTM_path)
        self.dtm_rows = self.dtm_gdata.RasterYSize
        self.dtm_cols = self.dtm_gdata.RasterXSize
        self.dtm_band = self.dtm_gdata.GetRasterBand(1)
        self.dtm_data = self.dtm_band.ReadAsArray(0, 0, self.dtm_cols, self.dtm_rows)
        print self.dtm_data
        self.nDSM_path = str(self.nDSM_path)
        self.ndsm_gdata = gdal.Open(self.nDSM_path)
        self.ndsm_rows = self.ndsm_gdata.RasterYSize
        self.ndsm_cols = self.ndsm_gdata.RasterXSize
        self.ndsm_band = self.ndsm_gdata.GetRasterBand(1)
        self.ndsm_data = self.ndsm_band.ReadAsArray(0, 0,self.ndsm_cols,self.ndsm_rows)
        print self.ndsm_data
        def get_value_at_point_dtm(pos):
            gt = self.dtm_gdata.GetGeoTransform()
            #get image size
            x = int((pos[0] - gt[0])/gt[1])
            y = int((pos[1] - gt[3])/gt[5])

            #data = band.ReadAsArray(x, y, 1, 1)
            value = self.dtm_data[y-1,x-1]
         
            return float(value)
        def get_value_at_point_ndsm(pos):
            gt = self.ndsm_gdata.GetGeoTransform()
            #get image size
            x = int((pos[0] - gt[0])/gt[1])
            y = int((pos[1] - gt[3])/gt[5])

            #data = band.ReadAsArray(x, y, 1, 1)
            value = self.ndsm_data[y-1,x-1]
            
            return float(value)

        # loop through the features in the layer
        self.driver = ogr.GetDriverByName('ESRI Shapefile')
        self.Footprint = str(self.footprint_path)
        self.footprintSource = self.driver.Open(self.Footprint,1)
        self.footprintLayer = self.footprintSource.GetLayer()



        # add field to the footprint shapefile
        new_field1 = ogr.FieldDefn('buildh', ogr.OFTReal) #ogr.OFTReal
        self.footprintLayer.CreateField(new_field1)
        new_field2 = ogr.FieldDefn('elevation',ogr.OFTReal)
        self.footprintLayer.CreateField(new_field2)
        new_field3 = ogr.FieldDefn('Height',ogr.OFTReal)
        self.footprintLayer.CreateField(new_field3)

        builfeature = self.footprintLayer.GetNextFeature()
        while builfeature:
           polyGeo = builfeature.GetGeometryRef()
           #feature= ogr.Feature(self.footprintLayer.GetLayerDefn())
           geomt = builfeature.GetGeometryRef()
           centroid=geomt.Centroid()
           #print 'centroid.GetX()' + str(centroid.GetX())
           #print 'centroid.GetY()' + str(centroid.GetY())
           poslst = []
           poslst = [centroid.GetX(),centroid.GetY()]
           ele = get_value_at_point_dtm(poslst)
           #print "ele:" + str(ele)
           build_hei = get_value_at_point_ndsm(poslst)
           #print "build_hei:" + str(build_hei)
           hei = ele + build_hei
           #hei = build_hei
           builfeature.SetField("elevation",ele)
           builfeature.SetField("buildh",build_hei)
           builfeature.SetField("Height",hei)
           #print 'build_height and elevation added'
           self.footprintLayer.SetFeature(builfeature)
           builfeature.Destroy()
           builfeature =self.footprintLayer.GetNextFeature()
        print 'build_height and elevation added'

class Ui_Dialog_WGL(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(657, 383)
        Dialog.setStyleSheet(_fromUtf8("QDialog{\n"
"color:navy; background-color: white;\n"
"\n"
"                     \n"
"}\n"
"QLabel{\n"
"color: navy; \n"
"                        \n"
"                        selection-color: yellow;\n"
"                        selection-background-color: blue;\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
" border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
""))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 40, 46, 13))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 10, 441, 61))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(200, 250, 161, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.create = QtGui.QPushButton(Dialog)
        self.create.setGeometry(QtCore.QRect(290, 310, 121, 31))
        self.create.setObjectName(_fromUtf8("create"))
        self.Resolution = QtGui.QSpinBox(Dialog)
        self.Resolution.setGeometry(QtCore.QRect(380, 250, 42, 22))
        self.Resolution.setMaximum(20)
        self.Resolution.setObjectName(_fromUtf8("Resolution"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 326, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Wind_Select = QtGui.QComboBox(Dialog)
        self.Wind_Select.setGeometry(QtCore.QRect(340, 210, 281, 20))
        self.Wind_Select.setObjectName(_fromUtf8("Wind_Select"))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Browse1 = QtGui.QPushButton(Dialog)
        self.Browse1.setGeometry(QtCore.QRect(530, 110, 84, 23))
        self.Browse1.setObjectName(_fromUtf8("Browse1"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 110, 291, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 181, 71))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(210, 160, 291, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 191, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Browse2 = QtGui.QPushButton(Dialog)
        self.Browse2.setGeometry(QtCore.QRect(530, 160, 84, 23))
        self.Browse2.setObjectName(_fromUtf8("Browse2"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.Browse1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.footprint_browse)
        QtCore.QObject.connect(self.Browse2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.wind_browse)
        QtCore.QObject.connect(self.create, QtCore.SIGNAL(_fromUtf8("clicked()")), self.create_wind)
        self.Resolution.valueChanged[str].connect(self.input_resolution)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Building's Elevation", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Create Wind Direction of Shape File</span></p></body></html>", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Enter wind line resolution:</span></p></body></html>", None))
        self.create.setToolTip(_translate("Dialog", "<html><head/><body><p>To create the wind direction of shape file</p></body></html>", None))
        self.create.setText(_translate("Dialog", "Create", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Select the direction for which Shape file is to be created:</span></p></body></html>", None))
        self.Wind_Select.setToolTip(_translate("Dialog", "<html><head/><body><p>Select the angle for the direction of wind </p></body></html>", None))
        self.Wind_Select.setItemText(0, _translate("Dialog", "Angles start from south & proceeds anticlockwise.", None))
        self.Wind_Select.setItemText(1, _translate("Dialog", "0 Degrees", None))
        self.Wind_Select.setItemText(2, _translate("Dialog", "45 Degrees", None))
        self.Wind_Select.setItemText(3, _translate("Dialog", "90 Degrees", None))
        self.Wind_Select.setItemText(4, _translate("Dialog", "135 Degrees", None))
        self.Wind_Select.setItemText(5, _translate("Dialog", "180 Degrees", None))
        self.Wind_Select.setItemText(6, _translate("Dialog", "225 Degrees", None))
        self.Wind_Select.setItemText(7, _translate("Dialog", "270 Degrees", None))
        self.Wind_Select.setItemText(8, _translate("Dialog", "315 Degrees", None))
        self.Browse1.setToolTip(_translate("Dialog", "<html><head/><body><p>Choose shape file for DTM file </p></body></html>", None))
        self.Browse1.setText(_translate("Dialog", "Browse", None))
        self.label_7.setText(_translate("Dialog", "Select Building Frootprint Shape-File:", None))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p>Output Wind-Lines direction Shape-file:</p></body></html>", None))
        self.Browse2.setToolTip(_translate("Dialog", "<html><head/><body><p>Choose shape file to generate the Output wind direction</p></body></html>", None))
        self.Browse2.setText(_translate("Dialog", "Browse", None))

    def footprint_browse(self):
        print ('selecting folder containing building footprint')
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home',filter= '*.shp')
        self.footprint_path = self.fname.replace('\\','/')
        self.lineEdit_3.setText(self.fname)
        print(self.footprint_path)

    def wind_browse(self):
        print ('selecting folder that will contain wind direction shape file')
        self.fname = QtGui.QFileDialog.getSaveFileName(None, 'Open file','/home',filter= '*.shp')
        self.wind_path = self.fname.replace('\\','/')
        self.lineEdit.setText(self.fname)
        print(self.wind_path)

    def input_resolution(self):
        self.reso_val = self.Resolution.value()

    def create_wind(self):
        self.driver = ogr.GetDriverByName('ESRI Shapefile')
        self.Wind_out = str(self.wind_path)
        self.Footprint = str(self.footprint_path)
        self.footprintSource = self.driver.Open(self.Footprint,0)
        self.footprintLayer = self.footprintSource.GetLayer()
        self.spatialRef = (self.footprintLayer.GetSpatialRef())
        # print(self.spatialRef)
        self.spatRef = osgeo.osr.SpatialReference()
        self.spatRef = self.spatialRef
        
        self.Index_ = self.Wind_Select.currentIndex()
        # print(self.Index_)
       

        if self.Index_ == 1:
            
            loopAdvance = 2
            lineSpacing = self.reso_val
            # Creates a line feature in south to north direction            
            dataSource = self.driver.CreateDataSource(self.Wind_out)
            lynLayer = dataSource.CreateLayer('lyn',self.spatRef,geom_type = ogr.wkbLineString)
            vertexLst = []
            print('*********************************************')
            feaObj = ogr.Feature(lynLayer.GetLayerDefn())          
            for vertices in self.footprintLayer.GetExtent():
                
                vertexLst.append(vertices)
            # print(vertexLst)
            lineReso = int(vertexLst[1] - vertexLst[0])/lineSpacing
            # print(lineReso)
            x1 = vertexLst[0]
            x2 = vertexLst[1]
            y1 = vertexLst[2]
            y2 = vertexLst[3]
            for i in range(0,int(lineReso+loopAdvance)):
                lynObj = ogr.Geometry(ogr.wkbLineString)
                lynObj.AddPoint(x1,y1)
                lynObj.AddPoint(x1,y2)        
                feaObj.SetGeometry(lynObj)
                x1 = x1 + lineSpacing
                print('bottom point is', x1,y1,'top point is',x1,y2)
                lynLayer.CreateFeature(feaObj)
            print "Success ! WindLines Generated ... :) "
            

        if self.Index_ == 2:
            vertexLst = []
            loopAdvance = 2
            lineSpacing = self.reso_val
            
            dataSource = self.driver.CreateDataSource(self.Wind_out)
            lynLayer = dataSource.CreateLayer('lyn',self.spatRef,geom_type = ogr.wkbLineString)
            feaObj = ogr.Feature(lynLayer.GetLayerDefn())
            feaObj = ogr.Feature(lynLayer.GetLayerDefn())
            for vertices in self.footprintLayer.GetExtent():
                vertexLst.append(vertices)
            # print(vertexLst)
            xLimit = vertexLst[1]-vertexLst[0]
            #loopAdvance = int(input('Supply the loop threshold value'))
            x1 = vertexLst[0]
            x2 = vertexLst[1]
            y1 = vertexLst[2]
            y2 = vertexLst[3]
            lineReso = xLimit/lineSpacing
            x3 = x1
            y3 = y1
            # x2=2*(x2-x1)
            # y2=2*(y2-y1)
            # if (y2<x2):
            #     x4=x2-y2
            #     y2=y2+x4
            # else:
            #     x4=y2-x2
            #     x2=x2+x4
            
            for i in range(0,int(2*lineReso)):
                
                lynObj = ogr.Geometry(ogr.wkbLineString)
                if(y3>=y2 and x3>=x2):
                    if(y1>=y2 and x1>=x2):
                        break
                    x1=x1+lineSpacing
                    
                    lynObj.AddPoint(x2,y1)
                    lynObj.AddPoint(x1,y2)
                    feaObj.SetGeometry(lynObj)
                    lynLayer.CreateFeature(feaObj)
                    y1=y1+lineSpacing
                elif(x3>=x2):
                    
                
                    lynObj.AddPoint(x2,y1)
                    lynObj.AddPoint(x1,y3)
                    feaObj.SetGeometry(lynObj)
                    y1=y1+lineSpacing
                    y3=y3+lineSpacing
                    lynLayer.CreateFeature(feaObj)
                elif(y3>=y2):
                    x1=x1+lineSpacing
                   
                    lynObj.AddPoint(x1,y2)
                    lynObj.AddPoint(x3,y1)
                    x3=x3+lineSpacing
                    
                    feaObj.SetGeometry(lynObj)
                    lynLayer.CreateFeature(feaObj)
                else:
                    lynObj.AddPoint(x3,y1)
                    lynObj.AddPoint(x1,y3)
                    feaObj.SetGeometry(lynObj)
                    x3 = x3 + lineSpacing
                    y3 = y3 + lineSpacing
                    print('bottom point is', x1,y1,'top point is',x1,y2)
                    lynLayer.CreateFeature(feaObj)
            print "Success ! WindLines Generated ... :) "  
           


        if self.Index_ == 3:
            loopAdvance = 2
            lineSpacing = self.reso_val
            vertexLst = []
            dataSource = self.driver.CreateDataSource(self.Wind_out)
            lynLayer = dataSource.CreateLayer('lyn',self.spatRef,geom_type = ogr.wkbLineString)
            feaObj = ogr.Feature(lynLayer.GetLayerDefn())
            for vertices in self.footprintLayer.GetExtent():
                vertexLst.append(vertices)
            # print(vertexLst)
            lineReso = int(vertexLst[3] - vertexLst[2])/lineSpacing
            # print(lineReso)
            x1 = vertexLst[0]
            x2 = vertexLst[1]
            y1 = vertexLst[2]
            y2 = vertexLst[3]
            for i in range(0,int(lineReso+loopAdvance)):
                lynObj = ogr.Geometry(ogr.wkbLineString)
                lynObj.AddPoint(x2,y1)
                lynObj.AddPoint(x1,y1)
                feaObj.SetGeometry(lynObj)
                y1 = y1 + lineSpacing
                print('bottom point is', x1,y1,'top point is',x1,y2)
                lynLayer.CreateFeature(feaObj)
            print "Success ! WindLines Generated ... :) "

        if self.Index_ == 4:
            loopAdvance = 2
            lineSpacing = self.reso_val
            vertexLst = []
            dataSource = self.driver.CreateDataSource(self.Wind_out)
            lynLayer = dataSource.CreateLayer('lyn',self.spatRef,geom_type = ogr.wkbLineString)
            feaObj = ogr.Feature(lynLayer.GetLayerDefn())
            for vertices in self.footprintLayer.GetExtent():
                vertexLst.append(vertices)
            # print(vertexLst)
            xLimit = vertexLst[1]-vertexLst[0]
            #loopAdvance = int(input('Supply the loop threshold value \n'))
            x1 = vertexLst[0]
            x2 = vertexLst[1]
            y1 = vertexLst[2]
            y2 = vertexLst[3]
            lineReso = xLimit/lineSpacing
            x3 = x2
            y3 = y1
            for i in range(0,int(2*lineReso)):
                
                lynObj = ogr.Geometry(ogr.wkbLineString)
                if(y3>=y2 and x3<=x1):
                    if(y1>=y2 and x2<=x1):
                        break
                    x2=x2-lineSpacing
                    
                    lynObj.AddPoint(x2,y2)
                    lynObj.AddPoint(x1,y1)
                    feaObj.SetGeometry(lynObj)
                    lynLayer.CreateFeature(feaObj)
                    y1=y1+lineSpacing

                elif(x3<=x1):
                    lynObj.AddPoint(x1,y1)
                    lynObj.AddPoint(x2,y3)
                    feaObj.SetGeometry(lynObj)
                    y1=y1+lineSpacing
                    y3=y3+lineSpacing
                    lynLayer.CreateFeature(feaObj)
                elif(y3>=y2):
                    x2=x2-lineSpacing
                   
                    lynObj.AddPoint(x3,y1)
                    lynObj.AddPoint(x2,y2)
                    x3=x3-lineSpacing
                    
                    feaObj.SetGeometry(lynObj)
                    lynLayer.CreateFeature(feaObj)
                else:
                    lynObj.AddPoint(x3,y1)
                    lynObj.AddPoint(x2,y3)
                    feaObj.SetGeometry(lynObj)
                    x3 = x3 - lineSpacing
                    y3 = y3 + lineSpacing
                    print('bottom point is', x1,y1,'top point is',x1,y2)
                    lynLayer.CreateFeature(feaObj)
            print "Success ! WindLines Generated ... :) "

        if self.Index_== 5:
            loopAdvance = 2
            lineSpacing = self.reso_val
            vertexLst = []
            dataSource = self.driver.CreateDataSource(self.Wind_out)
            lynLayer = dataSource.CreateLayer('lyn',self.spatRef,geom_type = ogr.wkbLineString)
            feaObj = ogr.Feature(lynLayer.GetLayerDefn())
            for vertices in self.footprintLayer.GetExtent():
                vertexLst.append(vertices)
            # print(vertexLst)
            lineReso = int(vertexLst[1] - vertexLst[0])/lineSpacing
            # print(lineReso)
            x1 = vertexLst[0]
            x2 = vertexLst[1]
            y1 = vertexLst[2]
            y2 = vertexLst[3]
            for i in range(0,int(lineReso+loopAdvance)):
                lynObj = ogr.Geometry(ogr.wkbLineString)
                lynObj.AddPoint(x1,y2)
                lynObj.AddPoint(x1,y1)        
                feaObj.SetGeometry(lynObj)
                x1 = x1 + lineSpacing
                print('bottom point is', x1,y1,'top point is',x1,y2)
                lynLayer.CreateFeature(feaObj)
            print "Success ! WindLines Generated ... :) "

        if self.Index_== 6:
            loopAdvance = 2
            lineSpacing = self.reso_val
            vertexLst = []
            dataSource = self.driver.CreateDataSource(self.Wind_out)
            lynLayer = dataSource.CreateLayer('lyn',self.spatRef,geom_type = ogr.wkbLineString)
            feaObj = ogr.Feature(lynLayer.GetLayerDefn())
            for vertices in self.footprintLayer.GetExtent():
                vertexLst.append(vertices)
            # print(vertexLst)
            xLimit = vertexLst[1]-vertexLst[0]
            #loopAdvance = int(input('Supply the loop threshold value'))
            x1 = vertexLst[0]
            x2 = vertexLst[1]
            y1 = vertexLst[2]
            y2 = vertexLst[3]
            lineReso = xLimit/lineSpacing
            x3 = x1
            y3 = y1
            for i in range(0,int(2*lineReso)):
                
                lynObj = ogr.Geometry(ogr.wkbLineString)
                if(y3>=y2 and x3>=x2):
                    if(y1>=y2 and x1>=x2):
                        break
                    x1=x1+lineSpacing
                    
                    lynObj.AddPoint(x2,y1)
                    lynObj.AddPoint(x1,y2)
                    feaObj.SetGeometry(lynObj)
                    lynLayer.CreateFeature(feaObj)
                    y1=y1+lineSpacing
                elif(x3>=x2):
                    
                
                    lynObj.AddPoint(x2,y1)
                    lynObj.AddPoint(x1,y3)
                    feaObj.SetGeometry(lynObj)
                    y1=y1+lineSpacing
                    y3=y3+lineSpacing
                    lynLayer.CreateFeature(feaObj)
                elif(y3>=y2):
                    x1=x1+lineSpacing
                   
                    lynObj.AddPoint(x1,y2)
                    lynObj.AddPoint(x3,y1)
                    x3=x3+lineSpacing
                    
                    feaObj.SetGeometry(lynObj)
                    lynLayer.CreateFeature(feaObj)
                else:
                    lynObj.AddPoint(x3,y1)
                    lynObj.AddPoint(x1,y3)
                    feaObj.SetGeometry(lynObj)
                    x3 = x3 + lineSpacing
                    y3 = y3 + lineSpacing
                    print('bottom point is', x1,y1,'top point is',x1,y2)
                    lynLayer.CreateFeature(feaObj)
            print "Success ! WindLines Generated ... :) "

        if self.Index_ == 7:
            loopAdvance = 2
            lineSpacing = self.reso_val
            vertexLst = []
            dataSource = self.driver.CreateDataSource(self.Wind_out)
            lynLayer = dataSource.CreateLayer('lyn',self.spatRef,geom_type = ogr.wkbLineString)
            feaObj = ogr.Feature(lynLayer.GetLayerDefn())
            for vertices in self.footprintLayer.GetExtent():
                vertexLst.append(vertices)
            # print(vertexLst)
            lineReso = int(vertexLst[3] - vertexLst[2])/lineSpacing
            # print(lineReso)
            #loopAdvance = int(input('Supply the loop threshold value \n'))
            x1 = vertexLst[0]
            x2 = vertexLst[1]
            y1 = vertexLst[2]
            y2 = vertexLst[3]
            for i in range(0,int(lineReso+loopAdvance)):
                lynObj = ogr.Geometry(ogr.wkbLineString)
                lynObj.AddPoint(x1,y1)
                lynObj.AddPoint(x2,y1)        
                feaObj.SetGeometry(lynObj)
                y1 = y1 + lineSpacing
                print('bottom point is', x1,y1,'top point is',x1,y2)
                lynLayer.CreateFeature(feaObj)
            print "Success ! WindLines Generated ... :) "
        
        if self.Index_ == 8:
            loopAdvance = 2
            lineSpacing = self.reso_val
            vertexLst = []
            dataSource = self.driver.CreateDataSource(self.Wind_out)
            lynLayer = dataSource.CreateLayer('lyn',self.spatRef,geom_type = ogr.wkbLineString)
            feaObj = ogr.Feature(lynLayer.GetLayerDefn())
            for vertices in self.footprintLayer.GetExtent():
                vertexLst.append(vertices)
            # print(vertexLst)
            xLimit = vertexLst[1]-vertexLst[0]
            #loopAdvance = int(input('Supply the loop threshold value \n'))
            x1 = vertexLst[0]
            x2 = vertexLst[1]
            y1 = vertexLst[2]
            y2 = vertexLst[3]
            lineReso = xLimit/lineSpacing
            x3 = x2
            y3 = y1
            for i in range(0,int(2*lineReso)):
                
                lynObj = ogr.Geometry(ogr.wkbLineString)
                if(y3>=y2 and x3<=x1):
                    if(y1>=y2 and x2<=x1):
                        break
                    x2=x2-lineSpacing
                    
                    lynObj.AddPoint(x2,y2)
                    lynObj.AddPoint(x1,y1)
                    feaObj.SetGeometry(lynObj)
                    lynLayer.CreateFeature(feaObj)
                    y1=y1+lineSpacing
                elif(x3<=x1):
                    
                
                    lynObj.AddPoint(x1,y1)
                    lynObj.AddPoint(x2,y3)
                    feaObj.SetGeometry(lynObj)
                    y1=y1+lineSpacing
                    y3=y3+lineSpacing
                    lynLayer.CreateFeature(feaObj)
                elif(y3>=y2):
                    x2=x2-lineSpacing
                   
                    lynObj.AddPoint(x3,y1)
                    lynObj.AddPoint(x2,y2)
                    x3=x3-lineSpacing
                    
                    feaObj.SetGeometry(lynObj)
                    lynLayer.CreateFeature(feaObj)
                else:
                    lynObj.AddPoint(x3,y1)
                    lynObj.AddPoint(x2,y3)
                    feaObj.SetGeometry(lynObj)
                    x3 = x3 - lineSpacing
                    y3 = y3 + lineSpacing
                    print('bottom point is', x1,y1,'top point is',x1,y2)
                    lynLayer.CreateFeature(feaObj)
            print "Success ! WindLines Generated ... :) "

class Ui_Dialog_CFA(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 448)
        Dialog.setStyleSheet(_fromUtf8("QDialog{\n"
"color:navy; background-color: white;\n"
"\n"
"                     \n"
"}\n"
"QRadioButton{\n"
"color:navy;\n"
"}\n"
"QLabel{\n"
"color: navy; \n"
"                        \n"
"                        selection-color: yellow;\n"
"                        selection-background-color: blue;\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
" border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
""))
        self.choice_3 = QtGui.QRadioButton(Dialog)
        self.choice_3.setGeometry(QtCore.QRect(10, 360, 291, 17))
        self.choice_3.setObjectName(_fromUtf8("choice_3"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(360, 360, 171, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Height_Select = QtGui.QSpinBox(Dialog)
        self.Height_Select.setGeometry(QtCore.QRect(300, 360, 42, 22))
        self.Height_Select.setObjectName(_fromUtf8("Height_Select"))
        self.choice_2 = QtGui.QRadioButton(Dialog)
        self.choice_2.setGeometry(QtCore.QRect(10, 330, 341, 17))
        self.choice_2.setObjectName(_fromUtf8("choice_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 20, 321, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.choice_1 = QtGui.QRadioButton(Dialog)
        self.choice_1.setGeometry(QtCore.QRect(10, 300, 261, 21))
        self.choice_1.setObjectName(_fromUtf8("choice_1"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 210, 261, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.Browse4 = QtGui.QPushButton(Dialog)
        self.Browse4.setGeometry(QtCore.QRect(490, 210, 84, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Browse4.setFont(font)
        self.Browse4.setObjectName(_fromUtf8("Browse4"))
        self.ok_btn = QtGui.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(390, 400, 84, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.cancel_btn = QtGui.QPushButton(Dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(490, 401, 84, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 170, 261, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 191, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 191, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(200, 90, 261, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.Browse1 = QtGui.QPushButton(Dialog)
        self.Browse1.setGeometry(QtCore.QRect(490, 90, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Browse1.setFont(font)
        self.Browse1.setObjectName(_fromUtf8("Browse1"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 191, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Browse3 = QtGui.QPushButton(Dialog)
        self.Browse3.setGeometry(QtCore.QRect(490, 170, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Browse3.setFont(font)
        self.Browse3.setObjectName(_fromUtf8("Browse3"))
        self.Browse2 = QtGui.QPushButton(Dialog)
        self.Browse2.setGeometry(QtCore.QRect(490, 130, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Browse2.setFont(font)
        self.Browse2.setObjectName(_fromUtf8("Browse2"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 130, 261, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 170, 151, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 326, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(340, 290, 161, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.Wind_Select = QtGui.QComboBox(Dialog)
        self.Wind_Select.setGeometry(QtCore.QRect(340, 250, 281, 20))
        self.Wind_Select.setObjectName(_fromUtf8("Wind_Select"))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Resolution = QtGui.QSpinBox(Dialog)
        self.Resolution.setGeometry(QtCore.QRect(520, 290, 42, 22))
        self.Resolution.setMaximum(20)
        self.Resolution.setObjectName(_fromUtf8("Resolution"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QObject.connect(self.Browse1,QtCore.SIGNAL("clicked()"),self.footprint_browse)
        QtCore.QObject.connect(self.Browse2,QtCore.SIGNAL("clicked()"),self.wind_browse)
        QtCore.QObject.connect(self.Browse3,QtCore.SIGNAL("clicked()"),self.grid_browse)
        QtCore.QObject.connect(self.Browse4,QtCore.SIGNAL("clicked()"),self.output_browse)
        QtCore.QObject.connect(self.ok_btn,QtCore.SIGNAL("clicked()"),self.myfunc_CFA)
        self.Resolution.valueChanged[str].connect(self.input_resolution)
        self.Height_Select.valueChanged[str].connect(self.input_height)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Compute Frontal Area", None))
        self.choice_3.setText(_translate("Dialog", "Compute Frontal Area at different Height values", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>Enter the Height limits</p><p><br/></p></body></html>", None))
        self.choice_2.setText(_translate("Dialog", "Compute Frontal Area based on Grid Overlayed", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Compute Frontal Area</span></p></body></html>", None))
        self.choice_1.setText(_translate("Dialog", "Compute overall Frontal Area", None))
        self.Browse4.setText(_translate("Dialog", "Browse", None))
        self.ok_btn.setText(_translate("Dialog", "Ok", None))
        self.cancel_btn.setText(_translate("Dialog", "Cancel", None))
        self.label_3.setText(_translate("Dialog", "Select the Wind Lines Shapefile:", None))
        self.label_4.setText(_translate("Dialog", "Select the footprint Building Shapefile:", None))
        self.Browse1.setText(_translate("Dialog", "Browse", None))
        self.label_5.setText(_translate("Dialog", "Select the output files location:", None))
        self.Browse3.setText(_translate("Dialog", "Browse", None))
        self.Browse2.setText(_translate("Dialog", "Browse", None))
        self.label_7.setText(_translate("Dialog", "Select the location of grid file..", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Select the direction for which Shape file is to be created:</span></p></body></html>", None))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Enter wind line resolution:</span></p></body></html>", None))
        self.Wind_Select.setToolTip(_translate("Dialog", "<html><head/><body><p>Select the angle for the direction of wind </p></body></html>", None))
        self.Wind_Select.setItemText(0, _translate("Dialog", "Angles start from south & proceeds anticlockwise.", None))
        self.Wind_Select.setItemText(1, _translate("Dialog", "0 Degrees", None))
        self.Wind_Select.setItemText(2, _translate("Dialog", "45 Degrees", None))
        self.Wind_Select.setItemText(3, _translate("Dialog", "90 Degrees", None))
        self.Wind_Select.setItemText(4, _translate("Dialog", "135 Degrees", None))
        self.Wind_Select.setItemText(5, _translate("Dialog", "180 Degrees", None))
        self.Wind_Select.setItemText(6, _translate("Dialog", "225 Degrees", None))
        self.Wind_Select.setItemText(7, _translate("Dialog", "270 Degrees", None))
        self.Wind_Select.setItemText(8, _translate("Dialog", "315 Degrees", None))

    def footprint_browse(self):
        print ('selecting folder containing building footprint')
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home',filter= '*.shp')
        self.footprint_path = self.fname.replace('\\','/')
        self.lineEdit.setText(self.fname)
        print(self.footprint_path)

    def wind_browse(self):
        print ('selecting folder that will contain wind direction shape file')
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home',filter= '*.shp')
        self.wind_path = self.fname.replace('\\','/')
        self.lineEdit_2.setText(self.fname)
        print(self.wind_path)

    def grid_browse(self):
        print ('selecting folder containing Grid shape file ')
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home',filter= '*.shp')
        self.grid_path = self.fname.replace('\\','/')
        self.lineEdit_4.setText(self.fname)
        print(self.grid_path)

    def output_browse(self):
        print ('selecting folder containing output text file')
        #self.fname = QtGui.QFileDialog.getSaveFileName(None, 'Save file','/home',filter = '*.txt')
        self.fname = QtGui.QFileDialog.getExistingDirectory(None, "Select Directory for saving output files")
        self.output_path = self.fname.replace('\\','/')
        self.lineEdit_3.setText(self.fname)
        print(self.output_path)

    def input_resolution(self):
        self.reso_val = self.Resolution.value()

    def input_height(self):
        self.HeightVal = self.Height_Select.value()

    def myfunc_CFA(self):
        self.Index_ = self.Wind_Select.currentIndex()
        if self.Index_ == 1:
            
            if self.choice_1.isChecked()== True:
                Driver = ogr.GetDriverByName('ESRI Shapefile')
                Footprint = str(self.footprint_path)
                polySource = Driver.Open(Footprint,0)
                polyLayer = polySource.GetLayer()
                wind = str(self.wind_path)
                windSource = Driver.Open(wind,0)
                windLayer = windSource.GetLayer()
                output = str(self.output_path)
                FrontalArea = 0
                name_of_file = 'Frontal Area 0 DEG'
                completeName = os.path.join(output, name_of_file+".txt") 
                cfa0 = open(completeName , "w")
                #sys.stdout = open(output,'w')            
                for wind in range(0,windLayer.GetFeatureCount()):
                    ptLst = []
                    PolyIntersectSeq = []
                    BuildingIntersectSeq = []
                    windFeature = windLayer.GetNextFeature()
                    windGeometry = windFeature.GetGeometryRef()
                    lineSpacing = self.reso_val
                    newGem = windGeometry.Buffer(lineSpacing);
                    # abc =  newGem.GetEnvelope()
                    polyLayer.SetSpatialFilter(newGem)
                    
                    
                    
                    for currentPoly in range (0,polyLayer.GetFeatureCount()):
                        currentPolyFeat = polyLayer.GetNextFeature()
                        currentPolyGeom = currentPolyFeat.GetGeometryRef()
                        FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                        if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                            PolyIntersectSeq.append(currentPolyFeat.GetFID())
                            ptLst.append(FirstIntersect.GetPoints())
                    ptRefDict = dict(zip(PolyIntersectSeq,ptLst))
                    PtSort = sorted(ptLst)
                    if (len(PtSort) > 0 and len(ptRefDict) > 0):
                        cfa0.write ("*******************************************************\n")
                        cfa0.write("WindLine \n".format(windFeature.GetFID()))
                        cfa0.write("This is the list of buildings that the windline {0} intersects {1} \n".format(windFeature.GetFID(),PolyIntersectSeq))
                        cfa0.write('This is the list of points that the windline {0} and building {1} intersects at {2}\n'.format(windFeature.GetFID(),currentPolyFeat.GetFID(),ptLst))        
                        cfa0.write('This is the dictionary that has the keys as polygon and value as respective coordinate {0} \n'.format(ptRefDict))        
                        cfa0.write('This is the list of intersection points sorted as the actually intersect {0} \n'.format(PtSort))
                        for x in range(0,len(PtSort)):
                            firstBuildingXY = PtSort[x]
                            for key in ptRefDict.keys():
                                if ptRefDict[key] ==  firstBuildingXY:
                                    BuildingIntersectSeq.append(key)
                        cfa0.write('This list contains the polygon FID in a order the windline {0} intersects buildings {1} \n'.format(windFeature.GetFID(),BuildingIntersectSeq))
                        size = len(BuildingIntersectSeq)
                        lineSpacing = self.reso_val
                        if size <= 1:
                            building = polyLayer.GetFeature(BuildingIntersectSeq[0])
                            height = building.GetField(Ui_MainWindow.hei_name)
                            frontalarea = lineSpacing * height
                        elif size > 1 :

                            firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[0])
                            height1 = firstBuild.GetField(Ui_MainWindow.hei_name)
                            MaxHeight=height1
                            for building1 in range (1,size):
                                firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[building1])
                                height1 = firstBuild.GetField(Ui_MainWindow.hei_name)
                                if(MaxHeight<height1):
                                        MaxHeight= height1
                            frontalarea= lineSpacing*MaxHeight   
                        
                        cfa0.write('The frontal area exposed to windline {0} is = {1}'.format(windFeature.GetFID(),frontalarea))
                        FrontalArea = FrontalArea + frontalarea

                cfa0.write('The total frontal area of the study area is = {0}'.format(FrontalArea))
                polyLayer.SetSpatialFilter(None)
                cfa0.close()
            
            if self.choice_2.isChecked()== True:
                                Driver1 = ogr.GetDriverByName('ESRI Shapefile')
                                Grid =str(self.grid_path)
                                GridSource = Driver1.Open(Grid,1)
                                GridLayer = GridSource.GetLayer()
                                length = GridLayer.GetFeatureCount()
                                frontalAreaList = list([0.0 for x in range(length)])
                                Footprint = str(self.footprint_path)
                                BuildingSource = Driver1.Open(Footprint,0)
                                BuildingLayer = BuildingSource.GetLayer()
                                wind = str(self.wind_path)
                                WindSource = Driver1.Open(wind,0)
                                WindLayer = WindSource.GetLayer()
                                output = str(self.output_path)
                                layer_defn = GridLayer.GetLayerDefn()
                                #print self.Wind_select.currentText()
                                text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for frontal area :')
                                if ok:
                                    name=str(text)
                                ldefn = GridLayer.GetLayerDefn()
                                sch= []
                                check=0
                                n=0
                                for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
                                    field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
                                    sch.append(field) 
                                n=0
                                for n in range(len(sch)):
                                   if(name==str(sch[n])):
                                       check=1
                                if (check==0):
                                    new_field = ogr.FieldDefn(name, ogr.OFTReal)
                                    GridLayer.CreateField(new_field)
                                FrontalArea = 0
                                GridFrontalArea = []
                                length = GridLayer.GetFeatureCount()
                                GridFeat = GridLayer.GetFeature(0)
                                GridGeom = GridFeat.GetGeometryRef()
                                list1 = GridLayer.GetExtent()
                                list2 = GridGeom.GetEnvelope()
                                noc = (list1[1]-list1[0])/(list2[1]-list2[0])
                                nor = (list1[3]-list1[2])/(list2[3]-list2[2])
                                i=0
                                f=0
                                l=0
                                k= -noc
                                height_list2 = []
                                height_list3 = [] 
                                height_list1 = []
                                area=0
                                name_of_file = 'Frontal Area Grid 0 DEG'
                                completeName = os.path.join(output, name_of_file+".txt") 
                                cfg0 = open(completeName , "w")
                                #sys.stdout = open('running.txt','w')

                                for Grid in range(0,length):
                                    

                                    BuildingSeq = []
                                    WindSeq = []
                                    polyIntersectSeq = []   
                                    polySeq = []
                                    if f<=nor-1:
                                        k=k+noc
                                        f=f+1
                                        
                                    else:
                                        k=l+1
                                        f= 1
                                        l=l+1
                                         
                                  
                                   
                                    GridFeat = GridLayer.GetFeature(int(abs(k)))
                                   
                                    GridGeom = GridFeat.GetGeometryRef()
                                    area=GridGeom.GetArea()
                                    BuildingLayer.SetSpatialFilter(GridGeom)
                                    WindLayer.SetSpatialFilter(GridGeom)

                                    GridList= list(GridGeom.GetEnvelope())
                                    # print GridList
                                    lineSpacing = self.reso_val
                                    
                                    for line in range(0,WindLayer.GetFeatureCount()):
                                         
                                        windFeature = WindLayer.GetNextFeature()
                                        windGeometry = windFeature.GetGeometryRef()
                                       
                                        
                                        for poly in range(0,BuildingLayer.GetFeatureCount()):
                                            polyFeature = BuildingLayer.GetNextFeature()
                                            if not polyFeature:
                                                continue
                                            polyGeom = polyFeature.GetGeometryRef()
                                            Intersect = windGeometry.Intersection(polyGeom)
                                            
                                            if Intersect.IsEmpty()==False:
                                                abc = list(Intersect.GetEnvelope())
                                                # print abc
                                                # print "Entering intersect"
                                                if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                                                # polyIntersectSeq.append(Intersect.GetPoints())
                                                # polySeq.append(polyFeature.GetFID())
                                                    height_list1.append(polyFeature.GetField('Height'))
                                                    # print "Entering GridCompare"
                                            # else:
                                            #     o=0
                                            #     height_list1.append(o)
                                        BuildingLayer.ResetReading()
                                        if height_list1:
                                            m = max(height_list1)
                                        else:
                                            m=0  
                                        #print m 
                                        #print "H1 is "
                                        #print height_list1   
                                        #print                 
                                        height_list2.append(m)
                                        del height_list1[:]
                                        #print ("Height_list2 earlier",height_list2)
                                    for x in range(0,len(height_list2)):
                                        if len(height_list3) == 0:
                                            FrontalArea = FrontalArea+ lineSpacing*(height_list2[x])
                                            # print 'hello : Length '
                                            # p print "len"rint len(height_list3)

                                        else:
                                        
                                            if (height_list2[x]-height_list3[x])>0:
                                                j = height_list2[x]-height_list3[x]
                                                # print"@@@@@@@"
                                                FrontalArea= FrontalArea+ lineSpacing*(j)
                                                # print k
                                            else:
                                                j=0
                                                FrontalArea= FrontalArea+ lineSpacing*(j)
                                    #print "H2 is "
                                    #print height_list2
                                    #print "h3 is "
                                    #print height_list3
                                    #FrontalArId= float(FrontalArea)*float(1/area)            
                                    cfg0.write("The Frontal area for Grid {0} is {1} \n " .format(GridFeat.GetFID(),FrontalArea))
                                    frontalAreaList[GridFeat.GetFID()] = FrontalArea
                                    #GridFeat.SetField('GridFA',FrontalArea)
                                    #GridLayer.SetFeature(GridFeat)
                                    GridFeat.SetField(name,FrontalArea)
                                    GridLayer.SetFeature(GridFeat)
                                    #print
                                    
                                    FrontalArea=0
                                    i=i+1 
                                    
                                    if(i>=nor):
                                        del height_list3[:]
                                        del height_list2[:]
                                        i=0
                                       
                                    else:
                                        del height_list3[:]
                                        height_list3= list(height_list2) 
                                        del height_list2[:]
                                        
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                cfg0.close()



            #### Computes the frontal area at different heights.
            if self.choice_3.isChecked() == True:
                Driver2 = ogr.GetDriverByName('ESRI Shapefile')
                poly = str(self.footprint_path)
                polySource = Driver2.Open(poly,0)
                polyLayer = polySource.GetLayer()
                wind = str(self.wind_path)
                windSource = Driver2.Open(wind,0)
                windLayer = windSource.GetLayer()
                spatialReference = polyLayer.GetSpatialRef()
                BuildLst = []
                lstPoints = []
                HWlst = []
                FrontalArea = 0
                HEIGHT = int(input("Supply the height value \n "))
                lineSpacing = self.reso_val
                for wind in range(0,windLayer.GetFeatureCount()):
                    frontalarea = 0
                    ptLst = []
                    PolyIntersectSeq = []
                    ptRefDict = {}
                    BuildingIntersectSeq = []
                    windFeature = windLayer.GetFeature(wind)
                    windGeometry = windFeature.GetGeometryRef()
                    IntersectPts = []
                    HeightLst = []
                    WidthLst = []
                    height = 0
                    IntersectPts = []
                    for currentPoly in range (0,polyLayer.GetFeatureCount()):
                        currentPolyFeat = polyLayer.GetFeature(currentPoly)
                        currentPolyGeom = currentPolyFeat.GetGeometryRef()
                        FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                        if FirstIntersect.IsEmpty() == False:
                            PolyIntersectSeq.append(currentPolyFeat.GetFID())
                            if FirstIntersect.GetGeometryName() == 'MULTILINESTRING':
                                pt1 = ()
                                pt2 = ()
                                PT1 =[]
                                PT2 = []
                                print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                                points = FirstIntersect.GetEnvelope()
                                count = len(points)
                                for i in range(0,count,2):
                                    pt1 = pt1 + (points[i],)
                                    pt2 = pt2 + (points[i+1],)
                                PT1.append(pt1)
                                PT2.append(pt2)
                                ptLst.append(PT1)
                                ptLst.append(PT2)
                
                            elif FirstIntersect.GetGeometryName() == 'LINESTRING':
                                print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                                Points = FirstIntersect.GetPoints()
                                ptLst.append(Points)
        
                    ptRefDict = dict(zip(PolyIntersectSeq,ptLst))                
                    ptSort = sorted(ptLst,key = operator.itemgetter(0),reverse = True)
                    print(ptSort)
                    if len(ptSort) > 0 and len(ptRefDict) > 0:
                        for k in range(0,len(ptSort)):
                            firstBuildingXY = ptSort[k]
                            for key in ptRefDict.keys():
                                if  firstBuildingXY == ptRefDict[key]:
                                    BuildingIntersectSeq.append(key)
                        print('Building Intersect Sequence is = ',BuildingIntersectSeq)
                    size = len(BuildingIntersectSeq)
                    if size == 1:
                        building = polyLayer.GetFeature(BuildingIntersectSeq[0])
                        Ht = building.GetField('Height')
                        if Ht > HEIGHT:
                            height = HEIGHT
                        elif Ht <= HEIGHT:
                            height = Ht
                        frontalarea = lineSpacing* height
                    elif size > 1 :
                        firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[0])
                        Ht1 = firstBuild.GetField('Height')
                        if Ht1 > HEIGHT:
                            height1 = HEIGHT
                        elif Ht1 <= HEIGHT:
                            height1 = Ht1
                        maxHeight = height1
                        frontalarea =  lineSpacing * height1
                        for building1 in range (1,size):
                            secondBuild = polyLayer.GetFeature(BuildingIntersectSeq[building1])
                            Ht2 = secondBuild.GetField('Height')
                            if Ht2 > HEIGHT:
                                height2 = HEIGHT
                            elif Ht2 <= HEIGHT:
                                height2 = Ht2
                            if height2>maxHeight:
                                effHeight = height2 - maxHeight
                                frontalarea =  frontalarea +(lineSpacing * effHeight)
                                MaxHeight = height2
                        print('\n The frontal area exposed to windline',windFeature.GetFID(),'is = ',frontalarea,'\n')
                    FrontalArea = FrontalArea + frontalarea
                print('\n The total frontal area of the study area is = ',FrontalArea)
                
        if self.Index_ == 2:
            if self.choice_1.isChecked()== True:
                Driver = ogr.GetDriverByName('ESRI Shapefile')
                Footprint = str(self.footprint_path)
                polySource = Driver.Open(Footprint,0)
                polyLayer = polySource.GetLayer()
                wind = str(self.wind_path)
                windSource = Driver.Open(wind,0)
                windLayer = windSource.GetLayer()
                output = str(self.output_path)
                FrontalArea = 0
                name_of_file = 'Frontal Area 45 DEG'
                completeName = os.path.join(output, name_of_file+".txt") 
                cfa45 = open(completeName , "w")
                #sys.stdout = open(output,'w')            
                for wind in range(0,windLayer.GetFeatureCount()):
                    ptLst = []
                    PolyIntersectSeq = []
                    BuildingIntersectSeq = []
                    windFeature = windLayer.GetNextFeature()
                    windGeometry = windFeature.GetGeometryRef()
                    lineSpacing = self.reso_val
                    newGem = windGeometry.Buffer(lineSpacing);
                    # abc =  newGem.GetEnvelope()
                    polyLayer.SetSpatialFilter(newGem)
                    
                    
                    
                    for currentPoly in range (0,polyLayer.GetFeatureCount()):
                        currentPolyFeat = polyLayer.GetNextFeature()
                        currentPolyGeom = currentPolyFeat.GetGeometryRef()
                        FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                        if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                            PolyIntersectSeq.append(currentPolyFeat.GetFID())
                            ptLst.append(FirstIntersect.GetPoints())
                    ptRefDict = dict(zip(PolyIntersectSeq,ptLst))
                    PtSort = sorted(ptLst)
                    if len(PtSort) > 0 and len(ptRefDict) > 0:
                        cfa45.write ("*******************************************************\n")
                        cfa45.write("WindLine \n".format(windFeature.GetFID()))
                        cfa45.write("This is the list of buildings that the windline {0} intersects {1} \n".format(windFeature.GetFID(),PolyIntersectSeq))
                        cfa45.write('This is the list of points that the windline {0} and building {1} intersects at {2}\n'.format(windFeature.GetFID(),currentPolyFeat.GetFID(),ptLst))        
                        cfa45.write('This is the dictionary that has the keys as polygon and value as respective coordinate {0} \n'.format(ptRefDict))        
                        cfa45.write('This is the list of intersection points sorted as the actually intersect {0} \n'.format(PtSort))
                        for x in range(0,len(PtSort)):
                            firstBuildingXY = PtSort[x]
                            for key in ptRefDict.keys():
                                if ptRefDict[key] ==  firstBuildingXY:
                                    BuildingIntersectSeq.append(key)
                        cfa45.write('This list contains the polygon FID in a order the windline {0} intersects buildings {1} \n'.format(windFeature.GetFID(),BuildingIntersectSeq))
                        size = len(BuildingIntersectSeq)
                        lineSpacing = self.reso_val
                        if size <= 1:
                            building = polyLayer.GetFeature(BuildingIntersectSeq[0])
                            height = building.GetField('Height')
                            frontalarea = lineSpacing * height
                        elif size > 1 :

                            firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[0])
                            height1 = firstBuild.GetField('Height')
                            MaxHeight=height1
                            for building1 in range (1,size):
                                firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[building1])
                                height1 = firstBuild.GetField('Height')
                                if(MaxHeight<height1):
                                        MaxHeight= height1
                            frontalarea= lineSpacing*MaxHeight   

                              
                        cfa45.write('The frontal area exposed to windline {0} is = {1}'.format(windFeature.GetFID(),frontalarea))
                        FrontalArea = FrontalArea + frontalarea
                cfa45.write('The total frontal area of the study area is = {0}'.format(FrontalArea))
                polyLayer.SetSpatialFilter(None)
                cfa45.close()

            if self.choice_2.isChecked()== True:
                                Driver1 = ogr.GetDriverByName('ESRI Shapefile')
                                Grid =str(self.grid_path)
                                GridSource = Driver1.Open(Grid,1)
                                GridLayer = GridSource.GetLayer()
                                Footprint = str(self.footprint_path)
                                BuildingSource = Driver1.Open(Footprint,0)
                                BuildingLayer = BuildingSource.GetLayer()
                                wind = str(self.wind_path)
                                WindSource = Driver1.Open(wind,0)
                                output = str(self.output_path)
                                WindLayer = WindSource.GetLayer()
                                layer_defn = GridLayer.GetLayerDefn()

                                text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for frontal area :')
                                if ok:
                                    name=str(text)
                                ldefn = GridLayer.GetLayerDefn()
                                sch= []
                                check=0
                                n=0
                                for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
                                    field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
                                    sch.append(field) 
                                n=0
                                for n in range(len(sch)):
                                   if(name==str(sch[n])):
                                       check=1
                                       print('Field Already exists')
                                if (check==0):
                                    new_field = ogr.FieldDefn(name, ogr.OFTReal)
                                    GridLayer.CreateField(new_field)
                                    print('New Field Created')

                                GridLayer.CreateField(new_field)
                                FrontalArea = 0
                                GridFrontalArea = []
                                length = GridLayer.GetFeatureCount()
                                lineSpacing= self.reso_val
                                ListTop = []
                                ListBottom = []
                                ListRight = []
                                ListLeft = []
                                windLeft = []
                                windRight = []
                                windBottomLeft = []
                                windBottomRight = []
                                listFrontalArea = list([0.0 for x in range(length)])
                                GridFeat =  GridLayer.GetFeature(0)

                                GridGeom = GridFeat.GetGeometryRef()
                                list1 = GridLayer.GetExtent()
                                list2 = GridGeom.GetEnvelope()
                                col = int((list1[1]-list1[0])/(list2[1]-list2[0]))
                                row = int((list1[3]-list1[2])/(list2[3]-list2[2]))
                                # print "COl"
                                # print col
                                # print "row"
                                # print row
                                name_of_file = 'Frontal Area Index 45 DEG'
                                completeName = os.path.join(output, name_of_file+".txt") 
                                cfg45 = open(completeName , "w")
                                #sys.stdout = open('running.txt','w')
                                k=1
                                q=0
                                
                                for Grid in range(0,GridLayer.GetFeatureCount()):
                                    if(Grid == k*col-1):
                                        k=k+1
                                        continue
                                    if(Grid == (row-1)*col):
                                        break

                                    GridFeat1 = GridLayer.GetFeature(int(Grid))
                                    GridGeom1 = GridFeat1.GetGeometryRef()
                                    GridList= list(GridGeom1.GetEnvelope())
                                    # print("Grid Points",GridList)
                                    # print
                                    WindLayer.SetSpatialFilter(GridGeom1)
                                    BuildingLayer.SetSpatialFilter(GridGeom1)
                                    
                                    
                                    for wind_line in range(0,WindLayer.GetFeatureCount()):

                                        maxx=0
                                        feature =  WindLayer.GetNextFeature()

                                        interWind = feature.GetGeometryRef()
                                        windLeft.append(feature.GetFID())
                                        for buildings in range(0,BuildingLayer.GetFeatureCount()):
                                             currentPolyFeat = BuildingLayer.GetNextFeature()
                                             currentPolyGeom = currentPolyFeat.GetGeometryRef()

                                             FirstIntersect =interWind.Intersection(currentPolyGeom)
                                             if FirstIntersect != None and FirstIntersect.IsEmpty()==False:
                                                abc = list(FirstIntersect.GetEnvelope())

                                                
                                                # if ((GridList[0] > abc[0] or GridList[1] < abc[0]) and (GridList[1]< abc[1] or GridList[0]> abc[1])) and ((GridList[2] < abc[2] or GridList[3] > abc[2]) and (GridList[3]> abc[3] or GridList[2]< abc[3])):
                                                   
                                                #    continue
                                             # if ( (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[3] < GridList[2]) and (abc[3] > GridList[3]))) or (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[2] < GridList[2]) and (abc[2] > GridList[3]))) ):                            
                                                if ( (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                                    curmaxOfLine = currentPolyFeat.GetField("Height")
                                                    if(curmaxOfLine > maxx):
                                                        maxx = curmaxOfLine
                                        ListLeft.append(maxx)
                                        
                                        BuildingLayer.ResetReading()
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                    WindLayer.ResetReading()
                                    BuildingLayer.ResetReading()

                                    
                                    
                                    # print ("ListLeft",ListLeft)
                                  
                                        

                                    GridFeat2 = GridLayer.GetFeature(int(Grid+1))
                                    GridGeom2 = GridFeat2.GetGeometryRef()
                                    GridList= list(GridGeom2.GetEnvelope())
                                    WindLayer.SetSpatialFilter(GridGeom2)
                                    BuildingLayer.SetSpatialFilter(GridGeom2)
                                    for wind_line in range(0,WindLayer.GetFeatureCount()):  
                                        maxx = 0
                                        feature = WindLayer.GetNextFeature() 
                                        # print("windline no . ",feature.GetFID())
                                        interWind = feature.GetGeometryRef()                 
                                        windRight.append(feature.GetFID())
                                        for buildings in range(0,BuildingLayer.GetFeatureCount()):
                                             currentPolyFeat = BuildingLayer.GetNextFeature()
                                             # print("Building is . ",currentPolyFeat.GetField('Id'))
                                             currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                             FirstIntersect = interWind.Intersection(currentPolyGeom)
                                             if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                                                abc = list(FirstIntersect.GetEnvelope())
                                                # print("Wind intersect ",abc)
                                                # if ((GridList[0] > abc[0] or GridList[1] < abc[0]) and (GridList[1]< abc[1] or GridList[0]> abc[1])) and ((GridList[2] < abc[2] or GridList[3] > abc[2]) and (GridList[3]> abc[3] or GridList[2]< abc[3])):
                                                   
                                                #    continue
                                                if ( (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):                            
                                                    curmaxOfLine = currentPolyFeat.GetField("Height")
                                                    if(curmaxOfLine > maxx):
                                                        maxx = curmaxOfLine

                                        ListRight.append(maxx)
                                        BuildingLayer.ResetReading()
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                    WindLayer.ResetReading()
                                    BuildingLayer.ResetReading()
                                    # print ("ListRight",ListRight)


                                    GridFeat3 = GridLayer.GetFeature(int(Grid+col))
                                    GridGeom3 = GridFeat3.GetGeometryRef()
                                    GridList= list(GridGeom3.GetEnvelope())
                                    WindLayer.SetSpatialFilter(GridGeom3)
                                    BuildingLayer.SetSpatialFilter(GridGeom3)
                                    for wind_line in range(0,WindLayer.GetFeatureCount()):
                                        maxx = 0
                                        feature = WindLayer.GetNextFeature()  
                                        interWind = feature.GetGeometryRef()
                                        windBottomLeft.append(feature.GetFID())
                                      
                                        for buildings in range(0,BuildingLayer.GetFeatureCount()):
                                             currentPolyFeat = BuildingLayer.GetNextFeature()
                                                                       
                                             currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                             FirstIntersect = interWind.Intersection(currentPolyGeom)
                                             if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                                                abc = list(FirstIntersect.GetEnvelope())
                                                
                                                # if ((GridList[0] > abc[0] or GridList[1] < abc[0]) and (GridList[1]< abc[1] or GridList[0]> abc[1])) :
                                                   
                                                #    continue
                                                if ( (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                                    curmaxOfLine = currentPolyFeat.GetField("Height")
                                                    if(curmaxOfLine > maxx):
                                                        maxx = curmaxOfLine
                                        ListTop.append(maxx)
                                        BuildingLayer.ResetReading()
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                    WindLayer.ResetReading()
                                    BuildingLayer.ResetReading()
                                    # print ("ListBottomLeft",ListTop)

                                    GridFeat4 = GridLayer.GetFeature(int(Grid+col+1))
                                    GridGeom4 = GridFeat4.GetGeometryRef()
                                    GridList= list(GridGeom4.GetEnvelope())          
                                    WindLayer.SetSpatialFilter(GridGeom4)
                                    BuildingLayer.SetSpatialFilter(GridGeom4)
                                    for wind_line in range(0,WindLayer.GetFeatureCount()):
                                        maxx = 0
                                        feature = WindLayer.GetNextFeature()  
                                        interWind = feature.GetGeometryRef()
                                        windBottomRight.append(feature.GetFID())
                                        for buildings in range(0,BuildingLayer.GetFeatureCount()):
                                             currentPolyFeat = BuildingLayer.GetNextFeature()
                                             currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                             FirstIntersect = interWind.Intersection(currentPolyGeom)
                                             if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                                                abc = list(FirstIntersect.GetEnvelope())
                                                
                                                # if ((GridList[0] > abc[0] or GridList[1] < abc[0]) and (GridList[1]< abc[1] or GridList[0]> abc[1])) :
                                                   
                                                #    continue
                                                if ( (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                                    curmaxOfLine = currentPolyFeat.GetField("Height")
                                                    if(curmaxOfLine > maxx):
                                                        maxx = curmaxOfLine
                                        ListBottom.append(maxx)
                                        BuildingLayer.ResetReading()
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                    WindLayer.ResetReading()
                                    BuildingLayer.ResetReading()
                                    # print ("ListBottomRight",ListBottom)

                                    #for GridRight
                                    for i in range(0,len(windLeft)):
                                        for j in range(0,len(windRight)):
                                            if windLeft[i]==windRight[j]:
                                                if ListLeft[i]<ListRight[j]:
                                                    ListRight[j]= ListRight[j]-ListLeft[i]
                                                else:
                                                    ListRight[j]=0
                                    # print ("ListRight",ListRight)
                                    #GridBottomLeft
                                    for i in range(0,len(windLeft)):
                                        for j in range(0,len(windBottomLeft)):
                                            if windLeft[i]==windBottomLeft[j]:
                                                if ListTop[j]>ListLeft[i]:
                                                    ListTop[j]= ListTop[j]-ListLeft[i]
                                                else:
                                                    ListTop[j]=0
                                    # print ("ListBottomLeft",ListTop)
                                    #GridBottomRight
                                    for i in range(0,len(windRight)):
                                        for j in range(0,len(windBottomRight)):
                                            if windRight[i]==windBottomRight[j]:
                                                if ListBottom[j]>ListRight[i]:
                                                    ListBottom[j]= ListBottom[j]-ListRight[i]
                                                else:
                                                    ListBottom[j]=0
                                    # print ("ListBottomRight",ListBottom)


                                    for i in range(0,len(windBottomLeft)):
                                        for j in range(0,len(windBottomRight)):
                                            if windBottomLeft[i]==windBottomRight[j]:
                                                if ListTop[i]<ListBottom[j]:
                                                    ListBottom[j]= ListBottom[j]-ListTop[i]
                                                else:
                                                    ListBottom[j]=0
                                    # print ("ListBottomRight",ListBottom)
                                    
                                    if(listFrontalArea[Grid] == 0):
                                        listFrontalArea[Grid] = sum(ListLeft)* lineSpacing ;
                                    if(listFrontalArea[Grid+1] == 0):
                                        listFrontalArea[Grid+1] = sum(ListRight)* lineSpacing ;
                                    if(listFrontalArea[Grid+col] == 0):
                                        listFrontalArea[Grid+col] = sum(ListTop)* lineSpacing ;
                                    if(listFrontalArea[Grid+col+1] == 0):
                                        listFrontalArea[Grid+col+1] = sum(ListBottom)* lineSpacing ;

                                    
                                    del windLeft[:]
                                    del windRight[:]
                                    del windBottomRight[:]
                                    del windBottomLeft[:]


                                    del ListLeft[:]
                                    del ListRight[:]
                                    del ListTop[:]
                                    del ListBottom[:]
                                for i in range(0,len(listFrontalArea)):
                                    cfg45( "Frontal Area for Grid {0} is {1}\n ".format(i,listFrontalArea[i]))
                                    Grid_feature = GridLayer.GetFeature(i)
                                    
                                    Grid_feature.SetField(name,listFrontalArea[i])
                                    GridLayer.SetFeature(Grid_feature)
                                
                                # print "Answer List is"
                                # print listFrontalArea
                                cfg45.write ("The total frontal area is {0} \n".format(sum(listFrontalArea)))
                                # for gridFrontal in range(0,len(listFrontalArea)):
                                #     Grid_feature = GridLayer.GetFeature(gridFrontal)
                                    
                                #     Grid_feature.SetField('GridFA',listFrontalArea[gridFrontal])
                                #     GridLayer.SetFeature(Grid_feature)
                                cfg45.close()

            if  self.choice_3.isChecked()== True:
                Driver2 = ogr.GetDriverByName('ESRI Shapefile')
                poly = self.footprint_path
                polySource = Driver2.Open(poly,0)
                polyLayer = polySource.GetLayer()
                wind = self.wind_path
                windSource = Driver2.Open(wind,0)
                windLayer = windSource.GetLayer()
                spatialReference = polyLayer.GetSpatialRef()
                BuildLst = []
                lstPoints = []
                HWlst = []
                FrontalArea = 0
                HEIGHT = int(input("Supply the height value \n "))
                lineSpacing = self.reso_val
                for wind in range(0,windLayer.GetFeatureCount()):
                    frontalarea = 0
                    ptLst = []
                    PolyIntersectSeq = []
                    ptRefDict = {}
                    BuildingIntersectSeq = []
                    windFeature = windLayer.GetFeature(wind)
                    windGeometry = windFeature.GetGeometryRef()
                    IntersectPts = []
                    HeightLst = []
                    WidthLst = []
                    height = 0
                    IntersectPts = []
                    for currentPoly in range (0,polyLayer.GetFeatureCount()):
                        currentPolyFeat = polyLayer.GetFeature(currentPoly)
                        currentPolyGeom = currentPolyFeat.GetGeometryRef()
                        FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                        if FirstIntersect.IsEmpty() == False:
                            PolyIntersectSeq.append(currentPolyFeat.GetFID())
                            if FirstIntersect.GetGeometryName() == 'MULTILINESTRING':
                                pt1 = ()
                                pt2 = ()
                                PT1 =[]
                                PT2 = []
                                print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                                points = FirstIntersect.GetEnvelope()
                                count = len(points)
                                for i in range(0,count,2):
                                    pt1 = pt1 + (points[i],)
                                    pt2 = pt2 + (points[i+1],)
                                PT1.append(pt1)
                                PT2.append(pt2)
                                ptLst.append(PT1)
                                ptLst.append(PT2)
                
                            elif FirstIntersect.GetGeometryName() == 'LINESTRING':
                                print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                                Points = FirstIntersect.GetPoints()
                                ptLst.append(Points)
        
                    ptRefDict = dict(zip(PolyIntersectSeq,ptLst))                
                    ptSort = sorted(ptLst,key = operator.itemgetter(0),reverse = True)
                    print(ptSort)
                    if len(ptSort) > 0 and len(ptRefDict) > 0:
                        for k in range(0,len(ptSort)):
                            firstBuildingXY = ptSort[k]
                            for key in ptRefDict.keys():
                                if  firstBuildingXY == ptRefDict[key]:
                                    BuildingIntersectSeq.append(key)
                        print('Building Intersect Sequence is = ',BuildingIntersectSeq)
                    size = len(BuildingIntersectSeq)
                    if size == 1:
                        building = polyLayer.GetFeature(BuildingIntersectSeq[0])
                        Ht = building.GetField('Height')
                        if Ht > HEIGHT:
                            height = HEIGHT
                        elif Ht <= HEIGHT:
                            height = Ht
                        frontalarea = lineSpacing* height
                    elif size > 1 :
                        firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[0])
                        Ht1 = firstBuild.GetField('Height')
                        if Ht1 > HEIGHT:
                            height1 = HEIGHT
                        elif Ht1 <= HEIGHT:
                            height1 = Ht1
                        maxHeight = height1
                        frontalarea =  lineSpacing * height1
                        for building1 in range (1,size):
                            secondBuild = polyLayer.GetFeature(BuildingIntersectSeq[building1])
                            Ht2 = secondBuild.GetField('Height')
                            if Ht2 > HEIGHT:
                                height2 = HEIGHT
                            elif Ht2 <= HEIGHT:
                                height2 = Ht2
                            if height2>maxHeight:
                                effHeight = height2 - maxHeight
                                frontalarea =  frontalarea +(lineSpacing * effHeight)
                                MaxHeight = height2
                        print('\n The frontal area exposed to windline',windFeature.GetFID(),'is = ',frontalarea,'\n')
                    FrontalArea = FrontalArea + frontalarea
                print('\n The total frontal area of the study area is = ',FrontalArea)
                

        if self.Index_ == 3:
            if self.choice_1.isChecked()== True:
                            Driver = ogr.GetDriverByName('ESRI Shapefile')
                            Footprint = str(self.footprint_path)
                            polySource = Driver.Open(Footprint,0)
                            polyLayer = polySource.GetLayer()
                            wind = str(self.wind_path)
                            windSource = Driver.Open(wind,0)
                            windLayer = windSource.GetLayer()
                            output = self.output_path
                            FrontalArea = 0
                            name_of_file = 'Frontal Area 90 DEG'
                            completeName = os.path.join(output, name_of_file+".txt") 
                            cfa90 = open(completeName , "w")
                            #sys.stdout = open(output,'w')            
                            for wind in range(0,windLayer.GetFeatureCount()):
                                ptLst = []
                                PolyIntersectSeq = []
                                BuildingIntersectSeq = []
                                windFeature = windLayer.GetNextFeature()
                                windGeometry = windFeature.GetGeometryRef()
                                lineSpacing = self.reso_val
                                newGem = windGeometry.Buffer(lineSpacing);
                                # abc =  newGem.GetEnvelope()
                                polyLayer.SetSpatialFilter(newGem)
                                
                                for currentPoly in range (0,polyLayer.GetFeatureCount()):
                                    currentPolyFeat = polyLayer.GetNextFeature()
                                    currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                    FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                                    if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                                        PolyIntersectSeq.append(currentPolyFeat.GetFID())
                                        ptLst.append(FirstIntersect.GetPoints())
                                ptRefDict = dict(zip(PolyIntersectSeq,ptLst))
                                PtSort = sorted(ptLst)
                                if len(PtSort) > 0 and len(ptRefDict) > 0:
                                    cfa90.write ("*******************************************************\n")
                                    cfa90.write("WindLine \n".format(windFeature.GetFID()))
                                    cfa90.write("This is the list of buildings that the windline {0} intersects {1} \n".format(windFeature.GetFID(),PolyIntersectSeq))
                                    cfa90.write('This is the list of points that the windline {0} and building {1} intersects at {2}\n'.format(windFeature.GetFID(),currentPolyFeat.GetFID(),ptLst))        
                                    cfa90.write('This is the dictionary that has the keys as polygon and value as respective coordinate {0} \n'.format(ptRefDict))        
                                    cfa90.write('This is the list of intersection points sorted as the actually intersect {0} \n'.format(PtSort))
                                    for x in range(0,len(PtSort)):
                                        firstBuildingXY = PtSort[x]
                                        for key in ptRefDict.keys():
                                            if ptRefDict[key] ==  firstBuildingXY:
                                                BuildingIntersectSeq.append(key)
                                    cfa90.write('This list contains the polygon FID in a order the windline {0} intersects buildings {1} \n'.format(windFeature.GetFID(),BuildingIntersectSeq))
                                    size = len(BuildingIntersectSeq)
                                    lineSpacing = self.reso_val
                                    if size <= 1:
                                        building = polyLayer.GetFeature(BuildingIntersectSeq[0])
                                        height = building.GetField('Height')
                                        frontalarea = lineSpacing * height
                                    elif size > 1 :

                                        firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[0])
                                        height1 = firstBuild.GetField('Height')
                                        MaxHeight=height1
                                        for building1 in range (1,size):
                                            firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[building1])
                                            height1 = firstBuild.GetField('Height')
                                            if(MaxHeight<height1):
                                                    MaxHeight= height1
                                        frontalarea= lineSpacing*MaxHeight   

                                         
                                    cfa90.write('The frontal area exposed to windline {0} is = {1}'.format(windFeature.GetFID(),frontalarea))
                                    FrontalArea = FrontalArea + frontalarea
                            cfa90.write('The total frontal area of the study area is = {0}'.format(FrontalArea))
                            polyLayer.SetSpatialFilter(None)
                            cfa90.close()

            if self.choice_2.isChecked()== True:
                                Driver1 = ogr.GetDriverByName('ESRI Shapefile')
                                Grid =str(self.grid_path)
                                # print(Grid)
                                GridSource = Driver1.Open(Grid,1)
                                GridLayer = GridSource.GetLayer()
                                length = GridLayer.GetFeatureCount()
                                frontalAreaList = list([0.0 for x in range(length)])
                                Footprint = str(self.footprint_path)
                                BuildingSource = Driver1.Open(Footprint,0)
                                BuildingLayer = BuildingSource.GetLayer()
                                wind = str(self.wind_path)
                                WindSource = Driver1.Open(wind,0)
                                output = str(self.output_path)
                                WindLayer = WindSource.GetLayer()
                                layer_defn = GridLayer.GetLayerDefn()
                                # new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
                                #new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
                                # GridLayer.CreateField(new_field)
                                GridLayer.CreateField(new_field)
                                FrontalArea = 0
                                GridFrontalArea = []
                                length = GridLayer.GetFeatureCount()
                                GridFeat = GridLayer.GetFeature(0)
                                GridGeom = GridFeat.GetGeometryRef()
                                list1 = GridLayer.GetExtent()
                                list2 = GridGeom.GetEnvelope()
                                noc = (list1[1]-list1[0])/(list2[1]-list2[0])
                                nor = (list1[3]-list1[2])/(list2[3]-list2[2])
                                i=0
                                height_list2 = []
                                height_list3 = [] 
                                height_list1 = [] 
                                text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for frontal area :')
                                if ok:
                                    name=str(text)
                                ldefn = GridLayer.GetLayerDefn()
                                sch= []
                                check=0
                                n=0
                                for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
                                    field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
                                    sch.append(field) 
                                n=0
                                for n in range(len(sch)):
                                   if(name==str(sch[n])):
                                       check=1
                                       print('Field Already exists')
                                if (check==0):
                                    new_field = ogr.FieldDefn(name, ogr.OFTReal)
                                    GridLayer.CreateField(new_field)
                                    print('New Field Created')
                                name_of_file = 'Frontal Area Grid 90 DEG'
                                completeName = os.path.join(output, name_of_file+".txt") 
                                cfg90 = open(completeName , "w")

                                for Grid in range(0,length):
                                    

                                    BuildingSeq = []
                                    WindSeq = []
                                    polyIntersectSeq = []   
                                    polySeq = []
                                    GridFeat = GridLayer.GetNextFeature()
                                    # print "Grid id "
                                    # print GridFeat.GetField('ID')
                                    GridGeom = GridFeat.GetGeometryRef()
                                    # print('The Building intersection and WindLine intersection sequence in the grid ',GridFeat.GetFID(),'is')
                                    BuildingLayer.SetSpatialFilter(GridGeom)
                                    WindLayer.SetSpatialFilter(GridGeom)
                                    GridList= list(GridGeom.GetEnvelope())
                        
                                    lineSpacing = self.reso_val
                                    
                                    for line in range(0,WindLayer.GetFeatureCount()):
                                         
                                        windFeature = WindLayer.GetNextFeature()
                                        windGeometry = windFeature.GetGeometryRef()
                                        # newGem = windGeometry.Buffer(lineSpacing);
                                      
                                        # # abc =  newGem.GetEnvelope()
                                        # BuildingLayer.SetSpatialFilter(newGem)
                                        for poly in range(0,BuildingLayer.GetFeatureCount()):
                                            polyFeature = BuildingLayer.GetNextFeature()
                                            if not polyFeature:
                                                continue
                                            polyGeom = polyFeature.GetGeometryRef()
                                            Intersect = windGeometry.Intersection(polyGeom)
                                            if Intersect.IsEmpty()==False:
                                                abc = list(Intersect.GetEnvelope())
                                                if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                                                    height_list1.append(polyFeature.GetField('Height'))
                                        BuildingLayer.ResetReading()
                                        
                                        if height_list1:
                                            m = max(height_list1)
                                        else:
                                            m=0  
                                                             
                                        height_list2.append(m)
                                        del height_list1[:]
                                    
                                    for x in range(0,len(height_list2)):
                                        if len(height_list3) == 0:
                                            FrontalArea = FrontalArea+ lineSpacing*(height_list2[x])
                                          

                                        else:
                                            
                                            if (height_list2[x]-height_list3[x])>0:
                                                k = height_list2[x]-height_list3[x]
                                                
                                            else:
                                                k=0
                                            FrontalArea= FrontalArea+ lineSpacing*(k)
                                    # print height_list2
                                    # print height_list3
                                    cfg90.write("The Frontal area for Grid {0} is {1}\n" .format(GridFeat.GetField('ID'),FrontalArea))
                                    frontalAreaList[GridFeat.GetFID()] = FrontalArea
                                    GridFeat.SetField(name,FrontalArea)
                                    GridLayer.SetFeature(GridFeat)
                                    FrontalArea=0
                                    i+=1 
                                    if(i>=noc):
                                        del height_list3[:]
                                        del height_list2[:]
                                        i=0
                                        
                                    else:
                                        del height_list3[:]
                                        height_list3= list(height_list2) 
                                        del height_list2[:]
                                        
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                cfg90.close()
                    
            if self.choice_3.isChecked() == True:
                Driver2 = ogr.GetDriverByName('ESRI Shapefile')
                poly = self.footprint_path
                polySource = Driver2.Open(poly,0)
                polyLayer = polySource.GetLayer()
                wind = self.wind_path
                windSource = Driver2.Open(wind,0)
                windLayer = windSource.GetLayer()
                spatialReference = polyLayer.GetSpatialRef()
                BuildLst = []
                lstPoints = []
                HWlst = []
                FrontalArea = 0
                HEIGHT = int(input("Supply the height value \n "))
                lineSpacing = self.reso_val
                for wind in range(0,windLayer.GetFeatureCount()):
                    frontalarea = 0
                    ptLst = []
                    PolyIntersectSeq = []
                    ptRefDict = {}
                    BuildingIntersectSeq = []
                    windFeature = windLayer.GetFeature(wind)
                    windGeometry = windFeature.GetGeometryRef()
                    IntersectPts = []
                    HeightLst = []
                    WidthLst = []
                    height = 0
                    IntersectPts = []
                    for currentPoly in range (0,polyLayer.GetFeatureCount()):
                        currentPolyFeat = polyLayer.GetFeature(currentPoly)
                        currentPolyGeom = currentPolyFeat.GetGeometryRef()
                        FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                        if FirstIntersect.IsEmpty() == False:
                            PolyIntersectSeq.append(currentPolyFeat.GetFID())
                            if FirstIntersect.GetGeometryName() == 'MULTILINESTRING':
                                pt1 = ()
                                pt2 = ()
                                PT1 =[]
                                PT2 = []
                                print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                                points = FirstIntersect.GetEnvelope()
                                count = len(points)
                                for i in range(0,count,2):
                                    pt1 = pt1 + (points[i],)
                                    pt2 = pt2 + (points[i+1],)
                                PT1.append(pt1)
                                PT2.append(pt2)
                                ptLst.append(PT1)
                                ptLst.append(PT2)
                
                            elif FirstIntersect.GetGeometryName() == 'LINESTRING':
                                print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                                Points = FirstIntersect.GetPoints()
                                ptLst.append(Points)
        
                    ptRefDict = dict(zip(PolyIntersectSeq,ptLst))                
                    ptSort = sorted(ptLst,key = operator.itemgetter(0),reverse = True)
                    print(ptSort)
                    if len(ptSort) > 0 and len(ptRefDict) > 0:
                        for k in range(0,len(ptSort)):
                            firstBuildingXY = ptSort[k]
                            for key in ptRefDict.keys():
                                if  firstBuildingXY == ptRefDict[key]:
                                    BuildingIntersectSeq.append(key)
                        print('Building Intersect Sequence is = ',BuildingIntersectSeq)
                    size = len(BuildingIntersectSeq)
                    if size == 1:
                        building = polyLayer.GetFeature(BuildingIntersectSeq[0])
                        Ht = building.GetField('Height')
                        if Ht > HEIGHT:
                            height = HEIGHT
                        elif Ht <= HEIGHT:
                            height = Ht
                        frontalarea = lineSpacing* height
                    elif size > 1 :
                        firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[0])
                        Ht1 = firstBuild.GetField('Height')
                        if Ht1 > HEIGHT:
                            height1 = HEIGHT
                        elif Ht1 <= HEIGHT:
                            height1 = Ht1
                        maxHeight = height1
                        frontalarea =  lineSpacing * height1
                        for building1 in range (1,size):
                            secondBuild = polyLayer.GetFeature(BuildingIntersectSeq[building1])
                            Ht2 = secondBuild.GetField('Height')
                            if Ht2 > HEIGHT:
                                height2 = HEIGHT
                            elif Ht2 <= HEIGHT:
                                height2 = Ht2
                            if height2>maxHeight:
                                effHeight = height2 - maxHeight
                                frontalarea =  frontalarea +(lineSpacing * effHeight)
                                MaxHeight = height2
                        print('\n The frontal area exposed to windline',windFeature.GetFID(),'is = ',frontalarea,'\n')
                    FrontalArea = FrontalArea + frontalarea
                print('\n The total frontal area of the study area is = ',FrontalArea)
                
        if self.Index_ == 4:
            if self.choice_1.isChecked()== True:
                Driver = ogr.GetDriverByName('ESRI Shapefile')
                Footprint = str(self.footprint_path)
                polySource = Driver.Open(Footprint,0)
                polyLayer = polySource.GetLayer()
                wind = str(self.wind_path)
                windSource = Driver.Open(wind,0)
                windLayer = windSource.GetLayer()
                output = self.output_path
                FrontalArea = 0
                name_of_file = 'Frontal Area 135 DEG'
                completeName = os.path.join(output, name_of_file+".txt") 
                cfa135 = open(completeName , "w")
               #sys.stdout = open(output,'w')            
                for wind in range(0,windLayer.GetFeatureCount()):
                    ptLst = []
                    PolyIntersectSeq = []
                    BuildingIntersectSeq = []
                    windFeature = windLayer.GetNextFeature()
                    windGeometry = windFeature.GetGeometryRef()
                    lineSpacing = self.reso_val
                    newGem = windGeometry.Buffer(lineSpacing);
                    # abc =  newGem.GetEnvelope()
                    polyLayer.SetSpatialFilter(newGem)
                    
                    
                    
                    for currentPoly in range (0,polyLayer.GetFeatureCount()):
                        currentPolyFeat = polyLayer.GetNextFeature()
                        currentPolyGeom = currentPolyFeat.GetGeometryRef()
                        FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                        if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                            PolyIntersectSeq.append(currentPolyFeat.GetFID())
                            ptLst.append(FirstIntersect.GetPoints())
                    ptRefDict = dict(zip(PolyIntersectSeq,ptLst))
                    PtSort = sorted(ptLst)
                    if len(PtSort) > 0 and len(ptRefDict) > 0:
                        cfa0.write ("*******************************************************\n")
                        cfa135.write("WindLine \n".format(windFeature.GetFID()))
                        cfa135.write("This is the list of buildings that the windline {0} intersects {1} \n".format(windFeature.GetFID(),PolyIntersectSeq))
                        cfa135.write('This is the list of points that the windline {0} and building {1} intersects at {2}\n'.format(windFeature.GetFID(),currentPolyFeat.GetFID(),ptLst))        
                        cfa135.write('This is the dictionary that has the keys as polygon and value as respective coordinate {0} \n'.format(ptRefDict))        
                        cfa135.write('This is the list of intersection points sorted as the actually intersect {0} \n'.format(PtSort))
                        for x in range(0,len(PtSort)):
                            firstBuildingXY = PtSort[x]
                            for key in ptRefDict.keys():
                                if ptRefDict[key] ==  firstBuildingXY:
                                    BuildingIntersectSeq.append(key)
                        cfa135.write('This list contains the polygon FID in a order the windline {0} intersects buildings {1} \n'.format(windFeature.GetFID(),BuildingIntersectSeq))
                        size = len(BuildingIntersectSeq)
                        lineSpacing = self.reso_val
                        if size <= 1:
                            building = polyLayer.GetFeature(BuildingIntersectSeq[0])
                            height = building.GetField('Height')
                            frontalarea = lineSpacing * height
                        elif size > 1 :

                            firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[0])
                            height1 = firstBuild.GetField('Height')
                            MaxHeight=height1
                            for building1 in range (1,size):
                                firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[building1])
                                height1 = firstBuild.GetField('Height')
                                if(MaxHeight<height1):
                                        MaxHeight= height1
                            frontalarea= lineSpacing*MaxHeight   

                        cfa135.write('The frontal area exposed to windline {0} is = {1}'.format(windFeature.GetFID(),frontalarea))
                        FrontalArea = FrontalArea + frontalarea
                cfa135.write('The total frontal area of the study area is = {0}'.format(FrontalArea))
                polyLayer.SetSpatialFilter(None)
                cfa135.close()


            if self.choice_2.isChecked()== True:
                                Driver1 = ogr.GetDriverByName('ESRI Shapefile')
                                Grid =str(self.grid_path)
                                GridSource = Driver1.Open(Grid,1)
                                GridLayer = GridSource.GetLayer()
                                Footprint = str(self.footprint_path)
                                BuildingSource = Driver1.Open(Footprint,0)
                                BuildingLayer = BuildingSource.GetLayer()
                                wind = str(self.wind_path)
                                WindSource = Driver1.Open(wind,0)
                                WindLayer = WindSource.GetLayer()
                                layer_defn = GridLayer.GetLayerDefn()
                                # new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
                                output = str(self.output_path)
                                #new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
                                # GridLayer.CreateField(new_field)
                                text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for frontal area :')
                                if ok:
                                    name=str(text)
                                ldefn = GridLayer.GetLayerDefn()
                                sch= []
                                check=0
                                n=0
                                for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
                                    field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
                                    sch.append(field) 
                                n=0
                                for n in range(len(sch)):
                                   if(name==str(sch[n])):
                                       check=1
                                       print('Field Already exists')
                                if (check==0):
                                    new_field = ogr.FieldDefn(name, ogr.OFTReal)
                                    GridLayer.CreateField(new_field)
                                    print('New Field Created')
                                GridLayer.CreateField(new_field)
                                FrontalArea = 0
                                GridFrontalArea = []
                                length = GridLayer.GetFeatureCount()
                                lineSpacing= self.reso_val
                                ListTop = []
                                ListBottom = []
                                ListRight = []
                                ListLeft = []
                                windLeft = []
                                windRight = []
                                windBottomLeft = []
                                windBottomRight = []

                                GridFeat =  GridLayer.GetFeature(0)

                                GridGeom = GridFeat.GetGeometryRef()
                                list1 = GridLayer.GetExtent()
                                list2 = GridGeom.GetEnvelope()
                                col = int((list1[1]-list1[0])/(list2[1]-list2[0]))
                                row = int((list1[3]-list1[2])/(list2[3]-list2[2]))
                                # print "COl"
                                # print col
                                # print "row"
                                # print row
                                name_of_file = 'Frontal Area Grid 135 DEG'
                                completeName = os.path.join(output, name_of_file+".txt") 
                                cfg135 = open(completeName , "w")
                                k=row
                                q=0
                                t= (row-1) *col
                                listFrontalArea = list([0.0 for x in range(int(col*row))])
                                for Grid in range(0,GridLayer.GetFeatureCount()):
                                    if(t == (k*col) -1):
                                        k=k-1
                                        t= t- (col+row-1)
                                        continue
                                    if(k == 1):
                                        break
                                    GridFeat1 = GridLayer.GetFeature(t)
                                    # print("left : ",GridFeat1.GetField('Id'))
                                    GridGeom1 = GridFeat1.GetGeometryRef()
                                    GridList= list(GridGeom1.GetEnvelope())
                                    WindLayer.SetSpatialFilter(GridGeom1)
                                    BuildingLayer.SetSpatialFilter(GridGeom1)
                                    
                                    for wind_line in range(0,WindLayer.GetFeatureCount()):
                                        maxx=0
                                        feature =  WindLayer.GetNextFeature() 
                                        interWind = feature.GetGeometryRef() 
                                        windLeft.append(feature.GetFID())
                                        for buildings in range(0,BuildingLayer.GetFeatureCount()):
                                             currentPolyFeat = BuildingLayer.GetNextFeature()
                                             currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                             FirstIntersect =interWind.Intersection(currentPolyGeom)
                                             if FirstIntersect != None and FirstIntersect.IsEmpty()==False:
                                                 abc = list(FirstIntersect.GetEnvelope())
                                                 # print "List is ",abc
                                                 
                                                 if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                                        
                                                            curmaxOfLine = currentPolyFeat.GetField("Height")
                                                            # print "cur max ",curmaxOfLine
                                                            if(curmaxOfLine >= maxx):
                                                                  maxx = curmaxOfLine
                                        ListLeft.append(maxx)

                                        
                                        BuildingLayer.ResetReading()
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                    WindLayer.ResetReading()
                                    BuildingLayer.ResetReading()
                                    # print ("ListLeft",ListLeft)
                                    
                                        

                                    GridFeat2 = GridLayer.GetFeature(int(t+1))
                                    GridGeom2 = GridFeat2.GetGeometryRef()
                                    GridList= list(GridGeom2.GetEnvelope())
                                    # print(GridFeat2.GetField('Id'))
                                    WindLayer.SetSpatialFilter(GridGeom2)
                                    BuildingLayer.SetSpatialFilter(GridGeom2)
                                    for wind_line in range(0,WindLayer.GetFeatureCount()):  
                                        maxx = 0
                                        feature = WindLayer.GetNextFeature() 
                                        interWind = feature.GetGeometryRef()                 
                                        windRight.append(feature.GetFID())
                                        for buildings in range(0,BuildingLayer.GetFeatureCount()):
                                             currentPolyFeat = BuildingLayer.GetNextFeature()
                                             currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                             FirstIntersect =interWind.Intersection(currentPolyGeom)
                                             if FirstIntersect != None and FirstIntersect.IsEmpty()==False:
                                                     abc = list(FirstIntersect.GetEnvelope())
                                                     if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                                        
                                                            curmaxOfLine = currentPolyFeat.GetField("Height")
                                                            # print "cur max ",curmaxOfLine
                                                            if(curmaxOfLine >= maxx):
                                                                  maxx = curmaxOfLine
                                        ListRight.append(maxx)
                                        BuildingLayer.ResetReading()
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                    WindLayer.ResetReading()
                                    BuildingLayer.ResetReading()
                                    


                                    GridFeat3 = GridLayer.GetFeature(int(t-col))
                                    GridGeom3 = GridFeat3.GetGeometryRef()
                                    GridList= list(GridGeom3.GetEnvelope())
                                    # print(GridFeat3.GetField('Id'))
                                    WindLayer.SetSpatialFilter(GridGeom3)
                                    BuildingLayer.SetSpatialFilter(GridGeom3)
                                    for wind_line in range(0,WindLayer.GetFeatureCount()):
                                        maxx = 0
                                        feature = WindLayer.GetNextFeature()  
                                        interWind = feature.GetGeometryRef()
                                        windBottomLeft.append(feature.GetFID())
                                      
                                        for buildings in range(0,BuildingLayer.GetFeatureCount()):
                                             currentPolyFeat = BuildingLayer.GetNextFeature()
                                                                       
                                             currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                             FirstIntersect =interWind.Intersection(currentPolyGeom)
                                             if FirstIntersect != None and FirstIntersect.IsEmpty()==False:
                                                     abc = list(FirstIntersect.GetEnvelope())
                                                     if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                                        
                                                            curmaxOfLine = currentPolyFeat.GetField("Height")
                                                            # print "cur max ",curmaxOfLine
                                                            if(curmaxOfLine >= maxx):
                                                                  maxx = curmaxOfLine
                                        ListTop.append(maxx)
                                        BuildingLayer.ResetReading()
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                    WindLayer.ResetReading()
                                    BuildingLayer.ResetReading()
                                    

                                    GridFeat4 = GridLayer.GetFeature(int(t-col+1))
                                    GridGeom4 = GridFeat4.GetGeometryRef()
                                    GridList= list(GridGeom4.GetEnvelope())  
                                    # print(GridFeat4.GetField('Id'))        
                                    WindLayer.SetSpatialFilter(GridGeom4)
                                    BuildingLayer.SetSpatialFilter(GridGeom4)
                                    for wind_line in range(0,WindLayer.GetFeatureCount()):
                                        maxx = 0
                                        feature = WindLayer.GetNextFeature()  
                                        interWind = feature.GetGeometryRef()
                                        windBottomRight.append(feature.GetFID())
                                        for buildings in range(0,BuildingLayer.GetFeatureCount()):
                                             currentPolyFeat = BuildingLayer.GetNextFeature()
                                             currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                             FirstIntersect =interWind.Intersection(currentPolyGeom)
                                             if FirstIntersect != None and FirstIntersect.IsEmpty()==False:
                                                     abc = list(FirstIntersect.GetEnvelope())
                                                     if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                                        
                                                            curmaxOfLine = currentPolyFeat.GetField("Height")
                                                            # print "cur max ",curmaxOfLine
                                                            if(curmaxOfLine >= maxx):
                                                                  maxx = curmaxOfLine
                                        ListBottom.append(maxx)
                                        BuildingLayer.ResetReading()
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                    WindLayer.ResetReading()
                                    BuildingLayer.ResetReading()
                                    
                                    # print 
                                    #for GridRight
                                    for i in range(0,len(windLeft)):
                                        for j in range(0,len(windRight)):
                                            if windLeft[i]==windRight[j]:
                                                if ListLeft[i]<ListRight[j]:
                                                    ListRight[j]= ListRight[j]-ListLeft[i]
                                                else:
                                                    ListRight[j]=0
                                    # print ("ListRight",ListRight)
                                    #GridBottomLeft
                                    for i in range(0,len(windLeft)):
                                        for j in range(0,len(windBottomLeft)):
                                            if windLeft[i]==windBottomLeft[j]:
                                                if ListTop[j]>ListLeft[i]:
                                                    ListTop[j]= ListTop[j]-ListLeft[i]
                                                else:
                                                    ListTop[j]=0
                                    # print ("Listtop",ListTop)
                                    for i in range(0,len(windRight)):
                                        for j in range(0,len(windBottomRight)):
                                            if windRight[i]==windBottomRight[j]:
                                                if ListBottom[j]>ListRight[i]:
                                                    ListBottom[j]= ListBottom[j]-ListRight[i]
                                                else:
                                                    ListBottom[j]=0
                                    

                                    for i in range(0,len(windBottomLeft)):
                                        for j in range(0,len(windBottomRight)):
                                            if windBottomLeft[i]==windBottomRight[j]:
                                                if ListTop[i]<ListBottom[j]:
                                                    ListBottom[j]= ListBottom[j]-ListTop[i]
                                                else:
                                                    ListBottom[j]=0
                                    # print ("ListBottomRight",ListBottom)
                                    if(listFrontalArea[t] == 0):
                                        listFrontalArea[t] = math.fsum(ListLeft)* lineSpacing ;
                                    if(listFrontalArea[t+1] == 0):
                                        listFrontalArea[t+1] = math.fsum(ListRight)* lineSpacing ;
                                    if(listFrontalArea[t-col] == 0):
                                        listFrontalArea[t-col] = sum(ListTop)* lineSpacing ;
                                    if(listFrontalArea[t-col+1] == 0):
                                        listFrontalArea[t-col+1] = sum(ListBottom)* lineSpacing ;

                                    t=t+1
                                    
                                    del windLeft[:]
                                    del windRight[:]
                                    del windBottomRight[:]
                                    del windBottomLeft[:]


                                    del ListLeft[:]  
                                    del ListRight[:]
                                    del ListTop[:]
                                    del ListBottom[:]
                                for i in range(0,len(listFrontalArea)):
                                    cfg135.write("Frontal Area Index for Grid {0} is {1} \n".format(i,listFrontalArea[i]))
                                    Grid_feature = GridLayer.GetFeature(i)
                                    
                                    Grid_feature.SetField('GridFA',listFrontalArea[i])
                                    GridLayer.SetFeature(Grid_feature) 
                                
                                # print "Answer List is"
                                # print listFrontalArea
                                cfg135.write("The total frontal area is {0} \n".format (sum(listFrontalArea)))
                                # for gridFrontal in range(0,len(listFrontalArea)):
                                cfg135.close()
                                    

            if self.choice_3.isChecked() == True:
                Driver2 = ogr.GetDriverByName('ESRI Shapefile')
                poly = self.footprint_path
                polySource = Driver2.Open(poly,0)
                polyLayer = polySource.GetLayer()
                wind = self.wind_path
                windSource = Driver2.Open(wind,0)
                windLayer = windSource.GetLayer()
                spatialReference = polyLayer.GetSpatialRef()
                BuildLst = []
                lstPoints = []
                HWlst = []
                FrontalArea = 0
                HEIGHT = int(input("Supply the height value \n "))
                lineSpacing = self.reso_val
                for wind in range(0,windLayer.GetFeatureCount()):
                    frontalarea = 0
                    ptLst = []
                    PolyIntersectSeq = []
                    ptRefDict = {}
                    BuildingIntersectSeq = []
                    windFeature = windLayer.GetFeature(wind)
                    windGeometry = windFeature.GetGeometryRef()
                    IntersectPts = []
                    HeightLst = []
                    WidthLst = []
                    height = 0
                    IntersectPts = []
                    for currentPoly in range (0,polyLayer.GetFeatureCount()):
                        currentPolyFeat = polyLayer.GetFeature(currentPoly)
                        currentPolyGeom = currentPolyFeat.GetGeometryRef()
                        FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                        if FirstIntersect.IsEmpty() == False:
                            PolyIntersectSeq.append(currentPolyFeat.GetFID())
                            if FirstIntersect.GetGeometryName() == 'MULTILINESTRING':
                                pt1 = ()
                                pt2 = ()
                                PT1 =[]
                                PT2 = []
                                print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                                points = FirstIntersect.GetEnvelope()
                                count = len(points)
                                for i in range(0,count,2):
                                    pt1 = pt1 + (points[i],)
                                    pt2 = pt2 + (points[i+1],)
                                PT1.append(pt1)
                                PT2.append(pt2)
                                ptLst.append(PT1)
                                ptLst.append(PT2)
                
                            elif FirstIntersect.GetGeometryName() == 'LINESTRING':
                                print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                                Points = FirstIntersect.GetPoints()
                                ptLst.append(Points)
        
                    ptRefDict = dict(zip(PolyIntersectSeq,ptLst))                
                    ptSort = sorted(ptLst,key = operator.itemgetter(0),reverse = True)
                    print(ptSort)
                    if len(ptSort) > 0 and len(ptRefDict) > 0:
                        for k in range(0,len(ptSort)):
                            firstBuildingXY = ptSort[k]
                            for key in ptRefDict.keys():
                                if  firstBuildingXY == ptRefDict[key]:
                                    BuildingIntersectSeq.append(key)
                        print('Building Intersect Sequence is = ',BuildingIntersectSeq)
                    size = len(BuildingIntersectSeq)
                    if size == 1:
                        building = polyLayer.GetFeature(BuildingIntersectSeq[0])
                        Ht = building.GetField('Height')
                        if Ht > HEIGHT:
                            height = HEIGHT
                        elif Ht <= HEIGHT:
                            height = Ht
                        frontalarea = lineSpacing* height
                    elif size > 1 :
                        firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[0])
                        Ht1 = firstBuild.GetField('Height')
                        if Ht1 > HEIGHT:
                            height1 = HEIGHT
                        elif Ht1 <= HEIGHT:
                            height1 = Ht1
                        maxHeight = height1
                        frontalarea =  lineSpacing * height1
                        for building1 in range (1,size):
                            secondBuild = polyLayer.GetFeature(BuildingIntersectSeq[building1])
                            Ht2 = secondBuild.GetField('Height')
                            if Ht2 > HEIGHT:
                                height2 = HEIGHT
                            elif Ht2 <= HEIGHT:
                                height2 = Ht2
                            if height2>maxHeight:
                                effHeight = height2 - maxHeight
                                frontalarea =  frontalarea +(lineSpacing * effHeight)
                                MaxHeight = height2
                        print('\n The frontal area exposed to windline',windFeature.GetFID(),'is = ',frontalarea,'\n')
                    FrontalArea = FrontalArea + frontalarea
                print('\n The total frontal area of the study area is = ',FrontalArea)
                    
        if self.Index_ == 5:
            if self.choice_1.isChecked()== True:
                            Driver = ogr.GetDriverByName('ESRI Shapefile')
                            Footprint = str(self.footprint_path)
                            polySource = Driver.Open(Footprint,0)
                            polyLayer = polySource.GetLayer()
                            wind = str(self.wind_path)
                            windSource = Driver.Open(wind,0)
                            windLayer = windSource.GetLayer()
                            output = str(self.output_path)
                            FrontalArea = 0
                            name_of_file = 'Frontal Area 180 DEG'
                            completeName = os.path.join(output, name_of_file+".txt") 
                            cfa180 = open(completeName , "w")
                            #sys.stdout = open(output,'w')            
                            for wind in range(0,windLayer.GetFeatureCount()):
                                ptLst = []
                                PolyIntersectSeq = []
                                BuildingIntersectSeq = []
                                windFeature = windLayer.GetNextFeature()
                                windGeometry = windFeature.GetGeometryRef()
                                lineSpacing = self.reso_val
                                newGem = windGeometry.Buffer(lineSpacing);
                                # abc =  newGem.GetEnvelope()
                                polyLayer.SetSpatialFilter(newGem)
                                
                                
                                
                                for currentPoly in range (0,polyLayer.GetFeatureCount()):
                                    currentPolyFeat = polyLayer.GetNextFeature()
                                    currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                    FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                                    if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                                        PolyIntersectSeq.append(currentPolyFeat.GetFID())
                                        ptLst.append(FirstIntersect.GetPoints())
                                ptRefDict = dict(zip(PolyIntersectSeq,ptLst))
                                PtSort = sorted(ptLst)
                                if len(PtSort) > 0 and len(ptRefDict) > 0:
                                    cfa180.write ("*******************************************************\n")
                                    cfa180.write("WindLine \n".format(windFeature.GetFID()))
                                    cfa180.write("This is the list of buildings that the windline {0} intersects {1} \n".format(windFeature.GetFID(),PolyIntersectSeq))
                                    cfa180.write('This is the list of points that the windline {0} and building {1} intersects at {2}\n'.format(windFeature.GetFID(),currentPolyFeat.GetFID(),ptLst))        
                                    cfa180.write('This is the dictionary that has the keys as polygon and value as respective coordinate {0} \n'.format(ptRefDict))        
                                    cfa180.write('This is the list of intersection points sorted as the actually intersect {0} \n'.format(PtSort))
                                    for x in range(0,len(PtSort)):
                                        firstBuildingXY = PtSort[x]
                                        for key in ptRefDict.keys():
                                            if ptRefDict[key] ==  firstBuildingXY:
                                                BuildingIntersectSeq.append(key)
                                    cfa180.write('This list contains the polygon FID in a order the windline {0} intersects buildings {1} \n'.format(windFeature.GetFID(),BuildingIntersectSeq))
                                    size = len(BuildingIntersectSeq)
                                    lineSpacing = self.reso_val
                                    if size <= 1:
                                        building = polyLayer.GetFeature(BuildingIntersectSeq[0])
                                        height = building.GetField('Height')
                                        frontalarea = lineSpacing * height
                                    elif size > 1 :

                                        firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[0])
                                        height1 = firstBuild.GetField('Height')
                                        MaxHeight=height1
                                        for building1 in range (1,size):
                                            firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[building1])
                                            height1 = firstBuild.GetField('Height')
                                            if(MaxHeight<height1):
                                                    MaxHeight= height1
                                        frontalarea= lineSpacing*MaxHeight   

                                    cfa180.write('The frontal area exposed to windline {0} is = {1}'.format(windFeature.GetFID(),frontalarea))
                                    FrontalArea = FrontalArea + frontalarea
                            cfa180.write('The total frontal area of the study area is = {0}'.format(FrontalArea))
                            polyLayer.SetSpatialFilter(None)
                            cfa180.close()

            if self.choice_2.isChecked()== True:
                                Driver1 = ogr.GetDriverByName('ESRI Shapefile')
                                Grid =str(self.grid_path)
                                # print(Grid)
                                GridSource = Driver1.Open(Grid,1)
                                GridLayer = GridSource.GetLayer()
                                length = GridLayer.GetFeatureCount()
                                frontalAreaList = list([0.0 for x in range(length)])
                                Footprint = str(self.footprint_path)
                                BuildingSource = Driver1.Open(Footprint,0)
                                BuildingLayer = BuildingSource.GetLayer()
                                wind = str(self.wind_path)
                                WindSource = Driver1.Open(wind,0)
                                WindLayer = WindSource.GetLayer()
                                layer_defn = GridLayer.GetLayerDefn()
                                output = str(self.output_path)
                                # new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
                                #new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
                                # GridLayer.CreateField(new_field)
                                #GridLayer.CreateField(new_field)
                                FrontalArea = 0

                                GridFrontalArea = []
                                length = GridLayer.GetFeatureCount()
                                GridFeat = GridLayer.GetFeature(0)
                                GridGeom = GridFeat.GetGeometryRef()
                                list1 = GridLayer.GetExtent()
                                list2 = GridGeom.GetEnvelope()
                                noc = (list1[1]-list1[0])/(list2[1]-list2[0])
                                nor = (list1[3]-list1[2])/(list2[3]-list2[2])
                                i=0
                                f=0
                                l=1
                                k= (nor) * noc 
                                height_list2 = []
                                height_list3 = [] 
                                height_list1 = [] 
                                #sys.stdout = open('running.txt','w')
                                text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for frontal area :')
                                if ok:
                                    name=str(text)
                                ldefn = GridLayer.GetLayerDefn()
                                sch= []
                                check=0
                                n=0
                                for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
                                    field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
                                    sch.append(field) 
                                n=0
                                for n in range(len(sch)):
                                   if(name==str(sch[n])):
                                       check=1
                                       print('Field Already exists')
                                if (check==0):
                                    new_field = ogr.FieldDefn(name, ogr.OFTReal)
                                    GridLayer.CreateField(new_field)
                                    print('New Field Created')

                                name_of_file = 'Frontal Area Grid 180 DEG'
                                completeName = os.path.join(output, name_of_file+".txt") 
                                cfa180 = open(completeName , "w")
                                for Grid in range(0,length):
                                    

                                    BuildingSeq = []
                                    WindSeq = []
                                    polyIntersectSeq = []   
                                    polySeq = []
                                    
                                    if f<=nor-1:
                                        k=k-noc
                                        
                                   
                                    GridFeat = GridLayer.GetFeature(int(abs(k)))
                                   
                                    GridGeom = GridFeat.GetGeometryRef()
                                    GridList = list(GridGeom.GetEnvelope())
                                    BuildingLayer.SetSpatialFilter(GridGeom)
                                    WindLayer.SetSpatialFilter(GridGeom)

                        
                                    lineSpacing = self.reso_val
                                    
                                    for line in range(0,WindLayer.GetFeatureCount()):
                                         
                                        windFeature = WindLayer.GetNextFeature()
                                        windGeometry = windFeature.GetGeometryRef()
                                        
                                        
                                        for poly in range(0,BuildingLayer.GetFeatureCount()):
                                            polyFeature = BuildingLayer.GetNextFeature()
                                            if not polyFeature:
                                                continue
                                            polyGeom = polyFeature.GetGeometryRef()
                                            Intersect = windGeometry.Intersection(polyGeom)
                                            if Intersect.IsEmpty()==False:
                                                abc = list(Intersect.GetEnvelope())
                                                # print abc
                                                # print "Entering intersect"
                                                if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                                                
                                                    height_list1.append(polyFeature.GetField('height'))
                                           
                                        BuildingLayer.ResetReading()
                                        if height_list1:
                                            m = max(height_list1)
                                        else:
                                            m=0  
                                                     
                                        height_list2.append(m)
                                        del height_list1[:]
                                    
                                    for x in range(0,len(height_list2)):
                                        if len(height_list3) == 0:
                                            FrontalArea = FrontalArea+ lineSpacing*(height_list2[x])
                                           
                                            
                                        else:
                                        
                                            if (height_list2[x]-height_list3[x])>0:
                                                j = height_list2[x]-height_list3[x]
                                              
                                            else:
                                                j=0
                                            FrontalArea= FrontalArea+ lineSpacing*(j)
                                    # print "H2 is "
                                    # print height_list2
                                    # print "h3 is "
                                    # print height_list3
                                    cfg180.write("The Frontal area for Grid {0} is {1}\n" .format(GridFeat.GetField('ID'),FrontalArea))
                                    frontalAreaList[GridFeat.GetFID()] = FrontalArea
                                    GridFeat.SetField(name,FrontalArea)
                                    GridLayer.SetFeature(GridFeat)
                                    # print
                                    
                                    FrontalArea=0
                                    
                                    f+=1
                                    if(f > nor-1):
                                        del height_list3[:]
                                        del height_list2[:]
                                        f=1
                                        k=nor*noc -noc +l
                                        l=l+1
                                      
                                    else:
                                        del height_list3[:]
                                        height_list3= list(height_list2) 
                                        del height_list2[:]
                                       
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                cfg180.close()

            if self.choice_3.isChecked() == True:
                Driver2 = ogr.GetDriverByName('ESRI Shapefile')
                poly = self.footprint_path
                polySource = Driver2.Open(poly,0)
                polyLayer = polySource.GetLayer()
                wind = self.wind_path
                windSource = Driver2.Open(wind,0)
                windLayer = windSource.GetLayer()
                spatialReference = polyLayer.GetSpatialRef()
                BuildLst = []
                lstPoints = []
                HWlst = []
                FrontalArea = 0
                HEIGHT = int(input("Supply the height value \n "))
                lineSpacing = self.reso_val
                for wind in range(0,windLayer.GetFeatureCount()):
                    frontalarea = 0
                    ptLst = []
                    PolyIntersectSeq = []
                    ptRefDict = {}
                    BuildingIntersectSeq = []
                    windFeature = windLayer.GetFeature(wind)
                    windGeometry = windFeature.GetGeometryRef()
                    IntersectPts = []
                    HeightLst = []
                    WidthLst = []
                    height = 0
                    IntersectPts = []
                    for currentPoly in range (0,polyLayer.GetFeatureCount()):
                        currentPolyFeat = polyLayer.GetFeature(currentPoly)
                        currentPolyGeom = currentPolyFeat.GetGeometryRef()
                        FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                        if FirstIntersect.IsEmpty() == False:
                            PolyIntersectSeq.append(currentPolyFeat.GetFID())
                            if FirstIntersect.GetGeometryName() == 'MULTILINESTRING':
                                pt1 = ()
                                pt2 = ()
                                PT1 =[]
                                PT2 = []
                                print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                                points = FirstIntersect.GetEnvelope()
                                count = len(points)
                                for i in range(0,count,2):
                                    pt1 = pt1 + (points[i],)
                                    pt2 = pt2 + (points[i+1],)
                                PT1.append(pt1)
                                PT2.append(pt2)
                                ptLst.append(PT1)
                                ptLst.append(PT2)
                
                            elif FirstIntersect.GetGeometryName() == 'LINESTRING':
                                print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                                Points = FirstIntersect.GetPoints()
                                ptLst.append(Points)
        
                    ptRefDict = dict(zip(PolyIntersectSeq,ptLst))                
                    ptSort = sorted(ptLst,key = operator.itemgetter(0),reverse = True)
                    print(ptSort)
                    if len(ptSort) > 0 and len(ptRefDict) > 0:
                        for k in range(0,len(ptSort)):
                            firstBuildingXY = ptSort[k]
                            for key in ptRefDict.keys():
                                if  firstBuildingXY == ptRefDict[key]:
                                    BuildingIntersectSeq.append(key)
                        print('Building Intersect Sequence is = ',BuildingIntersectSeq)
                    size = len(BuildingIntersectSeq)
                    if size == 1:
                        building = polyLayer.GetFeature(BuildingIntersectSeq[0])
                        Ht = building.GetField('Height')
                        if Ht > HEIGHT:
                            height = HEIGHT
                        elif Ht <= HEIGHT:
                            height = Ht
                        frontalarea = lineSpacing* height
                    elif size > 1 :
                        firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[0])
                        Ht1 = firstBuild.GetField('Height')
                        if Ht1 > HEIGHT:
                            height1 = HEIGHT
                        elif Ht1 <= HEIGHT:
                            height1 = Ht1
                        maxHeight = height1
                        frontalarea =  lineSpacing * height1
                        for building1 in range (1,size):
                            secondBuild = polyLayer.GetFeature(BuildingIntersectSeq[building1])
                            Ht2 = secondBuild.GetField('Height')
                            if Ht2 > HEIGHT:
                                height2 = HEIGHT
                            elif Ht2 <= HEIGHT:
                                height2 = Ht2
                            if height2>maxHeight:
                                effHeight = height2 - maxHeight
                                frontalarea =  frontalarea +(lineSpacing * effHeight)
                                MaxHeight = height2
                        print('\n The frontal area exposed to windline',windFeature.GetFID(),'is = ',frontalarea,'\n')
                    FrontalArea = FrontalArea + frontalarea
                print('\n The total frontal area of the study area is = ',FrontalArea)
        
                
        if self.Index_ == 6:
            
            if self.choice_1.isChecked()== True:
                            Driver = ogr.GetDriverByName('ESRI Shapefile')
                            Footprint = str(self.footprint_path)
                            polySource = Driver.Open(Footprint,0)
                            polyLayer = polySource.GetLayer()
                            wind = str(self.wind_path)
                            windSource = Driver.Open(wind,0)
                            windLayer = windSource.GetLayer()
                            output = self.output_path
                            FrontalArea = 0
                            name_of_file = 'Frontal Area 225 DEG'
                            completeName = os.path.join(output, name_of_file+".txt") 
                            cfa225 = open(completeName , "w")
                            #sys.stdout = open(output,'w')            
                            for wind in range(0,windLayer.GetFeatureCount()):
                                ptLst = []
                                PolyIntersectSeq = []
                                BuildingIntersectSeq = []
                                windFeature = windLayer.GetNextFeature()
                                windGeometry = windFeature.GetGeometryRef()
                                lineSpacing = self.reso_val
                                newGem = windGeometry.Buffer(lineSpacing);
                                # abc =  newGem.GetEnvelope()
                                polyLayer.SetSpatialFilter(newGem)
                                
                                
                                
                                for currentPoly in range (0,polyLayer.GetFeatureCount()):
                                    currentPolyFeat = polyLayer.GetNextFeature()
                                    currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                    FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                                    if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                                        PolyIntersectSeq.append(currentPolyFeat.GetFID())
                                        ptLst.append(FirstIntersect.GetPoints())
                                ptRefDict = dict(zip(PolyIntersectSeq,ptLst))
                                PtSort = sorted(ptLst)
                                if len(PtSort) > 0 and len(ptRefDict) > 0:
                                    cfa225.write ("*******************************************************\n")
                                    cfa225.write("WindLine \n".format(windFeature.GetFID()))
                                    cfa225.write("This is the list of buildings that the windline {0} intersects {1} \n".format(windFeature.GetFID(),PolyIntersectSeq))
                                    cfa225.write('This is the list of points that the windline {0} and building {1} intersects at {2}\n'.format(windFeature.GetFID(),currentPolyFeat.GetFID(),ptLst))        
                                    cfa225.write('This is the dictionary that has the keys as polygon and value as respective coordinate {0} \n'.format(ptRefDict))        
                                    cfa225.write('This is the list of intersection points sorted as the actually intersect {0} \n'.format(PtSort))
                                    for x in range(0,len(PtSort)):
                                        firstBuildingXY = PtSort[x]
                                        for key in ptRefDict.keys():
                                            if ptRefDict[key] ==  firstBuildingXY:
                                                BuildingIntersectSeq.append(key)
                                    cfa225.write('This list contains the polygon FID in a order the windline {0} intersects buildings {1} \n'.format(windFeature.GetFID(),BuildingIntersectSeq))
                                    size = len(BuildingIntersectSeq)
                                    lineSpacing = self.reso_val
                                    if size <= 1:
                                        building = polyLayer.GetFeature(BuildingIntersectSeq[0])
                                        height = building.GetField('Height')
                                        frontalarea = lineSpacing * height
                                    elif size > 1 :

                                        firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[0])
                                        height1 = firstBuild.GetField('Height')
                                        MaxHeight=height1
                                        for building1 in range (1,size):
                                            firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[building1])
                                            height1 = firstBuild.GetField('Height')
                                            if(MaxHeight<height1):
                                                    MaxHeight= height1
                                        frontalarea= lineSpacing*MaxHeight   

                                        
                                    cfa225.write('The frontal area exposed to windline {0} is = {1}'.format(windFeature.GetFID(),frontalarea))
                                    FrontalArea = FrontalArea + frontalarea
                            cfa225.write('The total frontal area of the study area is = {0}\n'.format(FrontalArea))
                            polyLayer.SetSpatialFilter(None)
                            cfa225.close()

            if self.choice_2.isChecked()== True:
                
                                Driver1 = ogr.GetDriverByName('ESRI Shapefile')
                                Grid =str(self.grid_path)
                                GridSource = Driver1.Open(Grid,1)
                                GridLayer = GridSource.GetLayer()
                                Footprint = str(self.footprint_path)
                                BuildingSource = Driver1.Open(Footprint,0)
                                BuildingLayer = BuildingSource.GetLayer()
                                wind = str(self.wind_path)
                                WindSource = Driver1.Open(wind,0)
                                WindLayer = WindSource.GetLayer()
                                output = str(self.output_path)
                                layer_defn = GridLayer.GetLayerDefn()
                                # new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
                                src = 'GridFA '+str(self.Wind_select.currentText())
                                #new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
                                #GridLayer.CreateField(new_field)
                                text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for frontal area :')
                                if ok:
                                    name=str(text)
                                ldefn = GridLayer.GetLayerDefn()
                                sch= []
                                check=0
                                n=0
                                for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
                                    field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
                                    sch.append(field) 
                                n=0
                                for n in range(len(sch)):
                                   if(name==str(sch[n])):
                                       check=1
                                       print('Field Already exists')
                                if (check==0):
                                    new_field = ogr.FieldDefn(name, ogr.OFTReal)
                                    GridLayer.CreateField(new_field)
                                    print('New Field Created')
                                FrontalArea = 0
                                GridFrontalArea = []
                                length = GridLayer.GetFeatureCount()
                                lineSpacing= self.reso_val
                                ListTop = []
                                ListBottom = []
                                ListRight = []
                                ListLeft = []
                                windLeft = []
                                windRight = []
                                windBottomLeft = []
                                windBottomRight = []

                                GridFeat =  GridLayer.GetFeature(0)

                                GridGeom = GridFeat.GetGeometryRef()
                                list1 = GridLayer.GetExtent()
                                list2 = GridGeom.GetEnvelope()
                                col = int((list1[1]-list1[0])/(list2[1]-list2[0]))
                                row = int((list1[3]-list1[2])/(list2[3]-list2[2]))
                                # print "COl"
                                # print col
                                # print "row"
                                # print row
                                #sys.stdout = open('running.txt','w')
                                name_of_file = 'Frontal Area 225 DEG'
                                completeName = os.path.join(output, name_of_file+".txt") 
                                cfa225 = open(completeName , "w")
                                k=row
                                q=0
                                t= (row *col)-1
                                listFrontalArea = list([0.0 for x in range(int(col*row))])
                                for Grid in range(0,GridLayer.GetFeatureCount()):
                                    if(t == (k*col) -col):
                                        k=k-1
                                        t= t-1
                                        continue
                                    if(k == 1):
                                        break
                                    GridFeat1 = GridLayer.GetFeature(t)
                                    GridGeom1 = GridFeat1.GetGeometryRef()
                                    GridList= list(GridGeom1.GetEnvelope())
                                    WindLayer.SetSpatialFilter(GridGeom1)
                                    BuildingLayer.SetSpatialFilter(GridGeom1)
                                    # print "Grid is ", GridFeat1.GetFID()
                                    for wind_line in range(0,WindLayer.GetFeatureCount()):
                                        maxx=0
                                        feature =  WindLayer.GetNextFeature() 
                                        interWind = feature.GetGeometryRef() 
                                        windLeft.append(feature.GetFID())
                                        for buildings in range(0,BuildingLayer.GetFeatureCount()):
                                             currentPolyFeat = BuildingLayer.GetNextFeature()
                                             currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                        #      FirstIntersect = interWind.Intersection(currentPolyGeom)
                                        #      if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                                        #            curmaxOfLine = currentPolyFeat.GetField("Height")
                                        #            if(curmaxOfLine > maxx):
                                        #                 maxx = curmaxOfLine
                                        # ListLeft.append(maxx)
                                             FirstIntersect =interWind.Intersection(currentPolyGeom)
                                             if FirstIntersect != None and FirstIntersect.IsEmpty()==False:
                                                    abc = list(FirstIntersect.GetEnvelope())
                                                    # print "List is ", abc
                                                    if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[3]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[2]<GridList[3] )):
                                                         
                                                      # if ( (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                                            curmaxOfLine = currentPolyFeat.GetField("Height")
                                                            # print "cur max ",curmaxOfLine
                                                            if(curmaxOfLine >= maxx):
                                                                  maxx = curmaxOfLine
                                        ListLeft.append(maxx)
                                        BuildingLayer.ResetReading()
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                    WindLayer.ResetReading()
                                    BuildingLayer.ResetReading()
                                    # print ("ListLeft",ListLeft)
                                    
                                        

                                    GridFeat2 = GridLayer.GetFeature(int(t-1))
                                    GridGeom2 = GridFeat2.GetGeometryRef()
                                    GridList= list(GridGeom2.GetEnvelope())
                                    WindLayer.SetSpatialFilter(GridGeom2)
                                    BuildingLayer.SetSpatialFilter(GridGeom2)
                                    for wind_line in range(0,WindLayer.GetFeatureCount()):  
                                        maxx = 0
                                        feature = WindLayer.GetNextFeature() 
                                        interWind = feature.GetGeometryRef()                 
                                        windRight.append(feature.GetFID())
                                        for buildings in range(0,BuildingLayer.GetFeatureCount()):
                                             currentPolyFeat = BuildingLayer.GetNextFeature()
                                             currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                             FirstIntersect = interWind.Intersection(currentPolyGeom)
                                             if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                                                    abc = list(FirstIntersect.GetEnvelope())
                                                    if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[3]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[2]<GridList[3] )):
                                                         
                                                      # if ( (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                                            curmaxOfLine = currentPolyFeat.GetField("Height")
                                                            # print "cur max ",curmaxOfLine
                                                            if(curmaxOfLine >= maxx):
                                                                  maxx = curmaxOfLine
                                        ListRight.append(maxx)
                                        BuildingLayer.ResetReading()
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                    WindLayer.ResetReading()
                                    BuildingLayer.ResetReading()
                                    # print ("ListRight",ListRight)


                                    GridFeat3 = GridLayer.GetFeature(int(t-col))
                                    GridGeom3 = GridFeat3.GetGeometryRef()
                                    GridList= list(GridGeom3.GetEnvelope())
                                    WindLayer.SetSpatialFilter(GridGeom3)
                                    BuildingLayer.SetSpatialFilter(GridGeom3)
                                    for wind_line in range(0,WindLayer.GetFeatureCount()):
                                        maxx = 0
                                        feature = WindLayer.GetNextFeature()  
                                        interWind = feature.GetGeometryRef()
                                        windBottomLeft.append(feature.GetFID())
                                      
                                        for buildings in range(0,BuildingLayer.GetFeatureCount()):
                                             currentPolyFeat = BuildingLayer.GetNextFeature()
                                                                       
                                             currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                             FirstIntersect = interWind.Intersection(currentPolyGeom)
                                             if FirstIntersect != None and FirstIntersect.IsEmpty() == False:

                                                    abc = list(FirstIntersect.GetEnvelope())
                                                    if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[3]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[2]<GridList[3] )):
                                                          
                                                      # if ( (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                                            curmaxOfLine = currentPolyFeat.GetField("Height")
                                                            # print "cur max ",curmaxOfLine
                                                            if(curmaxOfLine >= maxx):
                                                                  maxx = curmaxOfLine
                                        ListTop.append(maxx)
                                        BuildingLayer.ResetReading()
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                    WindLayer.ResetReading()
                                    BuildingLayer.ResetReading()
                                    # print ("ListBottomLeft",ListTop)

                                    GridFeat4 = GridLayer.GetFeature(int(t-col-1))
                                    GridGeom4 = GridFeat4.GetGeometryRef() 
                                    GridList= list(GridGeom4.GetEnvelope())         
                                    WindLayer.SetSpatialFilter(GridGeom4)
                                    BuildingLayer.SetSpatialFilter(GridGeom4)
                                    for wind_line in range(0,WindLayer.GetFeatureCount()):
                                        maxx = 0
                                        feature = WindLayer.GetNextFeature()  
                                        interWind = feature.GetGeometryRef()
                                        windBottomRight.append(feature.GetFID())
                                        for buildings in range(0,BuildingLayer.GetFeatureCount()):
                                             currentPolyFeat = BuildingLayer.GetNextFeature()
                                             currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                             FirstIntersect = interWind.Intersection(currentPolyGeom)
                                             if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                                                    abc = list(FirstIntersect.GetEnvelope())
                                                    if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[3]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[2]<GridList[3] )):
                                                          
                                                      # if ( (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                                            curmaxOfLine = currentPolyFeat.GetField("Height")
                                                            # print "cur max ",curmaxOfLine
                                                            if(curmaxOfLine >= maxx):
                                                                  maxx = curmaxOfLine
                                        ListBottom.append(maxx)
                                        BuildingLayer.ResetReading()
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                    WindLayer.ResetReading()
                                    BuildingLayer.ResetReading()
                                    # print ("ListBottomRight",ListBottom)

                                    #for GridRight
                                    for i in range(0,len(windLeft)):
                                        for j in range(0,len(windRight)):
                                            if windLeft[i]==windRight[j]:
                                                if ListLeft[i]<ListRight[j]:
                                                    ListRight[j]= ListRight[j]-ListLeft[i]
                                                else:
                                                    ListRight[j]=0
                                    # print ("ListRight",ListRight)
                                    #GridBottomLeft
                                    for i in range(0,len(windLeft)):
                                        for j in range(0,len(windBottomLeft)):
                                            if windLeft[i]==windBottomLeft[j]:
                                                if ListTop[j]>ListLeft[i]:
                                                    ListTop[j]= ListTop[j]-ListLeft[i]
                                                else:
                                                    ListTop[j]=0
                                    # print ("ListBottomLeft",ListTop)
                                    #GridBottomRight        
                                    for i in range(0,len(windRight)):   
                                        for j in range(0,len(windBottomRight)):
                                            if windRight[i]==windBottomRight[j]:
                                                if ListBottom[j]>ListRight[i]:
                                                    ListBottom[j]= ListBottom[j]-ListRight[i]
                                                else:
                                                    ListBottom[j]=0
                                    # print ("ListBottomRight",ListBottom)


                                    for i in range(0,len(windBottomLeft)):
                                        for j in range(0,len(windBottomRight)):
                                            if windBottomLeft[i]==windBottomRight[j]:
                                                if ListTop[i]<ListBottom[j]:
                                                    ListBottom[j]= ListBottom[j]-ListTop[i]
                                                else:
                                                    ListBottom[j]=0
                                    # print ("ListBottomRight",ListBottom)
                                    
                                    if(listFrontalArea[t] == 0):
                                        listFrontalArea[t] = sum(ListLeft)* lineSpacing ;
                                    if(listFrontalArea[t-1] == 0):
                                        listFrontalArea[t-1] = sum(ListRight)* lineSpacing ;
                                    if(listFrontalArea[t-col] == 0):
                                        listFrontalArea[t-col] = sum(ListTop)* lineSpacing ;
                                    if(listFrontalArea[t-col-1] == 0):
                                        listFrontalArea[t-col-1] = sum(ListBottom)* lineSpacing ;

                                    t=t-1
                                    
                                    del windLeft[:]
                                    del windRight[:]
                                    del windBottomRight[:]
                                    del windBottomLeft[:]


                                    del ListLeft[:]
                                    del ListRight[:]
                                    del ListTop[:]
                                    del ListBottom[:]
                                for i in range(0,len(listFrontalArea)):
                                    cfg225.write ("Frontal Area for Grid {0} is {1} \n".format(i,listFrontalArea[i]))
                                    Grid_feature = GridLayer.GetFeature(i)
                                    Grid_feature.SetField(name,listFrontalArea[i])
                                    GridLayer.SetFeature(Grid_feature)

                                
                                cfg225.write("The total frontal area is {0}" .format(sum(listFrontalArea)))
                                # for gridFrontal in range(0,len(listFrontalArea)):
                                #     Grid_feature = GridLayer.GetFeature(gridFrontal)
                                #     Grid_feature.SetField('GridFA',listFrontalArea[gridFrontal])
                                #     GridLayer.SetFeature(Grid_feature)
                                cfg225.close()
                                    

            if self.choice_3.isChecked() == True:
                Driver2 = ogr.GetDriverByName('ESRI Shapefile')
                poly = self.footprint_path
                polySource = Driver2.Open(poly,0)
                polyLayer = polySource.GetLayer()
                wind = self.wind_path
                windSource = Driver2.Open(wind,0)
                windLayer = windSource.GetLayer()
                spatialReference = polyLayer.GetSpatialRef()
                BuildLst = []
                lstPoints = []
                HWlst = []
                FrontalArea = 0
                HEIGHT = int(input("Supply the height value \n "))
                lineSpacing = self.reso_val
                for wind in range(0,windLayer.GetFeatureCount()):
                    frontalarea = 0
                    ptLst = []
                    PolyIntersectSeq = []
                    ptRefDict = {}
                    BuildingIntersectSeq = []
                    windFeature = windLayer.GetFeature(wind)
                    windGeometry = windFeature.GetGeometryRef()
                    IntersectPts = []
                    HeightLst = []
                    WidthLst = []
                    height = 0
                    IntersectPts = []
                    for currentPoly in range (0,polyLayer.GetFeatureCount()):
                        currentPolyFeat = polyLayer.GetFeature(currentPoly)
                        currentPolyGeom = currentPolyFeat.GetGeometryRef()
                        FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                        if FirstIntersect.IsEmpty() == False:
                            PolyIntersectSeq.append(currentPolyFeat.GetFID())
                            if FirstIntersect.GetGeometryName() == 'MULTILINESTRING':
                                pt1 = ()
                                pt2 = ()
                                PT1 =[]
                                PT2 = []
                                print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                                points = FirstIntersect.GetEnvelope()
                                count = len(points)
                                for i in range(0,count,2):
                                    pt1 = pt1 + (points[i],)
                                    pt2 = pt2 + (points[i+1],)
                                PT1.append(pt1)
                                PT2.append(pt2)
                                ptLst.append(PT1)
                                ptLst.append(PT2)
                
                            elif FirstIntersect.GetGeometryName() == 'LINESTRING':
                                print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                                Points = FirstIntersect.GetPoints()
                                ptLst.append(Points)
        
                    ptRefDict = dict(zip(PolyIntersectSeq,ptLst))                
                    ptSort = sorted(ptLst,key = operator.itemgetter(0))
                    print(ptSort)
                    if len(ptSort) > 0 and len(ptRefDict) > 0:
                        for k in range(0,len(ptSort)):
                            firstBuildingXY = ptSort[k]
                            for key in ptRefDict.keys():
                                if  firstBuildingXY == ptRefDict[key]:
                                    BuildingIntersectSeq.append(key)
                        print('Building Intersect Sequence is = ',BuildingIntersectSeq)
                    size = len(BuildingIntersectSeq)
                    if size == 1:
                        building = polyLayer.GetFeature(BuildingIntersectSeq[0])
                        Ht = building.GetField('Height')
                        if Ht > HEIGHT:
                            height = HEIGHT
                        elif Ht <= HEIGHT:
                            height = Ht
                        frontalarea = lineSpacing* height
                    elif size > 1 :
                        firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[0])
                        Ht1 = firstBuild.GetField('Height')
                        if Ht1 > HEIGHT:
                            height1 = HEIGHT
                        elif Ht1 <= HEIGHT:
                            height1 = Ht1
                        maxHeight = height1
                        frontalarea =  lineSpacing * height1
                        for building1 in range (1,size):
                            secondBuild = polyLayer.GetFeature(BuildingIntersectSeq[building1])
                            Ht2 = secondBuild.GetField('Height')
                            if Ht2 > HEIGHT:
                                height2 = HEIGHT
                            elif Ht2 <= HEIGHT:
                                height2 = Ht2
                            if height2>maxHeight:
                                effHeight = height2 - maxHeight
                                frontalarea =  frontalarea +(lineSpacing * effHeight)
                                MaxHeight = height2
                        print('\n The frontal area exposed to windline',windFeature.GetFID(),'is = ',frontalarea,'\n')
                    FrontalArea = FrontalArea + frontalarea
                print('\n The total frontal area of th estudy area is = ',FrontalArea)

        if self.Index_ == 7:
            
            if self.choice_1.isChecked()== True:
                            Driver = ogr.GetDriverByName('ESRI Shapefile')
                            Footprint = str(self.footprint_path)
                            polySource = Driver.Open(Footprint,0)
                            polyLayer = polySource.GetLayer()
                            wind = str(self.wind_path)
                            windSource = Driver.Open(wind,0)
                            windLayer = windSource.GetLayer()
                            output = str(self.output_path)
                            FrontalArea = 0
                            name_of_file = 'Frontal Area 270 DEG'
                            completeName = os.path.join(output, name_of_file+".txt") 
                            cfa270 = open(completeName , "w")
                            #sys.stdout = open(output,'w')            
                            for wind in range(0,windLayer.GetFeatureCount()):
                                ptLst = []
                                PolyIntersectSeq = []
                                BuildingIntersectSeq = []
                                windFeature = windLayer.GetNextFeature()
                                windGeometry = windFeature.GetGeometryRef()
                                lineSpacing = self.reso_val
                                newGem = windGeometry.Buffer(lineSpacing);
                                # abc =  newGem.GetEnvelope()
                                polyLayer.SetSpatialFilter(newGem)
                                
                                
                                
                                for currentPoly in range (0,polyLayer.GetFeatureCount()):
                                    currentPolyFeat = polyLayer.GetNextFeature()
                                    currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                    FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                                    if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                                        PolyIntersectSeq.append(currentPolyFeat.GetFID())
                                        ptLst.append(FirstIntersect.GetPoints())
                                ptRefDict = dict(zip(PolyIntersectSeq,ptLst))
                                PtSort = sorted(ptLst)
                                if len(PtSort) > 0 and len(ptRefDict) > 0:
                                    cfa270.write ("*******************************************************\n")
                                    cfa270.write("WindLine \n".format(windFeature.GetFID()))
                                    cfa270.write("This is the list of buildings that the windline {0} intersects {1} \n".format(windFeature.GetFID(),PolyIntersectSeq))
                                    cfa270.write('This is the list of points that the windline {0} and building {1} intersects at {2}\n'.format(windFeature.GetFID(),currentPolyFeat.GetFID(),ptLst))        
                                    cfa270.write('This is the dictionary that has the keys as polygon and value as respective coordinate {0} \n'.format(ptRefDict))        
                                    cfa270.write('This is the list of intersection points sorted as the actually intersect {0} \n'.format(PtSort))
                                    for x in range(0,len(PtSort)):
                                        firstBuildingXY = PtSort[x]
                                        for key in ptRefDict.keys():
                                            if ptRefDict[key] ==  firstBuildingXY:
                                                BuildingIntersectSeq.append(key)
                                    cfa270.write('This list contains the polygon FID in a order the windline {0} intersects buildings {1} \n'.format(windFeature.GetFID(),BuildingIntersectSeq))
                                    size = len(BuildingIntersectSeq)
                                    lineSpacing = self.reso_val
                                    if size <= 1:
                                        building = polyLayer.GetFeature(BuildingIntersectSeq[0])
                                        height = building.GetField('Height')
                                        frontalarea = lineSpacing * height
                                    elif size > 1 :

                                        firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[0])
                                        height1 = firstBuild.GetField('Height')
                                        MaxHeight=height1
                                        for building1 in range (1,size):
                                            firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[building1])
                                            height1 = firstBuild.GetField('Height')
                                            if(MaxHeight<height1):
                                                    MaxHeight= height1
                                        frontalarea= lineSpacing*MaxHeight   

                                           
                                    cfa270.write('The frontal area exposed to windline {0} is = {1}'.format(windFeature.GetFID(),frontalarea))
                                    FrontalArea = FrontalArea + frontalarea
                            cfa270.write('The total frontal area of the study area is = {0}\n'.format(FrontalArea))
                            polyLayer.SetSpatialFilter(None)
                            cfa270.close()

            if self.choice_2.isChecked()== True:
                
                                Driver1 = ogr.GetDriverByName('ESRI Shapefile')
                                Grid =str(self.grid_path)
                                # print(Grid)
                                GridSource = Driver1.Open(Grid,1)
                                GridLayer = GridSource.GetLayer()
                                length = GridLayer.GetFeatureCount()
                                frontalAreaList = list([0.0 for x in range(length)])
                                Footprint = str(self.footprint_path)
                                BuildingSource = Driver1.Open(Footprint,0)
                                BuildingLayer = BuildingSource.GetLayer()
                                wind = str(self.wind_path)
                                WindSource = Driver1.Open(wind,0)
                                WindLayer = WindSource.GetLayer()
                                layer_defn = GridLayer.GetLayerDefn()
                                output = str(self.output_path)
                                # new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
                                #new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
                                #GridLayer.CreateField(new_field)
                                text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for frontal area :')
                                if ok:
                                    name=str(text)
                                ldefn = GridLayer.GetLayerDefn()
                                sch= []
                                check=0
                                n=0
                                for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
                                    field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
                                    sch.append(field) 
                                n=0
                                for n in range(len(sch)):
                                   if(name==str(sch[n])):
                                       check=1
                                       print('Field Already exists')
                                if (check==0):
                                    new_field = ogr.FieldDefn(name, ogr.OFTReal)
                                    GridLayer.CreateField(new_field)
                                    print('New Field Created')                                
                                FrontalArea = 0
                                GridFrontalArea = []
                                length = GridLayer.GetFeatureCount()
                                GridFeat = GridLayer.GetFeature(0)
                                GridGeom = GridFeat.GetGeometryRef()
                                list1 = GridLayer.GetExtent()
                                list2 = GridGeom.GetEnvelope()
                                noc = (list1[1]-list1[0])/(list2[1]-list2[0])
                                nor = (list1[3]-list1[2])/(list2[3]-list2[2])
                                i=0
                                f=0
                                z=2
                                k=noc
                                height_list2 = []
                                height_list3 = [] 
                                height_list1 = [] 
                                #sys.stdout = open('running.txt','w')
                                name_of_file = 'Frontal Area Grid 270 DEG'
                                completeName = os.path.join(output, name_of_file+".txt") 
                                cfg270 = open(completeName , "w")

                                for Grid in range(0,length):
                                    

                                    BuildingSeq = []
                                    WindSeq = []
                                    polyIntersectSeq = []   
                                    polySeq = []
                                    if f<=noc-1:
                                        k=k-1
                                        
                                    else:
                                        k=(noc*z)-1
                                        z=z+1
                                        f=0
                                    
                                    GridFeat = GridLayer.GetFeature(int(abs(k)))
                                    
                                    GridGeom = GridFeat.GetGeometryRef()
                                    # print('The Building intersection and WindLine intersection sequence in the grid ',GridFeat.GetFID(),'is')
                                    BuildingLayer.SetSpatialFilter(GridGeom)
                                    WindLayer.SetSpatialFilter(GridGeom)
                                    GridList= list(GridGeom.GetEnvelope())                        
                                    lineSpacing = self.reso_val
                                    
                                    for line in range(0,WindLayer.GetFeatureCount()):
                                         
                                        windFeature = WindLayer.GetNextFeature()
                                        windGeometry = windFeature.GetGeometryRef()
                                       
                                        
                                        for poly in range(0,BuildingLayer.GetFeatureCount()):
                                            polyFeature = BuildingLayer.GetNextFeature()
                                            if not polyFeature:
                                                continue
                                            polyGeom = polyFeature.GetGeometryRef()
                                            Intersect = windGeometry.Intersection(polyGeom)
                                            if Intersect.IsEmpty()==False:
                                                abc = list(Intersect.GetEnvelope())
                                                if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                                                    height_list1.append(polyFeature.GetField('height'))
                                            
                                        BuildingLayer.ResetReading()
                                        if height_list1:
                                            m = max(height_list1)
                                        else:
                                            m=0  
                                                      
                                        height_list2.append(m)
                                        del height_list1[:]
                                    
                                    for x in range(0,len(height_list2)):
                                        if len(height_list3) == 0:
                                            FrontalArea = FrontalArea+ lineSpacing*(height_list2[x])
                                           

                                        else:
                                        
                                            if (height_list2[x]-height_list3[x])>0:
                                                j = height_list2[x]-height_list3[x]
                                             
                                            else:
                                                j=0
                                            FrontalArea= FrontalArea+ lineSpacing*(j)
                                    # print "H2 is "
                                    # print height_list2
                                    # print "h3 is "
                                    # print height_list3
                                    cfg90.write("The Frontal area for Grid {0} is {1}\n" .format(GridFeat.GetField('ID'),FrontalArea))
                                    frontalAreaList[GridFeat.GetFID()] = FrontalArea
                                    GridFeat.SetField(name,FrontalArea)
                                    GridLayer.SetFeature(GridFeat)
                                    # print
                                    FrontalArea=0
                                    i=i+1 
                                    f+=1
                                    if(i>=noc):
                                        del height_list3[:]
                                        del height_list2[:]
                                        i=0
                                        
                                    else:
                                        del height_list3[:]
                                        height_list3= list(height_list2) 
                                        del height_list2[:]
                                      
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                cfg270.close()

            if self.choice_3.isChecked() == True:
                Driver2 = ogr.GetDriverByName('ESRI Shapefile')
                poly = self.footprint_path
                polySource = Driver2.Open(poly,0)
                polyLayer = polySource.GetLayer()
                wind = self.wind_path
                windSource = Driver2.Open(wind,0)
                windLayer = windSource.GetLayer()
                spatialReference = polyLayer.GetSpatialRef()
                BuildLst = []
                lstPoints = []
                HWlst = []
                FrontalArea = 0
                HEIGHT = int(input("Supply the height value \n "))
                lineSpacing = self.reso_val
                for wind in range(0,windLayer.GetFeatureCount()):
                    frontalarea = 0
                    ptLst = []
                    PolyIntersectSeq = []
                    ptRefDict = {}
                    BuildingIntersectSeq = []
                    windFeature = windLayer.GetFeature(wind)
                    windGeometry = windFeature.GetGeometryRef()
                    IntersectPts = []
                    HeightLst = []
                    WidthLst = []
                    height = 0
                    IntersectPts = []
                    for currentPoly in range (0,polyLayer.GetFeatureCount()):
                        currentPolyFeat = polyLayer.GetFeature(currentPoly)
                        currentPolyGeom = currentPolyFeat.GetGeometryRef()
                        FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                        if FirstIntersect.IsEmpty() == False:
                            PolyIntersectSeq.append(currentPolyFeat.GetFID())
                            if FirstIntersect.GetGeometryName() == 'MULTILINESTRING':
                                pt1 = ()
                                pt2 = ()
                                PT1 =[]
                                PT2 = []
                                print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                                points = FirstIntersect.GetEnvelope()
                                count = len(points)
                                for i in range(0,count,2):
                                    pt1 = pt1 + (points[i],)
                                    pt2 = pt2 + (points[i+1],)
                                PT1.append(pt1)
                                PT2.append(pt2)
                                ptLst.append(PT1)
                                ptLst.append(PT2)
                
                            elif FirstIntersect.GetGeometryName() == 'LINESTRING':
                                print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                                Points = FirstIntersect.GetPoints()
                                ptLst.append(Points)
        
                    ptRefDict = dict(zip(PolyIntersectSeq,ptLst))                
                    ptSort = sorted(ptLst,key = operator.itemgetter(0))
                    print(ptSort)
                    if len(ptSort) > 0 and len(ptRefDict) > 0:
                        for k in range(0,len(ptSort)):
                            firstBuildingXY = ptSort[k]
                            for key in ptRefDict.keys():
                                if  firstBuildingXY == ptRefDict[key]:
                                    BuildingIntersectSeq.append(key)
                        print('Building Intersect Sequence is = ',BuildingIntersectSeq)
                    size = len(BuildingIntersectSeq)
                    if size == 1:
                        building = polyLayer.GetFeature(BuildingIntersectSeq[0])
                        Ht = building.GetField('Height')
                        if Ht > HEIGHT:
                            height = HEIGHT
                        elif Ht <= HEIGHT:
                            height = Ht
                        frontalarea = lineSpacing* height
                    elif size > 1 :
                        firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[0])
                        Ht1 = firstBuild.GetField('Height')
                        if Ht1 > HEIGHT:
                            height1 = HEIGHT
                        elif Ht1 <= HEIGHT:
                            height1 = Ht1
                        maxHeight = height1
                        frontalarea =  lineSpacing * height1
                        for building1 in range (1,size):
                            secondBuild = polyLayer.GetFeature(BuildingIntersectSeq[building1])
                            Ht2 = secondBuild.GetField('Height')
                            if Ht2 > HEIGHT:
                                height2 = HEIGHT
                            elif Ht2 <= HEIGHT:
                                height2 = Ht2
                            if height2>maxHeight:
                                effHeight = height2 - maxHeight
                                frontalarea =  frontalarea +(lineSpacing * effHeight)
                                MaxHeight = height2
                        print('\n The frontal area exposed to windline',windFeature.GetFID(),'is = ',frontalarea,'\n')
                    FrontalArea = FrontalArea + frontalarea
                print('\n The total frontal area of the study area is = ',FrontalArea)

        if self.Index_ == 8:
            if self.choice_1.isChecked()== True:
                            Driver = ogr.GetDriverByName('ESRI Shapefile')
                            Footprint = str(self.footprint_path)
                            polySource = Driver.Open(Footprint,0)
                            polyLayer = polySource.GetLayer()
                            wind = str(self.wind_path)
                            windSource = Driver.Open(wind,0)
                            windLayer = windSource.GetLayer()
                            output = str(self.output_path)
                            FrontalArea = 0
                            name_of_file = 'Frontal Area 315 DEG'
                            completeName = os.path.join(output, name_of_file+".txt") 
                            cfa315 = open(completeName , "w")
                            #sys.stdout = open(output,'w')            
                            for wind in range(0,windLayer.GetFeatureCount()):
                                ptLst = []
                                PolyIntersectSeq = []
                                BuildingIntersectSeq = []
                                windFeature = windLayer.GetNextFeature()
                                windGeometry = windFeature.GetGeometryRef()
                                lineSpacing = self.reso_val
                                newGem = windGeometry.Buffer(lineSpacing);
                                # abc =  newGem.GetEnvelope()
                                polyLayer.SetSpatialFilter(newGem)
                                
                                
                                
                                for currentPoly in range (0,polyLayer.GetFeatureCount()):
                                    currentPolyFeat = polyLayer.GetNextFeature()
                                    currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                    FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                                    if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                                        PolyIntersectSeq.append(currentPolyFeat.GetFID())
                                        ptLst.append(FirstIntersect.GetPoints())
                                ptRefDict = dict(zip(PolyIntersectSeq,ptLst))
                                PtSort = sorted(ptLst)
                                if len(PtSort) > 0 and len(ptRefDict) > 0:
                                    cfa315.write ("*******************************************************\n")
                                    cfa315.write("WindLine \n".format(windFeature.GetFID()))
                                    cfa315.write("This is the list of buildings that the windline {0} intersects {1} \n".format(windFeature.GetFID(),PolyIntersectSeq))
                                    cfa315.write('This is the list of points that the windline {0} and building {1} intersects at {2}\n'.format(windFeature.GetFID(),currentPolyFeat.GetFID(),ptLst))        
                                    cfa315.write('This is the dictionary that has the keys as polygon and value as respective coordinate {0} \n'.format(ptRefDict))        
                                    cfa315.write('This is the list of intersection points sorted as the actually intersect {0} \n'.format(PtSort))
                                    for x in range(0,len(PtSort)):
                                        firstBuildingXY = PtSort[x]
                                        for key in ptRefDict.keys():
                                            if ptRefDict[key] ==  firstBuildingXY:
                                                BuildingIntersectSeq.append(key)
                                    cfa315.write('This list contains the polygon FID in a order the windline {0} intersects buildings {1} \n'.format(windFeature.GetFID(),BuildingIntersectSeq))
                                    size = len(BuildingIntersectSeq)
                                    lineSpacing = self.reso_val
                                    if size <= 1:
                                        building = polyLayer.GetFeature(BuildingIntersectSeq[0])
                                        height = building.GetField('Height')
                                        frontalarea = lineSpacing * height
                                    elif size > 1 :

                                        firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[0])
                                        height1 = firstBuild.GetField('Height')
                                        MaxHeight=height1
                                        for building1 in range (1,size):
                                            firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[building1])
                                            height1 = firstBuild.GetField('Height')
                                            if(MaxHeight<height1):
                                                    MaxHeight= height1
                                        frontalarea= lineSpacing*MaxHeight   

                                          
                                    cfa315.write('The frontal area exposed to windline {0} is = {1}'.format(windFeature.GetFID(),frontalarea))
                                    FrontalArea = FrontalArea + frontalarea
                            cfa315.write('The total frontal area of the study area is = {0}\n'.format(FrontalArea))
                            polyLayer.SetSpatialFilter(None)

            if self.choice_2.isChecked()== True:
                                Driver1 = ogr.GetDriverByName('ESRI Shapefile')
                                Grid =str(self.grid_path)
                                GridSource = Driver1.Open(Grid,1)
                                GridLayer = GridSource.GetLayer()
                                Footprint = str(self.footprint_path)
                                BuildingSource = Driver1.Open(Footprint,0)
                                BuildingLayer = BuildingSource.GetLayer()
                                wind = str(self.wind_path)
                                WindSource = Driver1.Open(wind,0)
                                WindLayer = WindSource.GetLayer()
                                layer_defn = GridLayer.GetLayerDefn()
                                # new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
                                # GridLayer.CreateField(new_field)
                                #new_field = ogr.FieldDefn('GridFA', ogr.OFTInteger)
                                #GridLayer.CreateField(new_field)
                                output = str(self.output_path)
                                FrontalArea = 0
                                GridFrontalArea = []
                                text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter Field name for frontal area :')
                                if ok:
                                    name=str(text)
                                ldefn = GridLayer.GetLayerDefn()
                                sch= []
                                check=0
                                n=0
                                for n in range (1, GridLayer.GetFeature(0).GetFieldCount()):
                                    field = GridLayer.GetFeature(0).GetDefnRef().GetFieldDefn(n).GetName()
                                    sch.append(field) 
                                n=0
                                for n in range(len(sch)):
                                   if(name==str(sch[n])):
                                       check=1
                                       print('Field Already exists')
                                if (check==0):
                                    new_field = ogr.FieldDefn(name, ogr.OFTReal)
                                    GridLayer.CreateField(new_field)
                                    print('New Field Created')
                                length = GridLayer.GetFeatureCount()
                                lineSpacing= self.reso_val
                                ListTop = []
                                ListBottom = []
                                ListRight = []
                                ListLeft = []
                                windLeft = []
                                windRight = []
                                windBottomLeft = []
                                windBottomRight = []
                                name_of_file = 'Frontal Area Grid 315 DEG'
                                completeName = os.path.join(output, name_of_file+".txt") 
                                cfa315 = open(completeName , "w")

                                GridFeat =  GridLayer.GetFeature(0)

                                GridGeom = GridFeat.GetGeometryRef()
                                list1 = GridLayer.GetExtent()
                                list2 = GridGeom.GetEnvelope()
                                col = int((list1[1]-list1[0])/(list2[1]-list2[0]))
                                row = int((list1[3]-list1[2])/(list2[3]-list2[2]))
                                # print "COl"
                                # print col
                                # print "row"
                                # print row
                                sys.stdout = open('running.txt','w')
                                k=1
                                q=0
                                t=col-1
                                listFrontalArea = list([0.0 for x in range(int(col*row))])
                                for Grid in range(0,length):
                                    if(t == k*col or  t==0):
                                        k=k+1
                                        t=(k*col)-1
                                        continue
                                    if(t == (row-1)*col):
                                        break
                                    GridFeat1 = GridLayer.GetFeature(int(t))
                                    GridGeom1 = GridFeat1.GetGeometryRef()
                                    GridList= list(GridGeom1.GetEnvelope())
                                    # print GridList
                                    # print "Grid id"
                                    # print GridFeat1.GetField("Id")
                                    WindLayer.SetSpatialFilter(GridGeom1)
                                    BuildingLayer.SetSpatialFilter(GridGeom1)
                                    
                                    for wind_line in range(0,WindLayer.GetFeatureCount()):
                                        maxx=0
                                        feature =  WindLayer.GetNextFeature() 
                                        interWind = feature.GetGeometryRef() 
                                        windLeft.append(feature.GetFID())
                                        for buildings in range(0,BuildingLayer.GetFeatureCount()):
                                             currentPolyFeat = BuildingLayer.GetNextFeature()
                                             currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                             FirstIntersect =interWind.Intersection(currentPolyGeom)
                                             if FirstIntersect != None and FirstIntersect.IsEmpty()==False:
                                                     abc = list(FirstIntersect.GetEnvelope())
                                                     if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                                        
                                                            curmaxOfLine = currentPolyFeat.GetField("Height")
                                                            # print "cur max ",curmaxOfLine
                                                            if(curmaxOfLine >= maxx):
                                                                  maxx = curmaxOfLine

                                        ListLeft.append(maxx)
                                        
                                        BuildingLayer.ResetReading()
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                    WindLayer.ResetReading()
                                    BuildingLayer.ResetReading()
                                    # print ("ListLeft before and after",ListLeft)
                                    
                                        

                                    GridFeat2 = GridLayer.GetFeature(int(t-1))
                                    GridGeom2 = GridFeat2.GetGeometryRef()
                                    GridList= list(GridGeom2.GetEnvelope())
                                    WindLayer.SetSpatialFilter(GridGeom2)
                                    BuildingLayer.SetSpatialFilter(GridGeom2)
                                    for wind_line in range(0,WindLayer.GetFeatureCount()):  
                                        maxx = 0
                                        feature = WindLayer.GetNextFeature() 
                                        interWind = feature.GetGeometryRef()                 
                                        windRight.append(feature.GetFID())
                                        for buildings in range(0,BuildingLayer.GetFeatureCount()):
                                             currentPolyFeat = BuildingLayer.GetNextFeature()
                                             currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                             FirstIntersect = interWind.Intersection(currentPolyGeom)
                                             if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                                                   abc = list(FirstIntersect.GetEnvelope())
                                                   # print abc
                                                     # print abc
                                                     # print GridFeat1.GetField("Id")

                                                     
                                                     # if ((GridList[0] > abc[0] or GridList[1] < abc[0]) and (GridList[1]< abc[1] or GridList[0]> abc[1])) and ((GridList[2] < abc[2] or GridList[3] > abc[2]) and (GridList[3]> abc[3] or GridList[2]< abc[3])):
                                                        
                                                     #    continue
                                                  # if ( (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[3] < GridList[2]) and (abc[3] > GridList[3]))) or (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[2] < GridList[2]) and (abc[2] > GridList[3]))) ):                            
                                                   if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                                                         
                                                   # if ( (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                                            curmaxOfLine = currentPolyFeat.GetField("Height")
                                                            # print "cur max ",curmaxOfLine
                                                            if(curmaxOfLine >= maxx):
                                                                  maxx = curmaxOfLine
                                        ListRight.append(maxx)
                                        BuildingLayer.ResetReading()
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                    WindLayer.ResetReading()
                                    BuildingLayer.ResetReading()
                                    # print ("ListRight before",ListRight)


                                    GridFeat3 = GridLayer.GetFeature(int(t+col))
                                    GridGeom3 = GridFeat3.GetGeometryRef()
                                    GridList= list(GridGeom3.GetEnvelope())
                                    WindLayer.SetSpatialFilter(GridGeom3)
                                    BuildingLayer.SetSpatialFilter(GridGeom3)
                                    for wind_line in range(0,WindLayer.GetFeatureCount()):
                                        maxx = 0
                                        feature = WindLayer.GetNextFeature()  
                                        interWind = feature.GetGeometryRef()
                                        windBottomLeft.append(feature.GetFID())
                                      
                                        for buildings in range(0,BuildingLayer.GetFeatureCount()):
                                             currentPolyFeat = BuildingLayer.GetNextFeature()
                                                                       
                                             currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                             FirstIntersect = interWind.Intersection(currentPolyGeom)
                                             if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                                                    abc = list(FirstIntersect.GetEnvelope())
                                                     # print abc
                                                     # print GridFeat1.GetField("Id")

                                                     
                                                     # if ((GridList[0] > abc[0] or GridList[1] < abc[0]) and (GridList[1]< abc[1] or GridList[0]> abc[1])) and ((GridList[2] < abc[2] or GridList[3] > abc[2]) and (GridList[3]> abc[3] or GridList[2]< abc[3])):
                                                        
                                                     #    continue
                                                  # if ( (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[3] < GridList[2]) and (abc[3] > GridList[3]))) or (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[2] < GridList[2]) and (abc[2] > GridList[3]))) ):                            
                                                    if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                                                         
                                                   # if ( (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                                            curmaxOfLine = currentPolyFeat.GetField("Height")
                                                            # print "cur max ",curmaxOfLine
                                                            if(curmaxOfLine >= maxx):
                                                                  maxx = curmaxOfLine
                                        ListTop.append(maxx)
                                        BuildingLayer.ResetReading()
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                    WindLayer.ResetReading()
                                    BuildingLayer.ResetReading()
                                    # print ("ListBottomLeft before",ListTop)

                                    GridFeat4 = GridLayer.GetFeature(int(t+col-1))
                                    GridGeom4 = GridFeat4.GetGeometryRef()   
                                    GridList= list(GridGeom4.GetEnvelope())       
                                    WindLayer.SetSpatialFilter(GridGeom4)
                                    BuildingLayer.SetSpatialFilter(GridGeom4)
                                    for wind_line in range(0,WindLayer.GetFeatureCount()):
                                        maxx = 0
                                        feature = WindLayer.GetNextFeature()  
                                        interWind = feature.GetGeometryRef()
                                        windBottomRight.append(feature.GetFID())
                                        for buildings in range(0,BuildingLayer.GetFeatureCount()):
                                             currentPolyFeat = BuildingLayer.GetNextFeature()
                                             currentPolyGeom = currentPolyFeat.GetGeometryRef()
                                             FirstIntersect = interWind.Intersection(currentPolyGeom)
                                             if FirstIntersect != None and FirstIntersect.IsEmpty() == False:
                                                   abc = list(FirstIntersect.GetEnvelope())
                                                     # print abc
                                                     # print GridFeat1.GetField("Id")

                                                     
                                                     # if ((GridList[0] > abc[0] or GridList[1] < abc[0]) and (GridList[1]< abc[1] or GridList[0]> abc[1])) and ((GridList[2] < abc[2] or GridList[3] > abc[2]) and (GridList[3]> abc[3] or GridList[2]< abc[3])):
                                                        
                                                     #    continue
                                                  # if ( (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[3] < GridList[2]) and (abc[3] > GridList[3]))) or (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[2] < GridList[2]) and (abc[2] > GridList[3]))) ):                            
                                                    # if(( GridList[0]<abc[0]<GridList[1] and GridList[2]<abc[2]<GridList[3] ) or ( GridList[0]<abc[1]<GridList[1] and GridList[2]<abc[3]<GridList[3] )):
                                                         
                                                   if ( (((abc[1] < GridList[1]) and (abc[1] > GridList[0])) and ((abc[3] < GridList[3]) and (abc[3] > GridList[2]))) or (((abc[0] < GridList[1]) and (abc[0] > GridList[0])) and ((abc[2] < GridList[3]) and (abc[2] > GridList[2]))) ):
                                                            curmaxOfLine = currentPolyFeat.GetField("Height")
                                                            # print "cur max ",curmaxOfLine
                                                            if(curmaxOfLine >= maxx):
                                                                  maxx = curmaxOfLine
                                        ListBottom.append(maxx)
                                        BuildingLayer.ResetReading()
                                    BuildingLayer.SetSpatialFilter(None)
                                    WindLayer.SetSpatialFilter(None)
                                    WindLayer.ResetReading()
                                    BuildingLayer.ResetReading()
                                    # print ("ListBottomRight before",ListBottom)

                                    #for GridRight
                                    for i in range(0,len(windLeft)):
                                        for j in range(0,len(windRight)):
                                            if windLeft[i]==windRight[j]:
                                                if ListLeft[i]<ListRight[j]:
                                                    ListRight[j]= ListRight[j]-ListLeft[i]
                                                else:
                                                    ListRight[j]=0
                                    # print ("ListRight",ListRight)
                                    #GridBottomLeft
                                    for i in range(0,len(windLeft)):
                                        for j in range(0,len(windBottomLeft)):
                                            if windLeft[i]==windBottomLeft[j]:
                                                if ListTop[j]>ListLeft[i]:
                                                    ListTop[j]= ListTop[j]-ListLeft[i]
                                                else:
                                                    ListTop[j]=0
                                    # print ("ListBottomLeft",ListTop)
                                    #GridBottomRight
                                    for i in range(0,len(windRight)):
                                        for j in range(0,len(windBottomRight)):
                                            if windRight[i]==windBottomRight[j]:
                                                if ListBottom[j]>ListRight[i]:

                                                    ListBottom[j]= ListBottom[j]-ListRight[i]
                                                else:
                                    
                                                    ListBottom[j]=0

                                    # print "@@@@@@@@@@@@@@@@@@@@@@@"
                                    # print ("ListBottomRight",ListBottom)


                                    for i in range(0,len(windBottomLeft)):
                                        for j in range(0,len(windBottomRight)):
                                            if windBottomLeft[i]==windBottomRight[j]:
                                                if ListTop[i]<ListBottom[j]:
                                                    ListBottom[j]= ListBottom[j]-ListTop[i]
                                                else:
                                                    ListBottom[j]=0
                                    # print ("ListBottomRight",ListBottom)
                                    if(listFrontalArea[t] == 0):
                                        listFrontalArea[t] = sum(ListLeft)* lineSpacing ;
                                    if(listFrontalArea[t-1] == 0):
                                        listFrontalArea[t-1] = sum(ListRight)* lineSpacing ;
                                    if(listFrontalArea[t+col] == 0):
                                        listFrontalArea[t+col] = sum(ListTop)* lineSpacing ;
                                    if(listFrontalArea[t+col-1] == 0):
                                        listFrontalArea[t+col-1] = sum(ListBottom)* lineSpacing ;

                                    t=t-1
                                    
                                    del windLeft[:]
                                    del windRight[:]
                                    del windBottomRight[:]
                                    del windBottomLeft[:]


                                    del ListLeft[:]
                                    del ListRight[:]
                                    del ListTop[:]
                                    del ListBottom[:]

                                for i in range(0,len(listFrontalArea)):
                                    cfg315.write("Frontal Area for Grid {0} is {1}\n".format(i,listFrontalArea[i]))
                                    Grid_feature = GridLayer.GetFeature(i)
                                    
                                    Grid_feature.SetField('GridFA',listFrontalArea[i])
                                    GridLayer.SetFeature(Grid_feature)
                                
                                
                                cfg315.write( "The total frontal area is{0} \n".format(sum(listFrontalArea)))
                                # for gridFrontal in range(0,len(listFrontalArea)):
                                #     Grid_feature = GridLayer.GetFeature(gridFrontal)
                                    
                                #     Grid_feature.SetField('GridFA',listFrontalArea[gridFrontal])
                                #     GridLayer.SetFeature(Grid_feature)
                                cfg315.close()

            if self.choice_3.isChecked() == True:
                Driver2 = ogr.GetDriverByName('ESRI Shapefile')
                poly = self.footprint_path
                polySource = Driver2.Open(poly,0)
                polyLayer = polySource.GetLayer()
                wind = self.wind_path
                windSource = Driver2.Open(wind,0)
                windLayer = windSource.GetLayer()
                spatialReference = polyLayer.GetSpatialRef()
                BuildLst = []
                lstPoints = []
                HWlst = []
                FrontalArea = 0
                HEIGHT = int(input("Supply the height value \n "))
                lineSpacing = self.reso_val
                for wind in range(0,windLayer.GetFeatureCount()):
                    frontalarea = 0
                    ptLst = []
                    PolyIntersectSeq = []
                    ptRefDict = {}
                    BuildingIntersectSeq = []
                    windFeature = windLayer.GetFeature(wind)
                    windGeometry = windFeature.GetGeometryRef()
                    IntersectPts = []
                    HeightLst = []
                    WidthLst = []
                    height = 0
                    IntersectPts = []
                    for currentPoly in range (0,polyLayer.GetFeatureCount()):
                        currentPolyFeat = polyLayer.GetFeature(currentPoly)
                        currentPolyGeom = currentPolyFeat.GetGeometryRef()
                        FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                        if FirstIntersect.IsEmpty() == False:
                            PolyIntersectSeq.append(currentPolyFeat.GetFID())
                            if FirstIntersect.GetGeometryName() == 'MULTILINESTRING':
                                pt1 = ()
                                pt2 = ()
                                PT1 =[]
                                PT2 = []
                                print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                                points = FirstIntersect.GetEnvelope()
                                count = len(points)
                                for i in range(0,count,2):
                                    pt1 = pt1 + (points[i],)
                                    pt2 = pt2 + (points[i+1],)
                                PT1.append(pt1)
                                PT2.append(pt2)
                                ptLst.append(PT1)
                                ptLst.append(PT2)
                
                            elif FirstIntersect.GetGeometryName() == 'LINESTRING':
                                print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                                Points = FirstIntersect.GetPoints()
                                ptLst.append(Points)
        
                    ptRefDict = dict(zip(PolyIntersectSeq,ptLst))                
                    ptSort = sorted(ptLst,key = operator.itemgetter(0))
                    print(ptSort)
                    if len(ptSort) > 0 and len(ptRefDict) > 0:
                        for k in range(0,len(ptSort)):
                            firstBuildingXY = ptSort[k]
                            for key in ptRefDict.keys():
                                if  firstBuildingXY == ptRefDict[key]:
                                    BuildingIntersectSeq.append(key)
                        print('Building Intersect Sequence is = ',BuildingIntersectSeq)
                    size = len(BuildingIntersectSeq)
                    if size == 1:
                        building = polyLayer.GetFeature(BuildingIntersectSeq[0])
                        Ht = building.GetField('Height')
                        if Ht > HEIGHT:
                            height = HEIGHT
                        elif Ht <= HEIGHT:
                            height = Ht
                        frontalarea = lineSpacing* height
                    elif size > 1 :
                        firstBuild = polyLayer.GetFeature(BuildingIntersectSeq[0])
                        Ht1 = firstBuild.GetField('Height')
                        if Ht1 > HEIGHT:
                            height1 = HEIGHT
                        elif Ht1 <= HEIGHT:
                            height1 = Ht1
                        maxHeight = height1
                        frontalarea =  lineSpacing * height1
                        for building1 in range (1,size):
                            secondBuild = polyLayer.GetFeature(BuildingIntersectSeq[building1])
                            Ht2 = secondBuild.GetField('Height')
                            if Ht2 > HEIGHT:
                                height2 = HEIGHT
                            elif Ht2 <= HEIGHT:
                                height2 = Ht2
                            if height2>maxHeight:
                                effHeight = height2 - maxHeight
                                frontalarea =  frontalarea +(lineSpacing * effHeight)
                                MaxHeight = height2
                        print('\n The frontal area exposed to windline',windFeature.GetFID(),'is = ',frontalarea,'\n')
                    FrontalArea = FrontalArea + frontalarea
                print('\n The total frontal area of the study area is = ',FrontalArea)

class Ui_Dialog_PAFD(object):
    height=1
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(_fromUtf8("QDialog{background-image:url(\"C:/Users/Nimit Johri/Desktop/clouds.jpg\");\n"
"}\n"
"\n"
"QLabel{\n"
"color: navy; \n"
"                        \n"
"                        selection-color: yellow;\n"
"                        selection-background-color: blue;\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
" border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
""))
        self.PAF_btn = QtGui.QPushButton(Dialog)
        self.PAF_btn.setGeometry(QtCore.QRect(100, 140, 211, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PAF_btn.setFont(font)
        self.PAF_btn.setAutoFillBackground(False)
        self.PAF_btn.setObjectName(_fromUtf8("PAF_btn"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 230, 261, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 80, 141, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.Height_inc = QtGui.QSpinBox(Dialog)
        self.Height_inc.setGeometry(QtCore.QRect(270, 80, 42, 22))
        self.Height_inc.setObjectName(_fromUtf8("Height_inc"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.PAF_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cal_PAFD)
        self.Height_inc.valueChanged[str].connect(self.input_increment_height)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Plan Area Fraction Density", None))
        self.PAF_btn.setText(_translate("Dialog", "Calculate Plan Area Fraction Density", None))
        self.label.setText(_translate("Dialog", "**Note:-*****************", None))
        self.label_4.setText(_translate("Dialog", "Select the Height Increment", None))

    def input_increment_height(self):
        #print(self.Height_inc.value())
        Ui_Dialog_PAFD.height = self.Height_inc.value()

    def cal_PAFD(self):
        driver = ogr.GetDriverByName('ESRI Shapefile')
        unionfile = str(Ui_MainWindow.unionfile_path)
        unionSource = driver.Open(unionfile,1)
        unionLayer = unionSource.GetLayer()
        GridFeat = unionLayer.GetFeature(0)
        GridGeom = GridFeat.GetGeometryRef()
        output = str(Ui_MainWindow.outputfile_path)
        list1 = unionLayer.GetExtent()
        list2 = GridGeom.GetEnvelope()
        noc = (list1[1]-list1[0])/(list2[1]-list2[0])
        nor = (list1[3]-list1[2])/(list2[3]-list2[2])
        prod=noc*nor
        BuildId = []
        BuildGdId = []
        BuildHt = []
        BuildAr = []
        BuildSumAr = []
        BlankSumAr = []
        BuildMaxGdHt = []
        BuildMinGdHt = []
        #print (layer.GetFeatureCount())
        
        for i in range(unionLayer.GetFeatureCount()):
            
            feature=unionLayer.GetFeature(i)
            #print (feature)
            var1=feature.GetField('FIDGrid')
            BuildGdId.append(var1)
            var2=feature.GetField('FIDBuild')
            BuildId.append(var2)
            var3=feature.GetField('buildh')
            BuildHt.append(var3)
            var4=feature.GetField('buildarea')
            BuildAr.append(var4)
        count = 0
        #print (BuildId)
        #print (BuildGdId)
        while (count < prod):
            buildsum = 0
            blanksum = 0
            i=0
            for i in range(unionLayer.GetFeatureCount()):
                if (BuildGdId[i]==count and BuildId[i] > -1):
                    buildsum=buildsum+BuildAr[i]
                    
                elif (BuildGdId[i]==count and BuildId[i]==-1):
                    blanksum=blanksum+BuildAr[i]

                    
            count = count+1
            BuildSumAr.append(buildsum)
            BlankSumAr.append(blanksum)
        #    print("Total building area  for grid {0} is {1}".format((count-1), BuildSumAr[count-1]))
        #    print("Total blank area  for grid {0} is {1}".format((count-1), BlankSumAr[count-1]))

        count =0
        while (count < prod):
            i=0
            buildheight = []
            buildheight2 = []
            for i in range(unionLayer.GetFeatureCount()):
                if (BuildGdId[i]==count and BuildId[i] > -1):
                    buildheight.append(BuildHt[i])            
            count = count+1
            if(len(buildheight)==0):
                BuildMaxGdHt.append(0)
                BuildMinGdHt.append(0)

            else:
                
                BuildMaxGdHt.append(max(buildheight))
                BuildMinGdHt.append(min(buildheight))

        length=len(BlankSumAr)
        x=0
        PlAr = 0
        plan_area_fr = []
        for x in range(length):
            if (BuildSumAr[x]>0  and BlankSumAr[x]>0 ):
                PlAr= float(BuildSumAr[x]) / float(BlankSumAr[x]+BuildSumAr[x])
                plan_area_fr.append(PlAr)
            else:
                plan_area_fr.append('0')
            #print ("Plan area Fraction for grid {0} is {1} ".format((x+1),plan_area_fr[x]))
        inc =Ui_Dialog_PAFD.height
        count = 0
        temp=inc
        name_of_file = 'Plan Area Density'
        completeName = os.path.join(output, name_of_file+".txt") 
        f_pafd= open(completeName , "w")
        #f_pafd= open('Plan Area Density.txt','w')            
        while(count<=prod):
            inc=temp
            BuildPlanDen = []
            while(inc <= max(BuildMaxGdHt)):

                buildsum2=0
                blanksum2=0
                i=0
                plandenht=0
                for i in range(unionLayer.GetFeatureCount()):
                    if(BuildGdId[i]==count and BuildId[i] > -1 and BuildHt[i] >=inc):
                        buildsum2=buildsum2+BuildAr[i]
                    elif(BuildGdId[i]==count and BuildId[i] == -1):
                        blanksum2=blanksum2+BuildAr[i]
                inc=inc+temp
                if(buildsum2>0 and blanksum2>0):
                    plandenht=float(buildsum2)/float(blanksum2+buildsum2)/float(temp)
                    BuildPlanDen.append(plandenht)
                else:
                    BuildPlanDen.append('0')
            temp2 = 0
            for i in range(len(BuildPlanDen)):
                f_pafd.write(" Plan area Density for Grid {0} at height {1} is {2}\n".format( count, temp2 ,BuildPlanDen[i]))
                temp2=temp2+temp
            count=count+1
        f_pafd.close()
        print('Plan Area Density Completed')

class Ui_Dialog_SVF(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(647, 448)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        Dialog.setStyleSheet(_fromUtf8("QDialog{background-image:url(\"C:/Users/Nimit Johri/Desktop/clouds.jpg\");\n"
"}\n"
"\n"
"QLabel{\n"
"color: navy; \n"
"                        \n"
"                        selection-color: yellow;\n"
"                        selection-background-color: blue;\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
" border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
""))
        self.browse_1 = QtGui.QPushButton(Dialog)
        self.browse_1.setGeometry(QtCore.QRect(470, 150, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.browse_1.setFont(font)
        self.browse_1.setObjectName(_fromUtf8("browse_1"))
        self.Sweep_Res = QtGui.QSpinBox(Dialog)
        self.Sweep_Res.setGeometry(QtCore.QRect(130, 310, 42, 22))
        self.Sweep_Res.setObjectName(_fromUtf8("Sweep_Res"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 310, 181, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(250, 150, 201, 20))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.Radial_Length = QtGui.QSpinBox(Dialog)
        self.Radial_Length.setGeometry(QtCore.QRect(130, 260, 42, 22))
        self.Radial_Length.setObjectName(_fromUtf8("Radial_Length"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 10, 341, 61))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 200, 201, 20))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.browse_2 = QtGui.QPushButton(Dialog)
        self.browse_2.setGeometry(QtCore.QRect(470, 202, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.browse_2.setFont(font)
        self.browse_2.setObjectName(_fromUtf8("browse_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(210, 260, 221, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.OK = QtGui.QPushButton(Dialog)
        self.OK.setGeometry(QtCore.QRect(300, 360, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.OK.setFont(font)
        self.OK.setObjectName(_fromUtf8("OK"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 150, 191, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 190, 171, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.browse_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.SVFPoints_browse)
        QtCore.QObject.connect(self.browse_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.RadialSweep_browse)
        self.Radial_Length.valueChanged[str].connect(self.RadialLength_Select)
        self.Sweep_Res.valueChanged[str].connect(self.SweepRes_Select)
        QtCore.QObject.connect(self.OK, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cal_SVF)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "SVF", None))
        self.browse_1.setText(_translate("Dialog", "Browse", None))
        self.label_3.setText(_translate("Dialog", "Enter Sweep Resolution", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Compute Sky View Factor</span></p></body></html>", None))
        self.browse_2.setText(_translate("Dialog", "Browse", None))
        self.label_2.setText(_translate("Dialog", "Enter the length of the Radial lines", None))
        self.OK.setText(_translate("Dialog", "Compute SVF", None))
        self.label_4.setText(_translate("Dialog", "Select the path of point Shape file...", None))
        self.label_5.setText(_translate("Dialog", "Output Radial Sweep Shapefile", None))

    def SVFPoints_browse(self):
        print ('selecting folder containing shape file containg svf computation points')
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home',filter= '*.shp')
        self.SVF_path = self.fname.replace('\\','/')
        self.lineEdit.setText(self.fname)
        print(self.SVF_path)

    def RadialSweep_browse(self):
        print ('selecting folder to save radial lines shape file')
        self.fname = QtGui.QFileDialog.getSaveFileName(None, 'Save file','/home',filter = '*.shp')
        self.Radial_path = self.fname.replace('\\','/')
        self.lineEdit_2.setText(self.fname)
        print(self.Radial_path)

    def RadialLength_Select(self):
        self.RadialLength = self.Radial_Length.value()
        
    def SweepRes_Select(self):
         self.SweepRes = self.Sweep_Res.value()
        
    def cal_SVF(self):
        Driver = ogr.GetDriverByName('ESRI Shapefile')
        SVFPts = self.SVF_path
        PtSource = Driver.Open(SVFPts,1)
        ptLayer = PtSource.GetLayer()
        defn = ptLayer.GetLayerDefn()
        new_field1 = ogr.FieldDefn('SVF', ogr.OFTReal)
        ptLayer.CreateField(new_field1)
        new_field2 = ogr.FieldDefn('VF', ogr.OFTReal)
        ptLayer.CreateField(new_field2)
        spatRef = ptLayer.GetSpatialRef()
        Pts = 0
        PointXY = []
        RadialPath = self.Radial_path
        ds = Driver.CreateDataSource(RadialPath)
        dsLayer = ds.CreateLayer('Demo', spatRef, geom_type = ogr.wkbLineString)
        defn = dsLayer.GetLayerDefn()
        featObj = ogr.Feature(dsLayer.GetLayerDefn())
        lynobj = ogr.Geometry(ogr.wkbLineString)
        sweep_radius = int(self.RadialLength)
        sweep_res = int(self.SweepRes)

        for i in range(0,ptLayer.GetFeatureCount()):
            PtFeat = ptLayer.GetFeature(i)
            PtGeom =PtFeat.GetGeometryRef()
            PointXY.append(PtGeom.GetPoints())
        for j in range(0,len(PointXY)):
            Pt = PointXY[j]
            pt =Pt[0]
            focal_pt1 = Point(pt[0],pt[1])
            focal_pt2 = Point(pt[0],pt[1]+sweep_radius)
            line = LineString([(focal_pt1.x,focal_pt1.y),(focal_pt2.x,focal_pt2.y)])
            for k in range(0,360,sweep_res):
                radii= affinity.rotate(line, k, origin = focal_pt1, use_radians = False)
                geom = ogr.CreateGeometryFromWkb(radii.wkb)
                featObj.SetGeometry(geom) 
                dsLayer.CreateFeature(featObj)
        ds.Destroy()
        SVFLst = []
        lst = []
        Footprint = self.footprint_path
        polySource = Driver.Open(Footprint,0)
        polyLayer = polySource.GetLayer()
        RadialSource = Driver.Open(RadialPath,0)
        RadialLayer = RadialSource.GetLayer()
        threshold = 360/sweep_res
        count = 0
        RadialLines = RadialLayer.GetFeatureCount()
        print('Processing..............');
        for radial in range(0,RadialLayer.GetFeatureCount()):
            gamma = 0
            count = count+1
            alphaSelect = []
            RadialFeat = RadialLayer.GetFeature(radial)
            RadialGeom = RadialFeat.GetGeometryRef()
            for poly in range(0,polyLayer.GetFeatureCount()):
                PolyFeat = polyLayer.GetFeature(poly)
                PolyGeom = PolyFeat.GetGeometryRef()
                Intersect = RadialGeom.Intersection(PolyGeom)
                if Intersect.IsEmpty() == False:
                    Height = PolyFeat.GetField('Height')
                    RadialEndPoint = RadialGeom.GetPoint()
                    x2 = RadialEndPoint[0]
                    y2 = RadialEndPoint[1]
                    IntersectPt = Intersect.GetPoint()
                    x1 = IntersectPt[0]
                    y1 = IntersectPt[1]
                    Width = math.sqrt((x2-x1)**2 + (y2-y1)**2)
                    alpha = math.degrees(math.atan(Height/Width))
                    alphaSelect.append(alpha)
            AlphaSort = sorted(alphaSelect, reverse = True)
            if len(AlphaSort)>0:
                beta = AlphaSort[0]
                theta = (math.cos(beta)**2)*(sweep_res/360)
                lst.append(theta)
                gamma = gamma +theta
            if count > threshold-1:
                Sum = sum(lst)
                SVFLst.append(Sum)
                count = 0
                Sum = 0
                lst = []
                for i in range(0,ptLayer.GetFeatureCount()):
                    print('\r .')
        print('Done\n','The Values of the computed SVF and VF are updated to the SVF points shape file')
        Length = len(SVFLst)
        for svf in range(0,Length):
            Ptfeature = ptLayer.GetFeature(svf)
            Ptfeature.SetField('VF',SVFLst[svf])
            ptLayer.SetFeature(Ptfeature)   
            vf = 1 - SVFLst[svf]
            Ptfeature.SetField('SVF',vf)
            ptLayer.SetFeature(Ptfeature)

class Ui_Dialog_HWR(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(639, 356)
        Dialog.setStyleSheet(_fromUtf8("QDialog{\n"
"color:navy; background-color: white;\n"
"\n"
"                     \n"
"}\n"
"QRadioButton{\n"
"color:navy;\n"
"}\n"
"QLabel{\n"
"color: navy; \n"
"                        \n"
"                        selection-color: yellow;\n"
"                        selection-background-color: blue;\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
" border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
""))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 20, 321, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 170, 261, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.Browse4 = QtGui.QPushButton(Dialog)
        self.Browse4.setGeometry(QtCore.QRect(490, 170, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Browse4.setFont(font)
        self.Browse4.setObjectName(_fromUtf8("Browse4"))
        self.ok_btn = QtGui.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(250, 300, 84, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.cancel_btn = QtGui.QPushButton(Dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(350, 301, 84, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 191, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 191, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(200, 90, 261, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.Browse1 = QtGui.QPushButton(Dialog)
        self.Browse1.setGeometry(QtCore.QRect(490, 90, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Browse1.setFont(font)
        self.Browse1.setObjectName(_fromUtf8("Browse1"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 191, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Browse2 = QtGui.QPushButton(Dialog)
        self.Browse2.setGeometry(QtCore.QRect(490, 130, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Browse2.setFont(font)
        self.Browse2.setObjectName(_fromUtf8("Browse2"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 130, 261, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 326, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(160, 240, 161, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.Wind_Select = QtGui.QComboBox(Dialog)
        self.Wind_Select.setGeometry(QtCore.QRect(340, 210, 281, 20))
        self.Wind_Select.setObjectName(_fromUtf8("Wind_Select"))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Wind_Select.addItem(_fromUtf8(""))
        self.Resolution = QtGui.QSpinBox(Dialog)
        self.Resolution.setGeometry(QtCore.QRect(340, 240, 42, 22))
        self.Resolution.setMaximum(20)
        self.Resolution.setObjectName(_fromUtf8("Resolution"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QObject.connect(self.Browse1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.footprint_browse)
        QtCore.QObject.connect(self.Browse2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.wind_browse)
        QtCore.QObject.connect(self.Browse4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.HW_browse)
        QtCore.QObject.connect(self.ok_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.create_HWR)
        self.Resolution.valueChanged[str].connect(self.input_resolution)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Height to Width Ratio", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Height-to-Width Ratio</span></p></body></html>", None))
        self.Browse4.setText(_translate("Dialog", "Browse", None))
        self.ok_btn.setText(_translate("Dialog", "Ok", None))
        self.cancel_btn.setText(_translate("Dialog", "Cancel", None))
        self.label_3.setText(_translate("Dialog", "Select the Wind Lines Shapefile:", None))
        self.label_4.setText(_translate("Dialog", "Select the footprint Building Shapefile:", None))
        self.Browse1.setText(_translate("Dialog", "Browse", None))
        self.label_5.setText(_translate("Dialog", "Select the output files location:", None))
        self.Browse2.setText(_translate("Dialog", "Browse", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Select the direction for which Shape file is to be created:</span></p></body></html>", None))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Enter wind line resolution:</span></p></body></html>", None))
        self.Wind_Select.setToolTip(_translate("Dialog", "<html><head/><body><p>Select the angle for the direction of wind </p></body></html>", None))
        self.Wind_Select.setItemText(0, _translate("Dialog", "Angles start from south & proceeds anticlockwise.", None))
        self.Wind_Select.setItemText(1, _translate("Dialog", "0 Degrees", None))
        self.Wind_Select.setItemText(2, _translate("Dialog", "45 Degrees", None))
        self.Wind_Select.setItemText(3, _translate("Dialog", "90 Degrees", None))
        self.Wind_Select.setItemText(4, _translate("Dialog", "135 Degrees", None))
        self.Wind_Select.setItemText(5, _translate("Dialog", "180 Degrees", None))
        self.Wind_Select.setItemText(6, _translate("Dialog", "225 Degrees", None))
        self.Wind_Select.setItemText(7, _translate("Dialog", "270 Degrees", None))
        self.Wind_Select.setItemText(8, _translate("Dialog", "315 Degrees", None))

    def input_resolution(self):
        self.reso_val = self.Resolution.value()
 
    def footprint_browse(self):
        print ('selecting folder containing building footprint')
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home',filter= '*.shp')
        self.footprint_path = self.fname.replace('\\','/')
        self.lineEdit.setText(self.fname)
        print(self.footprint_path)

    def wind_browse(self):
        print ('selecting folder that will contain wind direction shape file')
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file','/home',filter= '*.shp')
        self.wind_path = self.fname.replace('\\','/')
        self.lineEdit_2.setText(self.fname)
        print(self.wind_path)

    def HW_browse(self):
        print ('selecting folder containing Height to Width Shape file')
        self.fname = QtGui.QFileDialog.getSaveFileName(None, 'Save file','/home',filter = '*.shp')
        self.HW_path = self.fname.replace('\\','/')
        self.lineEdit_3.setText(self.fname)
        print(self.HW_path)


    def create_HWR(self):
        self.Index_ = self.Wind_Select.currentIndex()
        if self.Index_ == 1:
            Driver2 = ogr.GetDriverByName('ESRI Shapefile')
            poly = str(self.footprint_path)
            polySource = Driver2.Open(poly,0)
            polyLayer = polySource.GetLayer()
            wind = str(self.wind_path)
            windSource = Driver2.Open(wind,0)
            windLayer = windSource.GetLayer()
            spatialReference = polyLayer.GetSpatialRef()
            HW = str(self.HW_path)
            PtSource = Driver2.CreateDataSource(HW) #so there we will store our data
            PtLayer = PtSource.CreateLayer('HWpts', spatialReference, ogr.wkbPoint) #this will create a corresponding layer for our data with given spatial information.
            layer_defn = PtLayer.GetLayerDefn() # gets parameters of the current shapefile
            new_field = ogr.FieldDefn('HWRatio', ogr.OFTReal)
            PtLayer.CreateField(new_field)
            lstPoints = []
            HWlst = []
            #output2 = str(self.output_path)
            lineSpacing = self.reso_val
            #sys.stdout = open(output2,'w') 
            #for wind in range(0,windLayer.GetFeatureCount()):
            for wind in range(0,windLayer.GetFeatureCount()):
                ptLst = []
                PolyIntersectSeq = []
                ptRefDict = {}
                BuildingIntersectSeq = []
                windFeature = windLayer.GetFeature(wind)
                windGeometry = windFeature.GetGeometryRef()
                IntersectPts = []
                HeightLst = []
                WidthLst = []
                height = 0
                IntersectPts = []
                for currentPoly in range (0,polyLayer.GetFeatureCount()):
                    currentPolyFeat = polyLayer.GetFeature(currentPoly)
                    currentPolyGeom = currentPolyFeat.GetGeometryRef()
                    FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                    if FirstIntersect.IsEmpty() == False:
                        PolyIntersectSeq.append(currentPolyFeat.GetFID())
                        if FirstIntersect.GetGeometryName() == 'MULTILINESTRING':
                            pt1 = ()
                            pt2 = ()
                            PT1 =[]
                            PT2 = []
                            print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                            points = FirstIntersect.GetEnvelope()
                            count = len(points)
                            for i in range(0,count,2):
                                pt1 = pt1 + (points[i],)
                                pt2 = pt2 + (points[i+1],)
                            PT1.append(pt1)
                            PT2.append(pt2)
                            ptLst.append(PT1)
                            ptLst.append(PT2)
                        elif FirstIntersect.GetGeometryName() == 'LINESTRING':
                            print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                            Points = FirstIntersect.GetPoints()
                            ptLst.append(Points)
                ptRefDict = dict(zip(PolyIntersectSeq,ptLst))                
                ptSort = sorted(ptLst,key = operator.itemgetter(0))
                print(ptSort)
                if len(ptSort) > 0 and len(ptRefDict) > 0:
                    for k in range(0,len(ptSort)):
                        firstBuildingXY = ptSort[k]
                        for key in ptRefDict.keys():
                            if  firstBuildingXY == ptRefDict[key]:
                                BuildingIntersectSeq.append(key)
                print(BuildingIntersectSeq)
                for i in range(0,len(BuildingIntersectSeq)):
                    HeightPoly = polyLayer.GetFeature(BuildingIntersectSeq[i])
                    HeightLst.append(HeightPoly.GetField('Height'))
                print(HeightLst)        
                for w in range(0,len(ptSort)):
                    pt = ptSort[w]
                    for z in range(len(pt)):
                        IntersectPts.append(pt[z])
                print('%%%%%%%%%%%%%',IntersectPts)
                if len(ptSort) > 1:
                    length = len(IntersectPts)-1
                    for xy in range(1,length,2):
                        PtSet1 = IntersectPts[xy]
                        PtSet2 = IntersectPts[xy+1]
                        x1 = PtSet1[0]
                        y1 = PtSet1[1]
                        x2 = PtSet2[0]
                        y2 = PtSet2[1]
                        midX = (x1+x2)/2
                        midY = (y1+y2)/2
                        print(midX,midY)
                        PolyWidth = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                        WidthLst.append(PolyWidth)
                        lstPoints.append([midX,midY])
                        pointGeom = ogr.Geometry(ogr.wkbPoint)
                        pointGeom.AddPoint(midX,midY)
                        Ptfeature = ogr.Feature(layer_defn)
                        Ptfeature.SetGeometry(pointGeom)
                        for x in range(0,len(WidthLst)):
                            print(WidthLst)
                            print(HeightLst)
                            Height1 = HeightLst[x]
                            Height2 = HeightLst[x+1]
                            AvgHeight = (Height1 + Height2)/2
                            hwRatio = AvgHeight/WidthLst[x]
                            HWlst.append(hwRatio)
                            Ptfeature.SetField('HWRatio',hwRatio)
                            PtLayer.CreateFeature(Ptfeature)
                            break
                print('\n**********************************************************************************')  
                        
        if self.Index_ == 2:
            Driver2 = ogr.GetDriverByName('ESRI Shapefile')
            poly = str(self.footprint_path)
            polySource = Driver2.Open(poly,0)
            polyLayer = polySource.GetLayer()
            wind = str(self.wind_path)
            windSource = Driver2.Open(wind,0)
            windLayer = windSource.GetLayer()
            spatialReference = polyLayer.GetSpatialRef()
            HW = str(self.HW_path)
            PtSource = Driver2.CreateDataSource(HW) #so there we will store our data
            PtLayer = PtSource.CreateLayer('HWpts', spatialReference, ogr.wkbPoint) #this will create a corresponding layer for our data with given spatial information.
            layer_defn = PtLayer.GetLayerDefn() # gets parameters of the current shapefile
            new_field = ogr.FieldDefn('HWRatio', ogr.OFTReal)
            PtLayer.CreateField(new_field)
            lstPoints = []
            HWlst = []
            #output2 = str(self.output_path)
            lineSpacing = self.reso_val
            #sys.stdout = open(output2,'w') 
            #for wind in range(0,windLayer.GetFeatureCount()):
            for wind in range(0,windLayer.GetFeatureCount()):
                ptLst = []
                PolyIntersectSeq = []
                ptRefDict = {}
                BuildingIntersectSeq = []
                windFeature = windLayer.GetFeature(wind)
                windGeometry = windFeature.GetGeometryRef()
                IntersectPts = []
                HeightLst = []
                WidthLst = []
                height = 0
                IntersectPts = []
                for currentPoly in range (0,polyLayer.GetFeatureCount()):
                    currentPolyFeat = polyLayer.GetFeature(currentPoly)
                    currentPolyGeom = currentPolyFeat.GetGeometryRef()
                    FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                    if FirstIntersect.IsEmpty() == False:
                        PolyIntersectSeq.append(currentPolyFeat.GetFID())
                        if FirstIntersect.GetGeometryName() == 'MULTILINESTRING':
                            pt1 = ()
                            pt2 = ()
                            PT1 =[]
                            PT2 = []
                            print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                            points = FirstIntersect.GetEnvelope()
                            count = len(points)
                            for i in range(0,count,2):
                                pt1 = pt1 + (points[i],)
                                pt2 = pt2 + (points[i+1],)
                            PT1.append(pt1)
                            PT2.append(pt2)
                            ptLst.append(PT1)
                            ptLst.append(PT2)
                        elif FirstIntersect.GetGeometryName() == 'LINESTRING':
                            print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                            Points = FirstIntersect.GetPoints()
                            ptLst.append(Points)
                ptRefDict = dict(zip(PolyIntersectSeq,ptLst))                
                ptSort = sorted(ptLst,key = operator.itemgetter(0), reverse =  True)
                print(ptSort)
                if len(ptSort) > 0 and len(ptRefDict) > 0:
                    for k in range(0,len(ptSort)):
                        firstBuildingXY = ptSort[k]
                        for key in ptRefDict.keys():
                            if  firstBuildingXY == ptRefDict[key]:
                                BuildingIntersectSeq.append(key)
                print(BuildingIntersectSeq)
                for i in range(0,len(BuildingIntersectSeq)):
                    HeightPoly = polyLayer.GetFeature(BuildingIntersectSeq[i])
                    HeightLst.append(HeightPoly.GetField('Height'))
                print(HeightLst)        
                for w in range(0,len(ptSort)):
                    pt = ptSort[w]
                    for z in range(len(pt)):
                        IntersectPts.append(pt[z])
                print('%%%%%%%%%%%%%',IntersectPts)
                if len(ptSort) > 1:
                    length = len(IntersectPts)-1
                    for xy in range(1,length,2):
                        PtSet1 = IntersectPts[xy]
                        PtSet2 = IntersectPts[xy+1]
                        x1 = PtSet1[0]
                        y1 = PtSet1[1]
                        x2 = PtSet2[0]
                        y2 = PtSet2[1]
                        midX = (x1+x2)/2
                        midY = (y1+y2)/2
                        print(midX,midY)
                        PolyWidth = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                        WidthLst.append(PolyWidth)
                        lstPoints.append([midX,midY])
                        pointGeom = ogr.Geometry(ogr.wkbPoint)
                        pointGeom.AddPoint(midX,midY)
                        Ptfeature = ogr.Feature(layer_defn)
                        Ptfeature.SetGeometry(pointGeom)
                        for x in range(0,len(WidthLst)):
                            print(WidthLst)
                            print(HeightLst)
                            Height1 = HeightLst[x]
                            Height2 = HeightLst[x+1]
                            AvgHeight = (Height1 + Height2)/2
                            hwRatio = AvgHeight/WidthLst[x]
                            HWlst.append(hwRatio)
                            Ptfeature.SetField('HWRatio',hwRatio)
                            PtLayer.CreateFeature(Ptfeature)
                            break
                print('\n**********************************************************************************') 
                                            
        if self.Index_ == 3:
            Driver2 = ogr.GetDriverByName('ESRI Shapefile')
            poly = str(self.footprint_path)
            polySource = Driver2.Open(poly,0)
            polyLayer = polySource.GetLayer()
            wind = str(self.wind_path)
            windSource = Driver2.Open(wind,0)
            windLayer = windSource.GetLayer()
            spatialReference = polyLayer.GetSpatialRef()
            HW = str(self.HW_path)
            PtSource = Driver2.CreateDataSource(HW) #so there we will store our data
            PtLayer = PtSource.CreateLayer('HWpts', spatialReference, ogr.wkbPoint) #this will create a corresponding layer for our data with given spatial information.
            layer_defn = PtLayer.GetLayerDefn() # gets parameters of the current shapefile
            new_field = ogr.FieldDefn('HWRatio', ogr.OFTReal)
            PtLayer.CreateField(new_field)
            lstPoints = []
            HWlst = []
            #output2 = str(self.output_path)
            lineSpacing = self.reso_val
            #sys.stdout = open(output2,'w') 
            #for wind in range(0,windLayer.GetFeatureCount()):
            for wind in range(0,windLayer.GetFeatureCount()):
                ptLst = []
                PolyIntersectSeq = []
                ptRefDict = {}
                BuildingIntersectSeq = []
                windFeature = windLayer.GetFeature(wind)
                windGeometry = windFeature.GetGeometryRef()
                IntersectPts = []
                HeightLst = []
                WidthLst = []
                height = 0
                IntersectPts = []
                for currentPoly in range (0,polyLayer.GetFeatureCount()):
                    currentPolyFeat = polyLayer.GetFeature(currentPoly)
                    currentPolyGeom = currentPolyFeat.GetGeometryRef()
                    FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                    if FirstIntersect.IsEmpty() == False:
                        PolyIntersectSeq.append(currentPolyFeat.GetFID())
                        if FirstIntersect.GetGeometryName() == 'MULTILINESTRING':
                            pt1 = ()
                            pt2 = ()
                            PT1 =[]
                            PT2 = []
                            print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                            points = FirstIntersect.GetEnvelope()
                            count = len(points)
                            for i in range(0,count,2):
                                pt1 = pt1 + (points[i],)
                                pt2 = pt2 + (points[i+1],)
                            PT1.append(pt1)
                            PT2.append(pt2)
                            ptLst.append(PT1)
                            ptLst.append(PT2)
                        elif FirstIntersect.GetGeometryName() == 'LINESTRING':
                            print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                            Points = FirstIntersect.GetPoints()
                            ptLst.append(Points)
                ptRefDict = dict(zip(PolyIntersectSeq,ptLst))                
                ptSort = sorted(ptLst,key = operator.itemgetter(0), reverse =  True)
                print(ptSort)
                if len(ptSort) > 0 and len(ptRefDict) > 0:
                    for k in range(0,len(ptSort)):
                        firstBuildingXY = ptSort[k]
                        for key in ptRefDict.keys():
                            if  firstBuildingXY == ptRefDict[key]:
                                BuildingIntersectSeq.append(key)
                print(BuildingIntersectSeq)
                for i in range(0,len(BuildingIntersectSeq)):
                    HeightPoly = polyLayer.GetFeature(BuildingIntersectSeq[i])
                    HeightLst.append(HeightPoly.GetField('Height'))
                print(HeightLst)        
                for w in range(0,len(ptSort)):
                    pt = ptSort[w]
                    for z in range(len(pt)):
                        IntersectPts.append(pt[z])
                print('%%%%%%%%%%%%%',IntersectPts)
                if len(ptSort) > 1:
                    length = len(IntersectPts)-1
                    for xy in range(1,length,2):
                        PtSet1 = IntersectPts[xy]
                        PtSet2 = IntersectPts[xy+1]
                        x1 = PtSet1[0]
                        y1 = PtSet1[1]
                        x2 = PtSet2[0]
                        y2 = PtSet2[1]
                        midX = (x1+x2)/2
                        midY = (y1+y2)/2
                        print(midX,midY)
                        PolyWidth = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                        WidthLst.append(PolyWidth)
                        lstPoints.append([midX,midY])
                        pointGeom = ogr.Geometry(ogr.wkbPoint)
                        pointGeom.AddPoint(midX,midY)
                        Ptfeature = ogr.Feature(layer_defn)
                        Ptfeature.SetGeometry(pointGeom)
                        for x in range(0,len(WidthLst)):
                            print(WidthLst)
                            print(HeightLst)
                            Height1 = HeightLst[x]
                            Height2 = HeightLst[x+1]
                            AvgHeight = (Height1 + Height2)/2
                            hwRatio = AvgHeight/WidthLst[x]
                            HWlst.append(hwRatio)
                            Ptfeature.SetField('HWRatio',hwRatio)
                            PtLayer.CreateFeature(Ptfeature)
                            break
                print('\n**********************************************************************************')
                

        if self.Index_ == 4:
            Driver2 = ogr.GetDriverByName('ESRI Shapefile')
            poly = str(self.footprint_path)
            polySource = Driver2.Open(poly,0)
            polyLayer = polySource.GetLayer()
            wind = str(self.wind_path)
            windSource = Driver2.Open(wind,0)
            windLayer = windSource.GetLayer()
            spatialReference = polyLayer.GetSpatialRef()
            HW = str(self.HW_path)
            PtSource = Driver2.CreateDataSource(HW) #so there we will store our data
            PtLayer = PtSource.CreateLayer('HWpts', spatialReference, ogr.wkbPoint) #this will create a corresponding layer for our data with given spatial information.
            layer_defn = PtLayer.GetLayerDefn() # gets parameters of the current shapefile
            new_field = ogr.FieldDefn('HWRatio', ogr.OFTReal)
            PtLayer.CreateField(new_field)
            lstPoints = []
            HWlst = []
            #output2 = str(self.output_path)
            lineSpacing = self.reso_val
            #sys.stdout = open(output2,'w') 
            #for wind in range(0,windLayer.GetFeatureCount()):
            for wind in range(0,windLayer.GetFeatureCount()):
                ptLst = []
                PolyIntersectSeq = []
                ptRefDict = {}
                BuildingIntersectSeq = []
                windFeature = windLayer.GetFeature(wind)
                windGeometry = windFeature.GetGeometryRef()
                IntersectPts = []
                HeightLst = []
                WidthLst = []
                height = 0
                IntersectPts = []
                for currentPoly in range (0,polyLayer.GetFeatureCount()):
                    currentPolyFeat = polyLayer.GetFeature(currentPoly)
                    currentPolyGeom = currentPolyFeat.GetGeometryRef()
                    FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                    if FirstIntersect.IsEmpty() == False:
                        PolyIntersectSeq.append(currentPolyFeat.GetFID())
                        if FirstIntersect.GetGeometryName() == 'MULTILINESTRING':
                            pt1 = ()
                            pt2 = ()
                            PT1 =[]
                            PT2 = []
                            print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                            points = FirstIntersect.GetEnvelope()
                            count = len(points)
                            for i in range(0,count,2):
                                pt1 = pt1 + (points[i],)
                                pt2 = pt2 + (points[i+1],)
                            PT1.append(pt1)
                            PT2.append(pt2)
                            ptLst.append(PT1)
                            ptLst.append(PT2)
                        elif FirstIntersect.GetGeometryName() == 'LINESTRING':
                            print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                            Points = FirstIntersect.GetPoints()
                            ptLst.append(Points)
                ptRefDict = dict(zip(PolyIntersectSeq,ptLst))                
                ptSort = sorted(ptLst,key = operator.itemgetter(0), reverse =  True)
                print(ptSort)
                if len(ptSort) > 0 and len(ptRefDict) > 0:
                    for k in range(0,len(ptSort)):
                        firstBuildingXY = ptSort[k]
                        for key in ptRefDict.keys():
                            if  firstBuildingXY == ptRefDict[key]:
                                BuildingIntersectSeq.append(key)
                print(BuildingIntersectSeq)
                for i in range(0,len(BuildingIntersectSeq)):
                    HeightPoly = polyLayer.GetFeature(BuildingIntersectSeq[i])
                    HeightLst.append(HeightPoly.GetField('Height'))
                print(HeightLst)        
                for w in range(0,len(ptSort)):
                    pt = ptSort[w]
                    for z in range(len(pt)):
                        IntersectPts.append(pt[z])
                print('%%%%%%%%%%%%%',IntersectPts)
                if len(ptSort) > 1:
                    length = len(IntersectPts)-1
                    for xy in range(1,length,2):
                        PtSet1 = IntersectPts[xy]
                        PtSet2 = IntersectPts[xy+1]
                        x1 = PtSet1[0]
                        y1 = PtSet1[1]
                        x2 = PtSet2[0]
                        y2 = PtSet2[1]
                        midX = (x1+x2)/2
                        midY = (y1+y2)/2
                        print(midX,midY)
                        PolyWidth = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                        WidthLst.append(PolyWidth)
                        lstPoints.append([midX,midY])
                        pointGeom = ogr.Geometry(ogr.wkbPoint)
                        pointGeom.AddPoint(midX,midY)
                        Ptfeature = ogr.Feature(layer_defn)
                        Ptfeature.SetGeometry(pointGeom)
                        for x in range(0,len(WidthLst)):
                            print(WidthLst)
                            print(HeightLst)
                            Height1 = HeightLst[x]
                            Height2 = HeightLst[x+1]
                            AvgHeight = (Height1 + Height2)/2
                            hwRatio = AvgHeight/WidthLst[x]
                            HWlst.append(hwRatio)
                            Ptfeature.SetField('HWRatio',hwRatio)
                            PtLayer.CreateFeature(Ptfeature)
                            break
                print('\n**********************************************************************************')
                
                
                
        if self.Index_ == 5:
            Driver2 = ogr.GetDriverByName('ESRI Shapefile')
            poly = str(self.footprint_path)
            polySource = Driver2.Open(poly,0)
            polyLayer = polySource.GetLayer()
            wind = str(self.wind_path)
            windSource = Driver2.Open(wind,0)
            windLayer = windSource.GetLayer()
            spatialReference = polyLayer.GetSpatialRef()
            HW = str(self.HW_path)
            PtSource = Driver2.CreateDataSource(HW) #so there we will store our data
            PtLayer = PtSource.CreateLayer('HWpts', spatialReference, ogr.wkbPoint) #this will create a corresponding layer for our data with given spatial information.
            layer_defn = PtLayer.GetLayerDefn() # gets parameters of the current shapefile
            new_field = ogr.FieldDefn('HWRatio', ogr.OFTReal)
            PtLayer.CreateField(new_field)
            lstPoints = []
            HWlst = []
            #output2 = str(self.output_path)
            lineSpacing = self.reso_val
            #sys.stdout = open(output2,'w') 
            #for wind in range(0,windLayer.GetFeatureCount()):
            for wind in range(0,windLayer.GetFeatureCount()):
                ptLst = []
                PolyIntersectSeq = []
                ptRefDict = {}
                BuildingIntersectSeq = []
                windFeature = windLayer.GetFeature(wind)
                windGeometry = windFeature.GetGeometryRef()
                IntersectPts = []
                HeightLst = []
                WidthLst = []
                height = 0
                IntersectPts = []
                for currentPoly in range (0,polyLayer.GetFeatureCount()):
                    currentPolyFeat = polyLayer.GetFeature(currentPoly)
                    currentPolyGeom = currentPolyFeat.GetGeometryRef()
                    FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                    if FirstIntersect.IsEmpty() == False:
                        PolyIntersectSeq.append(currentPolyFeat.GetFID())
                        if FirstIntersect.GetGeometryName() == 'MULTILINESTRING':
                            pt1 = ()
                            pt2 = ()
                            PT1 =[]
                            PT2 = []
                            print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                            points = FirstIntersect.GetEnvelope()
                            count = len(points)
                            for i in range(0,count,2):
                                pt1 = pt1 + (points[i],)
                                pt2 = pt2 + (points[i+1],)
                            PT1.append(pt1)
                            PT2.append(pt2)
                            ptLst.append(PT1)
                            ptLst.append(PT2)
                        elif FirstIntersect.GetGeometryName() == 'LINESTRING':
                            print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                            Points = FirstIntersect.GetPoints()
                            ptLst.append(Points)
                ptRefDict = dict(zip(PolyIntersectSeq,ptLst))                
                ptSort = sorted(ptLst,key = operator.itemgetter(0), reverse =  True)
                print(ptSort)
                if len(ptSort) > 0 and len(ptRefDict) > 0:
                    for k in range(0,len(ptSort)):
                        firstBuildingXY = ptSort[k]
                        for key in ptRefDict.keys():
                            if  firstBuildingXY == ptRefDict[key]:
                                BuildingIntersectSeq.append(key)
                print(BuildingIntersectSeq)
                for i in range(0,len(BuildingIntersectSeq)):
                    HeightPoly = polyLayer.GetFeature(BuildingIntersectSeq[i])
                    HeightLst.append(HeightPoly.GetField('Height'))
                print(HeightLst)        
                for w in range(0,len(ptSort)):
                    pt = ptSort[w]
                    for z in range(len(pt)):
                        IntersectPts.append(pt[z])
                print('%%%%%%%%%%%%%',IntersectPts)
                if len(ptSort) > 1:
                    length = len(IntersectPts)-1
                    for xy in range(1,length,2):
                        PtSet1 = IntersectPts[xy]
                        PtSet2 = IntersectPts[xy+1]
                        x1 = PtSet1[0]
                        y1 = PtSet1[1]
                        x2 = PtSet2[0]
                        y2 = PtSet2[1]
                        midX = (x1+x2)/2
                        midY = (y1+y2)/2
                        print(midX,midY)
                        PolyWidth = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                        WidthLst.append(PolyWidth)
                        lstPoints.append([midX,midY])
                        pointGeom = ogr.Geometry(ogr.wkbPoint)
                        pointGeom.AddPoint(midX,midY)
                        Ptfeature = ogr.Feature(layer_defn)
                        Ptfeature.SetGeometry(pointGeom)
                        for x in range(0,len(WidthLst)):
                            print(WidthLst)
                            print(HeightLst)
                            Height1 = HeightLst[x]
                            Height2 = HeightLst[x+1]
                            AvgHeight = (Height1 + Height2)/2
                            hwRatio = AvgHeight/WidthLst[x]
                            HWlst.append(hwRatio)
                            Ptfeature.SetField('HWRatio',hwRatio)
                            PtLayer.CreateFeature(Ptfeature)
                            break
                print('\n**********************************************************************************')
                
                
        if self.Index_ == 6:
            Driver2 = ogr.GetDriverByName('ESRI Shapefile')
            poly = str(self.footprint_path)
            polySource = Driver2.Open(poly,0)
            polyLayer = polySource.GetLayer()
            wind = str(self.wind_path)
            windSource = Driver2.Open(wind,0)
            windLayer = windSource.GetLayer()
            spatialReference = polyLayer.GetSpatialRef()
            HW = str(self.HW_path)
            PtSource = Driver2.CreateDataSource(HW) #so there we will store our data
            PtLayer = PtSource.CreateLayer('HWpts', spatialReference, ogr.wkbPoint) #this will create a corresponding layer for our data with given spatial information.
            layer_defn = PtLayer.GetLayerDefn() # gets parameters of the current shapefile
            new_field = ogr.FieldDefn('HWRatio', ogr.OFTReal)
            PtLayer.CreateField(new_field)
            lstPoints = []
            HWlst = []
            #output2 = str(self.output_path)
            lineSpacing = self.reso_val
            #sys.stdout = open(output2,'w') 
            #for wind in range(0,windLayer.GetFeatureCount()):
            for wind in range(0,windLayer.GetFeatureCount()):
                ptLst = []
                PolyIntersectSeq = []
                ptRefDict = {}
                BuildingIntersectSeq = []
                windFeature = windLayer.GetFeature(wind)
                windGeometry = windFeature.GetGeometryRef()
                IntersectPts = []
                HeightLst = []
                WidthLst = []
                height = 0
                IntersectPts = []
                for currentPoly in range (0,polyLayer.GetFeatureCount()):
                    currentPolyFeat = polyLayer.GetFeature(currentPoly)
                    currentPolyGeom = currentPolyFeat.GetGeometryRef()
                    FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                    if FirstIntersect.IsEmpty() == False:
                        PolyIntersectSeq.append(currentPolyFeat.GetFID())
                        if FirstIntersect.GetGeometryName() == 'MULTILINESTRING':
                            pt1 = ()
                            pt2 = ()
                            PT1 =[]
                            PT2 = []
                            print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                            points = FirstIntersect.GetEnvelope()
                            count = len(points)
                            for i in range(0,count,2):
                                pt1 = pt1 + (points[i],)
                                pt2 = pt2 + (points[i+1],)
                            PT1.append(pt1)
                            PT2.append(pt2)
                            ptLst.append(PT1)
                            ptLst.append(PT2)
                        elif FirstIntersect.GetGeometryName() == 'LINESTRING':
                            print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                            Points = FirstIntersect.GetPoints()
                            ptLst.append(Points)
                ptRefDict = dict(zip(PolyIntersectSeq,ptLst))                
                ptSort = sorted(ptLst,key = operator.itemgetter(0))
                print(ptSort)
                if len(ptSort) > 0 and len(ptRefDict) > 0:
                    for k in range(0,len(ptSort)):
                        firstBuildingXY = ptSort[k]
                        for key in ptRefDict.keys():
                            if  firstBuildingXY == ptRefDict[key]:
                                BuildingIntersectSeq.append(key)
                print(BuildingIntersectSeq)
                for i in range(0,len(BuildingIntersectSeq)):
                    HeightPoly = polyLayer.GetFeature(BuildingIntersectSeq[i])
                    HeightLst.append(HeightPoly.GetField('Height'))
                print(HeightLst)        
                for w in range(0,len(ptSort)):
                    pt = ptSort[w]
                    for z in range(len(pt)):
                        IntersectPts.append(pt[z])
                print('%%%%%%%%%%%%%',IntersectPts)
                if len(ptSort) > 1:
                    length = len(IntersectPts)-1
                    for xy in range(1,length,2):
                        PtSet1 = IntersectPts[xy]
                        PtSet2 = IntersectPts[xy+1]
                        x1 = PtSet1[0]
                        y1 = PtSet1[1]
                        x2 = PtSet2[0]
                        y2 = PtSet2[1]
                        midX = (x1+x2)/2
                        midY = (y1+y2)/2
                        print(midX,midY)
                        PolyWidth = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                        WidthLst.append(PolyWidth)
                        lstPoints.append([midX,midY])
                        pointGeom = ogr.Geometry(ogr.wkbPoint)
                        pointGeom.AddPoint(midX,midY)
                        Ptfeature = ogr.Feature(layer_defn)
                        Ptfeature.SetGeometry(pointGeom)
                        for x in range(0,len(WidthLst)):
                            print(WidthLst)
                            print(HeightLst)
                            Height1 = HeightLst[x]
                            Height2 = HeightLst[x+1]
                            AvgHeight = (Height1 + Height2)/2
                            hwRatio = AvgHeight/WidthLst[x]
                            HWlst.append(hwRatio)
                            Ptfeature.SetField('HWRatio',hwRatio)
                            PtLayer.CreateFeature(Ptfeature)
                            break
                print('\n**********************************************************************************')
                

        if self.Index_ == 7:
            Driver2 = ogr.GetDriverByName('ESRI Shapefile')
            poly = str(self.footprint_path)
            polySource = Driver2.Open(poly,0)
            polyLayer = polySource.GetLayer()
            wind = str(self.wind_path)
            windSource = Driver2.Open(wind,0)
            windLayer = windSource.GetLayer()
            spatialReference = polyLayer.GetSpatialRef()
            HW = str(self.HW_path)
            PtSource = Driver2.CreateDataSource(HW) #so there we will store our data
            PtLayer = PtSource.CreateLayer('HWpts', spatialReference, ogr.wkbPoint) #this will create a corresponding layer for our data with given spatial information.
            layer_defn = PtLayer.GetLayerDefn() # gets parameters of the current shapefile
            new_field = ogr.FieldDefn('HWRatio', ogr.OFTReal)
            PtLayer.CreateField(new_field)
            lstPoints = []
            HWlst = []
            #output2 = str(self.output_path)
            lineSpacing = self.reso_val
            #sys.stdout = open(output2,'w') 
            #for wind in range(0,windLayer.GetFeatureCount()):
            for wind in range(0,windLayer.GetFeatureCount()):
                ptLst = []
                PolyIntersectSeq = []
                ptRefDict = {}
                BuildingIntersectSeq = []
                windFeature = windLayer.GetFeature(wind)
                windGeometry = windFeature.GetGeometryRef()
                IntersectPts = []
                HeightLst = []
                WidthLst = []
                height = 0
                IntersectPts = []
                for currentPoly in range (0,polyLayer.GetFeatureCount()):
                    currentPolyFeat = polyLayer.GetFeature(currentPoly)
                    currentPolyGeom = currentPolyFeat.GetGeometryRef()
                    FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                    if FirstIntersect.IsEmpty() == False:
                        PolyIntersectSeq.append(currentPolyFeat.GetFID())
                        if FirstIntersect.GetGeometryName() == 'MULTILINESTRING':
                            pt1 = ()
                            pt2 = ()
                            PT1 =[]
                            PT2 = []
                            print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                            points = FirstIntersect.GetEnvelope()
                            count = len(points)
                            for i in range(0,count,2):
                                pt1 = pt1 + (points[i],)
                                pt2 = pt2 + (points[i+1],)
                            PT1.append(pt1)
                            PT2.append(pt2)
                            ptLst.append(PT1)
                            ptLst.append(PT2)
                        elif FirstIntersect.GetGeometryName() == 'LINESTRING':
                            print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                            Points = FirstIntersect.GetPoints()
                            ptLst.append(Points)
                ptRefDict = dict(zip(PolyIntersectSeq,ptLst))                
                ptSort = sorted(ptLst,key = operator.itemgetter(0))
                print(ptSort)
                if len(ptSort) > 0 and len(ptRefDict) > 0:
                    for k in range(0,len(ptSort)):
                        firstBuildingXY = ptSort[k]
                        for key in ptRefDict.keys():
                            if  firstBuildingXY == ptRefDict[key]:
                                BuildingIntersectSeq.append(key)
                print(BuildingIntersectSeq)
                for i in range(0,len(BuildingIntersectSeq)):
                    HeightPoly = polyLayer.GetFeature(BuildingIntersectSeq[i])
                    HeightLst.append(HeightPoly.GetField('Height'))
                print(HeightLst)        
                for w in range(0,len(ptSort)):
                    pt = ptSort[w]
                    for z in range(len(pt)):
                        IntersectPts.append(pt[z])
                print('%%%%%%%%%%%%%',IntersectPts)
                if len(ptSort) > 1:
                    length = len(IntersectPts)-1
                    for xy in range(1,length,2):
                        PtSet1 = IntersectPts[xy]
                        PtSet2 = IntersectPts[xy+1]
                        x1 = PtSet1[0]
                        y1 = PtSet1[1]
                        x2 = PtSet2[0]
                        y2 = PtSet2[1]
                        midX = (x1+x2)/2
                        midY = (y1+y2)/2
                        print(midX,midY)
                        PolyWidth = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                        WidthLst.append(PolyWidth)
                        lstPoints.append([midX,midY])
                        pointGeom = ogr.Geometry(ogr.wkbPoint)
                        pointGeom.AddPoint(midX,midY)
                        Ptfeature = ogr.Feature(layer_defn)
                        Ptfeature.SetGeometry(pointGeom)
                        for x in range(0,len(WidthLst)):
                            print(WidthLst)
                            print(HeightLst)
                            Height1 = HeightLst[x]
                            Height2 = HeightLst[x+1]
                            AvgHeight = (Height1 + Height2)/2
                            hwRatio = AvgHeight/WidthLst[x]
                            HWlst.append(hwRatio)
                            Ptfeature.SetField('HWRatio',hwRatio)
                            PtLayer.CreateFeature(Ptfeature)
                            break
                print('\n**********************************************************************************')
                    
        if self.Index_ == 8:
            Driver2 = ogr.GetDriverByName('ESRI Shapefile')
            poly = str(self.footprint_path)
            polySource = Driver2.Open(poly,0)
            polyLayer = polySource.GetLayer()
            wind = str(self.wind_path)
            windSource = Driver2.Open(wind,0)
            windLayer = windSource.GetLayer()
            spatialReference = polyLayer.GetSpatialRef()
            HW = str(self.HW_path)
            PtSource = Driver2.CreateDataSource(HW) #so there we will store our data
            PtLayer = PtSource.CreateLayer('HWpts', spatialReference, ogr.wkbPoint) #this will create a corresponding layer for our data with given spatial information.
            layer_defn = PtLayer.GetLayerDefn() # gets parameters of the current shapefile
            new_field = ogr.FieldDefn('HWRatio', ogr.OFTReal)
            PtLayer.CreateField(new_field)
            lstPoints = []
            HWlst = []
            #output2 =str (self.output_path)
            lineSpacing = self.reso_val
            #sys.stdout = open(output2,'w') 
            #for wind in range(0,windLayer.GetFeatureCount()):
            for wind in range(0,windLayer.GetFeatureCount()):
                ptLst = []
                PolyIntersectSeq = []
                ptRefDict = {}
                BuildingIntersectSeq = []
                windFeature = windLayer.GetFeature(wind)
                windGeometry = windFeature.GetGeometryRef()
                IntersectPts = []
                HeightLst = []
                WidthLst = []
                height = 0
                IntersectPts = []
                for currentPoly in range (0,polyLayer.GetFeatureCount()):
                    currentPolyFeat = polyLayer.GetFeature(currentPoly)
                    currentPolyGeom = currentPolyFeat.GetGeometryRef()
                    FirstIntersect = windGeometry.Intersection(currentPolyGeom)
                    if FirstIntersect.IsEmpty() == False:
                        PolyIntersectSeq.append(currentPolyFeat.GetFID())
                        if FirstIntersect.GetGeometryName() == 'MULTILINESTRING':
                            pt1 = ()
                            pt2 = ()
                            PT1 =[]
                            PT2 = []
                            print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                            points = FirstIntersect.GetEnvelope()
                            count = len(points)
                            for i in range(0,count,2):
                                pt1 = pt1 + (points[i],)
                                pt2 = pt2 + (points[i+1],)
                            PT1.append(pt1)
                            PT2.append(pt2)
                            ptLst.append(PT1)
                            ptLst.append(PT2)
                        elif FirstIntersect.GetGeometryName() == 'LINESTRING':
                            print('Building ',currentPolyFeat.GetFID(),'intersects windline ',windFeature.GetFID(),'at the following points \n', FirstIntersect)
                            Points = FirstIntersect.GetPoints()
                            ptLst.append(Points)
                ptRefDict = dict(zip(PolyIntersectSeq,ptLst))                
                ptSort = sorted(ptLst,key = operator.itemgetter(0))
                print(ptSort)
                if len(ptSort) > 0 and len(ptRefDict) > 0:
                    for k in range(0,len(ptSort)):
                        firstBuildingXY = ptSort[k]
                        for key in ptRefDict.keys():
                            if  firstBuildingXY == ptRefDict[key]:
                                BuildingIntersectSeq.append(key)
                print(BuildingIntersectSeq)
                for i in range(0,len(BuildingIntersectSeq)):
                    HeightPoly = polyLayer.GetFeature(BuildingIntersectSeq[i])
                    HeightLst.append(HeightPoly.GetField('Height'))
                print(HeightLst)        
                for w in range(0,len(ptSort)):
                    pt = ptSort[w]
                    for z in range(len(pt)):
                        IntersectPts.append(pt[z])
                print('%%%%%%%%%%%%%',IntersectPts)
                if len(ptSort) > 1:
                    length = len(IntersectPts)-1
                    for xy in range(1,length,2):
                        PtSet1 = IntersectPts[xy]
                        PtSet2 = IntersectPts[xy+1]
                        x1 = PtSet1[0]
                        y1 = PtSet1[1]
                        x2 = PtSet2[0]
                        y2 = PtSet2[1]
                        midX = (x1+x2)/2
                        midY = (y1+y2)/2
                        print(midX,midY)
                        PolyWidth = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                        WidthLst.append(PolyWidth)
                        lstPoints.append([midX,midY])
                        pointGeom = ogr.Geometry(ogr.wkbPoint)
                        pointGeom.AddPoint(midX,midY)
                        Ptfeature = ogr.Feature(layer_defn)
                        Ptfeature.SetGeometry(pointGeom)
                        for x in range(0,len(WidthLst)):
                            print(WidthLst)
                            print(HeightLst)
                            Height1 = HeightLst[x]
                            Height2 = HeightLst[x+1]
                            AvgHeight = (Height1 + Height2)/2
                            hwRatio = AvgHeight/WidthLst[x]
                            HWlst.append(hwRatio)
                            Ptfeature.SetField('HWRatio',hwRatio)
                            PtLayer.CreateFeature(Ptfeature)
                            break
                print('\n**********************************************************************************')



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
