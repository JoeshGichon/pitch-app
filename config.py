class Config:
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitchdb'

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}