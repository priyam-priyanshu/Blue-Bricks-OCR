import cv2
import pytesseract as pytes
import numpy as np
import os
import img_preprocess
from data_card import node
from pytesseract.pytesseract import Output
pytes.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

#takes pytes data and filters it and returns the text and confidence
def generate_contex(data):
    text=""
    confid=0
    n=0
    for i in range(len(data["level"])):
        if(data["text"][i]!="" and data["conf"][i]!=" "):
            text+=data["text"][i]+" "
            confid+=data["conf"][i]
            n+=1
    if n!=0:
        confid=confid/n
    return text, confid          


#takes part of image as input and returns a node containing its text and confidence
def make_nodes(img,x,y,w,h,i):
    #cropping image
    img= img[y:(y+h),x:(x+w)]
    #generating data from tesseract
    data =pytes.image_to_data(img,output_type=Output.DICT)

    #filter out the data and generate text and confidence 
    text,confid=generate_contex(data)

    #if confidence is not good then leave that data 
    if confid==0:
        new_node=node(text,confid)
        return new_node , False
    else :
        new_node=node(text,confid)
        return new_node , True


def dilate(img):
    img_to_dilate=img_preprocess.remove_lines(img)

    #invert image
    img_to_dilate=(255-img)
    
    #create kernel for dilation
    kernel=np.array([[0,0,0,0,0],
                     [1,1,1,1,1],
                     [1,1,1,1,1],
                     [1,1,1,1,1],
                     [0,0,0,0,0]],np.uint8)
    
    #dilation
    dilated_img=cv2.dilate(img_to_dilate,kernel,iterations=10)
    return dilated_img

def passing(img):
    #make a seperate copy of image to dilate
    img_to_dilate=img.copy()
    
    #get the dilated image
    dilated_img=dilate(img)
    
    #finding contours to make crop
    contours, _ = cv2.findContours(dilated_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #list for storing nodes
    lst=[]
    # img=img_preprocess.process_from_path("Images/1.png")
    for i in range(len(contours)) :
        x,y,w,h=cv2.boundingRect(contours[i])
        # img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        new_node,flag=make_nodes(img,x,y,w,h,i)
        if flag==True:
            lst.append(new_node)
    
    return lst