import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Application(Flask):
    def __init__(self, environment=None):
        super(Application, self).__init__(__name__)
        self._init_configuration()
        self._init_extensions()
        self._init_views()


    def _init_configuration(self):
        self.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            'DATABASE_URL',
            'postgres://localhost/simple-flask-celery'
        )

    def _init_extensions(self):
        db.init_app(self)

    def _init_views(self):
        return
        @self.route("/")
        def hello():
            return "Hello World!"


        @application.route("/tasks")
        def tasks():
            return str(Task.query.all())




class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(256))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<Task %r>' % self.title
