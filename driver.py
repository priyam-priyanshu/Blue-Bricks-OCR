import pass3
import json
import cv2
import img_preprocess
import pass3,pass1,search
import pdf2Text
#converting to json 
def to_json(dic):
    json_object = json.dumps(dic, indent = 4) 
    return json_object

def func(path,keys,ind):
    if ind=="png":
        return extract_from_img(path,keys)
    elif ind=="pdf":
        return extract_from_pdf(path,keys)

def extract_from_img(path,keys):
    img=img_preprocess.process_from_path(path)
    text=pass1.passing(img)
    lst=pass3.passing(text)
    dic=search.search(lst,keys)
    return(to_json(dic))

def extract_from_pdf(path,keys):
    text=pdf2Text.convert(path)
    lst=pass3.passing(text)
    dic=search.search(lst,keys)
    return(to_json(dic))