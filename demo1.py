# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_URPMainWindow(object):
    def setupUi(self, URPMainWindow):
        URPMainWindow.setObjectName("URPMainWindow")
        URPMainWindow.resize(1279, 714)
        self.centralwidget = QtWidgets.QWidget(URPMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(390, 10, 881, 681))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setStyleSheet("QTabBar::tab{width:100;height:30}\n"
"QTabBar::tab{font: 75 10pt \"等线\"}\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_main = QtWidgets.QWidget()
        self.tab_main.setObjectName("tab_main")
        self.tabWidget.addTab(self.tab_main, "")
        self.tab_illum = QtWidgets.QWidget()
        self.tab_illum.setObjectName("tab_illum")
        self.tab_illum_label1 = QtWidgets.QLabel(self.tab_illum)
        self.tab_illum_label1.setGeometry(QtCore.QRect(-70, 10, 1021, 261))
        self.tab_illum_label1.setText("")
        self.tab_illum_label1.setObjectName("tab_illum_label1")
        self.tab_illum_button1 = QtWidgets.QPushButton(self.tab_illum)
        self.tab_illum_button1.setGeometry(QtCore.QRect(10, 580, 51, 31))
        self.tab_illum_button1.setObjectName("tab_illum_button1")
        self.tabWidget.addTab(self.tab_illum, "")
        self.tab_hum = QtWidgets.QWidget()
        self.tab_hum.setObjectName("tab_hum")
        self.tab_hum_label1 = QtWidgets.QLabel(self.tab_hum)
        self.tab_hum_label1.setGeometry(QtCore.QRect(-70, 10, 1021, 261))
        self.tab_hum_label1.setText("")
        self.tab_hum_label1.setObjectName("tab_hum_label1")
        self.tabWidget.addTab(self.tab_hum, "")
        self.tab_temp = QtWidgets.QWidget()
        self.tab_temp.setObjectName("tab_temp")
        self.tab_temp_label1 = QtWidgets.QLabel(self.tab_temp)
        self.tab_temp_label1.setGeometry(QtCore.QRect(-70, 10, 1021, 261))
        self.tab_temp_label1.setText("")
        self.tab_temp_label1.setObjectName("tab_temp_label1")
        self.tabWidget.addTab(self.tab_temp, "")
        self.tab_co2 = QtWidgets.QWidget()
        self.tab_co2.setObjectName("tab_co2")
        self.tab_co2_label1 = QtWidgets.QLabel(self.tab_co2)
        self.tab_co2_label1.setGeometry(QtCore.QRect(-70, 10, 1021, 261))
        self.tab_co2_label1.setText("")
        self.tab_co2_label1.setObjectName("tab_co2_label1")
        self.tabWidget.addTab(self.tab_co2, "")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 371, 681))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox_currentState = QtWidgets.QGroupBox(self.frame)
        self.groupBox_currentState.setEnabled(True)
        self.groupBox_currentState.setGeometry(QtCore.QRect(10, 10, 351, 261))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_currentState.setFont(font)
        self.groupBox_currentState.setObjectName("groupBox_currentState")
        self.groupBox_illum = QtWidgets.QGroupBox(self.groupBox_currentState)
        self.groupBox_illum.setGeometry(QtCore.QRect(30, 40, 131, 91))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.groupBox_illum.setFont(font)
        self.groupBox_illum.setObjectName("groupBox_illum")
        self.label_illum = QtWidgets.QLabel(self.groupBox_illum)
        self.label_illum.setGeometry(QtCore.QRect(10, 30, 111, 51))
        self.label_illum.setTextFormat(QtCore.Qt.AutoText)
        self.label_illum.setObjectName("label_illum")
        self.groupBox_hum = QtWidgets.QGroupBox(self.groupBox_currentState)
        self.groupBox_hum.setGeometry(QtCore.QRect(190, 40, 131, 91))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_hum.setFont(font)
        self.groupBox_hum.setObjectName("groupBox_hum")
        self.label_hum = QtWidgets.QLabel(self.groupBox_hum)
        self.label_hum.setGeometry(QtCore.QRect(10, 30, 111, 51))
        self.label_hum.setTextFormat(QtCore.Qt.AutoText)
        self.label_hum.setObjectName("label_hum")
        self.groupBox_temp = QtWidgets.QGroupBox(self.groupBox_currentState)
        self.groupBox_temp.setGeometry(QtCore.QRect(30, 150, 131, 91))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.groupBox_temp.setFont(font)
        self.groupBox_temp.setObjectName("groupBox_temp")
        self.label_temp = QtWidgets.QLabel(self.groupBox_temp)
        self.label_temp.setGeometry(QtCore.QRect(10, 30, 111, 51))
        self.label_temp.setTextFormat(QtCore.Qt.AutoText)
        self.label_temp.setObjectName("label_temp")
        self.groupBox_co2 = QtWidgets.QGroupBox(self.groupBox_currentState)
        self.groupBox_co2.setGeometry(QtCore.QRect(190, 150, 131, 91))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.groupBox_co2.setFont(font)
        self.groupBox_co2.setObjectName("groupBox_co2")
        self.label_co2 = QtWidgets.QLabel(self.groupBox_co2)
        self.label_co2.setGeometry(QtCore.QRect(10, 30, 111, 51))
        self.label_co2.setTextFormat(QtCore.Qt.AutoText)
        self.label_co2.setObjectName("label_co2")
        URPMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(URPMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1279, 26))
        self.menubar.setObjectName("menubar")
        URPMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(URPMainWindow)
        self.statusbar.setObjectName("statusbar")
        URPMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(URPMainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(URPMainWindow)

    def retranslateUi(self, URPMainWindow):
        _translate = QtCore.QCoreApplication.translate
        URPMainWindow.setWindowTitle(_translate("URPMainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), _translate("URPMainWindow", "主页"))
        self.tab_illum_button1.setText(_translate("URPMainWindow", "刷新"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_illum), _translate("URPMainWindow", "光照"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hum), _translate("URPMainWindow", "湿度"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_temp), _translate("URPMainWindow", "温度"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_co2), _translate("URPMainWindow", "二氧化碳"))
        self.groupBox_currentState.setTitle(_translate("URPMainWindow", "Current State"))
        self.groupBox_illum.setTitle(_translate("URPMainWindow", "光照/lux"))
        self.label_illum.setText(_translate("URPMainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:20pt; color:#55aaff;\">NULL</span></p></body></html>"))
        self.groupBox_hum.setTitle(_translate("URPMainWindow", "湿度/%"))
        self.label_hum.setText(_translate("URPMainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:20pt; color:#55aaff;\">NULL</span></p></body></html>"))
        self.groupBox_temp.setTitle(_translate("URPMainWindow", "温度/℃"))
        self.label_temp.setText(_translate("URPMainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:20pt; color:#55aaff;\">NULL</span></p></body></html>"))
        self.groupBox_co2.setTitle(_translate("URPMainWindow", "二氧化碳/ppm"))
        self.label_co2.setText(_translate("URPMainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:20pt; color:#55aaff;\">NULL</span></p></body></html>"))

import test_rc
