from backend.database import db
from datetime import datetime

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    questions = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    form_id = db.Column(db.Integer, db.ForeignKey("form.id"))
    answers = db.Column(db.JSON)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
