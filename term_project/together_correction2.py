# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 22:59:02 2021

@author: ksy
"""
\
import random
import string
from pytchat import LiveChat
import pafy
import pandas
from googleapiclient.discovery import build
import numpy as np
from string import punctuation
import requests

import re
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GRU, Embedding
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.models import load_model


from konlpy.tag import Kkma
from db import Db
from gen import Generator
from parse import Parser
from sql import Sql
from rnd import Rnd
import sys
import sqlite3
import codecs

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QApplication,QGraphicsDropShadowEffect,QGraphicsOpacityEffect,QLabel
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtCore

import time

# id 무작위 생성하기

def randomID():
    candidate=string.ascii_letters+string.digits
    new_id=""
    for i in range(4,10):
        new_id=new_id+random.choice(candidate)
    return new_id

#댓글 불러오기(유튜브 댓글 크롤링)

comments = list()
api_obj = build('youtube', 'v3', developerKey='AIzaSyDmX546Img36i0nyTLi74Z_H_YmYApCxys')
response = api_obj.commentThreads().list(part='snippet,replies', videoId='HMyn6eMV0OA', maxResults=100).execute()


while response:
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append([comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'], comment['likeCount']])
 
        if item['snippet']['totalReplyCount'] > 0:
            for reply_item in item['replies']['comments']:
                reply = reply_item['snippet']
                comments.append([reply['textDisplay'], reply['authorDisplayName'], reply['publishedAt'], reply['likeCount']])
 
    if 'nextPageToken' in response:
        response = api_obj.commentThreads().list(part='snippet,replies', videoId='HMyn6eMV0OA', pageToken=response['nextPageToken'], maxResults=100).execute()
    else:
        break

df = pandas.DataFrame(comments)
df.to_excel('results.xlsx', header=['comment', 'author', 'date', 'num_likes'], index=None)

#댓글 다듬기(html 태그 가진 댓글 지우기)
ds=pandas.read_excel("results.xlsx")
real=ds[~(ds['comment'].str.contains('br')) & ~(ds['comment'].str.contains('<a href'))]

#학습 전 한 텍스트 파일에 모으기
real[['comment']].to_csv('clean.txt', index=False, header=False)

#감정 분석하기

#댓글 학습하기


real['comment'].to_csv('origin_list.txt', sep='\n', index=False)
text=open('origin_list.txt', 'r', encoding='UTF-8')

SENTENCE_SEPARATOR = '\n' # 문장 구분 코드
WORD_SEPARATOR = ' '      # 어절 구분 코드

# 학습하기
def train(text, name = 'steemit', depth = 2):
    db = Db(sqlite3.connect(name + '.db'), Sql())
    db.setup(depth);
    Parser(name, db, SENTENCE_SEPARATOR, WORD_SEPARATOR).parse(text)
    
train(text)

# 문장 생성하기
def generate(name = 'steemit', count = 5):
    db = Db(sqlite3.connect(name + '.db'), Sql())
    generator = Generator(name, db, Rnd())
    result = []
    for i in range(0, count):
        result.append(generator.generate(WORD_SEPARATOR))
    return result
        
generate()

#댓글창 만들기
FROM_CLASS = uic.loadUiType("comment.ui")[0]

class Windows(QMainWindow,FROM_CLASS):

    def __init__(self, on_top=True):
        super().__init__()

        # setup user interface
        self.setupUi(self) 
        
        # 내용 변경
        self.ID1.setText("random1234") #텍스트 변환       
        self.ID1.setStyleSheet("Color : lime") #글자색 변환
        self.ID2.setText("randomrand") #텍스트 변환       
        self.ID2.setStyleSheet("Color : pink") #글자색 변환
        self.ID3.setText("1234567890") #텍스트 변환       
        self.ID3.setStyleSheet("Color : orange") #글자색 변환
        
        
        # creating label
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
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
       

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
       
    def firstCommentPage(self, event): 
        random1=randomID()
        random2=randomID()
        random3=randomID()
        Windows.ID3.setText(random1)
        Windows.ID2.setText(random2)
        Windows.ID1.setText(random3)
        
        def commentChange(random2, random3):
            time.sleep(0.5)
            Windows.ID1.setText(random2)
            Windows.ID2.setText(random3)
            Windows.ID3.setText(randomID())
        
        
    

#댓글창 띄우기
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ShowApp = Windows()
    sys.exit(app.exec_())