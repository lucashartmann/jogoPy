from models import Item, Cena, Personagem
from textual.widgets import Label

class Init:

    lbl_cacador = Label() 

    cacador_margin = [0, 0, 0, 0]
    zumbi_morto = False
    pode_movimentar = True
    pode_agir = False
    objeto_iteracao = ""
    inventario_aberto = False

    sala_inicial = Cena.Cena("Sala Inicial")

    cacador = Personagem.Personagem()
    cacador.sala = sala_inicial
    cacador.set_icone("👮")

    contador = len(list(cacador.inventario.keys())) - 1

    chave = Item.Item()
    chave.set_nome("chave")
    chave.set_categoria("item_comum")
    chave.set_icon("🗝️")
    chave.set_dano(0)
    chave.set_protecao(0)
    chave.set_genero_objeto("feminino")
    chave.set_quant(1)

    sala_inicial.colocar_item(chave)

    espada = Item.Item()
    espada.set_nome("espada")
    espada.set_categoria("arma")
    espada.set_icon("🗡️")
    espada.set_dano(5)
    espada.set_protecao(0)
    espada.set_genero_objeto("feminino")
    espada.set_quant(1)

    sala_inicial.colocar_item(espada)
