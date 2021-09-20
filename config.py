import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitchdb'

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitchdb'
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}