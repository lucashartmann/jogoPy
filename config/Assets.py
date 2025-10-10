from textual.widgets import Static
from textual_image.widget import Image
import io
from view.widgets import Gif
import os


lbl_cacador = Gif.Gif(r"assets\Entities\Characters\Carry_Idle\Carry_Idle_Down-Sheet.png", id="cacador", pixel=True)

with open(r"assets/chave.png", 'rb') as file:
            blob = file.read()
lbl_chave_image = Image(io.BytesIO(blob))
lbl_chave = Static(id="stt_chave")

with open(r"assets/coracao.png", 'rb') as file:
            blob = file.read()
image_coracao = Image(io.BytesIO(blob))
stt_coracao = Static(Image, id="stt_coracao")


image_plano_fundo = Image(r"assets/plano_fundo.png", id="img_plano_fundo")
stt_plano_fundo = Static(id="stt_plano_fundo")

with open(r"assets\Weapons\Bone\Foice.png", 'rb') as file:
            blob = file.read()
image_foice = Image(io.BytesIO(blob))

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