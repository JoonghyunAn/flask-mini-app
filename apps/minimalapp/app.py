from flask import Flask, render_template, url_for, request, current_app, redirect

app = Flask(__name__)

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