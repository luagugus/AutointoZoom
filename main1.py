import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QCheckBox, QLineEdit, QTextEdit, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import pyautogui as pag
import json
import schedule
import time
import pyautogui as pag
import datetime as dt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        with open('datashcol.json', 'r') as f:
            json_data = json.load(f)
        self.zoomid1 = QLabel(json_data['0'], self)
        self.zoomid1.move(20, 40)

        self.zoomid2 = QLabel(json_data['1'], self)
        self.zoomid2.move(20, 70)

        self.zoomid3 = QLabel(json_data['2'], self)
        self.zoomid3.move(20, 100)

        self.zoomid4 = QLabel(json_data['3'], self)
        self.zoomid4.move(20, 130)

        self.zoomid5 = QLabel(json_data['4'], self)
        self.zoomid5.move(20, 160)

        self.zoomid6 = QLabel(json_data['5'], self)
        self.zoomid6.move(20, 190)

        self.zoomid7 = QLabel(json_data['6'], self)
        self.zoomid7.move(20, 220)

        self.setWindowTitle('AUZ')
        self.move(300, 300)
        self.resize(200, 300)
        self.show()
        while True:
            x = dt.datetime.now()
            if x.hour == int(json_data['start_time_Lookup_after_hour']) and x.minute == int(json_data["start_time_Lookup_after_minute"]):
                for i in range(int(json_data['period'])):
                    sec = int(45) * 60 + int(json_data['freetime'])
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
                    pag.typewrite(json_data[str(i)])


                    while (sec != 0 ):
                        sec = sec-1
                        time.sleep(1)
                        print(sec)

        


    

if __name__ == '__main__':
   
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())


