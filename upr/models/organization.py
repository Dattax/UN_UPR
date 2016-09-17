"""
Contains the organization model.
"""
from upr import db

class Organization(db.Model):
    """
    The organization model provides access to organizations.
    Organizations are a collection of users belonging to a group.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    acronym = db.Column(db.String)
    org_type = db.Column(db.String, nullable = False)
    accredited = db.Column(db.Boolean, default = False)
    address = db.Column(db.String, nullable = False)
    country = db.Column(db.String(32), nullable = False)
    country_code = db.Column(db.String(6))
    phone = db.Column(db.String)
    web = db.Column(db.String)
    