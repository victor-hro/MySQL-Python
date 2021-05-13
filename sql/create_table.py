from db import new_connection
from mysql.connector import ProgrammingError

contacts_table = """
        CREATE TABLE IF NOT EXISTS contacts(name VARCHAR(50), tel VARCHAR(40))
"""

emails_table = """
    CREATE TABLE IF NOT EXISTS emails(id INT AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(50))
"""

try:
    with new_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(contacts_table)
            cursor.execute(emails_table)
        except ProgrammingError as e:
            print(f'Error: {e.msg}')
except ProgrammingError as e:
        print(f'Connection error: {e.msg}') 