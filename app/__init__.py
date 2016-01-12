import os

from flask import Flask

from app.extensions import db

class Application(Flask):
    def __init__(self, environment=None):
        super(Application, self).__init__(__name__)
        self._init_configuration()
        self._init_extensions()
        self._init_views()


    def _init_configuration(self):
        self.config['DEBUG'] = True
        self.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            'DATABASE_URL',
            'postgres://localhost/simple-flask-celery'
        )

    def _init_extensions(self):
        db.init_app(self)

    def _init_views(self):
        from .views.example import example
        self.register_blueprint(example, url_prefix='/')
