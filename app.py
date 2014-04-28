from flask import Flask, request, render_template
from string import upper
from random import random, shuffle
from copy import deepcopy
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Glitch.db'
db = SQLAlchemy(app)

class Tutorials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False)
    image = db.Column(db.String(1024), unique=False)
    description = db.Column(db.String(80), unique=False)
    link = db.Column(db.String(1024), unique=False)

    def __init__(self, title, image, description, link):
        self.title = title
        self.image = image
        self.description = description
        self.link = link

    def __repr__(self):
        return '[title: %r, image:%r, description:%r, link:%r]' % (
            self.title, self.image, self.description, self.link)

class Models(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(1024), unique=False)

    def __init__(self, image):
        self.image = image

    def __repr__(self):
        return '[image:%r]' % (
            self.image)

class User2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(80), unique=False)
    last = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(80), unique=False)
    username = db.Column(db.String(80), unique=False)
    password = db.Column(db.String(80), unique=False)
    gender = db.Column(db.String(80), unique=False)

    def __init__(self, first, last, email, username, password, gender):
        self.first = first
        self.last = last
        self.email = email
        self.username = username
        self.gender = gender

    def __repr__(self):
        return '[first: %r, last:%r, email:%r, username:%r, password:%r, gender:%r]' % (
            self.first, self.last, self.email, self.username, self.password, self.gender)

class UserBinder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, unique=False)
    image = db.Column(db.String(1024), unique=False)
    description = db.Column(db.String(1024), unique=False)

    def __init__(self, title, image, description):
        self.title = title
        self.image = image
        self.description = description

    def __repr__(self):
        return '[title:%r, image%r, description%r]' % (self.title, self.image, self.description)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/myBinder/')
@app.route('/myBinder/<name>')
def myBinder(name=None):
    gravity = Models.query.limit(8).all()
    return render_template('myBinder.html', gravity=gravity)

@app.route('/signIn/')
@app.route('/signIn/<name>')
def signIn(name=None):
    return render_template('signIn.html', name=name)

@app.route('/signUp/')
@app.route('/signUp/<name>')
def signUp(name=None):
    return render_template('signUp.html', name=name)

@app.route('/tutorial/')
@app.route('/tutorial/<name>')
def tutorial(name=None):
    pet = Tutorials.query.limit(4).all()
    return render_template('tutorial.html', pet=pet)

@app.route('/forum/')
@app.route('/forum/<name>')
def forum(name=None):
    return render_template('forum.html', name=name)

@app.route('/forum_submitted/')
@app.route('/forum_submitted/<name>')
def forum_submitted(name=None):
    return render_template('forum_submitted.html', name=name)

@app.route('/upload/')
@app.route('/upload/<name>')
def upload(name=None):
    return render_template('upload.html', name=name)


@app.route('/view/<name>')
def view(name=None):

    location = User.query.filter_by(location=name).first()

    return render_template('view.html', location=location)


@app.route('/search', methods=['GET'])
def search():
    try:
        location = request.args.get('location', '')
        capacity = request.args.get('capacity', '')
    except KeyError:
        return 'No brah, you cannot go there'

    if location and capacity:
        results = db.session.query(User).filter(User.location.like(location)).filter(User.capacity.like(capacity)).all()
    elif location:
        results = db.session.query(User).filter(User.location.like(location)).all()
    elif capacity:
        results = db.session.query(User).filter(User.capacity.like(capacity)).all()    
    # results = db.session.query(User).filter(User.location.like(location)).filter(User.capacity.like(capacity)).all()
    #results += db.session.query(User).filter(User.capacity.like(capacity)).all()

    return render_template('search.html', results=results)

if __name__ == "__main__":
    app.run()

TutorialDatabase = [Tutorials('box', 'http://oi58.tinypic.com/122cig6.jpg', 'Basic box tutorial', 'http://www.youtube.com/watch?v=cy3ExIAcI2Y'),
Tutorials('heart', 'http://oi58.tinypic.com/soqnpu.jpg', 'Fun heart tutorial', 'https://www.youtube.com/watch?v=mxWq4zKE2jY'),
Tutorials('nut', 'http://oi57.tinypic.com/64jfc2.jpg', 'Great nut tutorial', 'http://www.youtube.com/watch?v=T_K79NHf9Gg'), 
Tutorials('screw', 'http://oi59.tinypic.com/id6iom.jpg', 'Best nuts and screw tutorial', 'http://www.youtube.com/watch?v=hXwCE1P02wc')]

ModelDatabase = [Models('http://files.solidworks.com/InternalMarketing/PressRoom/Automotive/solidworksbike.jpg'),
Models('http://www.nvidia.com/content/quadro/professional-solutions/solidworks/image/realview-enhanced-3d-mode.jpg'),
Models('http://www.personal.psu.edu/npf5008/SolidworksFinal_htm_m14df6603.jpg'),
Models('https://forum.solidworks.com/servlet/JiveServlet/showImage/2-321453-55572/Capture+2.JPG'),
Models('http://i35.tinypic.com/au7hc7.png'),
Models('http://www.topfreemodel.com/uploads/images/SolidWorks-Models-Boeing-757-aircraft.jpg'),
Models('http://www.topfreemodel.com/uploads/images/SolidWorks-Models-020-Vintage-Aircraft.jpg')]

UserDatabase = [User2('Bob', 'White', 'pitbull@dogs.com', 'Clean', 'Windex', 'male'),
User2('Girl', 'Waldenburgeourgew', 'golden@child.com', 'WonderBread', 'password', 'female')]

jokes = [UserBinder('box', 'http://oi58.tinypic.com/122cig6.jpg', 'Basic box tutorial'), 
UserBinder('heart', 'http://oi58.tinypic.com/soqnpu.jpg', 'Fun heart tutorial'), 
UserBinder('nut', 'http://oi57.tinypic.com/64jfc2.jpg', 'Great nut tutorial'), 
UserBinder('screw', 'http://oi59.tinypic.com/id6iom.jpg', 'Best screw tutorial')]