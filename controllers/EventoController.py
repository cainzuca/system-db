import services.database as db
import models.Evento as evento

def incluir(evento):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = db.cursor.execute("""
    INSERT INTO bsystem.evento (nome, local, valor, data, fk_artista, fk_contratante,fk_marca,porcentagem,custos)
    VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s)""",
    (evento.nome, evento.local, evento.valor, evento.data,evento.fk_artista,evento.fk_contratante,evento.fk_marca,evento.porcentagem,evento.custos ))
    db.cnxn.commit()

    cursor.close()
    cnxn.close()

def selecionarTodos():
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    db.cursor.execute("SELECT * FROM bsystem.evento")
    eventos = []
    
    for row in db.cursor.fetchall():
        evento = row_to_evento(row)
        eventos.append(evento)

    cursor.close()
    cnxn.close()        
        
    return eventos

def selecionarById(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    db.cursor.execute("SELECT * FROM bsystem.evento WHERE id = %s", (id,))
    row = db.cursor.fetchone()
    if row:
        return row_to_evento(row)
    
    cursor.close()
    cnxn.close()       

    return None

def selecionarById2(id):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    db.cursor.execute("SELECT* FROM bsystem.evento ORDER BY CASE WHEN id = %s THEN 0 ELSE 1 END,id", (id,))
    eventos = []
    
    for row in db.cursor.fetchall():
        evento = row_to_evento(row)
        eventos.append(evento)

    cursor.close()
    cnxn.close()  
        
    return eventos

def selecionarByName(nome):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    db.cursor.execute("SELECT * FROM bsystem.evento WHERE nome = %s", (nome,))
    row = db.cursor.fetchone()
    if row:
        return row_to_evento(row)
    
    cursor.close()
    cnxn.close()  

    return None

def Excluir(id):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = db.cursor.execute("DELETE FROM bsystem.evento WHERE id = %s", (id,))
    db.cnxn.commit()

    cursor.close()
    cnxn.close()  


def Alterar(evento):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = db.cursor.execute("""
    UPDATE bsystem.evento
    SET nome = %s, local = %s, valor = %s, data = %s, fk_artista = %s, fk_contratante = %s, fk_marca = %s, porcentagem = %s, custos = %s
    WHERE id = %s
    """,
    (evento.nome, evento.local, evento.valor, evento.data,evento.fk_artista,evento.fk_contratante,evento.fk_marca,evento.porcentagem,evento.custos,evento.id))
    db.cnxn.commit()

    cursor.close()
    cnxn.close()  


def row_to_evento(row):
    return evento.evento(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9])

#GPT

'''import services.database as db
import models.Evento as evento

def incluir(evento):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("""
    INSERT INTO bsystem.evento (nome, local, valor, data, fk_artista, fk_contratante, fk_marca, porcentagem, custos)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
    (evento.nome, evento.local, evento.valor, evento.data, evento.fk_artista, evento.fk_contratante, evento.fk_marca, evento.porcentagem, evento.custos))
    cnxn.commit()

    cursor.close()
    cnxn.close()

def selecionarTodos():
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.evento")
    eventos = []
    
    for row in cursor.fetchall():
        evento = row_to_evento(row)
        eventos.append(evento)

    cursor.close()
    cnxn.close()        
        
    return eventos

def selecionarById(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.evento WHERE id = %s", (id,))
    row = cursor.fetchone()
    if row:
        return row_to_evento(row)
    
    cursor.close()
    cnxn.close()       

    return None

def selecionarById2(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.evento ORDER BY CASE WHEN id = %s THEN 0 ELSE 1 END, id", (id,))
    eventos = []
    
    for row in cursor.fetchall():
        evento = row_to_evento(row)
        eventos.append(evento)

    cursor.close()
    cnxn.close()  
        
    return eventos

def selecionarByName(nome):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.evento WHERE nome = %s", (nome,))
    row = db.cursor.fetchone()
    if row:
        return row_to_evento(row)
    
    cursor.close()
    cnxn.close()  

    return None

def Excluir(id):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("DELETE FROM bsystem.evento WHERE id = %s", (id,))
    cnxn.commit()

    cursor.close()
    cnxn.close()  

def Alterar(evento):
    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("""
    UPDATE bsystem.evento
    SET nome = %s, local = %s, valor = %s, data = %s, fk_artista = %s, fk_contratante = %s, fk_marca = %s, porcentagem = %s, custos = %s
    WHERE id = %s
    """,
    (evento.nome, evento.local, evento.valor, evento.data, evento.fk_artista, evento.fk_contratante, evento.fk_marca, evento.porcentagem, evento.custos, evento.id))
    cnxn.commit()

    cursor.close()
    cnxn.close()  

def row_to_evento(row):
    return evento.evento(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])

# Exemplo de uso
# eventos = selecionarTodos()
# for evento in eventos:
#     print(evento.nome)'''
