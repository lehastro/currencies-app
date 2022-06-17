import psycopg

conn = psycopg.connect(
"""
    host=rc1a-7uwsuhdx1lg2ilre.mdb.yandexcloud.net
    port=6432
    dbname=postgresql
    user=postgresql
    password=<password>
    target_session_attrs=read-write
    sslmode=verify-full
""")

conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
def create_database_and_table():
  delete_database='DROP DATABASE IF EXISTS currencies';
  delete_table='DROP TABLE IF EXISTS currencies';
  create_database = '''CREATE DATABASE currencies ''';
  create_table='CREATE TABLE IF NOT EXISTS currencies (data VARCHAR(255), id VARCHAR(255), numcode VARCHAR(255), charcode VARCHAR(255), nominal VARCHAR(255), name VARCHAR(255), value VARCHAR(255))';
  cursor.execute(delete_database)
  cursor.execute(delete_table)
  print("Database deleted successfully........")
  cursor.execute(create_database)
  print("Database created successfully........")
  cursor.execute(create_table)
  print("Table created successfully........")




#Closing the connection
#conn.close()

