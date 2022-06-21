from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:postgres@localhost:5432/example'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Singer(db.Model):
    __tablename__ = 'singer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    voicePart = db.Column(db.String(), nullable=False)
    Days_Not_Available = db.Column(db.String(), nullable=True)

class Soloist(db.Model):
    __tablename__ = 'soloist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=True)
    choir = db.Column(db.String(), nullable=True)


class Choir(db.Model):
    __tablename__ = 'choir'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=True)
    practice_time = db.Column(db.String(), nullable=True)





try:
    db.create_all()
except Exception as e:
    print(e)






@app.route('/')
def index():
    return 'hello '