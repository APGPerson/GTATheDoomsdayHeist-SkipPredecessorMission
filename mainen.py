import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import pyautogui
from PyQt5.QtCore import QThread,pyqtSignal
from os import system
import time
import ctypes
from tkinter import messagebox
import logging
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 359)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "SkipPredecessorMission"))
        self.radioButton.setText(_translate("MainWindow", "connect to the network"))
        self.NETOFF.setText(_translate("MainWindow", "Disconnection of the network(recommended)"))
        self.label.setText(_translate("MainWindow", "Dangerious:does not cost money, there is a certain risk, there will be no loss if there is a problem with the program, recommended"))
        self.label_2.setText(_translate("MainWindow", "GTATheDoomsdayHeist-SkipPredecessorMission"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Log view</p></body></html>"))
        self.Mission_3.setText(_translate("MainWindow", "Mission 3"))
        self.Mission_2.setText(_translate("MainWindow", "Mission 2"))
        self.Mission.setText(_translate("MainWindow", "Mission 1"))
        self.pushButton.setText(_translate("MainWindow", "Skip Predecessor Mission"))
        self.pushButton_2.setText(_translate("MainWindow", "Skip wait times"))

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
        text='\n['+time.ctime()+']Add an outbound rule'
        system('netsh advfirewall firewall set rule name="GTASKIPRULE100" new enable=yes')
        text+='\n['+time.ctime()+']Start an outbound rule'
        return text
    elif need == False:
        system('netsh advfirewall firewall set rule name="GTASKIPRULE100" new enable=no')
        text='\n['+time.ctime()+']Stop an outbound rule'
        system('netsh advfirewall firewall delete rule name="GTASKIPRULE100"')
        text+='\n['+time.ctime()+']Remove an outbound rule'
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
            self.text = '\ncountdown:' + str(9 - i) + 'sec'
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
        self.sinout.emit('\n!!!Please use Alt+F4 key combination to force save, and press ESC after "No ESC" appears in the lower right corner to continue the game!!!\n')
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
            self.text = '\ncountdown:' + str(9 - i) + 'sec'
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
            self.sinout2.emit('\n!!!Please check that you purchased the correct task, and if not, call Lester to cancel the mission!!!')
        else:
            self.sinout2.emit('\n!!!Please check whether to enter the purchase screen for the task you want to skip the CD, and if not, press ESC to exit!!!')
        self.sinout2.emit('\n!!!Please use Alt+F4 key combination to force save, and press ESC after "No ESC" appears in the lower right corner to continue the game!!!\n')
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
        self.text='['+time.ctime()+']Start skipping predecessors:'+self.mode+'\n['+time.ctime()+']Whether the network is not interrupted:'+str(self.connect)
        self.ui.textBrowser.setText(self.text)
        self.text+='\nPlease enter the task pre-task interface in advance and select the pre-task in the upper left corner (not the preparation task)'
        self.ui.textBrowser.setText(self.text)
        self.th=Thread(self.mode,self.connect,self.ui)
        self.th.start()
        self.th.sinout.connect(self.display)
    def Skipt(self):
        while self.start:
            if messagebox.askquestion(title='CD-free mission',message='Doom 1 data breach if there is no CD')=='yes':
                self.start='M1'
                break
            if messagebox.askquestion(title='CD-free mission',message='Doomsday Havoc 2 Bogdan Crisis Is There No CD')=='yes':
                self.start='M2'
                break
            if messagebox.askquestion(title='CD-free mission',message='Doom 3: Is Doom Coming No CD')=='yes':
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
        self.text = '[' + time.ctime() + ']Start skipping CDs:' + str(self.start)+':'+str(self.mode) + '\n[' + time.ctime() + ']Whether the network is not interrupted:' + str(self.connect)
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