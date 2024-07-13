import psycopg2
import os

server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT')

# Configuração da conexão com o PostgreSQL
conn_str = (
    f"dbname='{database}' "
    f"user='{username}' "
    f"password='{password}' "
    f"host='{server}' "
    f"port='{port}' "  # Adiciona a porta à string de conexão
)

# Estabelece a conexão com o banco de dados PostgreSQL
def criar_conexao():
    return psycopg2.connect(conn_str)

cnxn = criar_conexao()
cursor = cnxn.cursor()

# Cria um cursor
#cursor = cnxn.cursor()

# Seu código para manipular o banco de dados aqui...

# Fechando a conexão
#cnxn.close()

