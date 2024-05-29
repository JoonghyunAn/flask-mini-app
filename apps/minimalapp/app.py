from flask import Flask, render_template, url_for, request, current_app, redirect, flash
from email_validator import validate_email, EmailNotValidError
import logging 
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

#adding a secret key 
app.config["SECRET_KEY"] = "djakl23fjdkEKRjSxE4"

# set the log level
app.logger.setLevel(logging.DEBUG)
app.debug = True

# to not stop redirecting
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
toolbar = DebugToolbarExtension(app)

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
        

        # redirect to contact endpoint
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")


with app.test_request_context():
    print(url_for("index"))
    print(url_for("hello-endpoint",username = "world"))
    print(url_for("show_name", name = "aj", page = "1"))

with app.test_request_context("/users?updated=true"):
    print(request.args.get("updated"))


# set the python interpreter to the corresponding env, 
# ctrl+shift+p -> python interpreter -> select
# url - url
# endpoint - URI to approach an api 