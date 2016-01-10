import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'postgres://localhost/simple-flask-celery'
)
db = SQLAlchemy(application)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(256))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<Task %r>' % self.title


@application.route("/")
def hello():
    return "Hello World!"


@application.route("/tasks")
def tasks():
    return str(Task.query.all())

if __name__ == "__main__":
    application.run(debug=True)
