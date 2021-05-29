from mysql.connector import connect
from contextlib import contextmanager

# =================== NOVA CONEXÃO =================== #

parameters = dict(
    host= 'localhost',
    port=3306,
    user='root',
    passwd='roots',
    database='agenda'
)

@contextmanager
def new_connection():

    # criando a conexão
    connection = connect(**parameters)

    try:

        # retorna a conexão
        yield connection
        print('Conected')

    # Quando sair do bloco WITH, finally automaticamente irá ser ativado. Se a conexão existir e estiver aberta, será fechada.

    finally:
        if(connection and connection.is_connected()):
            connection.close()
            print('Finally...')
