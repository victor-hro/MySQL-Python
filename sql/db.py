from mysql.connector import connect
from contextlib import contextmanager

parameters = dict(
    host= '127.0.0.1',
    port=3306,
    user='root',
    passwd='roots',
    database='agenda'
)

# função a ser passada no bloco WITH
@contextmanager
def new_connection():
    
    # criando a conexão
    connection = connect(**parameters)
    
    try:
        
        # retorna a conexão
        yield connection
        
    # Quando sair do bloco WITH, finally automaticamente irá ser ativado. Se a conexão existir e esiver aberta, será fechada.
    
    finally:
        if(connection and connection.is_connected()):
            connection.close()
            print('Finally...')
        