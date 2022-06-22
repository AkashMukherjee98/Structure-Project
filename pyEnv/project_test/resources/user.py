from flask_restful import Resource
from flask import request
from models import db_user


class Users(Resource):
    def get(self):
        db_user.db.create_all()
        return {'msg': 'Tables created'}

    def post(self):
        #return "okk"
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.get_json()
            user_name=data['username']
            print(user_name)
            user_email=data['email']
            print(user_email)
            # exit(0)
            user=db_user.User(username=user_name, email=user_email)
            print("---- :",user)
            db_user.db.session.add(user)
            db_user.db.session.commit()         
        return "insert data"
    