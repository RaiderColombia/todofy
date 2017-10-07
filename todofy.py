from flask import Flask
from .views import *
from .models import db

app = Flask(__name__)
app.secret_key = "\xbf\xd9\xe4B\xae\xffw\x11\xefu\xf2\x12\xc8\xc7xBC\x80\xb9\x88\xb2\x8c/Y"
app.config["MONGODB_SETTINGS"] = {
    "db": "todofy",
    "host": "localhost"
}
db.init_app(app)

app.add_url_rule("/login", view_func=Login.as_view("login_view"))
app.add_url_rule("/logout", view_func=Logout.as_view("logout_view"))
app.add_url_rule("/register", view_func=Register.as_view("register_view"))
app.add_url_rule("/index", view_func=Index.as_view("index"))
app.add_url_rule("/complete", view_func=Complete.as_view("complete"))
