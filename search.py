import numpy as np
import re
from thefuzz import fuzz
import math
import matplotlib.pyplot as plt
import img_preprocess
import cv2
from PIL import Image, ImageFilter
from pytesseract import Output 

def process(lst):
    new_list=[[]]
    for line in lst:
        mylist=[]
        for word in line:
            new_word=re.sub("[^A-Za-z0-9/ ]+", "", word,0,)
            new_word=re.sub("^ +", "", new_word,0)
            new_word=re.sub(" +$", "", new_word,0)
            # new_word=new_word.lower()
            mylist.append(new_word)
        new_list.append(mylist)
    return new_list
            
def search(lst,keys):
    new_list=process(lst)
    # print(new_list)
    dic={}
    for line in new_list:
        for i in range(len(line)-1):
            key_res=[i for key in keys if(fuzz.ratio(key.lower(),line[i].lower())>=80)]
            if(len(key_res)>0):
                dic[line[i]]=line[i+1]

    return dic