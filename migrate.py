"""
Migrate.py: create or update database.

Migrate.py is used to create or update the underlying database for the website.
"""
from upr import db
db.create_all()
