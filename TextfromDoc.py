from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
import os
import string
import random
import img_preprocess
from pdf2Text import convert_from_path
import time
from driver import func
import cv2

uploaded_folder = "Images"
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@app.route("/")
def home():
    return "<h1>SMART OCR EXTRACTION </h1>"


@app.route("/TextFromDoc", methods=['POST'])

def textfromdoc():

    document= request.files['doc']
    keys= request.args.getlist('key')
    filename_complete_name = secure_filename(document.filename)
    filename_front_name = filename_complete_name.split(".")[0]

    idx = len(filename_complete_name.split('.')) - 1 
    filename_ext = filename_complete_name.split(".")[idx]
    filename_new_name = filename_front_name + str(id_generator()) + "." + filename_ext
    document.save(os.path.join(uploaded_folder, filename_new_name))
    image_path = os.path.join(uploaded_folder, filename_new_name)

    data=func(image_path,keys,filename_ext)

    return data 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9510, debug=True)
