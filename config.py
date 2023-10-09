"""Flask config class."""

import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    """
    Class Config: Loads all the config from env here and can be accessed when needed
    Note: I know most of the values right now are same so we don't really need the if condition to check as everything 
    is same for now, but eventually things will change and there will be some things which we wouldn't have in test. 
    Based on value present in env we also make some logic decisions such as global logging 
    `"""
    FLASK_ENV = os.environ.get('FLASK_ENV')
    if FLASK_ENV == "PROD":
        DEBUG = False
        FLASK_PORT = os.environ.get("FLASK_PORT")
        FLASK_HOST = os.environ.get("FLASK_HOST")
        DB_HOST = os.environ.get("DB_HOST")
        DB_PORT = os.environ.get("DB_PORT")
        DB_USER = os.environ.get("DB_USER")
        DB_PASSWORD = os.environ.get("DB_PASSWORD")
        DB_DATABASE = os.environ.get("DB_DATABASE")
        GOOGLE_AUTH_SECRET_KEY = os.environ.get("GOOGLE_AUTH_SECRET_KEY")
        GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
    else:
        DEBUG = True
        FLASK_PORT = os.environ.get("FLASK_PORT")
        FLASK_HOST = os.environ.get("FLASK_HOST")
        DB_HOST = os.environ.get("DB_HOST")
        DB_PORT = os.environ.get("DB_PORT")
        DB_USER = os.environ.get("DB_USER")
        DB_PASSWORD = os.environ.get("DB_PASSWORD")
        DB_DATABASE = os.environ.get("DB_DATABASE")
        GOOGLE_AUTH_SECRET_KEY = os.environ.get("GOOGLE_AUTH_SECRET_KEY_DEV")
        GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID_DEV")

