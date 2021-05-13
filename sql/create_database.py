from mysql.connector import connect


# =================== CONECTANDO AO SERVIDOR =================== #
conection = connect(
    host= 'localhost',
    port=3306,
    user='root',
    passwd='roots'
)
print(conection)

cursor = conection.cursor()

# create database
cursor.execute('CREATE DATABASE IF NOT EXISTS agenda')
