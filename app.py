#!/usr/bin/env python
# coding: utf-8


from flask import Flask,request,render_template
import json
import pytesseract
import datefinder
import re
from PIL import Image
from itertools import chain


app=Flask(__name__,template_folder='/home/acer/Desktop/fyle_ass')

def find_date2(filename):
    text=pytesseract.image_to_string(Image.open(filename),lang='eng')
    datepattern = '%d-%m-%Y'
    x=[]
    for i in text.split('\n'):
        z=re.findall('\d\d-\d\d-\d\d\d\d',i)
        if(z==[]):
            continue
        else:
            for j in list(chain(z)):
                x.append(j)
    return(render_template('user.html',users=x))

@app.route('/date_finder',methods=['POST'])
def date_finder():
    if request.method=='POST':
        if ('media' in request.files):    
            file1 = request.files.get('media')
            return(find_date2(file1))
app.run(debug=True)
