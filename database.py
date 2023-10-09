from mysql.connector import pooling
from config import Config

connection_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=10,
    host=Config.DB_HOST,
    port=Config.DB_PORT,
    user=Config.DB_USER,
    password=Config.DB_PASSWORD,
    database=Config.DB_DATABASE,
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