"""
Creates the UPR package and imports and initializes all required objects.
"""
#import top-level flask bits.
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

#create the app.
app = Flask("upr")
#load the app's config.
app.config.from_object('upr.config')
#initialize the sqlalchemy object.
db = SQLAlchemy(app)
