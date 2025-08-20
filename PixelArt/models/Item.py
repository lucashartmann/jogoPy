import random

objetos = [
    {"nome": "Rocha", "genero": "f"},
    {"nome": "Espada", "genero": "f"},
    {"nome": "Capa", "genero": "f"},
    {"nome": "Foice", "genero": "f"},
    {"nome": "Capacete", "genero": "m"},
    {"nome": "Peitoral", "genero": "m"},
    {"nome": "Calça", "genero": "f"},
    {"nome": "Picareta", "genero": "f"},
    {"nome": "Machado", "genero": "m"},
    {"nome": "Cenoura", "genero": "f"},
    {"nome": "Gema", "genero": "f"},
    {"nome": "Moeda", "genero": "f"},
    {"nome": "lira", "genero": "f"}
]

adjetivos = [
    {"f": "Feroz", "m": "Feroz"},
    {"f": "Fulminante", "m": "Fulminante"},
    {"f": "Vingativa", "m": "Vingativo"},
    {"f": "Bela como a Lua", "m": "Belo como a Lua"},
    {"f": "Reluzente", "m": "Reluzente"},
    {"f": "Fervescente", "m": "Fervescente"}
]

complementos = [
    {"f": "Forjada na lua", "m": "Forjado na lua"},
    {"f": "do Minotauro", "m": "do Minotauro"},
    {"f": "dos confins do inferno", "m": "dos confins do inferno"},
    {"f": "Enferrujada", "m": "Enferrujado"},
    {"f": "Perfeita", "m": "Perfeito"},
    {"f": "Usada pelo Rei de Minas", "m": "Usado pelo Rei de Minas"},
]

icone_objeto = {
    "espada": "🗡️",
    "machado": "🪓",
    "picareta": "⛏️",
    # "foice" : "",
    "escudo": "🛡️",
    "calça": "👖",
    # "capacete" : "🪖",
    # "capa" : "",
    # "peitoral" : "",
    # "rocha" : "🪨",
    "cenoura": "🥕",
    "gema": "💎",
    # "moeda" : "🪙",
    # "lira" : "",
}

icone_adjetivo = {
    # "feroz" : "",
    "fulminante": "💥",
    # "vingativo" : "",
    "belo como a lua": "🌙",
    "reluzente": "🌟",
}

icone_complemento = {
    "forjada na lua": "🌙",
    # "do minotauro" : "",
    # "dos confins do inferno" : "🔥",
    # "enferrujada" : "",
    # "perfeita" : "",
}


class Item:

    def __init__(self):
        self.dano = 0
        self.protecao = 0
        self.categoria = ""
        self.nome = str()

        self.objeto = random.choice(objetos)
        self.adjetivo = random.choice(adjetivos)
        self.complemento = random.choice(complementos)

        self.genero_objeto = self.objeto["genero"]

        try:
            self.icon = icone_objeto[self.objeto["nome"].lower()]
            self.nome = f"{self.icon} {self.objeto['nome']} {self.adjetivo[self.genero_objeto]} {self.complemento[self.genero_objeto]}"
        except:
            self.icon = ""
            self.nome = f"{self.objeto['nome']} {self.adjetivo[self.genero_objeto]} {self.complemento[self.genero_objeto]}"

        if self.objeto["nome"].lower() in ["espada", "machado", "picareta"]:
            self.dano = random.randint(1, 10)
            self.categoria = "arma"
        elif self.objeto["nome"].lower() in ["calça", "capacete", "capa", "peitoral"]:
            self.protecao = random.randint(1, 10)
            self.categoria = "armadura"
        elif self.objeto["nome"].lower() in ["rocha", "cenoura", "gema", "moeda", "lira"]:
            self.categoria = "item_comum"

    def get_categoria(self):
        return self.categoria

    def get_icon(self):
        return self.icon

    def get_objeto(self):
        return self.objeto

    def get_adjetivo(self):
        return self.adjetivo

    def get_complemento(self):
        return self.complemento

    def get_genero_objeto(self):
        return self.genero_objeto

    def get_nome(self):
        return self.nome

    def set_genero_objeto(self, genero):
        self.genero_objeto = genero

    def set_icon(self, novo_icon):
        self.icon = novo_icon

    def set_categoria(self, nova_categoria):
        self.categoria = nova_categoria

    def set_quant(self, nova_quant):
        self.quant = nova_quant

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_dano(self, novo_Dano):
        self.dano = novo_Dano

    def get_dano(self):
        return self.dano

    def set_protecao(self, nova_protecao):
        self.protecao = nova_protecao

    def get_protecao(self):
        return self.protecao

    def __str__(self):
        if self.dano > 0:
            return f"Item [Nome: {self.get_nome()}, dano = {self.get_dano()}]"

        if self.protecao > 0:
            return f"Item [Nome: {self.get_nome()}, protecao = {self.protecao}]"

        if self.dano > 0 and self.protecao > 0:
            return f"Item [Nome: {self.get_nome()}, dano = {self.get_dano()}, protecao = {self.protecao}]"

        return f"Item [Nome: {self.get_nome()}]"
