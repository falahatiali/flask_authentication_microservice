from os import environ


class Config:
    ################ SYS CONFIGS ###################
    ENV = environ.get("MICRO_AUTH_ENV", "production")
    DEBUG = int(environ.get("MICRO_AUTH_DEBUG", "0"))
    TESTING = int(environ.get("MICRO_AUTH_TESTING", "0"))