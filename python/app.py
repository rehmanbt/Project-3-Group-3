from flask import Flask, jsonify
import datetime as dt
from sqlalchemy import func
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


# Create an instance of the Flask application
app = Flask(__name__)

#Create the engine to the SQLite database file
engine = create_engine(f"sqlite:///Resources/hawaii.sqlite")

#Tried putting the flask down to see if operational error does not come but it was still there. So just keeping it as reference.
#app = Flask(__name__)

# Reflect the database schema
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
session = Session(engine)


# Define the homepage route
