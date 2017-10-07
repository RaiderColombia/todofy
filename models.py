from flask_mongoengine import MongoEngine

db = MongoEngine()

class Users(db.Document):
    email = db.StringField()
    password = db.StringField()
    username = db.StringField()

class Tasks(db.Document):
    name = db.StringField()
    done = db.BooleanField()
    user = db.ReferenceField(Users)
