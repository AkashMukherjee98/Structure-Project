from flask import Flask
from configparser import ConfigParser
from app.database import Base

app=Flask(__name__)

file="config.ini"
config=ConfigParser()
config.read(file)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/alchemy'
app.config['SQLALCHEMY_DATABASE_URI'] = "'"+config['mysql']['conn']+":"+"//"+config['mysql']['user']+":"+config['mysql']['pwd']+"@"+config['mysql']['host']+"/"+config['mysql']['db']+"'"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False





class User(Base):
__tablename__ = 'users'













'''

import configparser
import MySQLdb.cursors

config = configparser.ConfigParser()
config.read('config.ini')

def connect():
    return MySQLdb.connect(host = config['mysqlDB']['host'],
                           user = config['mysqlDB']['user'],
                           passwd = config['mysqlDB']['pass'],
                           db = config['mysqlDB']['db'])

'''