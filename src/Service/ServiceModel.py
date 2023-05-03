from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model
from datetime import datetime


class Service(db.Model, Model):
    title = db.Column(db.String(50))
    short_description = db.Column(db.String(400))
    long_description = db.Column(db.Text)
    image = relationship("Image", uselist=False)

    name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    patronymic = db.Column(db.String(400))
    data = db.Column(db.String(400))
    city = db.Column(db.String(100))
    gender = db.Column(db.String(400))
    problem = db.Column(db.String(400))
    exercise = db.Column(db.String(400))

    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    creator = relationship("User")
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())

    paid = db.Column(db.Boolean, default=False)

