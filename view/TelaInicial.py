from textual.widgets import Header, Footer, Static, Button
from textual.screen import ModalScreen
from textual.containers import VerticalGroup


class TelaInicial(ModalScreen):
    CSS_PATH = "css/TelaInicial.tcss"
    BINDINGS = []

    titulo = '''
██████╗░██╗░░░██╗███╗░░██╗░██████╗░███████╗░█████╗░██╗░░░██╗███╗░░██╗
██╔══██╗██║░░░██║████╗░██║██╔════╝░██╔════╝██╔══██╗██║░░░██║████╗░██║
██║░░██║██║░░░██║██╔██╗██║██║░░██╗░█████╗░░██║░░██║██║░░░██║██╔██╗██║
██║░░██║██║░░░██║██║╚████║██║░░╚██╗██╔══╝░░██║░░██║██║░░░██║██║╚████║
██████╔╝╚██████╔╝██║░╚███║╚██████╔╝███████╗╚█████╔╝╚██████╔╝██║░╚███║
╚═════╝░░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░╚══╝'''

    def compose(self):
        yield Header()
        with VerticalGroup():
            yield Static(self.titulo)
            yield Static("𝔘𝔪 𝔡𝔲𝔫𝔤𝔢𝔬𝔫 𝔠𝔯𝔞𝔴𝔩𝔢𝔯 𝔢𝔪 𝔪𝔬𝔡𝔬 𝔱𝔢𝔵𝔱𝔯𝔬")
            yield Button("I̴̢̦͙̓͆̕n̴̼̞͓̓͛͘i̸͉͉͐̔͋c̵̡͖͚̿̓̚i̸̘̪̫̔͆̓a̸̙͚̓͝͝r̸͕̠̦̓̾ J̴̙͓̼͊͌ò̴̫̿͜g̵͙͚͙͑̽͝o̸͉̫͎̐̐̕")
        yield Footer(show_command_palette=False)

    def on_button_pressed(self):
        self.app.switch_screen("fase_inicial")

    def _on_screen_resume(self):
        self.sub_title = "Tela Inicial"
