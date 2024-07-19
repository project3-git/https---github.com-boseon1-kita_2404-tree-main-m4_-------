from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    contents=db.Column(db.Text, nullable=False)
    input_date=db.Column(db.Date, nullable=False, default=datetime.utcnow)
    due_date=db.Column(db.Date, nullable=False)
    new = db.Column(db.Date, nullable=False)