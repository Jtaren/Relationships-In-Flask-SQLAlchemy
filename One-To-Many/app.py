from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

database_name = "one_to_many"
database_path = "postgresql://{}:{}@{}/{}".format("postgres", "eazye5000", "localhost:5432", database_name)
app.config['SQLALCHEMY_DATABASE_URI'] = database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONs'] = False
db = SQLAlchemy(app)
app.app_context().push()

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(100))
    pets = db.relationship('Pet', backref='owner')

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
