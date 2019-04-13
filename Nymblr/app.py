import os, json, mysql.connector as mariadb, pprint, sqlite3
from datetime import datetime
from flask import Flask, render_template, request
from flask_googlelogin import GoogleLogin
from flask_login import LoginManager

# Initialization
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
googlelogin = GoogleLogin(app, login_manager)

@app.route('/')
@login_required
def home():
    return render_template(
        'editor.htm'
        )

@app.route('/update', methods=['POST'])
def update():
    text =  request.form['text'];
    return text

@app.route('/oauth2callback')
@googlelogin.oauth2callback
def create_or_update_user(token, userinfo, **params):
    print(google_id=userinfo['id'])
    return redirect(url_for('/'))