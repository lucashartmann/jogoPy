from textual.app import App, ComposeResult
from textual.widgets import Label, ListItem, ListView, Footer, Header, TextArea
from models.Item import Item
from textual.events import Load
from textual import on
from textual.containers import HorizontalGroup, VerticalGroup, Container
from textual.screen import Screen
from textual.events import Key
from textual.binding import Binding
from models import Init
import platform


class TelaLoja(Screen):
    CSS_PATH = "css/TelaLoja.tcss"

    cacador_padding = [0, 0, 0, 0]

    casa_tijolos = f'''
    🧱🧱🧱🧱🧱🧱🧱
    🧱🪟 🪟 🧱🪟 🪟 🧱
    🧱🪟 🪟 🧱🪟 🪟 🧱
    🧱🧱🧱🧱🧱🧱🧱
    🧱🧱🚪🧱🚪🧱🧱
        '''

    caminho = f'''🚧🚧🚧🌳🚧🚧🚧🌳🚧🚧🌳🚧🚧🚧
    '''

    loja_itens = f"""
        /\\
       /  \\
      /    \\
     /      \\
    /________\\
   |   Loja   |
   |          |
   |____🧝____| 
    """

    casa_ascii = f"""
                   /\\
                  /  \\ 
                 /    \\ 
                /      \\ 
               /        \\ 
              /          \\
             /            \\
            /              \\
           /________________\\
          /                  \\
         /____________🛁🚽____\\
         |                     |
         |                     |
   📫📮  |____🛏️_🛋️___🚪_________| 
    """

    sol = f"☀️"

    caminho_vertical = f"""
  🚧
  🚧
  🚧
  🌳
  🚧
  🚧
  🚧
  🌳
  🚧
  🚧
  🌳
  🚧
  🚧
  🚧
  """
  

    def sistema_operacional(self):
        if platform.system() == "Windows":
            versao = platform.release()
            if versao == "11":
                return True
        return False

    
    def on_screen_resume(self):
        Init.lbl_cacador = self.query_one("#cacador")
        Init.cacador_padding = [0, 0, 0, 0]
    
    def on_mount(self):
        if self.sistema_operacional() == False:
            for wigdt in self.query(".caminho"):
                wigdt.styles.padding = [14, 0, 0, 0]
            self.query_one("#loja_itens", Label).styles.padding = [6, 0, 0, 0]

    def compose(self):
        yield Header(show_clock=False)
        with HorizontalGroup():
            yield Label(self.caminho, classes="caminho")
            yield Label(self.caminho, classes="caminho")
            yield Label(self.loja_itens, id="loja_itens")
            yield Label(self.caminho, classes="caminho")
            if self.sistema_operacional() == True:
                yield Label(self.casa_tijolos, id="casa_tijolos")
            else:
                yield Label(self.casa_ascii, id="casa_ascii")
            yield Label(self.sol, id="sol")
        with VerticalGroup():
            yield Label("👮", id="cacador")
            with HorizontalGroup(id="caminhos_baixo"):
                yield Label(self.caminho, classes="caminho2")
                yield Label(self.caminho, classes="caminho2")
                yield Label(self.caminho, classes="caminho2")
                yield Label(self.caminho, classes="caminho2")
                yield Label("🚧🚧🌳", classes="caminho2")
                yield Label(self.caminho_vertical, classes="caminho_vertical")
        yield Footer(show_command_palette=False)

    def on_key(self, evento: Key):
        if evento.key == "z":
            if Init.cacador_padding >= [0, 0, 0, 58] and Init.cacador_padding <= [0, 0, 0, 68]:
                self.app.switch_screen("loja")


class Loja(Screen):

    CSS_PATH = "css/TelaLoja.tcss"

    BINDINGS = [
        Binding("z", "a1", "Sair"),
        Binding("x", "comprar", "Comprar"),
    ]
    
    def on_key(self, evento: Key):
        if evento.key == "z":
            self.app.switch_screen('tela_loja')

    descricoes = {
        "Rocha": "Uma simples rocha, útil para arremessar ou bloquear caminhos.",
        "Espada": "Uma espada afiada, perfeita para combates corpo a corpo.",
        "Capa": "Uma capa leve, protege do frio e do vento.",
        "Foice": "Uma foice curva, ideal para colher ou lutar.",
        "Capacete": "Um capacete resistente, protege a cabeça de impactos.",
        "Peitoral": "Um peitoral de armadura, oferece grande proteção ao torso.",
        "Calça": "Uma calça reforçada, protege as pernas durante batalhas.",
        "Picareta": "Uma picareta robusta, essencial para minerar pedras e metais.",
        "Machado": "Um machado pesado, ótimo para cortar madeira ou lutar.",
        "Cenoura": "Uma cenoura fresca, pode ser comida para recuperar energia.",
        "Gema": "Uma gema brilhante, valiosa e rara.",
        "Moeda": "Uma moeda de ouro, usada para comprar itens na loja.",
        "Lira": "Uma lira musical, perfeita para encantar e entreter."
    }

    TITLE = "🧝 Loja do Elfo"

    lista_items = []
    item_highlited = None

    def action_comprar(self):
        if self.item_highlited:
            self.lista_items.remove(self.item_highlited)
            self.atualizar_view()
            Init.cacador.inventario[self.item_highlited.get_nome()] = self.item_highlited
            self.notify(f"{self.item_highlited.get_nome()} comprado!")
        else:
            self.notify("Selecione um item para comprar")

    def atualizar_view(self):
        list_view = self.query_one("#lst_item", ListView)
        list_view.remove_children()
        for item in self.lista_items:
            list_view.append(
                ListItem(Label(item.get_nome().capitalize(), classes="item")))

    def on_mount(self):
        for i in range(12):
            self.lista_items.append(Item())
        list_view = self.query_one("#lst_item", ListView)
        for item in self.lista_items:
            list_view.append(
                ListItem(Label(item.get_nome().capitalize(), classes="item")))

    def compose(self) -> ComposeResult:
        yield Header()
        with HorizontalGroup(id="ctn_bemvindo"):
            yield Label("🧝")
            yield Label(id="tx_dot1")
            yield Label(id="tx_dot2")
            yield Label("Bem vindo!", id="tx_bemvindo")
        yield ListView(id="lst_item")
        yield Label("item", id="tx_info")
        yield Footer()

    @on(ListView.Highlighted, "#lst_item")
    def item_selecionado(self) -> None:
        lista = self.query_one("#lst_item", ListView)
        info = self.query_one("#tx_info", Label)
        nome_item = self.lista_items[lista.index].get_nome().capitalize()
        self.item_highlited = self.lista_items[lista.index]
        if self.lista_items[lista.index].get_icon() != "":
            if nome_item.split()[1].capitalize() in self.descricoes.keys():
                info.update(
                    f"{nome_item}: {self.descricoes[nome_item.split()[1].capitalize()]}")
            else:
                info.update(f"{nome_item}")
        else:
            if nome_item.split()[0] in self.descricoes.keys():
                info.update(
                    f"{nome_item}: {self.descricoes[nome_item.split()[0]]}")
            else:
                info.update(f"{nome_item}")
