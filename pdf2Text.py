from pdf2image import convert_from_path
import numpy
import pytesseract
import cv2
from img_preprocess import process_from_img
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
custom_config = r'-c preserve_interword_spaces=1 --psm 4'

def convert(path):
    images=convert_from_path(path,fmt="png",poppler_path=r"C:\poppler-23.01.0\Library\bin")
    txt=""
    for img in images:
        opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
        opencvImage=process_from_img(opencvImage)
        txt=txt+"\n"+ pytesseract.image_to_string(opencvImage, config=custom_config)
    return txt
