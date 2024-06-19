from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_wtf.form import FlaskForm
from wtforms.fields.simple import SubmitField

class UploadImageForm(FlaskForm):
    image = FileField(
        validators=[
            FileRequired("add an image file"),
            FileAllowed(["png","jpg","jpeg",], "Type not supported."),
        ]
    )
    submit = SubmitField("Upload")

class DetectorForm(FlaskForm):
    submit = SubmitField("Click to Detect")

class DeleteForm(FlaskForm):
    submit = SubmitField("Delete")