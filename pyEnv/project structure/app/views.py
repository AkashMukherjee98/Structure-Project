from app import app
from resources import user

@app.route('/')
def dummy_api():
    return "Welcome To Project"

@app.route('/cre', methods=['GET'])
def create():
    return user.create()

# @api.route('/inn', methods=['GET'])
# def insert():
#     return user.insert()