import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import pooling
load_dotenv()

db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_database = os.environ.get("DB_DATABASE")

connection_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=10,
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
    database=db_database,
    auth_plugin='mysql_native_password'
)

 # Define a context manager for getting database connections from the pool
class DBConnection:
    def __enter__(self):
        self.db_connection = connection_pool.get_connection()
        return self.db_connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.db_connection:
            self.db_connection.close() 