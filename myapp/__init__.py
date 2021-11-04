import flask
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
#instance of the Flask Class
myapp_obj = flask.Flask(__name__)
myapp_obj.config.from_mapping(SECRET_KEY = "key", SQLALCHEMY_DATABSE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'), SQLALCHEMY_TRACK_MODIFICATIONS = False)

db = SQLAlchemy(myapp_obj)


from myapp import routes, models
