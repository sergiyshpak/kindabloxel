# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:29:45 2018

@author: sergiy
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:44:31 2018

@author: me           
looks like sprite creation board for  Bloxels Build Your Own Video Game  
"""

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize   

colorez={0:'QPushButton {background: #313131;}', 
         1:'QPushButton {background: #00FF00;}', 
         2:'QPushButton {background: #0000FF;}', 
         3:"QPushButton {background: #FF0000;}"}


class myButt(QPushButton):
    color=0
    
    def buttonclickMethod(self):
        self.color=self.color+1
        if self.color == 4:
            self.color =0
        self.setStyleSheet(colorez.get(self.color));
    

class MainWindow(QMainWindow):


    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(660, 660))   
        self.setWindowTitle("")
        self.setStyleSheet("QMainWindow {background: 'black';}");

        for  y in range (0,13):
            for  x in range (0,13):
                pybutton = myButt('', self)
                pybutton.setStyleSheet("QPushButton {background: #313131;}");
                pybutton.clicked.connect(pybutton.buttonclickMethod)
                pybutton.resize(34,34)
                pybutton.move(50+x*44, 50+y*44)       


    def clickMethod(self):
        self.setStyleSheet("QPushButton {background: #FF0000;}");
        print('Clicked Pyqt button.')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )