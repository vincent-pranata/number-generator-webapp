from flask import Flask, request, url_for

from MainEngine import MainEngine

# Initialize the app
app = Flask(__name__, instance_relative_config=True)
app.secret_key='abcd1234'

main_engine = MainEngine()

# Load the views
from app import views
# Load the config file
app.config.from_object('config')