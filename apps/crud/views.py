from flask import Blueprint, render_template
from apps.app import db
#importing User class from apps/crud/models.py
from apps.crud.models import User

crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# index endpoint, return index.html

@crud.route("/")
def index():
    return render_template("crud/index.html")

@crud.route("/sql")
def sql():
    db.session.query(User).all()
    return "check the console log"