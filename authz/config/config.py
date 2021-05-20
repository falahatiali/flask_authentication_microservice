from os import environ


class Config:
    ################ SYS CONFIGS ###################
    ENV = environ.get("MICRO_AUTH_ENV", "production")
    DEBUG = int(environ.get("MICRO_AUTH_DEBUG", "0"))
    TESTING = int(environ.get("MICRO_AUTH_TESTING", "0"))

    ##################### USER CONFIGURATIONS #####################
    USER_DEFAULT_ROLE = environ.get("MICRO_AUTH_DEFAULT_ROLE", "member")
    USER_DEFAULT_STATUS = environ.get("MICRO_AUTH_DEFAULT_STATUS", "inactive")


    ##################### USER CONFIGURATIONS #####################
    SQLALCHEMY_TRACK_MODIFICATIONS = TESTING
    SQLALCHEMY_DATABASE_URI = environ.get('MICRO_AUTH_DATABASE_URI', None)