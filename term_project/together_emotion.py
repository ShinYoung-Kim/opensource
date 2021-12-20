# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 21:27:21 2021

@author: ksy
"""

import pyautogui
import pyperclip
import time
import sys
import pandas as pd

df = pd.read_excel('feeling.xlsx', sheet_name="Sheet1")
words=df[df["감정범주"].isin(["긍정"])][:][["단어"]].drop_duplicates().values.flatten()

def click(x,y):
    time.sleep(0.5)
    pyautogui.moveTo(x,y)
    pyautogui.click(clicks=1)
    time.sleep(0.5)

for i in range(len(words)):
    click(700,1900)
    
    pyperclip.copy(words[i])
    pyautogui.hotkey("ctrl", "v")
    click(2200,1400)
    