from .models import *
from bson.objectid import ObjectId
from werkzeug.security import check_password_hash

def login(email, password):
    data = {"error":None}
    try:
        user = Users.objects.get(email=email)
        if check_password_hash(user.password, password):
            data["user"] = user
        else:
            data["error"] = "Invalid password!"
    except Users.DoesNotExist:
        pass
    return data

def register(username, email, password):
    data = {"error":None}
    try:
        user = Users.objects.get(email=email)
        data["error"] = "%s is already registered!" %email
    except Users.DoesNotExist:
        user = Users(email=email, username=username)
        user.set_password(password)
        user.save()
        data["info"] = "Account created!"
    return data

def add_task(user, task):
    user = Users.objects.get(id=ObjectId(user["_id"]["$oid"]))
    Tasks(name=task, user=user).save()

def get_tasks(user):
    user = Users.objects.get(id=ObjectId(user["_id"]["$oid"]))
    return Tasks.objects(user=user)

def complete_task(user, task_id, is_checked):
    task = Tasks.objects.get(id=ObjectId(task_id))
    task.done = is_checked
    task.save()
    return task
