import os
from dotenv import load_dotenv
import mysql.connector
load_dotenv()

db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_database = os.environ.get("DB_DATABASE")

def get_db_connection():
    db_connection = mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_database,
        auth_plugin='mysql_native_password'
    )
    return db_connection