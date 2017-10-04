from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    data = {"title": "Login", "content":"This is the login page"}
    if request.method == "POST":
        return redirect(url_for("register"))
    return render_template("login.html", **data)

@app.route("/register", methods=["GET", "POST"])
def register():
    data = {"title": "Register", "content":"This is the register page"}
    if request.method == "POST":
        return redirect(url_for("login"))
    return render_template("register.html", **data)
