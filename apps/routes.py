from resources import user
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return user.dummy_api()