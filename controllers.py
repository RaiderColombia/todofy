database = {
    "users":{
        "gmail":{
            "email":"gmail",
            "password":"lara",
            "username":"raider"
        }
    },
    "tasks":{
        "gmail":[
            {"id":1, "name":"Task One", "done":False}
        ]
    }
}

def login(email, password):
    print(database)
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
        database["users"][email] = {"email":email,"username":username, "password":password}
        database["tasks"][email] = []
        data["info"] = "Account created!"
    return data

def add_task(user, task):
    id = len(database["tasks"][user]) + 1
    database["tasks"][user].append({"id":id, "name":task, "done":False})
    print(user, task, database)

def get_tasks(user):
    return database["tasks"][user]
