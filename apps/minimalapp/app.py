from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flask!"

# set the python interpreter to the corresponding env, 
# ctrl+shift+p -> python interpreter -> select