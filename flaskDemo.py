from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import sqlite3
app = Flask(__name__)

DATABASE = '/tmp/demo.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

@app.route("/")
def hello():
    
    return "Stats monitor"

if __name__ == "__main__":
    app.run()
