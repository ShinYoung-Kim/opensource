# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 05:53:03 2021

@author: ksy
"""

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QApplication,QGraphicsDropShadowEffect,QGraphicsOpacityEffect,QLabel
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtCore

import time
import random
import string


def randomID():
    candidate=string.ascii_letters+string.digits
    new_id=""
    for i in range(4,10):
        new_id=new_id+random.choice(candidate)
    return new_id

random1=randomID()
random2=randomID()
random3=randomID()

FROM_CLASS = uic.loadUiType("comment.ui")[0]

class Windows(QMainWindow,FROM_CLASS):

    def __init__(self, on_top=True):
        super().__init__()

        # setup user interface
        self.setupUi(self) 
        
        # 내용 변경
        
        self.ID1.setStyleSheet("Color : lime") #글자색 변환
        self.ID2.setStyleSheet("Color : pink") #글자색 변환
        self.ID3.setStyleSheet("Color : orange") #글자색 변환
        
        label1 = QLabel("김신영이 제작한 Study With me", self)
  
        # setting geometry to the label
        label1.setGeometry(210, 20, 700, 150)
        label1.setAlignment(Qt.AlignTop)
        # making it multi line
        label1.setWordWrap(True)
        label1.setStyleSheet("Color:white;")
        
        label2 = QLabel("다들 준비 되셨나요?", self)
  
        # setting geometry to the label
        label2.setGeometry(210, 80, 700, 150)
        label2.setAlignment(Qt.AlignTop)
        # making it multi line
        label2.setWordWrap(True)
        label2.setStyleSheet("Color:white;")
        
        label3 = QLabel("그럼 시작합니다!", self)
  
        # setting geometry to the label
        label3.setGeometry(210, 140, 700, 150)
        label3.setAlignment(Qt.AlignTop)
        # making it multi line
        label3.setWordWrap(True)
        label3.setStyleSheet("Color:white;")
        
        #그림자
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(5)
        self.shadow.setXOffset(3)
        self.shadow.setYOffset(3)
        self.shadow2 = QGraphicsDropShadowEffect()
        self.shadow2.setBlurRadius(5)
        self.shadow2.setXOffset(3)
        self.shadow2.setYOffset(3)
        self.shadow3 = QGraphicsDropShadowEffect()
        self.shadow3.setBlurRadius(5)
        self.shadow3.setXOffset(3)
        self.shadow3.setYOffset(3)
        self.shadow4 = QGraphicsDropShadowEffect()
        self.shadow4.setBlurRadius(5)
        self.shadow4.setXOffset(3)
        self.shadow4.setYOffset(3)
        self.shadow5 = QGraphicsDropShadowEffect()
        self.shadow5.setBlurRadius(5)
        self.shadow5.setXOffset(3)
        self.shadow5.setYOffset(3)
        self.shadow6 = QGraphicsDropShadowEffect()
        self.shadow6.setBlurRadius(5)
        self.shadow6.setXOffset(3)
        self.shadow6.setYOffset(3)
        
        self.ID1.setGraphicsEffect(self.shadow)
        self.ID2.setGraphicsEffect(self.shadow2)
        self.ID3.setGraphicsEffect(self.shadow3)
        label1.setGraphicsEffect(self.shadow4)
        label2.setGraphicsEffect(self.shadow5)
        label3.setGraphicsEffect(self.shadow6)
        # Widget Setup
        self.initUI()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
        # Timer Application
       
    def initUI(self):
        # creating label
        random1="random1234"
        random2="randomrand"
        random3="1234567890"
        self.ID3.setText(random1) #텍스트 변환  
        self.ID2.setText(random2)
        self.ID1.setText(random3)
        self.firstCommentPage()
        
    # Drag Event Method
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)
        
        
    
    
    def firstCommentPage(self): 
        
        self.ID3.setText(random1)
        self.ID2.setText(random2)
        self.ID1.setText(random3)
        
        self.timer = QTimer()
        self.timer.setInterval(500)   
        self.timer.timeout.connect(lambda:self.commentChange())
        self.timer.start()
        
    def commentChange(self):
        global random2
        global random1
        random3=random2
        random2=random1
        random1=randomID()
        self.ID3.setText(random1)
        self.ID2.setText(random2)
        self.ID1.setText(random3)       
        return random1, random2, random3
        
       
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ShowApp = Windows()
    
    sys.exit(app.exec_())