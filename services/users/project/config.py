# services/ users/project/config.py
import os

class BaseConfig:
    """ Base config """
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """ Dev config """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig(BaseConfig):
    """ Test config """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')

class ProductionConfig(BaseConfig):
    """ Prod config """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
