from textual.widgets import Input, Label, Button, Static, Label
from textual.containers import HorizontalGroup, VerticalGroup
from textual.screen import Screen
from textual_image.widget import Image
from config import Assets


class TelaConfig(Screen):
    CSS_PATH = "css/TelaConfig.tcss"
    montou = False

    #assets/coracao.png

    def compose(self):
        with HorizontalGroup():
            with VerticalGroup():
                yield Input(placeholder="caminho", id="inpt_caminho")
                yield Input(placeholder="width", classes="ipt_size")
                yield Input(placeholder="height", classes="ipt_size")
            yield HorizontalGroup(id="hg_resultado")
        with HorizontalGroup():
            yield Label()
            yield Button("Voltar", id="bt_voltar")
            yield Button("Criar", id="bt_criar")

    def on_button_pressed(self, evento: Button.Pressed):
        if evento.button.id == "bt_criar":
            hg = self.query_one("#hg_resultado", HorizontalGroup)
            if self.montou:
                self.query_one(Static).remove()
                hg.remove_children("#cacador")
            caminho = str(self.query_one("#inpt_caminho", Input).value)
            width = int(self.query_one("#inpt_width", Input).value)
            height = int(self.query_one("#inpt_height", Input).value)
            
            stt_personagem = Image(caminho, id="cacador")
            stt_personagem.styles.height = height
            stt_personagem.styles.width = width
            
            hg.mount(stt_personagem)
            Assets.lbl_cacador = ""
            Assets.lbl_cacador = stt_personagem
            self.montou = True
        if evento.button.id == "bt_voltar":
            self.app.switch_screen("tela_inicial")


# assets/coracao.png
