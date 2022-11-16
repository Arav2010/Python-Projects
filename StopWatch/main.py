# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore , QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# creating class
class Window(QMainWindow):
    # constructor 
    # QMainWindow = parent class and Window = child class
    def __init__(self):
        super().__init__()
        
        #setting property of window
        self.setWindowTitle("STOPWATCH!")
        self.setGeometry(100, 100, 400, 500) #x,y,width,height

        #adding actions
        self.UiComponents()

        # show widgets
        self.show()

    def UiComponents(self):
        # initially count will be 0
        self.count = 0

        #flags gives a signal : true/false
        self.flag = False

        # creating label
        self.label = QLabel(self)

        self.label.setGeometry(75, 100, 250, 70)
        self.label.setStyleSheet("border:5px solid #014d4e;")
        self.label.setText(str(self.count))
        self.label.setFont(QFont("Arial", 25))
        self.label.setAlignment(Qt.AlignCenter)

        #start button
        start = QPushButton("Start", self)
        start.setGeometry(125, 250, 150, 50)
        #assign event
        start.pressed.connect(self.Start)

        #pause button
        pause = QPushButton("Pause", self)
        pause.setGeometry(125, 300, 150, 50)
        #assign event
        pause.pressed.connect(self.Pause)

        #reset button
        reset = QPushButton("Reset", self)
        reset.setGeometry(125, 350, 150, 50)
        #assign event
        reset.pressed.connect(self.reset)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100) #miliseconds

    def showTime(self):
        if self.flag:
            self.count += 1
            text = str(self.count/10)
            self.label.setText(text)

    def Start(self):
        self.flag = True

    def Pause(self):
        self.flag = False

    def reset(self):
        self.flag = False
        self.count = 0
        self.label.setText(str(0))

#create object
App = QApplication(sys.argv)

#object from child class
window = Window()
sys.exit(App.exec())