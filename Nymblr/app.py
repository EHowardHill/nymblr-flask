import os, json, pprint
from flask import Flask, render_template, request, send_from_directory

# Initialization
UPLOAD_FOLDER = '/txt-uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'fountain'])
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('editor.htm')

@app.route('/save', methods=['POST'])
def save():
    return send_from_directory('./temp/', 'myfile.txt')