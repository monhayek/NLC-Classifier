main.py
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint #random is module, randit is a function from that module
import json
import WNLCInterface as wlnc

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        'index.html',**locals())

@app.route("/train", methods=['POST', 'GET'])
def train():
    return render_template(
        'train.html',**locals())

@app.route("/trainResult", methods=['POST'])
def trainResult():
    ServiceUserName = request.form['servicename']
    ServicePW = request.form['servicepw']
    CLFName = request.form['classifiername']
    NLCService = wlnc.getNLCService(ServiceUserName, ServicePW)
    status = wlnc.listClassifiers(NLCService)
    # status = wlnc.createClassifier(NLCService, CLFName, FilePath)
    return render_template(
        'trainResult.html',**locals())

@app.route("/classify", methods=['POST', 'GET'])
def classify():
    return render_template(
        'classify.html',**locals())

@app.route("/classifyResult", methods=['POST'])
def classifyResult():
    ServiceUserName = request.form['servicename']
    ServicePW = request.form['servicepw']
    CLFName = request.form['classifiername']
    TopNPredictions = int(request.form['classNum'])
    InputText = request.form['inputText']
    NLCService = wlnc.getNLCService(ServiceUserName, ServicePW)
    result = wlnc.getTextPrediction(NLCService, CLFName, TopNPredictions, InputText)
    return render_template(
        'classifyResult.html',**locals())

if __name__ == "__main__":
    app.run()
