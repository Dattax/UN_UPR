"""
Contains user registration
"""
from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email


class RegistrationForm(Form):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    first_name = StringField('FName')
    last_name = StringField('LName')
    phone = StringField('Phone')
    address = StringField('Address')
    postal_code = StringField('PostalCode')
    province = StringField('Province')
    country = StringField('Country')
