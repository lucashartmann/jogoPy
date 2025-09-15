from textual.screen import Screen
from textual.widgets import Label
from textual.containers import Container
from models import Init

class TelaCasa(Screen):
    CSS_PATH = "css/TelaCasa.tcss"
    
    def compose(self):
        with Container(id="casa"):
            yield Label("🛌", classes="itens", id="cama")
            yield Label("🗄️", classes="itens", id="item")
            yield Label("🪜", classes="itens", id="escada")
            yield Label("📺", classes="itens", id="tv")
            yield Label("🚽", classes="itens", id="vaso")
            yield Label("🛁", classes="itens", id="banheiro")
            yield Label(Init.cacador.icone, id="cacador")
            
    def on_screen_resume(self):
        Init.lbl_cacador = self.query_one("#cacador")
        Init.cacador_padding = [0, 0, 0, 0]
