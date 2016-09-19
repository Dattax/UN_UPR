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
    email = db.Column(db.Unicode(128), unique=True, nullable=False)
    password = db.Column(db.Unicode(128), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    is_authenticated = db.Column(db.Boolean, nullable=False, default=False)
    first_name = db.Column(db.Unicode(32), nullable=False)
    last_name = db.Column(db.Unicode(32), nullable=False)
    address = db.Column(db.Unicode)
    postal_code = db.Column(db.Unicode)
    province = db.Column(db.Unicode(32), nullable=False)
    country = db.Column(db.Unicode(32), nullable=False, default=U"US")
    country_code = db.Column(db.Unicode(6))
    phone = db.Column(db.Unicode(16))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'),
                                nullable=True)
    organization = db.relationship('Organization')

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @db.reconstructor
    def init_load(self):
        self.is_anonymous = False

    def commit(self):
        """
        Commit this object to the db
        """
        db.session.add(self)
        db.session.commit()

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
    """ looks up the user by their user id """
    return User.find_by_id(int(id))
