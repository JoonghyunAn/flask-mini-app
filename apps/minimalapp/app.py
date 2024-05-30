from flask import Flask, render_template, url_for, request, current_app, redirect, flash
from email_validator import validate_email, EmailNotValidError
import logging 
from flask_debugtoolbar import DebugToolbarExtension
import os
from flask_mail import Mail, Message


app = Flask(__name__)

#adding a secret key 
app.config["SECRET_KEY"] = "****"

# set the log level
app.logger.setLevel(logging.DEBUG)
app.debug = True

# to not stop redirecting
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
toolbar = DebugToolbarExtension(app)

# adding config to Mail Class
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

mail = Mail(app)


@app.route("/", methods = ["GET","POST"])
def index():
    return "Hello, Flask!"

@app.route("/hello/<username>",
           methods=["GET","POST"],
           endpoint ="hello-endpoint") 
def hello(username):
    return f"Hello, {username}!"


# using html template with render_template
@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods=["GET","POST"])
def contact_complete():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        #input check
        is_valid = True

        if not username:
            flash("Username is required")
            is_valid=False

        if not email:
            flash("email is requried")
            is_valid=False
        
        try:
            validate_email(email)
        except EmailNotValidError:
            flash("Please check the format of your email address")
            is_valid=False

        if not description:
            flash("description must be put in")
            is_valid=False

        if not is_valid:
            return redirect(url_for("contact"))
        
        flash("Thank you for the inqury")
        
        # sending an email 
        send_email(
            email,
            "Thank you for the inquiry.",
            "contact_mail",
            username=username,
            description=description,
        )
        # redirect to contact endpoint
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")


with app.test_request_context():
    print(url_for("index"))
    print(url_for("hello-endpoint",username = "world"))
    print(url_for("show_name", name = "aj", page = "1"))

with app.test_request_context("/users?updated=true"):
    print(request.args.get("updated"))



def send_email(to, subject, template, **kwargs):
    """function for sending an email"""
    msg = Message(subject, recipient=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)
# set the python interpreter to the corresponding env, 
# ctrl+shift+p -> python interpreter -> select
# url - url
# endpoint - URI to approach an api 