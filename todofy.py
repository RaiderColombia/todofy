from flask import Flask, request, redirect, url_for, render_template, session, \
        flash
from .controllers import *

app = Flask(__name__)
app.secret_key = "my secret key"

@app.route("/login", methods=["GET", "POST"])
def login_view():
    data = {"error": None, "title":"Login"}
    if request.method == "POST":
        result = login(request.form["email"], request.form["password"])
        if "user" in result:
            session["data"] = result
            flash("Welcome %s!"%result["user"]["username"])
            return redirect(url_for("index"))
        elif result["error"]:
            data["error"] = result["error"]
        else:
            flash("Please create an account!")
            return redirect(url_for("register_view"))
    elif "data" in session:
        return redirect(url_for("index"))
    else:
        return render_template("login.html", **data)

@app.route("/logout")
def logout_view():
    session.pop("data", None)
    return redirect(url_for("login_view"))

@app.route("/register", methods=["GET", "POST"])
def register_view():
    data = {"error": None, "title":"Register"}
    if request.method == "POST":
        result = register(
            request.form["username"],
            request.form["email"],
            request.form["password"]
        )
        if "info" in result:
            flash(result["info"])
            return redirect(url_for("login_view"))
        else:
            data["error"] = result["error"]
    elif "data" in session:
        return redirect(url_for("index"))
    else:
        return render_template("register.html", **data)

@app.route("/index", methods=["GET", "POST"])
def index():
    if "data" in session:
        if request.method == "POST":
            add_task("gmail", request.form["task_name"])
        return render_template("index.html", **session["data"])
    else:
        return redirect(url_for("login_view"))
