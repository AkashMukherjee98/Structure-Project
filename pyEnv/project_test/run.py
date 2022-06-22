from flask import Flask
from flask_restful import Resource, Api
from db_con import db
from resources.user import Users


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/student'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)

api = Api(app)
api.add_resource(Users, '/')


if __name__== "__main__":
    
    app.run(debug=True, host="0.0.0.0", port="5001", use_reloader=True)
    print(app)
