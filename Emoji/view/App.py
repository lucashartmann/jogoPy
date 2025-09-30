from textual.app import App
from textual.binding import Binding
from textual.containers import Container
from textual.widgets import Static, Header, Button, Label
from view import TelaLoja, TelaInicial, FaseInicial, TelaCasa
from models import Init


class Jogo(App):

    SCREENS = {
        "tela_inicial": TelaInicial.TelaInicial,
        "fase_inicial": FaseInicial.FaseInicial,
        "tela_loja": TelaLoja.TelaLoja,
        "loja": TelaLoja.Loja,
        "tela_casa": TelaCasa.TelaCasa
    }

    BINDINGS = [
        Binding("left", "left", "Andar para a esquerda"),
        Binding("right", "right", "Andar para a direita"),
        Binding("up", "up", "Andar para cima"),
        Binding("down", "down", "Andar para baixo"),
        Binding("z", "a1", "Interagir"),
        Binding("c", "c", "Abrir inventário"),
        Binding("x", "x", "Equipar item"),
        Binding("q", "exit", "Encerrar")
    ]

    def on_mount(self):
        self.push_screen("tela_casa")

    def compose(self):
        yield Header()

    def abrir_inventario(self):
        if Init.inventario_aberto:
            self.screen.query_one("#inventario", Container).remove()
            Init.inventario_aberto = False
        else:
            self.screen.mount(Container(id="inventario"))
            for item in Init.cacador.inventario.values():
                self.screen.query_one("#inventario").mount(Static(
                    f"{item.get_icon()}   - {item.get_nome().capitalize()}", classes="item_inventario"))
            Init.inventario_aberto = True

    def action_exit(self):
        self.app.exit()

    def atualizar_header(self):
        self.screen.query_one(Header).icon = f"❤️: {Init.cacador.vida}"
        if Init.cacador.item_equipado:
            self.title = f"Item equipado: {Init.cacador.item_equipado.get_icon()}  {Init.cacador.item_equipado.get_nome().capitalize()}"
        else:
            self.title = f"Item equipado: Nenhum"

    def action_x(self):
        if Init.cacador.inventario:
            lista_items = list(Init.cacador.inventario.keys())
            Init.cacador.equipar_item(lista_items[Init.contador])
            self.atualizar_header()
            self.notify(
                f"Item equipado: {Init.cacador.item_equipado.get_nome()}")
            Init.contador -= 1
            if Init.contador < 0:
                Init.contador = len(lista_items) - 1
        else:
            self.notify("Inventário vazio")

    def action_c(self):
        self.abrir_inventario()

    def reiniciar(self):
        Init.cacador.inventario.clear()
        Init.cacador.set_vida(100)
        Init.cacador_margin = [0, 0, 0, 0]
        Init.pode_movimentar = True
        Init.lbl_cacador = Label()
        Init.pode_agir = False
        Init.zumbi_morto = False
        Init.objeto_iteracao = ""
        Init.inventario_aberto = False

    def tela_morte(self):
        self.screen.mount(Container(id="container_morte"))
        self.screen.query_one("#container_morte", Container).mount(
            Static("V̶o̶c̶ê̶ M̶o̶r̶r̶e̶u̶", id="stt_morte"))
        self.screen.query_one("#container_morte", Container).mount(
            Button("Tentar Novamente", id="bt_morte"))

    async def on_button_pressed(self, evento: Button.Pressed):
        if evento.button.id == "bt_morte":
            for screen in self.screen_stack:
                screen.remove()
            self.reiniciar()
            self.push_screen("tela_inicial")

    def action_left(self):
        if Init.pode_movimentar:
            if Init.cacador_margin[3] > 0:
                Init.cacador_margin[3] -= 1
            else:
                Init.cacador_margin[1] += 1

            Init.lbl_cacador.styles.margin = (
                Init.cacador_margin[0], Init.cacador_margin[1], Init.cacador_margin[2], Init.cacador_margin[3])

    def action_right(self):
        if Init.pode_movimentar:
            if Init.cacador_margin[1] > 0:
                Init.cacador_margin[1] -= 1
            else:
                Init.cacador_margin[3] += 1
            Init.lbl_cacador.styles.margin = (
                Init.cacador_margin[0], Init.cacador_margin[1], Init.cacador_margin[2], Init.cacador_margin[3])

    def action_up(self):
        if Init.pode_movimentar:
            if Init.cacador_margin[0] > 0:
                Init.cacador_margin[0] -= 1
            else:
                Init.cacador_margin[2] += 1
            Init.lbl_cacador.styles.margin = (
                Init.cacador_margin[0], Init.cacador_margin[1], Init.cacador_margin[2], Init.cacador_margin[3])

    def action_down(self):
        if Init.pode_movimentar:
            if Init.cacador_margin[2] > 0:
                Init.cacador_margin[2] -= 1
            else:
                Init.cacador_margin[0] += 1
            Init.lbl_cacador.styles.margin = (
                Init.cacador_margin[0], Init.cacador_margin[1], Init.cacador_margin[2], Init.cacador_margin[3])
