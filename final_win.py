# напиши здесь код третьего экрана приложения
# напиши здесь код основного приложения и первого экрана 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout,
        QPushButton, QLabel,QLineEdit)
from  instr import *

class WinThree( QWidget) :
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.txt_index = QLabel(txt_index)
        self.txt_workheart  = QLabel(txt_workheart )
        self.layot =  QVBoxLayout()

        self.layot.addWidget(self.txt_index)
        self.layot.addWidget(self.txt_workheart)

        self.setLayout(self.layot)

        
    def connects(self):
        pass
    
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()



app = QApplication([])
mw = WinThree()
app.exec_()
