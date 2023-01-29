from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model
from datetime import datetime


class Service(db.Model, Model):
    title = db.Column(db.String(50), nullable=False)
    short_description = db.Column(db.String(400), nullable=False)
    long_description = db.Column(db.Text)
    image = relationship("Image", uselist=False)

    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    creator = relationship("User")
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())

