#!/usr/bin/env python

from flask import Flask, render_template
import MySQLdb

app = Flask(__name__)
app.debug = True

@app.route('/')
def db():
    db = MySQLdb.connect("172.17.0.2", "app_user", "h3ll0w0rld", "hello_world")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM hello_world")
    data = cursor.fetchall()
    db.close()
    return render_template('db.html', data = data)

if __name__ == "__main__":
    app.run()

