import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import pyautogui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread,pyqtSignal
from os import system
import time
import ctypes
from tkinter import messagebox
import logging
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 359)
        MainWindow.setMinimumSize(QtCore.QSize(595, 359))
        MainWindow.setMaximumSize(QtCore.QSize(595, 359))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QtCore.QRect(50, 210, 261, 16))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.NETOFF = QtWidgets.QRadioButton(self.centralwidget)
        self.NETOFF.setGeometry(QtCore.QRect(50, 230, 281, 21))
        self.NETOFF.setObjectName("NETOFF")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 260, 291, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 361, 91))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(340, 10, 241, 301))
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 70, 321, 80))
        self.widget.setObjectName("widget")
        self.Mission_3 = QtWidgets.QRadioButton(self.widget)
        self.Mission_3.setGeometry(QtCore.QRect(210, 30, 89, 16))
        self.Mission_3.setObjectName("Mission_3")
        self.Mission_2 = QtWidgets.QRadioButton(self.widget)
        self.Mission_2.setGeometry(QtCore.QRect(110, 30, 89, 16))
        self.Mission_2.setObjectName("Mission_2")
        self.Mission = QtWidgets.QRadioButton(self.widget)
        self.Mission.setGeometry(QtCore.QRect(0, 30, 89, 16))
        self.Mission.setChecked(True)
        self.Mission.setObjectName("Mission")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 140, 171, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 140, 131, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 595, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "末日豪劫跳前置助手"))
        self.radioButton.setText(_translate("MainWindow", "连接网络"))
        self.NETOFF.setText(_translate("MainWindow", "不连接网络(推荐)"))
        self.label.setText(_translate("MainWindow", "危险：不花钱，有一定的风险，如果程序出现问题也不会有损失，推荐"))
        self.label_2.setText(_translate("MainWindow", "GTA末日豪劫 跳前置助手"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">日志记录</p></body></html>"))
        self.Mission_3.setText(_translate("MainWindow", "任务3"))
        self.Mission_2.setText(_translate("MainWindow", "任务2"))
        self.Mission.setText(_translate("MainWindow", "任务1"))
        self.pushButton.setText(_translate("MainWindow", "跳过前置任务"))
        self.pushButton_2.setText(_translate("MainWindow", "跳过等待时间"))

def PressKey(sec,key):
    pyautogui.keyDown(key)
    time.sleep(sec)
    pyautogui.keyUp(key)
def SkipTime(start,end):
    if end==start:
        PressKey(0.5,'enter')
    elif end>start:
        PressKey(0.5, 'enter')
        time.sleep(0.1)
        for i in range(end-start):
            PressKey(0.1,'s')
            time.sleep(0.1)
    else:
        PressKey(0.5,'enter')
        time.sleep(0.1)
        for i in range(start-end):
            PressKey(0.1, 'w')
            time.sleep(0.1)
def RestartScreen():
    PressKey(0.1,'m')
    time.sleep(0.2)
    PressKey(0.1,'down')
    time.sleep(0.2)
    PressKey(0.1,'enter')
    time.sleep(0.2)
    PressKey(0.1,'up')
    time.sleep(0.2)
    PressKey(0.1, 'left')
    time.sleep(0.5)
    PressKey(0.1, 'left')
    time.sleep(0.2)
    PressKey(0.1,'esc')
    time.sleep(0.2)
    PressKey(0.1,'esc')
def Mission1_2():
    for i in range(4):
        PressKey(1,'space')
        PressKey(0.1,'d')
        time.sleep(0.5)
        PressKey(0.1,'enter')
        if i < 3:
            PressKey(0.1,'down')
    PressKey(0.1,'esc')
    RestartScreen()
def Mission3():
    for v in range(3):
        PressKey(0.1,'down')
        time.sleep(0.2)
    PressKey(1,'space')
    pyautogui.keyDown('s')
    pyautogui.keyDown('d')
    time.sleep(0.1)
    pyautogui.keyUp('s')
    pyautogui.keyUp('d')
    PressKey(0.1,'enter')
    PressKey(0.1,'esc')
    RestartScreen()
def Network(need):
    if need == True:
        system('netsh advfirewall firewall add rule name="GTASKIPRULE100" dir=out action=block')
        text='\n['+time.ctime()+']添加出站规则'
        system('netsh advfirewall firewall set rule name="GTASKIPRULE100" new enable=yes')
        text+='\n['+time.ctime()+']启动出站规则'
        return text
    elif need == False:
        system('netsh advfirewall firewall set rule name="GTASKIPRULE100" new enable=no')
        text='\n['+time.ctime()+']停止出站规则'
        system('netsh advfirewall firewall delete rule name="GTASKIPRULE100"')
        text+='\n['+time.ctime()+']移除出站规则'
        return text

class Thread(QThread):
    sinout=pyqtSignal(str)
    def __init__(self,mode,connect,ui):
        super(Thread,self).__init__()
        self.mode=mode
        self.connect=connect
        self.ui=ui
    def run(self):
        for i in range(10):
            self.text = '\n倒计时:' + str(9 - i) + '秒'
            self.sinout.emit(self.text)
            self.sleep(1)
        if self.connect == False:
            self.text=Network(True)
            self.sinout.emit(self.text)
        if self.mode == 'Mission1' or self.mode == 'Mission2':
            Mission1_2()
        elif self.mode == 'Mission3':
            Mission3()
        if self.connect == False:
            self.text=Network(False)
            self.sinout.emit(self.text)
        self.sinout.emit('\n['+time.ctime()+']Success')
        self.sinout.emit('\n!!!请使用Alt+F4组合键强制保存,右下角出现“否ESC”后按ESC以继续游戏!!!\n')
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.radioButton.setEnabled(True)
        self.ui.NETOFF.setEnabled(True)
        self.ui.Mission.setEnabled(True)
        self.ui.Mission_2.setEnabled(True)
        self.ui.Mission_3.setEnabled(True)
class Thread2(QThread):
    sinout2=pyqtSignal(str)
    def __init__(self,mode,connect,start,ui):
        super(Thread2,self).__init__()
        self.mode=mode
        self.connect=connect
        self.starta=start
        self.ui=ui
    def run(self):
        for i in range(10):
            self.text = '\n倒计时:' + str(9 - i) + '秒'
            self.sinout2.emit(self.text)
            self.sleep(1)
        if self.connect == False:
            self.text=Network(True)
            self.sinout2.emit(self.text)
        SkipTime(self.starta,self.mode)
        self.sinout2.emit('\n[' + time.ctime() + ']Success')
        if self.connect == False:
            PressKey(1,'enter')
            self.text=Network(False)
            self.sinout2.emit(self.text)
            self.sinout2.emit('\n!!!请查看是否购买正确任务，如果不正确请打给莱斯特以取消任务!!!')
        else:
            self.sinout2.emit('\n!!!请查看是否进入购买您想要跳过CD的任务的购买界面，如果未进入请按ESC退出!!!')
        self.sinout2.emit('\n!!!请使用Alt+F4组合键强制保存,右下角出现“否ESC”后按ESC以继续游戏!!!\n')
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.radioButton.setEnabled(True)
        self.ui.NETOFF.setEnabled(True)
        self.ui.Mission.setEnabled(True)
        self.ui.Mission_2.setEnabled(True)
        self.ui.Mission_3.setEnabled(True)
class window(object):
    def __init__(self):
        self.mode = 'unknown'
        self.start = True
        self.connect=False
        self.text=''
    def display(self,inp):
        self.text+=inp
        self.ui.textBrowser.setText(self.text)
        QApplication.processEvents()
    def choose(self):
        self.ui.radioButton.setEnabled(False)
        self.ui.NETOFF.setEnabled(False)
        self.ui.Mission.setEnabled(False)
        self.ui.Mission_2.setEnabled(False)
        self.ui.Mission_3.setEnabled(False)
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        if self.ui.Mission.isChecked() == True:
            self.mode='Mission1'
        elif self.ui.Mission_2.isChecked() == True:
            self.mode='Mission2'
        elif self.ui.Mission_3.isChecked() == True:
            self.mode='Mission3'
        if self.ui.radioButton.isChecked() == True:
            self.connect=True
        elif self.ui.NETOFF.isChecked() == True:
            self.connect=False
        self.text='['+time.ctime()+']开始跳过前置:'+self.mode+'\n['+time.ctime()+']是否不断网:'+str(self.connect)
        self.ui.textBrowser.setText(self.text)
        self.text+='\n请提前进入任务前置界面并选择左上角的前置任务(不是准备任务)'
        self.ui.textBrowser.setText(self.text)
        self.th=Thread(self.mode,self.connect,self.ui)
        self.th.start()
        self.th.sinout.connect(self.display)
    def Skipt(self):
        while self.start:
            if messagebox.askquestion(title='无CD任务',message='末日豪劫1数据泄露是否没有CD')=='yes':
                self.start='M1'
                break
            if messagebox.askquestion(title='无CD任务',message='末日豪劫2博格丹危机是否没有CD')=='yes':
                self.start='M2'
                break
            if messagebox.askquestion(title='无CD任务',message='末日豪劫3末日将至是否没有CD')=='yes':
                self.start='M3'
                break
        self.start=int(self.start[1])
        self.ui.radioButton.setEnabled(False)
        self.ui.NETOFF.setEnabled(False)
        self.ui.Mission.setEnabled(False)
        self.ui.Mission_2.setEnabled(False)
        self.ui.Mission_3.setEnabled(False)
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        if self.ui.Mission.isChecked() == True:
            self.mode = 1
        elif self.ui.Mission_2.isChecked() == True:
            self.mode = 2
        elif self.ui.Mission_3.isChecked() == True:
            self.mode = 3
        if self.ui.radioButton.isChecked() == True:
            self.connect = True
        elif self.ui.NETOFF.isChecked() == True:
            self.connect = False
        self.text = '[' + time.ctime() + ']开始跳过CD:' + str(self.start)+':'+str(self.mode) + '\n[' + time.ctime() + ']是否不断网:' + str(self.connect)
        self.ui.textBrowser.setText(self.text)
        self.th1 = Thread2(self.mode, self.connect,self.start, self.ui)
        self.th1.start()
        self.th1.sinout2.connect(self.display)
    def GUI(self):
        self.app = QApplication(sys.argv)
        self.Mainwindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.Mainwindow)
        self.Mainwindow.show()
        self.ui.pushButton.clicked.connect(self.choose)
        self.ui.pushButton_2.clicked.connect(self.Skipt)
        sys.exit(self.app.exec_())
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if __name__ == '__main__':
    logging.basicConfig(filename='log.txt', filemode='w', level=logging.DEBUG)
    try:
        if is_admin():
            main = window()
            main.GUI()
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    except Exception as e:
        messagebox.showerror(title='ERROR',message=str(e))
        logging.error(str(e))
        sys.exit(1)