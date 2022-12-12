from dbase import dbase
from flask import Flask
import json

from flask_cors import CORS




app = Flask(__name__)
CORS(app)
@app.route('/')
def hello_world():
    return 'Welcome to the backend!'

@app.route('/get_data/<username>/<password>')
def get_data(username, password):
    return json.dumps(db.get_data(username, password))

@app.route('/login/<username>/<password>')
def login(username, password):
    return json.dumps(dbase.login(username, password))

@app.route('/insert/<username>/<password>')
def insert(username, password):
    return json.dumps(str(dbase.insert(username, password)))



app.run()