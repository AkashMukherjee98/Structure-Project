from models import db_user
from flask import request

def create():
    return "okkkkkk"
    db_user.db.create_all()
    return "Table created."

'''

def insert():
    #return "okk"
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        user_name=data['username']
        print(user_name)
        user_email=data['email']
        print(user_email)
        user=db_user.User(username=user_name, email=user_email)
        print("---- :",user)
        db_user.db.session.add(user)
        db_user.db.session.commit()         
    return "insert data"
'''