from models import Item, Cena, Personagem
from config import Assets
import os

class Init:

    cacador_margin = [4, 0, 0, 0]
    zumbi_morto = False
    pode_movimentar = True
    pode_agir = False
    objeto_iteracao = ""
    inventario_aberto = False

    caminho_assets = f"{os.getcwd()}\\assets\\"

    sala_inicial = Cena.Cena("Sala Inicial")

    cacador = Personagem.Personagem()
    # cacador.set_imagem(Assets.lbl_image)
    cacador.sala = sala_inicial

    contador = len(list(cacador.inventario.keys())) - 1

    chave = Item.Item()
    chave.set_nome("chave")
    chave.set_categoria("item_comum")
    chave.set_icon("🗝️")
    chave.set_imagem(Assets.lbl_chave_image)
    chave.set_dano(0)
    chave.set_protecao(0)
    chave.set_genero_objeto("feminino")
    chave.set_quant(1)

    sala_inicial.colocar_item(chave)
    
    picareta = Item.Item()
    picareta.set_nome("picareta")
    picareta.set_categoria("arma")
    chave.set_imagem(Assets.image_foice)
    picareta.set_dano(5)
    picareta.set_protecao(0)
    picareta.set_genero_objeto("feminino")
    picareta.set_quant(1)
    picareta.set_icon("⛏️")
    

    # espada = Item.Item()
    # espada.set_nome("espada")
    # espada.set_categoria("arma")
    # espada.set_icon("🗡️")
    # espada.set_dano(5)
    # espada.set_protecao(0)
    # espada.set_genero_objeto("feminino")
    # espada.set_quant(1)

    sala_inicial.colocar_item(chave)
    
    cacador.inventario["picareta"] = picareta
    cacador.item_equipado = picareta

    coracao = Item.Item()
    coracao.set_nome("coracao")
    coracao.set_genero_objeto("maculino")
    coracao.set_imagem(Assets.image_coracao)
