import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QCheckBox, QLineEdit, QTextEdit, QLabel
from PyQt5.QtCore import QCoreApplication, QThread
from PyQt5.QtGui import QFontDatabase, QFont, QIcon

import pyautogui as pag
import json
import schedule
import time
import pyautogui as pag
import datetime as dt
with open('datashcol.json', 'r') as f:
    json_data = json.load(f)
if dt.datetime.today().weekday() != 5 or 6:
    a = dt.datetime.today().weekday()
else: 
    quit()
class Loopday(QThread):
    def run(self):
        with open('datashcol.json', 'r') as f:
            json_data = json.load(f)
        a = dt.datetime.today().weekday()
        while True:
            x = dt.datetime.now()
            hour = int(json_data[str(a) + 'day']['start_time_Lookup_after_hour'])
            minute = int(json_data[str(a) + 'day']["start_time_Lookup_after_minute"])
            if x.hour == hour and x.minute == minute:
                for i in range(int(json_data[str(a) + 'day']['period'])):
                    sec = int(45) * 60 + int(json_data[str(a) + 'day']['freetime'])
                    print(sec)

                    x, y = pag.position()
                    print(x, y)  

                    pag.moveTo(231,1067)
                    pag.click()
                    pag.typewrite("zoom")
                    pag.press('enter')
                    pag.moveTo(951,530)
                    time.sleep(2)
                    pag.click()

                    pag.moveTo(946,486)
                    time.sleep(2)
                    pag.click()
                    pag.typewrite(json_data[str(a) + 'day'][str(i)])


                    while (sec != 0 ):
                        sec = sec-1
                        time.sleep(1)
                        print(sec)

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #424242')
        self.initUI()

    def initUI(self):

        self.zoomid1 = QLabel(json_data[str(a) + 'day']['0'], self)
        self.zoomid1.move(20, 40)
        self.zoomid1.setStyleSheet("Color : white;""image:url(pictures/buttonidd.png);border:0px;")
        self.zoomid1.setFont(QFont('여기어때 잘난체', 9))

        self.zoomid2 = QLabel(json_data[str(a) + 'day']['1'], self)
        self.zoomid2.move(20, 70)
        self.zoomid2.setStyleSheet("Color : white;""image:url(pictures/buttonidd.png);border:0px;")
        self.zoomid2.setFont(QFont('여기어때 잘난체', 9))

        self.zoomid3 = QLabel(json_data[str(a) + 'day']['2'], self)
        self.zoomid3.move(20, 100)
        self.zoomid3.setStyleSheet("Color : white;""image:url(pictures/buttonidd.png);border:0px;")
        self.zoomid3.setFont(QFont('여기어때 잘난체', 9))

        self.zoomid4 = QLabel(json_data[str(a) + 'day']['3'], self)
        self.zoomid4.move(20, 130)
        self.zoomid4.setStyleSheet("Color : white;""image:url(pictures/buttonidd.png);border:0px;")
        self.zoomid4.setFont(QFont('여기어때 잘난체', 9))

        self.zoomid5 = QLabel(json_data[str(a) + 'day']['4'], self)
        self.zoomid5.move(20, 160)
        self.zoomid5.setStyleSheet("Color : white;""image:url(pictures/buttonidd.png);border:0px;")
        self.zoomid5.setFont(QFont('여기어때 잘난체', 9))

        self.zoomid6 = QLabel(json_data[str(a) + 'day']['5'], self)
        self.zoomid6.move(20, 190)
        self.zoomid6.setStyleSheet("Color : white;""image:url(pictures/buttonidd.png);border:0px;")
        self.zoomid6.setFont(QFont('여기어때 잘난체', 9))

        self.zoomid7 = QLabel(json_data[str(a) + 'day']['6'], self)
        self.zoomid7.move(20, 220)
        self.zoomid7.setStyleSheet("Color : white;""image:url(pictures/buttonidd.png);border:0px;")
        self.zoomid7.setFont(QFont('여기어때 잘난체', 9))

        self.setWindowTitle('ATZ')
        self.move(300, 300)
        self.resize(200, 300)
        self.setWindowIcon(QIcon('pictures/zoomicon.png'))
        self.show()
        self.loopday = Loopday()
        self.loopday.start()

        


    

if __name__ == '__main__':
   
   
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())


