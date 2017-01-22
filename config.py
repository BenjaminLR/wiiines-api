class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///wines.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my-super-secret-key'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///wines.db'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
