from flask import views, request, redirect, url_for, render_template, session, \
        flash
from .controllers import *

class Login(views.View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        data = {"error": None, "title":"Login"}
        if "data" in session:
            return redirect(url_for("index"))
        if request.method == "POST":
            result = login(request.form["email"], request.form["password"])
            if result["error"]:
                data["error"] = result["error"]
            elif "user" in result:
                session["data"] = result
                flash("Welcome %s!"%result["user"]["username"], "info")
                return redirect(url_for("index"))
            else:
                flash("Please create an account!", "error")
                return redirect(url_for("register_view"))
        return render_template("login.html", **data)

class Logout(views.View):
    def dispatch_request(self):
        session.pop("data", None)
        return redirect(url_for("login_view"))

class Register(views.View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        data = {"error": None, "title":"Register"}
        if "data" in session:
            return redirect(url_for("index"))
        if request.method == "POST":
            result = register(
                request.form["username"],
                request.form["email"],
                request.form["password"]
            )
            if "info" in result:
                flash(result["info"], "success")
                return redirect(url_for("login_view"))
            else:
                data["error"] = result["error"]
        return render_template("register.html", **data)

class Index(views.View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        if "data" not in session:
            return redirect(url_for("login_view"))
        if request.method == "POST":
            add_task(session["data"]["user"], request.form["task_name"])
            flash('"%s" added to the list!' %request.form["task_name"], "success")
        session["data"]["tasks"] = get_tasks(session["data"]["user"])
        session["data"]["title"] = "Task List"
        return render_template("index.html", **session["data"])

class Complete(views.View):
    methods = ['POST']
    def dispatch_request(self):
        id = request.json["task_id"]
        task = complete_task(session["data"]["user"], **request.json)
        return render_template("labels.html", task = task, id = id)
