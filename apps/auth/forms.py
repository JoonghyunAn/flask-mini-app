from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignUpForm(FlaskForm):
    username = StringField(
        "user name",
        validators=[
            DataRequired("user name is required."),
            Length(1, 30, "input must be within 30 characters"),
        ],
        )
    email = StringField(
        "email address",
        validators=[
            DataRequired("email address is a must."),
            Email("Input must match an email address format"),
        ]
        )
    password = PasswordField(
        "password",
        validators = [
            DataRequired("password is needed.")])
    submit = SubmitField("New Registration")
class LoginForm(FlaskForm):
    email = StringField(
        "email address",
        validators=[
            DataRequired("email address is required"),
            Email("input must be a valid email format"),
        ]
    )
    password = PasswordField("password", validators=[DataRequired("password is required.")])
    submit = SubmitField("Login by clicking here")

    