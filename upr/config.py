"""
Configuration module.
Holds all variables and extra information for the app.
TODO: extend this to load a non-repo config file to override defaults.
"""
import os
# application path.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# enable debugging on development.
DEBUG = True
# define our sqlite database.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS=False
#secret key, for sessions and etc.
SECRET_KEY = 'b01PfBh0AYL8xS7dB6t4AnVeAARaQGiGYMwmjMLT'