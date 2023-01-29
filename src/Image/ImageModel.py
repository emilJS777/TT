from src import db
from src.__Parents.Model import Model


class Image(db.Model, Model):
    filename = db.Column(db.String(180), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    service_id = db.Column(db.Integer, db.ForeignKey("service.id"))
    creator_id = db.Column(db.Integer)
