import mysql.connector as conn
from mysql.connector import errorcode

def create_connection(args):
  connection = None

  try:
    connection = conn.connect(**args)
    if connection.is_connected():
      dbinfo = connection.get_server_info()
      print("Connected to MySQL Server version ", dbinfo)    

  except Exception as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)

  return connection


args = {
    'user': 'db_username',
    'password': 'db_password',
    'host': '127.0.0.1',
    'database': 'test',
    'raise_on_warnings': True,
    'use_pure': False,
    'autocommit': True,
    'pool_size': 5
}

conn = create_connection(args)
crsr = conn.cursor()


def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format("DB_NAME"))
    except conn.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    crsr.execute("USE {}".format("DB_NAME"))
except conn.connector.Error as err:
    print("Database {} does not exists.".format("DB_NAME"))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(crsr)
        print("Database {} created successfully.".format("DB_NAME"))
    else:
        print(err)
        exit(1)