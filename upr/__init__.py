"""
Creates the UPR package and imports and initializes all required objects.
"""

# import top-level flask bits.
from flask import Flask, render_template
<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy
#create the app.
=======
from flask.ext.sqlalchemy import SQLAlchemy

# create the app.
>>>>>>> 8aad1d4291029fbc3d0dd72814d0d3aa2810c475
app = Flask("upr")
# load the app's config.
app.config.from_object('upr.config')
# initialize the sqlalchemy object.
db = SQLAlchemy(app)

<<<<<<< HEAD
#import controlers to establish routes.
import controlers
#import models to create them:
import models
=======
# import controlers to establish routes.
import controlers
>>>>>>> 8aad1d4291029fbc3d0dd72814d0d3aa2810c475
