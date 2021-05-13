from mysql.connector import connect

# =================== CONECTANDO AO SERVIDOR =================== #
conection = connect(
    host= '127.0.0.1',
    port=3306,
    user='root',
    passwd='roots'
)

cursor = conection.cursor()
cursor.execute('SHOW DATABASES')

for c, database in enumerate(cursor, start=1):
    print(f'Database {c}: {database[0]}')
