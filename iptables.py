# save this as app.py
from flask import Flask
from flask import render_template
from flask import session

app = Flask(__name__)

@app.route("/")
def start():
    if 'username' in session :
        return render_template("index.html")
    return render_template("login.html")

@app.route("/log", method = ["GET", "POST"])
def login():
    if request.method == "POST":
        session['username'] = True
        return redirect(url_for("/"))


@app.route("/alias")
def alias():
    return render_template("alias.html")

@app.route("/rules_filter")
def rules_filter():
    return render_template("rules_filter.html")

@app.route("/rules_nat")
def rules_nat():
    return render_template("rules_nat.html")