import img_preprocess
import pytesseract


def preprocess(corpus):
    txt = corpus.split("\n")
    while "" in txt:
        txt.remove("")
    
    txt = '\n'.join(txt)
    return txt

def passing(img):
    custom_config = r'-c preserve_interword_spaces=1 --psm 4'
    txt = pytesseract.image_to_string(img, config=custom_config)
    txt = preprocess(txt)
    return txt