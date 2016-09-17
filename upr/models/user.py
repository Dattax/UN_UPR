"""
Includes the user model.
"""
from upr import db

    
class User(db.Model):
    """
    The user model is responsible for handling all user operations.
    These include creation, search and delete.
        """
    id = db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))

    def __init__(self, email, password):
        self.email = email
        self.password = password
    def commit(self):
        """
        Commit this object to the db
        """
        db.session.add(self)

    @staticmethod
    def find_by_email(search):
        """
        Returns the user by the specified email address.
        """
        return User.query.filter_by(email=search).first()