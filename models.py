from flask_mongoengine import MongoEngine
from werkzeug.security import generate_password_hash

db = MongoEngine()

class Users(db.Document):
    email = db.StringField()
    password = db.StringField()
    username = db.StringField()

    def set_password(self, password):
        self.password = generate_password_hash(password)

class Tasks(db.Document):
    name = db.StringField()
    done = db.BooleanField(default=False)
    user = db.ReferenceField(Users)
