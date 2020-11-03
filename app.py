from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import pickle as pk
# Keras
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer


# Flask utils
from flask import Flask, redirect, url_for, request, render_template, jsonify
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
ECML_CNN = 'models/ecmlcnnkeras.h5'
ECML_DNN = 'models/ecmldnnkeras.h5'
CSIC_CNN = 'models/csiccnnkeras.hs'
CSIC_DNN = 'models/csicdnnkeras.h5'
# Load trained model

# CNN trained with ECML/PKDD 2007 dataset
ecmlcnn_model = load_model(ECML_CNN)
ecmlcnn_model._make_predict_function()          # Necessary

# DNN trained with ECML/PKDD 2007 dataset
# ecmldnn_model = load_model(ECML_DNN)
# ecmldnn_model._make_predict_function()          # Necessary

# CNN trained with CSIC 2010 dataset
csiccnn_model = load_model(CSIC_CNN)
csiccnn_model._make_predict_function()          # Necessary

#DNN trained with CSIC 2010 dataset
# csicdnn_model = load_model(CSIC_DNN)
# csicdnn_model._make_predict_function()          # Necessary

# load tokenizer object
tokenizer_file = open('models/tokenizerecml.pickle','rb') 
tokenizer = pk.load(tokenizer_file)

print('Model loaded. Check http://127.0.0.1:5000/')

# prediction from ecml/pkdd trained cnn model
def ecmlcnnmodel(minput):
    return ecmlcnn_model.predict(minput)

# prediction from ecml/pkdd trained dnn model
# def ecmldnnmodel(minput):
#     return ecmldnn_model.predict(minput)

# prediction from csic trained cnn model
def csiccnnmodel(minput):
    return csiccnn_model.predict(minput)

# prediction from csic trained dnn model
# def csicdnnmodel(minput):
#     return csicdnn_model.predict(minput)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/ecml/cnn/predict',methods=['GET','POST'])
def ecmlcnnpredict():
    if request.method == 'POST':
        body = request.get_data()
        requestparams = str(body)
    elif request.method == 'GET':
        query = request.query_string
        requestparams = str(query)
    else:
        return None
    requestparams = requestparams[2:len(requestparams)-1]
    character_indexes = tokenizer.texts_to_sequences(requestparams) #get character indexes
    character_indexes = [char_index for chars in character_indexes for char_index in chars] #flatten char index array to 1d
    data = pad_sequences([character_indexes],maxlen=840,padding='post') #pad char indexes to reach length 840
    result = ecmlcnnmodel(data)#get predictions
    benign = result[0][0] #benign probability
    malicious = result[0][1] #malicious probability
    response = {"benign":float(benign),"malicious":float(malicious)} #response
    return jsonify(response)

# @app.route('/ecml/dnn/predict',methods=['GET','POST'])
# def ecmldnnpredict():
#     if request.method == 'POST':
#         body = request.get_data()
#         requestparams = str(body)
#     elif request.method == 'GET':
#         query = request.query_string
#         requestparams = str(query)
#     else:
#         return None
#     requestparams = requestparams[2:len(requestparams)-1]
#     character_indexes = tokenizer.texts_to_sequences(requestparams) #get character indexes
#     character_indexes = [char_index for chars in character_indexes for char_index in chars] #flatten char index array to 1d
#     data = pad_sequences([character_indexes],maxlen=840,padding='post') #pad char indexes to reach length 840
#     result = ecmldnnmodel(data)#get predictions
#     benign = result[0][0] #benign probability
#     malicious = result[0][1] #malicious probability
#     response = {"benign":float(benign),"malicious":float(malicious)} #response
#     return jsonify(response)

@app.route('/csic/cnn/predict',methods=['GET','POST'])
def csiccnnpredict():
    if request.method == 'POST':
        body = request.get_data()
        requestparams = str(body)
    elif request.method == 'GET':
        query = request.query_string
        requestparams = str(query)
    else:
        return None
    requestparams = requestparams[2:len(requestparams)-1]
    character_indexes = tokenizer.texts_to_sequences(requestparams) #get character indexes
    character_indexes = [char_index for chars in character_indexes for char_index in chars] #flatten char index array to 1d
    data = pad_sequences([character_indexes],maxlen=840,padding='post') #pad char indexes to reach length 840
    result = csiccnnmodel(data)#get predictions
    benign = result[0][0] #benign probability
    malicious = result[0][1] #malicious probability
    response = {"benign":float(benign),"malicious":float(malicious)} #response
    return jsonify(response)

# @app.route('/csic/dnn/predict',methods=['GET','POST'])
# def csicdnnpredict():
#     if request.method == 'POST':
#         body = request.get_data()
#         requestparams = str(body)
#     elif request.method == 'GET':
#         query = request.query_string
#         requestparams = str(query)
#     else:
#         return None
#     requestparams = requestparams[2:len(requestparams)-1]
#     character_indexes = tokenizer.texts_to_sequences(requestparams) #get character indexes
#     character_indexes = [char_index for chars in character_indexes for char_index in chars] #flatten char index array to 1d
#     data = pad_sequences([character_indexes],maxlen=840,padding='post') #pad char indexes to reach length 840
#     result = csicdnnmodel(data)#get predictions
#     benign = result[0][0] #benign probability
#     malicious = result[0][1] #malicious probability
#     response = {"benign":float(benign),"malicious":float(malicious)} #response
#     return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True, threaded=True)

    # Serve the app with gevent
    # http_server = WSGIServer(('0.0.0.0', 5000), app)
    # http_server.serve_forever()
