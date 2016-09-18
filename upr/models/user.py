"""
Includes the user model.
"""
from upr import db, login_manager

class User(db.Model):
    """
    The user model is responsible for handling all user operations.
    These include creation, search and delete.
        """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable = False)
    password = db.Column(db.String(128), nullable = False)
    is_active = db.Column(db.Boolean, nullable=False)
    first_name = db.Column(db.String(32), nullable = False)
    last_name = db.Column(db.String(32), nullable = False)
    address = db.Column(db.String)
    postal_code = db.Column(db.String)
    province = db.Column(db.String(32), nullable = False)
    country = db.Column(db.String(32), nullable = False)
    country_code = db.Column(db.String(6))
    phone = db.Column(db.String(16))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable = True)
    organization = db.relationship('Organization')

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.is_authenticated = False
        self.is_anonymous = False

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
    @staticmethod
    def find_by_id(search):
        """
        Locates the user by id and returns it.
        """
        return User.query.filter_by(id=search).first()
    def get_id(self):
        return unicode(self.id)

@login_manager.user_loader
def load_user(id):
    return User.find_by_id(id)
