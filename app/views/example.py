from flask import Blueprint

from app.models.task import Task

example = Blueprint('example', __name__)

@example.route("/")
def hello():
    return "Hello World!"


@example.route("/tasks")
def tasks():
    return str(Task.query.all())
