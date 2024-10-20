# напиши здесь код основного приложения и первого экрана 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout,
        QPushButton, QLabel,QLineEdit)
from  instr import *
from second_win import *

class MainWin( QWidget) :

    def next_click(self):
        self.tw = TestWin()
        self.hide()
        


    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.txt_hello = QLabel(txt_hello)
        self.txt_instruction = QLabel(txt_instruction)
        self.txt_next = QPushButton(txt_next)
        self.layot =  QVBoxLayout()

        self.layot.addWidget(self.txt_hello)
        self.layot.addWidget(self.txt_instruction)
        self.layot.addWidget(self.txt_next)
        self.setLayout(self.layot)

        

    def connects(self):
        self.txt_next.clicked.connect(self.next_click)

    
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()






app = QApplication([])
mw = MainWin()
app.exec_()




