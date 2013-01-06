from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
import json
import urllib2

from threading import Thread
from time import sleep
import pymongo
from pymongo import Connection

app = Flask(__name__)

DATABASE = '/tmp/demo.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

class db():

    connection = None

    def __enter__(self):
        print 'enter db'
	self.connection = Connection()
	db = self.connection.stats_db
	return db.stats_db
    def __exit__(self, type, value, traceback):
        self.connection.close()
        print 'exit db'

def database_check_loop():
    while 1:
        print 'loop'
        try:
            jsonData = urllib2.urlopen('http://localhost:1234')
            data = json.load(jsonData)
            add_data_to_db(data)
        except Exception, e:
            print 'Data not received. Number server not running?'
	sleep(10)

def add_data_to_db(new_data):
    print 'add'
    with db() as a:
        a.save(new_data)

def get_latest_data():
    with db() as a:
        data =  a.find().sort("_id", -1).limit(1)[0]
    return data

@app.route('/_update_data')
def _update_data():
    print get_latest_data()
    return jsonify(get_latest_data()["data"])

@app.route("/")
def root():
    return render_template("layout.html")

@app.route("/cpu")
def cpu():
    return render_template("data.html", data = get_latest_data(), key = 'cpu')

@app.route("/mem")
def mem():
    return render_template('data.html', data = get_latest_data(), key = 'mem')

@app.route("/dbdump")
def dbdump():
    with db() as a:
        data = a.find()
    toReturn = []
    for doc in data:
        toReturn.append( str(doc))
    return render_template('dbdump.html', data = toReturn)

if __name__ == "__main__":
#    app.run(debug = True)
    a = Thread(target = app.run)
    a.start()
    b = Thread(target = database_check_loop)
    b.start()
