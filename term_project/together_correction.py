# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 03:27:17 2021

@author: ksy
"""

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

# id 무작위 생성하기
candidate=string.ascii_letters+string.digits
new_id=""
for i in range(4,10):
    new_id=new_id+random.choice(candidate)
print(new_id)

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
feel = pandas.read_excel('feeling.xlsx', sheet_name="Sheet1")


def storeTraining(text, label):
    key = "e7d2f5d0-6008-11ec-b52f-c1ff1db62c35713caa07-21a0-4a2b-9475-0c928a962ffe"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/train"

    response = requests.post(url, json={ "data" : text, "label" : label })

    if response.ok == False:
        # if something went wrong, display the error
        print (response.json())

for i in range(0,4868):
    training=feel['단어']
    label="good"


storeTraining(training, label)

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "e7d2f5d0-6008-11ec-b52f-c1ff1db62c35713caa07-21a0-4a2b-9475-0c928a962ffe"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify
demo = classify("The text that you want to test")

label = demo["class_name"]
confidence = demo["confidence"]

# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (label, confidence))



#댓글 학습하기



#댓글창 만들기


#댓글창 띄우기
