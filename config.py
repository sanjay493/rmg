class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "KUmarSanjay"

    DB_NAME = "test"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    UPLOAD = "D:\\Applications\\website\\static\\upload"
    UPLOAD_EXTENSIONS = ['.pdf', '.xls', '.xlsx']

    SESSION_COOKIE_SECURE = True
    RECAPTCHA_PUBLIC_KEY = '6LdOxtYhAAAAAGjQjmiP0GPAlVUt3ZMJuTI96T8z'
    RECAPTCHA_PRIVATE_KEY = '6LdOxtYhAAAAAGXACuPItWpc7sevCK5ZZj0frXiq'


class ProductionConfig(Config):
    pass


class DevelopmentCofig(Config):
    DEBUG = True

    DB_NAME = "test"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    UPLOAD = "D:\\Applications\\website\\static\\upload"
    SESSION_COOKIE_SECURE = False
    UPLOAD_EXTENSIONS = ['.pdf', '.xls', '.xlsx']


class TestingCofig(Config):
    TESTING = True

    DB_NAME = "test"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    UPLOAD = "D:\\Applications\\website\\static\\upload"
    SESSION_COOKIE_SECURE = False
    UPLOAD_EXTENSIONS = ['.pdf', '.xls', '.xlsx']
