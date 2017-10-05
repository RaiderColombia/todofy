database = {
    "users":{
        "gmail":{
            "password":"lara",
            "username":"raider",
            "tasks":[{"id":1, "name":"Task One"}]
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
        database["users"][email] = {"username":username, "password":password}
        data["info"] = "Account created!"
    return data

def add_task(user, task):
    database["users"][user]["tasks"].append(
        {"id":len(database["users"][user]["tasks"])+1, "name":task}
    )
