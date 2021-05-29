from mysql.connector import ProgrammingError
from db import new_connection
import pandas as pd

sql = 'SELECT * FROM contacts'

data = []
with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        contacts = cursor.fetchall()
    except ProgrammingError as e:
        print('Error', e.msg)
    else:
        for contact in contacts:
            data.append([contact[1], contact[0]])
            print(f'{contact[2]:2d} - {contact[1]:10s} | Cell: {contact[0]}')
            

df = pd.DataFrame(data, columns=['ID', 'Name'])
print(df)
