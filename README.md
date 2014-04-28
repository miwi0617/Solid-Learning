Solid-Learning
==============
Danim Jeong and Michael Williams <br />
Rapid Prototyping 2014 <br />

To run: python app.py

To create database: <br />
from app import db <br />
db.create_all() <br />
from app import Models <br />
from app import Tutorials <br />
from app import ModelDatabase <br />
from app import TutorialDatabase <br />
db.session.add_all(ModelDatabase) <br />
db.session.add_all(TutorialDatabase) <br />
db.session.commit() <br />
Models.query.all() <br />
Tutorials.query.all()