import os

class Config:
    # إعدادات عامة
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'eco-plant-dz-secret-key-2023'
    JSON_AS_ASCII = False
    
    # إعدادات قاعدة البيانات
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '5432')
    DB_NAME = os.environ.get('DB_NAME', 'ecoplant_db')
    DB_USER = os.environ.get('DB_USER', 'ecoplant_user')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'ecoplant_pass')
    
    # إعدادات أخرى
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}