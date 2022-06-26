from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:postgres@localhost:5432/capstone'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Singer(db.Model):
    __tablename__ = 'singer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    voice_part = db.Column(db.String(), nullable=False)
    not_available = db.Column(db.String(), nullable=False)
    enrollment = db.relationship('ChoirEnrollment', backref='singer', lazy=True)


# class Soloist(db.Model):
#     __tablename__ = 'soloist'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(), nullable=True)
#     choir = db.Column(db.String(), nullable=True)


class Choir(db.Model):
    __tablename__ = 'choir'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=True)
    practice_time = db.Column(db.String(), nullable=True)
    enrollment = db.relationship('ChoirEnrollment', backref='choir', lazy=True)
#
#
#

class ChoirEnrollment(db.Model):
    __tablename__ = 'enrollment'

    id = db.Column(db.Integer, primary_key=True)
    choir_id = db.Column(db.Integer, db.ForeignKey('choir.id'), nullable=False)
    singer_id = db.Column(db.Integer, db.ForeignKey('singer.id'), nullable=False)





# try:
#     db.create_all()
# except Exception as e:
#     print(e)




@app.route('/')
def index():
    return 'hello '

# @app.route('/register_singer'):
# def register_singer():
