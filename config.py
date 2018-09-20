#config.py

import os

class Config(object):
	# Required to use Forms
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
# Enable Flask's debugging features. Should be False in production
DEBUG = True