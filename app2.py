from flask import Flask, request, render_template
from string import upper
from random import random, shuffle
from copy import deepcopy
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///n2.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(80), unique=False)
    capacity = db.Column(db.String(80), unique=False)
    contact = db.Column(db.String(80), unique=False)
    image_url = db.Column(db.String(1024), unique=False)

    def __init__(self, location, capacity, contact, image_url):
        self.location = location
        self.capacity = capacity
        self.contact = contact
        self.image_url = image_url

    def __repr__(self):
        return '[location: %r, capacity:%r, contact:%r, URL:%r]' % (
            self.location, self.capacity, self.contact, self.image_url)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run()


