import os
from flask import Flask

class Config:
    debug = True
    SECRET_KEY = os.environ.get('SECRET_KEY')

    app = Flask(__name__)
    app.config.from_object(__name__)