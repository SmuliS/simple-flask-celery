from app.extensions import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(256))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<Task %r>' % self.title
