"""
Creates the UPR package and imports and initializes all required objects.
"""

# import top-level flask bits.
from flask import Flask, render_template
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect
=======
# from sqlalchemy import create_engine
# from flask.ext.sqlalchemy import SQLAlchemy
>>>>>>> Stashed changes
=======
# from sqlalchemy import create_engine
# from flask.ext.sqlalchemy import SQLAlchemy
>>>>>>> Stashed changes
=======
# from sqlalchemy import create_engine
# from flask.ext.sqlalchemy import SQLAlchemy
>>>>>>> Stashed changes
=======
# from sqlalchemy import create_engine
# from flask.ext.sqlalchemy import SQLAlchemy
>>>>>>> Stashed changes

# create the app.
app = Flask("upr")

# load the app's config.
app.config.from_object('upr.config')

# initialize the sqlalchemy object.
# db = SQLAlchemy(app)
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream

# create the login manager class.
login_manager = LoginManager()
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

# import controlers to establish routes.
import controlers
# import models to create them:
import models
#import all forms and their validators
import forms

# create all tables if hte database doesent exist
db.create_all()

# finish initializing the login manager
CsrfProtect(app)
login_manager.init_app(app)
