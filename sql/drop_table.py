from mysql import connector
from db import new_connection
from mysql.connector import ProgrammingError

try:
    with new_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute('DROP TABLE IF EXISTS emails')
        except ProgrammingError as e:
            print('Error', e.msg )
except ProgrammingError as e:
    print('Connection error', e.msg )