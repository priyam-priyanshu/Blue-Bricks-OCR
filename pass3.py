import cv2
import numpy as np
import pandas as pd
import re
import math
import search
import matplotlib.pyplot as plt
import pass1
import json
from flask import jsonify
import pytesseract as pytes
from data_card import node
import pass2
import img_preprocess
import pdf2Text
from PIL import Image, ImageFilter
from pytesseract import Output 
pytes.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def passing(text):

    lines =text.split("\n")
    ans=[[]]
    for line in lines:
        tokens = re.findall('\s+', line)
        mylist=[]
        words=re.split("\s+", line)
        prefix=""
        
        for i in range(0,len(words)-1):
            if i!=0:
                prefix+=" "+words[i]
            else:
                prefix=words[i]
            
            if len(tokens[i])>1:
                mylist.append(prefix)
                prefix=""
        mylist.append(prefix+" "+words[len(words)-1])
        ans.append(mylist)
    return ans 



