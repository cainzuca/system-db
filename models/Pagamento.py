class pagamento:
    def __init__(self,id, valor, forma, data, status ,fk_evento,fk_contratante,fk_marca,parcela,entrada):
        self.id = id
        self.valor = valor
        self.forma = forma
        self.data = data
        self.status = status
        self.fk_evento = fk_evento
        self.fk_contratante = fk_contratante
        self.fk_marca = fk_marca
        self.parcela = parcela
        self.entrada = entrada