import mariadb
import configparser

db_filename = "database.ini"

db = configparser.ConfigParser()
db.read(db_filename)


def close_connection(conn):
    conn.close()
    return


def open_connection():
    conn = ""
    try:
        conn = mariadb.connect(
            user=db['db']['user'],
            password=db['db']['pass'],
            host=db['db']['host'],
            port=int(db['db']['port']),
            database=db['db']['base']
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        #gui_close()
    return conn
