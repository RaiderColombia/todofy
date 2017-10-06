database = {
    "users":{
        "raider@gmail":{
            "email":"raider@gmail",
            "password":"lara",
            "username":"raider"
        }
    },
    "tasks":{
        "raider@gmail":{
            1: {"name":"Task One", "done":True},
            2: {"name":"Task Two", "done":False}
        }
    }
}

def login(email, password):
    data = {"error":None}
    if email in database["users"]:
        if database["users"][email]["password"] == password:
            data["user"] = database["users"][email]
        else:
            data["error"] = "Invalid password!"
    return data

def register(username, email, password):
    data = {"error":None}
    if email in database["users"]:
        data["error"] = "%s is already registered!" %email
    else:
        database["users"][email] = {
            "email":email,
            "username":username,
            "password":password
        }
        database["tasks"][email] = {}
        data["info"] = "Account created!"
    return data

def add_task(user, task):
    id = len(database["tasks"][user]) + 1
    database["tasks"][user][id] = {"name":task, "done":False}

def get_tasks(user):
    return database["tasks"][user]

def complete_task(user, task_id, is_checked):
    database["tasks"][user][task_id]["done"] = is_checked
