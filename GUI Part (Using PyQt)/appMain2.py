
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
                    ser = serial.Serial('com10', 9600)
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


class Canvas_illum(FigureCanvas):
    def __init__(self):
        self.fig = Figure()

        FigureCanvas.__init__(self, self.fig)
        self.axes = self.fig.add_subplot(1,1,1,label = "plot1")

    def draw_1(self, datax, datay):
        datax_1 = []
        datax_2 = []
        for i in range(len(datax)):
            datax_1.append(datax[i].split("/"))
        for i in range(len(datax_1)):
            datax_2.append(datax_1[i][3]+"/"+datax_1[i][4])

        self.axes.plot(datax_2, datay, linewidth = 2, marker = 'o', color = 'mediumturquoise')

        # self.axes.set_xlabel('X(m)')
        # self.axes.set_ylabel('lux')
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['top'].set_visible(False)
        # self.axes.spines['bottom'].set_visible(False)
        # self.axes.spines['left'].set_visible(False)

        self.axes.spines['bottom'].set_color('lightsteelblue')
        self.axes.spines['bottom'].set_alpha(0.7)
        self.axes.spines['bottom'].set_linewidth(1.5)
        self.axes.spines['left'].set_color('lightsteelblue')
        self.axes.spines['left'].set_alpha(0.7)
        self.axes.spines['left'].set_linewidth(1.5)

        self.axes.set_ylim(min(datay)-0.05,max(datay)+0.05)

        self.axes.grid(axis="y",c = "lightsteelblue",alpha = 0.5, linewidth = 1.5)

        self.axes.tick_params(labelsize='small', colors = 'darkcyan')

        # self.axes.set_ylim([0, 300])

        self.fig.tight_layout()
        self.draw()

class Canvas_illum2(FigureCanvas):
    def __init__(self):
        self.fig = Figure()

        FigureCanvas.__init__(self, self.fig)
        self.axes = self.fig.add_subplot(1,1,1,label = "plot1")

    def draw_1(self, datax, datay):
        datax_1 = []
        datax_2 = []
        for i in range(len(datax)):
            datax_1.append(datax[i].split("/"))
        for i in range(len(datax_1)):
            datax_2.append(datax_1[i][3]+"/"+datax_1[i][4])

        # self.axes.grid(axis="y", c="lightsteelblue", alpha=0.5, linewidth=1.5)
        self.axes.bar(datax_2, datay,color = 'mediumturquoise')
        for x,y in zip(datax_2,datay):
            self.axes.text(x, y, '%.1f' % float(y), ha='center',va='bottom', color = 'darkcyan' )

        self.axes.spines['right'].set_visible(False)
        self.axes.spines['top'].set_visible(False)

        self.axes.spines['bottom'].set_color('lightsteelblue')
        self.axes.spines['bottom'].set_alpha(0.7)
        self.axes.spines['bottom'].set_linewidth(1.5)
        self.axes.spines['left'].set_color('lightsteelblue')
        self.axes.spines['left'].set_alpha(0.7)
        self.axes.spines['left'].set_linewidth(1.5)

        self.axes.tick_params(colors='darkcyan')

        # self.axes.set_title('Illumination in 7 Days')

        self.fig.tight_layout()
        self.draw()

class Canvas_illum3(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)
        self.axes = self.fig.add_subplot(1,1,1,label = "plot1")

    def draw_1(self, datax, datay):
        datax_1 = []
        datax_2 = []
        for i in range(len(datax)):
            datax_1.append(datax[i].split("/"))
        for i in range(len(datax_1)):
            datax_2.append(datax_1[i][3]+"/"+datax_1[i][4])

        low = 0
        mid = 0
        high = 0
        for i in range(len(datay)):
            if datay[i]<25:
                low = low+1
            elif datay[i]<27:
                mid = mid+1
            else:
                high = high+1
        values = [low,mid,high]
        explode = [0.01, 0.01, 0.01]
        label = ['low','mid','high']
        self.axes.pie(values, radius = 1, wedgeprops=dict(width=0.4,edgecolor='w'),explode=explode,colors = ['lightskyblue','mediumspringgreen','coral'],labels = label, autopct='%1.1f%%')  # 绘制饼图

        # self.axes.set_title("Statistics")

        self.fig.tight_layout()
        self.draw()

class Canvas_hum(FigureCanvas):
    def __init__(self):
        self.fig = Figure()

        FigureCanvas.__init__(self, self.fig)
        self.axes = self.fig.add_subplot(1, 1, 1, label="plot1")

    def draw_1(self, datax, datay):
        datax_1 = []
        datax_2 = []
        for i in range(len(datax)):
            datax_1.append(datax[i].split("/"))
        for i in range(len(datax_1)):
            datax_2.append(datax_1[i][3] + "/" + datax_1[i][4])

        self.axes.plot(datax_2, datay, linewidth=2, marker='o', color='mediumturquoise')

        # self.axes.set_xlabel('X(m)')
        # self.axes.set_ylabel('%')
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['top'].set_visible(False)
        # self.axes.spines['bottom'].set_visible(False)
        # self.axes.spines['left'].set_visible(False)

        self.axes.spines['bottom'].set_color('lightsteelblue')
        self.axes.spines['bottom'].set_alpha(0.7)
        self.axes.spines['bottom'].set_linewidth(1.5)
        self.axes.spines['left'].set_color('lightsteelblue')
        self.axes.spines['left'].set_alpha(0.7)
        self.axes.spines['left'].set_linewidth(1.5)

        self.axes.set_ylim(min(datay) - 0.05, max(datay) + 0.05)

        self.axes.grid(axis="y", c="lightsteelblue", alpha=0.5, linewidth=1.5)

        self.axes.tick_params(labelsize='small', colors='darkcyan')

        # self.axes.set_ylim([0, 300])

        self.fig.tight_layout()
        self.draw()

class Canvas_hum2(FigureCanvas):
    def __init__(self):
        self.fig = Figure()

        FigureCanvas.__init__(self, self.fig)
        self.axes = self.fig.add_subplot(1,1,1,label = "plot1")

    def draw_1(self, datax, datay):
        datax_1 = []
        datax_2 = []
        for i in range(len(datax)):
            datax_1.append(datax[i].split("/"))
        for i in range(len(datax_1)):
            datax_2.append(datax_1[i][3]+"/"+datax_1[i][4])

        # self.axes.grid(axis="y", c="lightsteelblue", alpha=0.5, linewidth=1.5)
        self.axes.bar(datax_2, datay,color = 'mediumturquoise')
        for x,y in zip(datax_2,datay):
            self.axes.text(x, y, '%.1f' % float(y), ha='center',va='bottom', color = 'darkcyan' )

        self.axes.spines['right'].set_visible(False)
        self.axes.spines['top'].set_visible(False)

        self.axes.spines['bottom'].set_color('lightsteelblue')
        self.axes.spines['bottom'].set_alpha(0.7)
        self.axes.spines['bottom'].set_linewidth(1.5)
        self.axes.spines['left'].set_color('lightsteelblue')
        self.axes.spines['left'].set_alpha(0.7)
        self.axes.spines['left'].set_linewidth(1.5)

        self.axes.tick_params(colors='darkcyan')

        # self.axes.set_title('Illumination in 7 Days')

        self.fig.tight_layout()
        self.draw()

class Canvas_hum3(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)
        self.axes = self.fig.add_subplot(1,1,1,label = "plot1")

    def draw_1(self, datax, datay):
        datax_1 = []
        datax_2 = []
        for i in range(len(datax)):
            datax_1.append(datax[i].split("/"))
        for i in range(len(datax_1)):
            datax_2.append(datax_1[i][3]+"/"+datax_1[i][4])

        low = 0
        mid = 0
        high = 0
        for i in range(len(datay)):
            if datay[i]<25:
                low = low+1
            elif datay[i]<27:
                mid = mid+1
            else:
                high = high+1
        values = [low,mid,high]
        explode = [0.01, 0.01, 0.01]
        label = ['low','mid','high']
        self.axes.pie(values, radius = 1, wedgeprops=dict(width=0.4,edgecolor='w'),explode=explode,colors = ['lightskyblue','mediumspringgreen','coral'],labels = label, autopct='%1.1f%%')  # 绘制饼图

        # self.axes.set_title("Statistics")

        self.fig.tight_layout()
        self.draw()

class Canvas_temp(FigureCanvas):
    def __init__(self):
        self.fig = Figure()

        FigureCanvas.__init__(self, self.fig)
        self.axes = self.fig.add_subplot(1, 1, 1, label="plot1")

    def draw_1(self, datax, datay):
        datax_1 = []
        datax_2 = []
        for i in range(len(datax)):
            datax_1.append(datax[i].split("/"))
        for i in range(len(datax_1)):
            datax_2.append(datax_1[i][3] + "/" + datax_1[i][4])

        self.axes.plot(datax_2, datay, linewidth=2, marker='o', color='mediumturquoise')

        # self.axes.set_xlabel('X(m)')
        # self.axes.set_ylabel('℃')
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['top'].set_visible(False)
        # self.axes.spines['bottom'].set_visible(False)
        # self.axes.spines['left'].set_visible(False)

        self.axes.spines['bottom'].set_color('lightsteelblue')
        self.axes.spines['bottom'].set_alpha(0.7)
        self.axes.spines['bottom'].set_linewidth(1.5)
        self.axes.spines['left'].set_color('lightsteelblue')
        self.axes.spines['left'].set_alpha(0.7)
        self.axes.spines['left'].set_linewidth(1.5)

        self.axes.set_ylim(min(datay) - 0.05, max(datay) + 0.05)

        self.axes.grid(axis="y", c="lightsteelblue", alpha=0.5, linewidth=1.5)

        self.axes.tick_params(labelsize='small', colors='darkcyan')

        # self.axes.set_ylim([0, 300])

        self.fig.tight_layout()
        self.draw()

class Canvas_temp2(FigureCanvas):
    def __init__(self):
        self.fig = Figure()

        FigureCanvas.__init__(self, self.fig)
        self.axes = self.fig.add_subplot(1,1,1,label = "plot1")

    def draw_1(self, datax, datay):
        datax_1 = []
        datax_2 = []
        for i in range(len(datax)):
            datax_1.append(datax[i].split("/"))
        for i in range(len(datax_1)):
            datax_2.append(datax_1[i][3]+"/"+datax_1[i][4])

        # self.axes.grid(axis="y", c="lightsteelblue", alpha=0.5, linewidth=1.5)
        self.axes.bar(datax_2, datay,color = 'mediumturquoise')
        for x,y in zip(datax_2,datay):
            self.axes.text(x, y, '%.1f' % float(y), ha='center',va='bottom', color = 'darkcyan' )

        self.axes.spines['right'].set_visible(False)
        self.axes.spines['top'].set_visible(False)

        self.axes.spines['bottom'].set_color('lightsteelblue')
        self.axes.spines['bottom'].set_alpha(0.7)
        self.axes.spines['bottom'].set_linewidth(1.5)
        self.axes.spines['left'].set_color('lightsteelblue')
        self.axes.spines['left'].set_alpha(0.7)
        self.axes.spines['left'].set_linewidth(1.5)

        self.axes.tick_params(colors='darkcyan')

        # self.axes.set_title('Illumination in 7 Days')

        self.fig.tight_layout()
        self.draw()

class Canvas_temp3(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)
        self.axes = self.fig.add_subplot(1,1,1,label = "plot1")

    def draw_1(self, datax, datay):
        datax_1 = []
        datax_2 = []
        for i in range(len(datax)):
            datax_1.append(datax[i].split("/"))
        for i in range(len(datax_1)):
            datax_2.append(datax_1[i][3]+"/"+datax_1[i][4])

        low = 0
        mid = 0
        high = 0
        for i in range(len(datay)):
            if datay[i]<25:
                low = low+1
            elif datay[i]<27:
                mid = mid+1
            else:
                high = high+1
        values = [low,mid,high]
        explode = [0.01, 0.01, 0.01]
        label = ['low','mid','high']
        self.axes.pie(values, radius = 1, wedgeprops=dict(width=0.4,edgecolor='w'),explode=explode,colors = ['lightskyblue','mediumspringgreen','coral'],labels = label, autopct='%1.1f%%')  # 绘制饼图

        # self.axes.set_title("Statistics")

        self.fig.tight_layout()
        self.draw()

class Canvas_co2(FigureCanvas):
    def __init__(self):
        self.fig = Figure()

        FigureCanvas.__init__(self, self.fig)
        self.axes = self.fig.add_subplot(1, 1, 1, label="plot1")

    def draw_1(self, datax, datay):
        datax_1 = []
        datax_2 = []
        for i in range(len(datax)):
            datax_1.append(datax[i].split("/"))
        for i in range(len(datax_1)):
            datax_2.append(datax_1[i][3] + "/" + datax_1[i][4])

        self.axes.plot(datax_2, datay, linewidth=2, marker='o', color='mediumturquoise')

        # self.axes.set_xlabel('X(m)')
        # self.axes.set_ylabel('ppm')
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['top'].set_visible(False)
        # self.axes.spines['bottom'].set_visible(False)
        # self.axes.spines['left'].set_visible(False)

        self.axes.spines['bottom'].set_color('lightsteelblue')
        self.axes.spines['bottom'].set_alpha(0.7)
        self.axes.spines['bottom'].set_linewidth(1.5)
        self.axes.spines['left'].set_color('lightsteelblue')
        self.axes.spines['left'].set_alpha(0.7)
        self.axes.spines['left'].set_linewidth(1.5)

        self.axes.set_ylim(min(datay) - 0.05, max(datay) + 0.05)

        self.axes.grid(axis="y", c="lightsteelblue", alpha=0.5, linewidth=1.5)

        self.axes.tick_params(labelsize='small', colors='darkcyan')

        # self.axes.set_ylim([0, 300])

        self.fig.tight_layout()
        self.draw()

class Canvas_co22(FigureCanvas):
    def __init__(self):
        self.fig = Figure()

        FigureCanvas.__init__(self, self.fig)
        self.axes = self.fig.add_subplot(1,1,1,label = "plot1")

    def draw_1(self, datax, datay):
        datax_1 = []
        datax_2 = []
        for i in range(len(datax)):
            datax_1.append(datax[i].split("/"))
        for i in range(len(datax_1)):
            datax_2.append(datax_1[i][3]+"/"+datax_1[i][4])

        # self.axes.grid(axis="y", c="lightsteelblue", alpha=0.5, linewidth=1.5)
        self.axes.bar(datax_2, datay,color = 'mediumturquoise')
        for x,y in zip(datax_2,datay):
            self.axes.text(x, y, '%.1f' % float(y), ha='center',va='bottom', color = 'darkcyan' )

        self.axes.spines['right'].set_visible(False)
        self.axes.spines['top'].set_visible(False)

        self.axes.spines['bottom'].set_color('lightsteelblue')
        self.axes.spines['bottom'].set_alpha(0.7)
        self.axes.spines['bottom'].set_linewidth(1.5)
        self.axes.spines['left'].set_color('lightsteelblue')
        self.axes.spines['left'].set_alpha(0.7)
        self.axes.spines['left'].set_linewidth(1.5)

        self.axes.tick_params(colors='darkcyan')

        # self.axes.set_title('Illumination in 7 Days')

        self.fig.tight_layout()
        self.draw()

class Canvas_co23(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)
        self.axes = self.fig.add_subplot(1,1,1,label = "plot1")

    def draw_1(self, datax, datay):
        datax_1 = []
        datax_2 = []
        for i in range(len(datax)):
            datax_1.append(datax[i].split("/"))
        for i in range(len(datax_1)):
            datax_2.append(datax_1[i][3]+"/"+datax_1[i][4])

        low = 0
        mid = 0
        high = 0
        for i in range(len(datay)):
            if datay[i]<25:
                low = low+1
            elif datay[i]<27:
                mid = mid+1
            else:
                high = high+1
        values = [low,mid,high]
        explode = [0.01, 0.01, 0.01]
        label = ['low','mid','high']
        self.axes.pie(values, radius = 1, wedgeprops=dict(width=0.4,edgecolor='w'),explode=explode,colors = ['lightskyblue','mediumspringgreen','coral'],labels = label, autopct='%1.1f%%')  # 绘制饼图

        # self.axes.set_title("Statistics")

        self.fig.tight_layout()
        self.draw()

class QmyMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_URPMainWindow()
        self.ui.setupUi(self)
        self.updateUI()

        self.query_SqlData()

        self.set_tab_illum_label1()
        self.set_tab_illum_label2()
        self.set_tab_illum_label3()

        self.set_tab_hum_label1()
        self.set_tab_hum_label2()
        self.set_tab_hum_label3()

        self.set_tab_temp_label1()
        self.set_tab_temp_label2()
        self.set_tab_temp_label3()

        self.set_tab_co2_label1()
        self.set_tab_co2_label2()
        self.set_tab_co2_label3()

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


    def set_tab_illum_label1(self):
        self.plot1 = Canvas_illum()
        self.plot1.draw_1(self.sqlData_time,self.sqlData_illum)
        layout = QVBoxLayout()
        layout.addWidget(self.plot1)
        self.ui.tab_illum_label1.setLayout(layout)
        self.ui.tab_illum_label1.show()

    def set_tab_illum_label2(self):
        self.plot11 = Canvas_illum2()
        self.plot11.draw_1(self.sqlData_time,self.sqlData_illum)
        layout = QVBoxLayout()
        layout.addWidget(self.plot11)
        self.ui.tab_illum_label2.setLayout(layout)
        self.ui.tab_illum_label2.show()

    def set_tab_illum_label3(self):
        self.plot12 = Canvas_illum3()
        self.plot12.draw_1(self.sqlData_time,self.sqlData_illum)
        layout = QVBoxLayout()
        layout.addWidget(self.plot12)
        self.ui.tab_illum_label3.setLayout(layout)
        self.ui.tab_illum_label3.show()

    def set_tab_hum_label1(self):
        self.plot2 = Canvas_hum()
        self.plot2.draw_1(self.sqlData_time, self.sqlData_hum)
        layout = QVBoxLayout()
        layout.addWidget(self.plot2)
        self.ui.tab_hum_label1.setLayout(layout)
        self.ui.tab_hum_label1.show()

    def set_tab_hum_label2(self):
        self.plot21 = Canvas_hum2()
        self.plot21.draw_1(self.sqlData_time, self.sqlData_hum)
        layout = QVBoxLayout()
        layout.addWidget(self.plot21)
        self.ui.tab_hum_label2.setLayout(layout)
        self.ui.tab_hum_label2.show()

    def set_tab_hum_label3(self):
        self.plot22 = Canvas_hum3()
        self.plot22.draw_1(self.sqlData_time, self.sqlData_hum)
        layout = QVBoxLayout()
        layout.addWidget(self.plot22)
        self.ui.tab_hum_label3.setLayout(layout)
        self.ui.tab_hum_label3.show()

    def set_tab_temp_label1(self):
        self.plot3 = Canvas_temp()
        self.plot3.draw_1(self.sqlData_time, self.sqlData_temp)
        layout = QVBoxLayout()
        layout.addWidget(self.plot3)
        self.ui.tab_temp_label1.setLayout(layout)
        self.ui.tab_temp_label1.show()

    def set_tab_temp_label2(self):
        self.plot31 = Canvas_temp2()
        self.plot31.draw_1(self.sqlData_time, self.sqlData_temp)
        layout = QVBoxLayout()
        layout.addWidget(self.plot31)
        self.ui.tab_temp_label2.setLayout(layout)
        self.ui.tab_temp_label2.show()

    def set_tab_temp_label3(self):
        self.plot32 = Canvas_temp3()
        self.plot32.draw_1(self.sqlData_time, self.sqlData_temp)
        layout = QVBoxLayout()
        layout.addWidget(self.plot32)
        self.ui.tab_temp_label3.setLayout(layout)
        self.ui.tab_temp_label3.show()

    def set_tab_co2_label1(self):
        self.plot4 = Canvas_co2()
        self.plot4.draw_1(self.sqlData_time, self.sqlData_co2)
        layout = QVBoxLayout()
        layout.addWidget(self.plot4)
        self.ui.tab_co2_label1.setLayout(layout)
        self.ui.tab_co2_label1.show()

    def set_tab_co2_label2(self):
        self.plot41 = Canvas_co22()
        self.plot41.draw_1(self.sqlData_time, self.sqlData_co2)
        layout = QVBoxLayout()
        layout.addWidget(self.plot41)
        self.ui.tab_co2_label2.setLayout(layout)
        self.ui.tab_co2_label2.show()

    def set_tab_co2_label3(self):
        self.plot42 = Canvas_co23()
        self.plot42.draw_1(self.sqlData_time, self.sqlData_co2)
        layout = QVBoxLayout()
        layout.addWidget(self.plot42)
        self.ui.tab_co2_label3.setLayout(layout)
        self.ui.tab_co2_label3.show()


    def updateUI(self):
        self.thread = BackendThread()
        self.thread.serial_data.connect(self.showData)
        self.thread.start()

    def showData(self,s_data):

        self.Lab = s_data.split(" ")

        _translate = QtCore.QCoreApplication.translate
        self.Lab_illum = self.Lab[0]
        self.Lab_hum = self.Lab[1]
        self.Lab_temp = self.Lab[2]
        self.Lab_co2 = self.Lab[3]

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

    # def draw_in_illum1(self):
    #     x = [1,2,3,4,5]
    #     y = [1,2,3,4,5]
    #     plt.plot(x,y)
    #     plt.title("DEMO")
    #     self.ui.tab_illum_label1.canvas.draw()



if __name__=="__main__":
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.setWindowTitle("基于环境监测的物联网系统")
    form.show()
    # myWidget.btnClose.setText("不关闭了")
    sys.exit(app.exec_())


