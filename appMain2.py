import sys

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, QThread, QObject, QDateTime, QTimer, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout
from demo1 import Ui_URPMainWindow

import serial
import time

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.style as mplStyle

import sqlite3

# 以类的方式创建线程，实时访问数据库，并为界面的实时刷新做准备
class BackendThread(QThread):
    serial_data = pyqtSignal(str)

    def __init__(self):
        super(BackendThread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        # ser = serial.Serial('com7', 9600)
        k = 0
        while True:
            try:
                if k == 0:
                    ser = serial.Serial('com9', 9600)  # 串口可能是com10也可能是com9也可能是其他
                if ser.isOpen():
                    print("open serial successfully")
                    data = ser.readline()
                    data = data.decode()
                    data = data.strip("\r\n").split(" ")
                    dataf = [float(x) for x in data]
                    s_data = str(dataf[0]) + " " + str(dataf[1]) + " " + str(dataf[2]) + " " + str(dataf[4])
                    k = 1
                else:
                    print("can't open serial")
                    s_data = "NULL NULL NULL NULL"
                    k = 0
            except:
                print("There is no serial!")
                s_data = "NULL NULL NULL NULL"
                k = 0

            print(s_data)
            self.serial_data.emit(s_data)
            time.sleep(0.1)

# 以类的方式创建光照界面中绘制曲线的画布，为后续在界面中绘图做准备
class Canvas_illum(FigureCanvas):
    def __init__(self):
        fig = Figure()
        FigureCanvas.__init__(self, fig)
        self.axes = fig.add_subplot(1,1,1,label = "plot1")

    def draw_1(self, datax, datay):
        datax_1 = []
        datax_2 = []
        for i in range(len(datax)):
            datax_1.append(datax[i].split("/"))
        for i in range(len(datax_1)):
            datax_2.append(datax_1[i][3]+"/"+datax_1[i][4])

        self.axes.plot(datax_2, datay, linewidth = 2, color = 'mediumturquoise')
        self.axes.set_title('Illumination in 24 Hours')
        # self.axes.set_xlabel('X(m)')
        # self.axes.set_ylabel('lux')
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['bottom'].set_visible(False)
        self.axes.spines['left'].set_visible(False)
        self.axes.grid(axis="y",c = "lightsteelblue",alpha = 0.5, linewidth = 1.5)
        self.axes.set_ylim([0, 300])
        self.draw()

# 以类的方式创建湿度界面中绘制曲线的画布，为后续在界面中绘图做准备
class Canvas_hum(FigureCanvas):
    def __init__(self):
        fig = Figure()
        FigureCanvas.__init__(self, fig)
        self.axes = fig.add_subplot(1,1,1,label = "plot1")

    def draw_1(self, datax, datay):
        datax_1 = []
        datax_2 = []
        for i in range(len(datax)):
            datax_1.append(datax[i].split("/"))
        for i in range(len(datax_1)):
            datax_2.append(datax_1[i][3] + "/" + datax_1[i][4])

        self.axes.plot(datax_2, datay, linewidth = 2, color = 'mediumturquoise')
        self.axes.set_title('Humidity(air) in 24 Hours')
        # self.axes.set_xlabel('X(m)')
        # self.axes.set_ylabel('%')

        self.axes.spines['right'].set_visible(False)
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['bottom'].set_visible(False)
        self.axes.spines['left'].set_visible(False)
        self.axes.grid(axis="y",c = "lightsteelblue",alpha = 0.5, linewidth = 1.5)
        self.axes.set_ylim([20,80])
        self.draw()

# 以类的方式创建温度界面中绘制曲线的画布，为后续在界面中绘图做准备
class Canvas_temp(FigureCanvas):
    def __init__(self):
        fig = Figure()
        FigureCanvas.__init__(self, fig)
        self.axes = fig.add_subplot(1,1,1,label = "plot1")

    def draw_1(self, datax, datay):
        datax_1 = []
        datax_2 = []
        for i in range(len(datax)):
            datax_1.append(datax[i].split("/"))
        for i in range(len(datax_1)):
            datax_2.append(datax_1[i][3] + "/" + datax_1[i][4])

        self.axes.plot(datax_2, datay, linewidth = 2, color = 'mediumturquoise')
        self.axes.set_title('Temperature in 24 Hours')
        # self.axes.set_xlabel('X(m)')
        # self.axes.set_ylabel('℃')
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['bottom'].set_visible(False)
        self.axes.spines['left'].set_visible(False)
        self.axes.grid(axis="y",c = "lightsteelblue",alpha = 0.5, linewidth = 1.5)
        self.axes.set_ylim([-20, 40])
        self.draw()

# 以类的方式创建CO2界面中绘制曲线的画布，为后续在界面中绘图做准备
class Canvas_co2(FigureCanvas):
    def __init__(self):
        fig = Figure()
        FigureCanvas.__init__(self, fig)
        self.axes = fig.add_subplot(1,1,1,label = "plot1")

    def draw_1(self, datax, datay):
        datax_1 = []
        datax_2 = []
        for i in range(len(datax)):
            datax_1.append(datax[i].split("/"))
        for i in range(len(datax_1)):
            datax_2.append(datax_1[i][3] + "/" + datax_1[i][4])

        self.axes.plot(datax_2, datay, linewidth = 2, color = 'mediumturquoise')
        self.axes.set_title('CO2(air) in 24 Hours')
        # self.axes.set_xlabel('X(m)')
        # self.axes.set_ylabel('ppm')
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['bottom'].set_visible(False)
        self.axes.spines['left'].set_visible(False)
        self.axes.grid(axis="y",c = "lightsteelblue",alpha = 0.5, linewidth = 1.5)
        self.axes.set_ylim([200, 1000])
        self.draw()

# 窗口类
class QmyMainWindow(QMainWindow):

    # 初始化
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_URPMainWindow()
        self.ui.setupUi(self)
        self.updateUI()

        self.query_SqlData()

        self.set_tab_illum_label1()
        self.set_tab_hum_label1()
        self.set_tab_temp_label1()
        self.set_tab_co2_label1()

    # 以下函数访问数据库中相关数据
    def query_SqlData(self):
        self.conn = sqlite3.connect('test.db')
        print("Open database successfully")
        self.cursor = self.conn.execute("SELECT * from demo")
        self.sqlData_time = []
        self.sqlData_illum = []
        self.sqlData_hum = []
        self.sqlData_temp = []
        self.sqlData_co2 = []
        for it in self.cursor:
            self.sqlData_time.append(it[0])
            self.sqlData_illum.append(it[1])
            self.sqlData_hum.append(it[2])
            self.sqlData_temp.append(it[3])
            self.sqlData_co2.append(it[4])

    # 以下函数根据数据库中数据在光照相关界面绘制曲线
    def set_tab_illum_label1(self):
        self.plot1 = Canvas_illum()
        self.plot1.draw_1(self.sqlData_time,self.sqlData_illum)
        layout = QVBoxLayout()
        layout.addWidget(self.plot1)
        self.ui.tab_illum_label1.setLayout(layout)
        self.ui.tab_illum_label1.show()

    # 以下函数根据数据库中数据在湿度相关界面绘制曲线
    def set_tab_hum_label1(self):
        self.plot2 = Canvas_hum()
        self.plot2.draw_1(self.sqlData_time, self.sqlData_hum)
        layout = QVBoxLayout()
        layout.addWidget(self.plot2)
        self.ui.tab_hum_label1.setLayout(layout)
        self.ui.tab_hum_label1.show()

    # 以下函数根据数据库中数据在温度相关界面绘制曲线
    def set_tab_temp_label1(self):
        self.plot3 = Canvas_temp()
        self.plot3.draw_1(self.sqlData_time, self.sqlData_temp)
        layout = QVBoxLayout()
        layout.addWidget(self.plot3)
        self.ui.tab_temp_label1.setLayout(layout)
        self.ui.tab_temp_label1.show()

    # 以下函数根据数据库中数据在CO2相关界面绘制曲线
    def set_tab_co2_label1(self):
        self.plot4 = Canvas_co2()
        self.plot4.draw_1(self.sqlData_time, self.sqlData_co2)
        layout = QVBoxLayout()
        layout.addWidget(self.plot4)
        self.ui.tab_co2_label1.setLayout(layout)
        self.ui.tab_co2_label1.show()

    # 以下函数调用线程，实时更新相关数据
    def updateUI(self):
        self.thread = BackendThread()
        self.thread.serial_data.connect(self.showData)
        self.thread.start()

    # 以下函数用于在界面左上角的四个label中实时显示相关数据
    def showData(self,s_data):

        self.Lab = s_data.split(" ")

        _translate = QtCore.QCoreApplication.translate
        self.Lab_illum = self.Lab[0]
        self.Lab_hum = self.Lab[1]
        self.Lab_temp = self.Lab[2]
        self.Lab_co2 = self.Lab[3]

        # 设置label中字体样式
        self.ui.label_illum.setText(_translate("URPMainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; color:#55aaff;\">%s</span></p></body></html>") % self.Lab_illum)
        self.ui.label_hum.setText(_translate("URPMainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                             "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; color:#55aaff;\">%s</span></p></body></html>") % self.Lab_hum)
        self.ui.label_temp.setText(_translate("URPMainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; color:#55aaff;\">%s</span></p></body></html>") % self.Lab_temp)
        self.ui.label_co2.setText(_translate("URPMainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                             "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; color:#55aaff;\">%s</span></p></body></html>") % self.Lab_co2)


# 主函数
if __name__=="__main__":
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.setWindowTitle("基于环境监测的物联网系统")
    form.show()
    # myWidget.btnClose.setText("不关闭了")
    sys.exit(app.exec_())





