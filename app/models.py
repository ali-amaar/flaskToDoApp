from app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(500))
    complete = db.Column(db.Boolean)
    date = db.Column(db.String(20))
