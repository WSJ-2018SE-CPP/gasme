#config.py

# Enable Flask's debugging features. Should be False in production
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://gasme:8PE-dSn-MC9-MmW@gasmedb.c22idrbk0ds6.us-east-2.rds.amazonaws.com/gasmedb'
