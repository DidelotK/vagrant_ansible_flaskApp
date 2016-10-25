# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy (for the sqlite database)
#from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')


# Define the database object which is imported
# by modules and controllers
#db = SQLAlchemy(app)

# Import the routes
from app.router import router
router(app);

# Build the database:
# This will create the database file using SQLAlchemy
#db.create_all()