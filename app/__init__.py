from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initiate an app
app = Flask(__name__)
# load ../config.py file
app.config.from_object('config')

# initiate a database
db = SQLAlchemy(app)

# need "from app" syntax here
from app import views, models

# __init__.py files make Python treat the directories as containing packages
# In the simplest case, __init__.py can just be an empty file
# but it can also execute initialization code for the package

# so before that (which means right in the __init__ module)
# could not use the following syntax:
# [ import views ]
# [ from . import models ]

