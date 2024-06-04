from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class UserForm(FlaskForm):

    username = StringField(
        "username",
        validators=[
            DataRequired(message="User name is required."),
            Length(max=30, message="Input must be within 30 characters."),
        ]
    )

    email = StringField(
        "email_address",
        validators=[
            DataRequired(message="email is required"),
            Email(message="Input must be an email format"),
        ]
    )

    password = PasswordField(
        "password",
        validators=[DataRequired(message="password is a required")]
    )
    submit = SubmitField("New Registration")