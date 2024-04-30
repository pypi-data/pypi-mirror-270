import pymysql
from peewee import MySQLDatabase


def db_connect(self, statement):
    try:
        self.debug_print("db_connect")
        pointer = statement["pointer"]
        db = str(self.execute_statement(pointer["db"]))
        host = str(self.execute_statement(pointer["host"]))
        port = str(self.execute_statement(pointer["port"]))
        username = str(self.execute_statement(pointer["username"]))
        password = str(self.execute_statement(pointer["password"]))
        
        conn = pymysql.connect(host=host, user=username, passwd=password, port=int(port))
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db};")
        cursor.close()
        conn.close()
        
        self.BOT_DATABASE_NAME = db
        self.BOT_DATABASE = MySQLDatabase(db, host=host, port=int(port), user=username, passwd=password)
    except Exception as e:
        self.show_error(statement, e)