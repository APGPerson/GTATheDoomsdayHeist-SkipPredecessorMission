import sys,pywintypes
#import pywintypes to pack to exe file
from PyQt5.QtWidgets import QApplication,QMainWindow
import pyautogui,time
import ENGUI
def PressKey(sec,key):
    pyautogui.keyDown(key)
    time.sleep(sec)
    pyautogui.keyUp(key)
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
def GUI():
    app = QApplication(sys.argv)
    Mainwindow = QMainWindow()
    ui = ENGUI.Ui_MainWindow()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    #GUI()
    print('---------------------------')
    print('|    GTA Doomsday Heist   |')
    print('| Skip Predecessor Mission|')
    print('|       Powered by APG    |')
    print('---------------------------')
    print('This program is completely free, please do not sell this software')
    print('Copyright APG 2023')
    print('警告:执行完成后请按Alt+F4强制保存游戏')
    print('Warning: After the execution is complete, press Alt+F4 to force the game to save')
    isUserInput = False
    while not isUserInput:
        print("Please enter you want to skip predecessor mission's mission's numeric(1,2 or 3)")
        print('请输入你想跳过前置任务的任务的数字顺序(1,2或3)')
        uin = input('>>')
        if uin == '1' or uin == '2':
            isUserInput = True
            for a in range(1,11):
                print(str(10-a)+'s')
                time.sleep(1)
            Mission1_2()
        elif uin == '3':
            isUserInput = True
            for b in range(1,11):
                print(str(10-b)+'s')
                time.sleep(1)
            Mission3()
    print('Success')
    time.sleep(5)
    sys.exit(0)