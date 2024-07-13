import services.database as db
import models.Pagamento as pagamento

def incluir(pagamento):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = db.cursor.execute("""
    INSERT INTO bsystem.pagamento (valor, forma, data, status,fk_evento,fk_contratante,fk_marca, parcela, entrada)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
    (pagamento.valor, pagamento.forma, pagamento.data, pagamento.status, pagamento.fk_evento,pagamento.fk_contratante,pagamento.fk_marca,pagamento.parcela,pagamento.entrada ))
    db.cnxn.commit()

    cursor.close()
    cnxn.close()


def selecionarTodos():

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    db.cursor.execute("SELECT * FROM bsystem.pagamento")
    pagamentos = []
    
    for row in db.cursor.fetchall():
        pagamento = row_to_pagamento(row)
        pagamentos.append(pagamento)

    cursor.close()
    cnxn.close()
        
    return pagamentos

def selecionarById(id):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    db.cursor.execute("SELECT * FROM bsystem.pagamento WHERE id = %s", (id,))
    row = db.cursor.fetchone()
    if row:
        return row_to_pagamento(row)
    
    cursor.close()
    cnxn.close()

    return None

def selecionarById2(id):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    db.cursor.execute("SELECT* FROM bsystem.pagamento ORDER BY CASE WHEN id = %s THEN 0 ELSE 1 END,id", (id,))
    pagamentos = []
    
    for row in db.cursor.fetchall():
        pagamento = row_to_pagamento(row)
        pagamentos.append(pagamento)

    cursor.close()
    cnxn.close()        
        
    return pagamentos

def Excluir(id):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = db.cursor.execute("DELETE FROM bsystem.pagamento WHERE id = %s", (id,))
    db.cnxn.commit()

    cursor.close()
    cnxn.close()

def Alterar(pagamento):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = db.cursor.execute("""
    UPDATE bsystem.pagamento
    SET valor = %s, forma = %s, data = %s, status = %s, fk_evento = %s, fk_contratante = %s, fk_marca = %s, parcela = %s, entrada = %s
    WHERE id = %s
    """,
    (pagamento.valor,pagamento.forma, pagamento.data, pagamento.status,pagamento.fk_evento,pagamento.fk_contratante,pagamento.fk_marca,pagamento.parcela, pagamento.entrada,pagamento.id))
    db.cnxn.commit()

    cursor.close()
    cnxn.close()

def row_to_pagamento(row):
    return pagamento.pagamento(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9])

#GPT

'''import services.database as db
import models.Pagamento as pagamento

def incluir(pagamento):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("""
    INSERT INTO bsystem.pagamento (valor, forma, data, status, fk_evento, fk_contratante, fk_marca)
    VALUES (%s, %s, %s, %s, %s, %s, %s)""",
    (pagamento.valor, pagamento.forma, pagamento.data, pagamento.status, pagamento.fk_evento, pagamento.fk_contratante, pagamento.fk_marca))
    cnxn.commit()

    cursor.close()
    cnxn.close()

def selecionarTodos():

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.pagamento")
    pagamentos = []
    
    for row in cursor.fetchall():
        pagamento = row_to_pagamento(row)
        pagamentos.append(pagamento)

    cursor.close()
    cnxn.close()
        
    return pagamentos

def selecionarById(id):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.pagamento WHERE id = %s", (id,))
    row = cursor.fetchone()
    if row:
        return row_to_pagamento(row)
    
    cursor.close()
    cnxn.close()

    return None

def selecionarById2(id):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM bsystem.pagamento ORDER BY CASE WHEN id = %s THEN 0 ELSE 1 END, id", (id,))
    pagamentos = []
    
    for row in cursor.fetchall():
        pagamento = row_to_pagamento(row)
        pagamentos.append(pagamento)

    cursor.close()
    cnxn.close()        
        
    return pagamentos

def Excluir(id):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("DELETE FROM bsystem.pagamento WHERE id = %s", (id,))
    cnxn.commit()

    cursor.close()
    cnxn.close()

def Alterar(pagamento):

    cnxn = db.criar_conexao()
    cursor = cnxn.cursor()

    count = cursor.execute("""
    UPDATE bsystem.pagamento
    SET valor = %s, forma = %s, data = %s, status = %s, fk_evento = %s, fk_contratante = %s, fk_marca = %s
    WHERE id = %s
    """,
    (pagamento.valor, pagamento.forma, pagamento.data, pagamento.status, pagamento.fk_evento, pagamento.fk_contratante, pagamento.fk_marca, pagamento.id))
    cnxn.commit()

    cursor.close()
    cnxn.close()

def row_to_pagamento(row):
    return pagamento.pagamento(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
'''