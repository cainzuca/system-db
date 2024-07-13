class evento:
    def __init__(self,id, nome, local, valor, data, fk_artista, fk_contratante,fk_marca,porcentagem,custos ):
        self.id = id
        self.nome = nome
        self.local = local
        self.valor = valor
        self.data = data
        self.fk_artista = fk_artista
        self.fk_contratante = fk_contratante
        self.fk_marca = fk_marca
        self.porcentagem = porcentagem
        self.custos = custos