from os import environ


class Config:
    ################ SYS CONFIGS ###################
    ENV = environ.get("MICRO_AUTH_ENV", "production")
    DEBUG = int(environ.get("MICRO_AUTH_DEBUG", "0"))
    TESTING = int(environ.get("MICRO_AUTH_TESTING", "0"))

    AUTHZ_SECRET = environ.get("MICRO_AUTH_SECRET","HARD-SECURE-@-123-CODE-A#FERDFRQWEUYTRGCSS")
    JWT_ALGO = environ.get("MICRO_AUTH_JWT_ALGO" , "HS512")
    JWT_TOKEN_LIFETIME = int(environ.get("MICRO_AUTH_JWT_LIFETIME" , "86400"))

    ##################### USER CONFIGURATIONS #####################
    USER_DEFAULT_ROLE = environ.get("MICRO_AUTH_DEFAULT_ROLE", "member")
    USER_DEFAULT_STATUS = environ.get("MICRO_AUTH_DEFAULT_STATUS", "inactive")


    ##################### USER CONFIGURATIONS #####################
    SQLALCHEMY_TRACK_MODIFICATIONS = TESTING
    SQLALCHEMY_DATABASE_URI = environ.get('MICRO_AUTH_DATABASE_URI', None)
    