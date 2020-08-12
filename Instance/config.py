import os


class Config:
    """parent configuration class"""
    DEBUG = False
    CSRF_ENABLED = True

    DB_HOST = os.getenv('DB_HOST')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')

    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(Config):
    """configurations for development"""
    DEBUG = True


class TestingConfig(Config):
    """configurations for testing, with a separate database"""
    TESTING = True
    DEBUG = True

    DB_HOST = os.getenv('DB_HOST')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')


class ProductionConfig(Config):
    """configuration for production"""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
