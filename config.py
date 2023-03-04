import os
from sqlalchemy import create_engine

class Config(object):
  SECRET_KEY = 'una-clave-secreta-bien-pro'
  SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
  DEBUG = True
  # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:topsecret@localhost:3306/idgs802'
  SQLALCHEMY_TRACK_MODIFICATIONS = False