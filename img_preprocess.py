import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytesseract as pytes
from PIL import Image, ImageFilter

#=========================***UTILITY FUNCTIONs***==========================#

def show_img(img, txt="--NO_NAME--)"):
    cv2.imshow(txt, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass


def normalise(img) :
    norm_img=np.zeros((img.shape[0],img.shape[1]))
    img=cv2.normalize(img,norm_img,0,255,cv2.NORM_MINMAX)
    return img


def noise_removal(img):
    return cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)


def image_scale(img):
    img = cv2.resize(img, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC)
    return img


def remove_lines(img):
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25,1))
    detected_lines = cv2.morphologyEx(img, cv2.MORPH_OPEN, horizontal_kernel, iterations=7)
    cnts = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    
    for c in cnts:
        cv2.drawContours(img, [c], -1, (255,255,255), 7)


    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,25))
    detected_lines = cv2.morphologyEx(img, cv2.MORPH_OPEN, vertical_kernel, iterations=10)
    cnts = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(img, [c], -1, (255,255,255), 10)


    return img

#=========================================MAIN FUNCTION(s)====================================================

def process_from_path(path):
    img = cv2.imread(path)

    #normalisation
    img=normalise(img)

    #image_scale
    img=image_scale(img)

    #noise removal
    img=noise_removal(img)

    #greyscale and blur
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img=cv2.medianBlur(img, 1)
    img=cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # img=remove_lines(img)

    return img


def process_from_img(img):
    
    #normalisation
    img=normalise(img)

    #image_scale
    img=image_scale(img)

    #noise removal
    img=noise_removal(img)

    #greyscale and blur
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img=cv2.medianBlur(img, 1)
    img=cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # img=remove_lines(img)

    return img