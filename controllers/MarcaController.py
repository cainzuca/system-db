import services.database as db
import models.Marca as marca

def incluir(marca):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = db.cursor.execute("""
    INSERT INTO bsystem.marca (nome, telefone, email,cnpj)
    VALUES (%s, %s, %s, %s)""",
    (marca.nome, marca.telefone, marca.email,marca.cnpj ))
    db.cnxn.commit()

    cursor.close()
    cnxn.close()

def selecionarTodos():

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    db.cursor.execute("SELECT * FROM bsystem.marca")
    marcas = []
    
    for row in db.cursor.fetchall():
        marca = row_to_marca(row)
        marcas.append(marca)

    cursor.close()
    cnxn.close()
        
    return marcas

def selecionarById(id):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    db.cursor.execute("SELECT * FROM bsystem.marca WHERE id = %s", (id,))
    row = db.cursor.fetchone()
    if row:
        return row_to_marca(row)
    
    cursor.close()
    cnxn.close()

    return None

def selecionarByName(nome):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    db.cursor.execute("SELECT * FROM bsystem.marca WHERE nome = %s", (nome,))
    row = db.cursor.fetchone()
    if row:
        return row_to_marca(row)
    
    cursor.close()
    cnxn.close()

    return None

def selecionarById2(id):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    db.cursor.execute("SELECT* FROM bsystem.marca ORDER BY CASE WHEN id = %s THEN 0 ELSE 1 END,id", (id,))
    marcas = []
    
    for row in db.cursor.fetchall():
        marca = row_to_marca(row)
        marcas.append(marca)

    cursor.close()
    cnxn.close()
        
    return marcas

def Excluir(id):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = db.cursor.execute("DELETE FROM bsystem.marca WHERE id = %s", (id,))
    db.cnxn.commit()

    cursor.close()
    cnxn.close()

def Alterar(marca):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = db.cursor.execute("""
    UPDATE bsystem.marca
    SET nome = %s, telefone = %s, email = %s, cnpj = %s
    WHERE id = %s
    """,
    (marca.nome, marca.telefone, marca.email,marca.cnpj,marca.id))
    db.cnxn.commit()

    cursor.close()
    cnxn.close()


def row_to_marca(row):
    return marca.marca(row[0], row[1], row[2], row[3],row[4])

#GPT

'''import services.database as db
import models.Marca as marca

def incluir(marca):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("""
    INSERT INTO bsystem.marca (nome, telefone, email)
    VALUES (%s, %s, %s)""",
    (marca.nome, marca.telefone, marca.email))
    cnxn.commit()

    cursor.close()
    cnxn.close()

def selecionarTodos():
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.marca")
    marcas = []
    
    for row in cursor.fetchall():
        marca = row_to_marca(row)
        marcas.append(marca)

    cursor.close()
    cnxn.close()
        
    return marcas

def selecionarById(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.marca WHERE id = %s", (id,))
    row = cursor.fetchone()
    if row:
        marca = row_to_marca(row)
    else:
        marca = None
    
    cursor.close()
    cnxn.close()

    return marca

def selecionarByName(nome):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.marca WHERE nome = %s", (nome,))
    row = cursor.fetchone()
    if row:
        marca = row_to_marca(row)
    else:
        marca = None
    
    cursor.close()
    cnxn.close()

    return marca

def selecionarById2(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.marca ORDER BY CASE WHEN id = %s THEN 0 ELSE 1 END, id", (id,))
    marcas = []
    
    for row in cursor.fetchall():
        marca = row_to_marca(row)
        marcas.append(marca)

    cursor.close()
    cnxn.close()
        
    return marcas

def Excluir(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("DELETE FROM bsystem.marca WHERE id = %s", (id,))
    cnxn.commit()

    cursor.close()
    cnxn.close()

def Alterar(marca):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("""
    UPDATE bsystem.marca
    SET nome = %s, telefone = %s, email = %s
    WHERE id = %s
    """,
    (marca.nome, marca.telefone, marca.email, marca.id))
    cnxn.commit()

    cursor.close()
    cnxn.close()

def row_to_marca(row):
    return marca.marca(row[0], row[1], row[2], row[3])'''

# Exemplo de uso
# marcas = selecionarTodos()
# for marca in marcas:
#     print(marca.nome)
