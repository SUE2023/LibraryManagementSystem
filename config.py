import os

class Config:
    """Base configuration class."""
    
    # General Config
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_default_secret_key')  # Secret key for security
    
    # SQLAlchemy Config (Database)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://user:password@localhost/LMS')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking to save resources
    
    # CORS (Cross-Origin Resource Sharing)
    CORS_HEADERS = 'Content-Type'
    
    # Additional security settings
    SESSION_COOKIE_SECURE = True  # Use secure cookies for session data
    REMEMBER_COOKIE_SECURE = True
    REMEMBER_COOKIE_HTTPONLY = True


class DevelopmentConfig(Config):
    """Configuration for development."""
    
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL', 'mysql+pymysql://user:password@localhost/LMS_dev')


class TestingConfig(Config):
    """Configuration for testing."""
    
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL', 'mysql+pymysql://user:password@localhost/LMS_test')
    WTF_CSRF_ENABLED = False  # Disable CSRF for testing purposes


class ProductionConfig(Config):
    """Configuration for production."""
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://user:password@localhost/LMS_prod')
    SESSION_COOKIE_SECURE = True  # Secure cookies in production
    REMEMBER_COOKIE_SECURE = True  # Secure cookies in production


# Mapping of configuration environments
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
