# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 15:08:09 2021

@author: ksy
"""

import random
import string
import pandas
from googleapiclient.discovery import build
import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, LSTM

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QApplication,QGraphicsDropShadowEffect,QGraphicsOpacityEffect,QLabel
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtCore

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

#댓글 학습하기(1) 댓글만 모으고 단어집합 만들기
cut=[]
for i in range(0,4610):
    cut.append(real['comment'].values[i])
    
tokenizer=Tokenizer()
tokenizer.fit_on_texts(cut)
vocab_size=len(tokenizer.word_index)+1

#댓글 학습하기(2) 훈련 데이터 구성
sequences=list()
for sentence in cut:
    encoded=tokenizer.texts_to_sequences([sentence])[0]
    for i in range(1, len(encoded)):
        sequence=encoded[:i+1]
        sequences.append(sequence)
        
#댓글 학습하기(3) 예측할 단어에 해당되는 레이블 분리
index_to_word = {}
for key, value in tokenizer.word_index.items(): 
    index_to_word[value] = key

max_len = max(len(l) for l in sequences)

sequences = pad_sequences(sequences, maxlen=max_len, padding='pre')

sequences = np.array(sequences)
X = sequences[:,:-1]
y = sequences[:,-1]

y = to_categorical(y, num_classes=vocab_size)

#댓글 학습하기(4) 모델 설계하기
embedding_dim = 10
hidden_units = 128

model = Sequential()
model.add(Embedding(vocab_size, embedding_dim))
model.add(LSTM(hidden_units))
model.add(Dense(vocab_size, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=50, verbose=2)

def sentence_generation(model, tokenizer, current_word, n): # 모델, 토크나이저, 현재 단어, 반복할 횟수
    init_word = current_word
    sentence = ''

    # n번 반복
    for _ in range(n):
        encoded = tokenizer.texts_to_sequences([current_word])[0]
        encoded = pad_sequences([encoded], maxlen=max_len-1, padding='pre')

        # 입력한 X(현재 단어)에 대해서 y를 예측하고 y(예측한 단어)를 result에 저장.
        result = model.predict(encoded, verbose=0)
        result = np.argmax(result, axis=1)

        for word, index in tokenizer.word_index.items(): 
            # 만약 예측한 단어와 인덱스와 동일한 단어가 있다면
            if index == result:
                break

        # 현재 단어 + ' ' + 예측 단어를 현재 단어로 변경
        current_word = current_word + ' '  + word

        # 예측 단어를 문장에 저장
        sentence = sentence + ' ' + word

    sentence = init_word + sentence
    return sentence

seed=['공부', '파이팅', '와','ㅋㅋㅋ', '대단', '아니', '열심', '열정', '중간고사', '기말고사', '시험', '오늘', '매일', '존경', '리스펙', '멋지다', '덕분에', '끝', '보면서', '재밌다', '집중', '화이팅', '성공', '고맙다', '좋아요', '힘내', '기념', '또', '밤', '아침']

#print(sentence_generation(model,tokenizer, random.choice(seed), random.randrange(1,30)))


#댓글창 만들기

random1=randomID()
random2=randomID()
random3=randomID()
ran_comment1=sentence_generation(model,tokenizer, random.choice(seed), random.randrange(1,30))
ran_comment2=sentence_generation(model,tokenizer, random.choice(seed), random.randrange(1,30))
ran_comment3=sentence_generation(model,tokenizer, random.choice(seed), random.randrange(1,30))

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
        
        self.label1 = QLabel("김신영이 제작한 Study With me", self)
  
        # setting geometry to the label
        self.label1.setGeometry(210, 20, 700, 150)
        self.label1.setAlignment(Qt.AlignTop)
        # making it multi line
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet("Color:white;")
        
        self.label2 = QLabel("다들 준비 되셨나요?", self)
  
        # setting geometry to the label
        self.label2.setGeometry(210, 140, 700, 150)
        self.label2.setAlignment(Qt.AlignTop)
        # making it multi line
        self.label2.setWordWrap(True)
        self.label2.setStyleSheet("Color:white;")
        
        self.label3 = QLabel("그럼 시작합니다!", self)
  
        # setting geometry to the label
        self.label3.setGeometry(210, 260, 700, 150)
        self.label3.setAlignment(Qt.AlignTop)
        # making it multi line
        self.label3.setWordWrap(True)
        self.label3.setStyleSheet("Color:white;")
        
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
        self.label1.setGraphicsEffect(self.shadow4)
        self.label2.setGraphicsEffect(self.shadow5)
        self.label3.setGraphicsEffect(self.shadow6)
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
        self.label3.setText(ran_comment1)
        self.label2.setText(ran_comment2)
        self.label1.setText(ran_comment3)
        
        self.timer = QTimer()
        self.timer.setInterval(500)   
        self.timer.timeout.connect(lambda:self.commentChange())
        self.timer.start()
        
    def commentChange(self):
        global random2
        global random1
        global ran_comment1
        global ran_comment2
        random3=random2
        random2=random1
        random1=randomID()
        ran_comment3=ran_comment2
        ran_comment2=ran_comment1
        ran_comment1=sentence_generation(model,tokenizer, random.choice(seed), random.randrange(1,30))
        self.ID3.setText(random1)
        self.ID2.setText(random2)
        self.ID1.setText(random3) 
        self.label3.setText(ran_comment1)
        self.label2.setText(ran_comment2)
        self.label1.setText(ran_comment3)
        return random1, random2, random3, ran_comment1, ran_comment2, ran_comment3

#댓글창 띄우기

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ShowApp = Windows()
    sys.exit(app.exec_())
