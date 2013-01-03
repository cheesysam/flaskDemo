from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import json
import urllib2
import sqlite3

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


@app.route("/")
def root():
    return str(data)

def database_check_loop():
    while 1:
        print 'loop'
        try:
            jsonData = urllib2.urlopen('http://localhost:1234')
            data = json.load(jsonData)
            add_data_to_db(data)
        except Exception, e:
            data = 'Data not received. Number server not running?'
	sleep(10)

def add_data_to_db(new_data):
    print 'add'
    with db() as a:
        a.save(new_data)

if __name__ == "__main__":
    db_thread = Thread(target = database_check_loop())
    db_thread.start()
    app.run()
