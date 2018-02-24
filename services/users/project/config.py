# services/ users/project/config.py

class BaseConfig:
    """ Base config """
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """ Dev config """
    pass

class TestingConfig(BaseConfig):
    """ Test config """
    TESTING = True

class ProductionConfig(BaseConfig):
    """ Prod config """
    pass
