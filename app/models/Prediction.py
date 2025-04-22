from app.models import db
from datetime import datetime

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plant_name = db.Column(db.String(120))
    benefit = db.Column(db.Text)
    confidence = db.Column(db.Float)
    image_path = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)