from models import Init
from textual.widgets import Static
from textual_image.widget import Image

lbl_image = Image("assets/personagem.png")
lbl_image.styles.width = 5
lbl_image.styles.height = 3
lbl_cacador = Static(id="cacador")
lbl_image.styles.width = 5
lbl_image.styles.height = 3

lbl_chave_image = Image("assets/chave.png")
lbl_chave_image.styles.width = 30
lbl_chave_image.styles.height = 30
lbl_chave = Static(id=f"{Init.chave.get_nome()}")
lbl_chave.styles.width = 30
lbl_chave.styles.height = 30

# lbl_zumbi = Static(Controller.gerar_pixel(
    # "", 8), id="zumbi")
# lbl_cacador.styles.width = 8
# lbl_cacador.styles.height = 8

# lbl_porta = Static(Controller.gerar_pixel(
    # "", 8), id="porta")
# lbl_cacador.styles.width = 8
# lbl_cacador.styles.height = 8

# lbl_espada = Static(Controller.gerar_pixel(
    # "", 8), id=f"{Init.espada.get_nome()}")
# lbl_cacador.styles.width = 8
# lbl_cacador.styles.height = 8