import os

class Config():

    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://user:carrying1996+@localhost/blog"

class DevConfig(Config):

    DEBUG=True

class ProdConfig(Config):

    pass

config_options={
    "development": DevConfig,
    "production": ProdConfig
}