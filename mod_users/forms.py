from flask_wtf import FlaskForm
from wtforms.fields import EmailField
from wtforms import PasswordField
from wtforms.validators import data_required

class LogingForm(FlaskForm):
    email = EmailField(validators=[data_required()])
    password = PasswordField(validators=[data_required()])