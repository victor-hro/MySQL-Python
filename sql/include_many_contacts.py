from mysql.connector import ProgrammingError
from db import new_connection

sql = 'INSERT INTO contacts (name, tel) VALUES (%s, %s)'
args = (
    ('Victor1', '1010'),
    ('Victor2', '2020'),
    ('Victor3', '3030'),
    ('Victor4', '4040')
 )

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.executemany(sql, args)
        connection.commit()
    except ProgrammingError as e:
        print('Error', e.msg)
    else:
        print(f'{cursor.lastrowid} registros incluídos.')

