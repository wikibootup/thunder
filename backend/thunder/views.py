from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from thunder.models import Result
from thunder import app


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
