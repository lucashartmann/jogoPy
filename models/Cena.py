class Cena():
    def __init__(self, nome="Indefinida"):
        self.nome = nome
        self.itens = {}
        self.norte = None
        self.sul = None
        self.leste = None
        self.oeste = None

    def colocar_item(self, item):
        self.itens[item.get_nome()] = item

    def coletar_item(self, nome_item):
        item_coletado = self.itens[nome_item]
        del self.itens[nome_item]
        return item_coletado

    def __str__(self):
        return f'''
[{self.nome}]
Itens: {self.itens}
'''
