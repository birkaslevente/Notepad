from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import timedelta
import datetime

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    #csak a másodpercig jelenjen meg az idő a jegyzetben
    date = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(255))
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    notes = db.relationship('Note')
