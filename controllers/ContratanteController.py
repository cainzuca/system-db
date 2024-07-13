import services.database as db
import models.Contratante as contratante

def incluir(contratante):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = db.cursor.execute("""
    INSERT INTO bsystem.contratante (nome, telefone, email,cnpj)
    VALUES (%s, %s, %s, %s)""",
    (contratante.nome, contratante.telefone, contratante.email,contratante.cnpj ))
    db.cnxn.commit()

    cursor.close()
    cnxn.close()

def selecionarTodos():
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    db.cursor.execute("SELECT* FROM bsystem.contratante")
    contratantes = []
    
    for row in db.cursor.fetchall():
        contratante = row_to_contratante(row)
        contratantes.append(contratante)

    cursor.close()
    cnxn.close()
        
    return contratantes

def selecionarById(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    db.cursor.execute("SELECT * FROM bsystem.contratante WHERE id = %s", (id,))
    row = db.cursor.fetchone()
    if row:
        return row_to_contratante(row)
    
    cursor.close()
    cnxn.close()

    return None

def selecionarByName(nome):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    db.cursor.execute("SELECT * FROM bsystem.contratante WHERE nome = %s", (nome,))
    row = db.cursor.fetchone()
    if row:
        return row_to_contratante(row)
    
    cursor.close()
    cnxn.close()

    return None

def selecionarById2(id):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()
    
    db.cursor.execute("SELECT* FROM bsystem.contratante ORDER BY CASE WHEN id = %s THEN 0 ELSE 1 END,id", (id,))
    contratantes = []
    
    for row in db.cursor.fetchall():
        contratante = row_to_contratante(row)
        contratantes.append(contratante)

    cursor.close()
    cnxn.close()
        
    return contratantes

def Excluir(id):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = db.cursor.execute("DELETE FROM bsystem.contratante WHERE id = %s", (id,))
    db.cnxn.commit()

    cursor.close()
    cnxn.close()    

def Alterar(contratante):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = db.cursor.execute("""
    UPDATE bsystem.contratante
    SET nome = %s, telefone = %s, email = %s, cnpj = %s
    WHERE id = %s
    """,
    (contratante.nome, contratante.telefone, contratante.email,contratante.cnpj,contratante.id))
    db.cnxn.commit()

    cursor.close()
    cnxn.close()       

def row_to_contratante(row):
    return contratante.contratante(row[0], row[1], row[2], row[3], row[4])

#GPT

'''import services.database as db
import models.Contratante as contratante

def incluir(contratante):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("""
    INSERT INTO bsystem.contratante (nome, telefone, email)
    VALUES (%s, %s, %s)""",
    (contratante.nome, contratante.telefone, contratante.email))
    cnxn.commit()

    cursor.close()
    cnxn.close()

def selecionarTodos():
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.contratante")
    contratantes = []
    
    for row in cursor.fetchall():
        contratante = row_to_contratante(row)
        contratantes.append(contratante)

    cursor.close()
    cnxn.close()
        
    return contratantes

def selecionarById(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.contratante WHERE id = %s", (id,))
    row = cursor.fetchone()
    if row:
        contratante = row_to_contratante(row)
    else:
        contratante = None
    
    cursor.close()
    cnxn.close()

    return contratante

def selecionarByName(nome):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.contratante WHERE nome = %s", (nome,))
    row = cursor.fetchone()
    if row:
        contratante = row_to_contratante(row)
    else:
        contratante = None
    
    cursor.close()
    cnxn.close()

    return contratante

def selecionarById2(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()
    
    cursor.execute("SELECT * FROM bsystem.contratante ORDER BY CASE WHEN id = %s THEN 0 ELSE 1 END, id", (id,))
    contratantes = []
    
    for row in cursor.fetchall():
        contratante = row_to_contratante(row)
        contratantes.append(contratante)

    cursor.close()
    cnxn.close()
        
    return contratantes

def Excluir(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("DELETE FROM bsystem.contratante WHERE id = %s", (id,))
    cnxn.commit()

    cursor.close()
    cnxn.close()    

def Alterar(contratante):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("""
    UPDATE bsystem.contratante
    SET nome = %s, telefone = %s, email = %s
    WHERE id = %s
    """,
    (contratante.nome, contratante.telefone, contratante.email, contratante.id))
    cnxn.commit()

    cursor.close()
    cnxn.close()       

def row_to_contratante(row):
    return contratante.contratante(row[0], row[1], row[2], row[3])

# Exemplo de uso
# contratantes = selecionarTodos()
# for contratante in contratantes:
#     print(contratante.nome)
'''