from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import json
import urllib2
import sqlite3
app = Flask(__name__)

DATABASE = '/tmp/demo.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

@app.route("/")
def root():
    try:
        jsonData = urllib2.urlopen('http://localhost:1234')
        data = json.load(jsonData)
    except Exception, e:
        data = 'Data not received. Number server not running?'
    return str(data)
    
if __name__ == "__main__":
    app.run()
