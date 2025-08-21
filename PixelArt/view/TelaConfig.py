from textual.widgets import Input, Label, Button, Static, Label
from textual.containers import HorizontalGroup, VerticalGroup
from textual.screen import Screen
from controller import Controller
from config import Assets
from config import Assets


class TelaConfig(Screen):
    CSS_PATH = "css/TelaConfig.tcss"
    montou = False

    def compose(self):
        with HorizontalGroup():
            with VerticalGroup():
                yield Input(placeholder="caminho", id="inpt_caminho")
                yield Input(placeholder="tamanho", id="inpt_tamanho")
            yield HorizontalGroup(id="hg_resultado")
        with HorizontalGroup():
            yield Label()
            yield Button("Voltar", id="bt_voltar")
            yield Button("Criar", id="bt_criar")

    def on_button_pressed(self, evento: Button.Pressed):
        if evento.button.id == "bt_criar":
            hg = self.query_one("#hg_resultado", HorizontalGroup)
            if self.montou:
                hg.remove_children()
            caminho = str(self.query_one("#inpt_caminho", Input).value)
            tamanho = int(self.query_one("#inpt_tamanho", Input).value)
            stt_personagem = Static(Controller.gerar_pixel(
                caminho, tamanho), id="cacador")
            hg.mount(stt_personagem)
            Assets.lbl_cacador = ""
            Assets.lbl_cacador = stt_personagem
            self.montou = True
        if evento.button.id == "bt_voltar":
            self.app.switch_screen("tela_inicial")


# assets/coracao.png
