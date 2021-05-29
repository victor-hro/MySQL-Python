from mysql.connector import ProgrammingError
from db import new_connection

sql = 'INSERT INTO contacts (name, tel) VALUES (%s, %s)'
args = ('Victor', '91234-5678')

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, args)
        connection.commit()
    except ProgrammingError as e:
        print('Error', e.msg)
    else:
        print('1 registro incluído, ID:', cursor.lastrowid)

