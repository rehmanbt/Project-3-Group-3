from flask import Flask, jsonify
import datetime as dt
from sqlalchemy import func
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Create an instance of the Flask application
app = Flask(__name__)

# Define the homepage route
@app.route("/")
def home():
    """Homepage"""
    
# Define the precipitation route
