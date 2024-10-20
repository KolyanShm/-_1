# напиши здесь код третьего экрана приложения
# напиши здесь код основного приложения и первого экрана 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout,
        QPushButton, QLabel,QLineEdit)
from  instr import *
from second_win import *

class WinThree( QWidget) :
    
    

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def result(self):
        self.index = (4*(int(self.exp.starttest1)+int(self.exp.starttest2)+int(self.exp.starttest3)) - 200)/10
        # if self.exp.age >= 15:
        #     if self.index >= 15:
        #         return txt_res1
        #     elif self.index<15 and self.index>=11:
        #         return txt_res2

        # elif >=self.exp.age  >= 15:
        #     if self.index >= 15:
        #         return txt_res1
        #     elif self.index<15 and self.index>=11:
        #         return txt_res2
        # elif self.exp.age >=










    def initUI(self):
        self.txt_index   = QLabel(txt_index + str(self.index))
        self.txt_workheart  = QLabel(txt_workheart )
        self.layot =  QVBoxLayout()
        self.layot.addWidget(self.txt_index)
        self.layot.addWidget(self.txt_workheart)

        self.setLayout(self.layot)

        


    
    def __init__(self, exp):
        super().__init__()
        self.exp =exp
        self.result()
        self.set_appear()
        self.initUI()
        
        self.show()
