# todofy
A web app to manage a To-Do list

[Live Demo](http://35.190.141.246:5000/login)

# Requirements
[Flask](http://flask.pocoo.org/)

[MongoDB](https://www.mongodb.com/)

[Flask-Mongoengine](https://github.com/MongoEngine/flask-mongoengine)

# Usage
`export FLASK_APP=todofy.py`

`flask run --host 0.0.0.0`

# Architecture
## `todofy.py`
Main file with the flask app

## `views.py`
Contains the views with the presentation logic to get the user requests and build the responses

## `controllers.py`
Contains the methods to query the database and persist information on it

## `models.py`
Defines the database models

## `static` folder
Contains the static files: scripts, css, imgs...

## `templates` folder
Contains the html pages to be rendered
