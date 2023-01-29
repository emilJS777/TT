from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model
from datetime import datetime


class User(Model, db.Model):
    name = db.Column(db.String(60), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    image = relationship("Image", uselist=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
