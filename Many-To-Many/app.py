
from flask import Flask
from flask_sqlachemy import SQLAlchemy

app = Flask(__name__)

database_name = "many_to_many"
database_path = "postgresql://{}:{}@{}/{}".format("postgres", "eazye5000", "local:5432", database_name)
app.config['SQLALCHEMY_DATABASE_URI'] = database_path
db = SQLAlchemy(app)
app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __repr__(self):
        return f'<User: {self.name}>'

class Channel(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __repr__(self):
        return f'<Channel {self.name}>'
