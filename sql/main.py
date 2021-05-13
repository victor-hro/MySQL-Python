try:
    from mysql import connector
except ModuleNotFoundError:
    print('MySQL connector não instalado')
else:
    print('MySQL pronto')
    
from mysql.connector import connect

# =================== CONECTANDO AO SERVIDOR =================== #
conection = connect(
    host= 'localhost',
    port=3306,
    user='root',
    passwd='roots'
)
print(conection)
