from models import Init
from textual.widgets import Static
from controller import Controller


lbl_cacador = Static(Controller.gerar_pixel(
    "assets/personagem.png", 6), id="cacador")

lbl_chave = Static(Controller.gerar_pixel(
    "assets/chave.png", 8), id=f"{Init.chave.get_nome()}")

# lbl_zumbi = Static(Controller.gerar_pixel(
    # "", 8), id="zumbi")

# lbl_porta = Static(Controller.gerar_pixel(
    # "", 8), id="porta")

# lbl_espada = Static(Controller.gerar_pixel(
    # "", 8), id=f"{Init.espada.get_nome()}")
