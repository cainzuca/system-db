import services.database as db
import models.Artista as artista
import mysql.connector


def incluir(artista):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("""
    INSERT INTO bsystem.artista (nome, idade, cpf, pix, rg, titulo_eleitor, cnpj, data_nascimento, login_sesc, login_nota, login_gov, presskit, nota,senha_sesc,senha_nota,senha_gov,senha_presskit,banco,agencia)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
    (artista.nome, artista.idade, artista.cpf, artista.pix, artista.rg, artista.titulo_eleitor, artista.cnpj, artista.data_nascimento, artista.login_sesc, artista.login_nota, artista.login_gov, artista.presskit, artista.nota,artista.senha_sesc,artista.senha_nota,artista.senha_gov,artista.senha_presskit,artista.banco,artista.agencia))
    cnxn.commit()

    cursor.close()
    cnxn.close()

def selecionarTodos():
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.artista")
    artistas = []
    
    for row in cursor.fetchall():
        artista = row_to_artista(row)
        artistas.append(artista)
        
    cursor.close()
    cnxn.close()

    return artistas

def selecionarById(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.artista WHERE id = %s", (id,))
    row = cursor.fetchone()
    if row:
        artista = row_to_artista(row)
    else:
        artista = None

    cursor.close()
    cnxn.close()

    return artista

def selecionarById2(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.artista ORDER BY CASE WHEN id = %s THEN 0 ELSE 1 END, id", (id,))
    artistas = []
    
    for row in cursor.fetchall():
        artista = row_to_artista(row)
        artistas.append(artista)
        
    cursor.close()
    cnxn.close()

    return artistas

def selecionarByName(nome):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.artista WHERE nome = %s", (nome,))
    row = cursor.fetchone()
    if row:
        artista = row_to_artista(row)
    else:
        artista = None

    cursor.close()
    cnxn.close()

    return artista

def Excluir(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("DELETE FROM bsystem.artista WHERE id = %s", (id,))
    cnxn.commit()

    cursor.close()
    cnxn.close()

def Alterar(artista):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("""
    UPDATE bsystem.artista
    SET nome = %s, idade = %s, cpf = %s, pix = %s, rg = %s, titulo_eleitor = %s, cnpj = %s, data_nascimento = %s, login_sesc = %s, login_nota = %s, login_gov = %s, presskit = %s, nota = %s, senha_sesc = %s, senha_nota = %s, senha_gov = %s, senha_presskit = %s, banco = %s, agencia = %s
    WHERE id = %s
    """,
    (artista.nome, artista.idade, artista.cpf, artista.pix, artista.rg, artista.titulo_eleitor, artista.cnpj, artista.data_nascimento, artista.login_sesc, artista.login_nota, artista.login_gov, artista.presskit, artista.nota,artista.senha_sesc,artista.senha_nota,artista.senha_gov,artista.senha_presskit,artista.banco, artista.agencia, artista.id))
    cnxn.commit()

    cursor.close()
    cnxn.close()

def row_to_artista(row):
    return artista.artista(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14],row[15],row[16],row[17],row[18],row[19],row[20])

# Exemplo de uso
# artistas = selecionarTodos()
# for artista in artistas:
#     print(artista.nome)



#GPT
'''import services.database as db
import models.Artista as artista
import mysql.connector
import psycopg2

def incluir(artista):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("""
    INSERT INTO bsystem.artista (nome, idade, cpf, pix, rg, titulo_eleitor, cnpj, data_nascimento, login_sesc, login_nota, login_gov, presskit, nota)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
    (artista.nome, artista.idade, artista.cpf, artista.pix, artista.rg, artista.titulo_eleitor, artista.cnpj, artista.data_nascimento, artista.login_sesc, artista.login_nota, artista.login_gov, artista.presskit, artista.nota))
    cnxn.commit()

    cursor.close()
    cnxn.close()

def selecionarTodos():
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.artista")
    artistas = []
    
    for row in cursor.fetchall():
        artista = row_to_artista(row)
        artistas.append(artista)
        
    cursor.close()
    cnxn.close()

    return artistas

def selecionarById(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.artista WHERE id = %s", (id,))
    row = cursor.fetchone()
    if row:
        artista = row_to_artista(row)
    else:
        artista = None

    cursor.close()
    cnxn.close()

    return artista

def selecionarById2(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.artista ORDER BY CASE WHEN id = %s THEN 0 ELSE 1 END, id", (id,))
    artistas = []
    
    for row in cursor.fetchall():
        artista = row_to_artista(row)
        artistas.append(artista)
        
    cursor.close()
    cnxn.close()

    return artistas

def selecionarByName(nome):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.artista WHERE nome = %s", (nome,))
    row = cursor.fetchone()
    if row:
        artista = row_to_artista(row)
    else:
        artista = None

    cursor.close()
    cnxn.close()

    return artista

def Excluir(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("DELETE FROM bsystem.artista WHERE id = %s", (id,))
    cnxn.commit()

    cursor.close()
    cnxn.close()

def Alterar(artista):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("""
    UPDATE bsystem.artista
    SET nome = %s, idade = %s, cpf = %s, pix = %s, rg = %s, titulo_eleitor = %s, cnpj = %s, data_nascimento = %s, login_sesc = %s, login_nota = %s, login_gov = %s, presskit = %s, nota = %s
    WHERE id = %s
    """,
    (artista.nome, artista.idade, artista.cpf, artista.pix, artista.rg, artista.titulo_eleitor, artista.cnpj, artista.data_nascimento, artista.login_sesc, artista.login_nota, artista.login_gov, artista.presskit, artista.nota, artista.id))
    cnxn.commit()

    cursor.close()
    cnxn.close()

def row_to_artista(row):
    return artista.artista(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14])

# Exemplo de uso
# artistas = selecionarTodos()
# for artista in artistas:
#     print(artista.nome)
'''