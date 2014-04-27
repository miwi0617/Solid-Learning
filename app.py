from flask import Flask, request, render_template
from string import upper
from random import random, shuffle
from copy import deepcopy
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Glitch.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.String(80), unique=False)
    gender = db.Column(db.String(80), unique=False)
    breed_type = db.Column(db.String(80), unique=False)
    age = db.Column(db.String(80), unique=False)
    image_url = db.Column(db.String(1024), unique=False)

    def __init__(self, pet_name, gender, breed_type, age, image_url):
        self.pet_name = pet_name
        self.gender = gender
        self.breed_type = breed_type
        self.age = age
        self.image_url = image_url

    def __repr__(self):
        return '[pet name: %r, gender:%r, breed type:%r, age:%r, URL:%r]' % (
            self.pet_name, self.gender, self.breed_type, self.age, self.image_url)

class User2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(80), unique=False)
    last = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(80), unique=False)
    username = db.Column(db.String(80), unique=False)
    password = db.Column(db.String(80), unique=False)
    gender = db.Column(db.String(80), unique=False)
    image_url = db.Column(db.String(1024), unique=False)
    title = db.Column(db.String(80), unique=False)

    def __init__(self, first, last, email, contact, image_url):
        self.first = first
        self.last = last
        self.email = email
        self.image_url = image_url
        self.title = title

    def __repr__(self):
        return '[first:%r, last:%r, email:%r, URL:%r, title:%r]' % (
            self.first, self.last, self.email, self.image_url, self.title)

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
    pet = User.query.limit(10).all()
    return render_template('myBinder.html', pet=pet)

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
    return render_template('tutorial.html', name=name)

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


h = [User('bob', 'male', 'pitbull', '11', 'http://www.monstropedia.org/images/thumb/d/d0/Boogeyman.jpg/250px-Boogeyman.jpg'),
User('zack', 'male', 'golden', '3', 'http://www.monstropedia.org/images/thumb/d/d0/Boogeyman.jpg/250px-Boogeyman.jpg'),
User('jenny', 'female', 'shepard', '4', 'http://wpc.556e.edgecastcdn.net/80556E/img.news/NE8zZcdd0INrbd_1_1.jpg'),
User('mirna', 'female', 'akita', '5', 'http://www.tenorama.com/sites/default/files/fotoranking/boogeyman.jpg'),
User('zara', 'female', 'terrier', '1', 'https://f0.bcbits.com/img/a3244199060_10.jpg'),
User('guido', 'male', 'bulldog', '33', 'http://images1.wikia.nocookie.net/__cb20090303004114/ghostbusters/images/d/d4/Boogieman02.png'),
User('ken', 'male', 'griffon', '112', 'http://4.bp.blogspot.com/_iMHXEljpe8s/Sd1pZHBI01I/AAAAAAAALJc/NU5hAmIfusE/s400/mcfarlane+toys-wonderful+wizard+of+oz-Boogeyman13-flickr.jpg'),
User('ada', 'female', 'collie', '98', 'http://annalisegreen.com/wp-content/uploads/2011/09/Oogie-Boogie-nightmare-before-christmas-2854985-2033-2560.jpg'),
User('steve', 'male', 'bloodhound', '111', 'http://anythinghorror.files.wordpress.com/2011/04/the-boogeyman-monster-make-up.jpg'),
User('ztu', 'male', 'borzoi', '3244', 'http://www.boxofficeprophets.com/tickermaster/loadimage.cfm?image=boogeyman.jpg'),
User('foo', 'NA', 'bulmastiff', '90', 'http://cdn2-b.examiner.com/sites/default/files/styles/image_content_width/hash/98/94/98945acd304212be5e59e7fb2f0fddd6.jpg?itok=SXLHPU2y')]

i = [User2()]