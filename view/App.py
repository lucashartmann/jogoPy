from textual.app import App
from textual.binding import Binding
from textual.containers import Container
from textual.widgets import Static
from view import TelaLoja, TelaInicial, FaseInicial
from models import Init


class Jogo(App):

    SCREENS = {
        "tela_inicial": TelaInicial.TelaInicial,
        "fase_inicial": FaseInicial.FaseInicial,
        "tela_loja": TelaLoja.TelaLoja,
        "loja": TelaLoja.Loja
    }

    BINDINGS = [
        Binding("left", "left", "Andar para a esquerda"),
        Binding("right", "right", "Andar para a direita"),
        Binding("up", "up", "Andar para cima"),
        Binding("down", "down", "Andar para baixo"),
        Binding("z", "a1", "Interagir"),
        Binding("c", "c", "Abrir inventário"),
        Binding("x", "x", "Equipar item"),
        Binding("q", "exit()", "Encerrar")  # Fazer funcionar
    ]

    def on_mount(self):
        self.push_screen("fase_inicial")

    def abrir_inventario(self):
        if Init.inventario_aberto:
            self.query_one("#inventario", Container).remove()
            Init.inventario_aberto = False
        else:
            self.mount(Container(id="inventario"))
            for item in Init.cacador.inventario.values():
                self.query_one("#inventario").mount(Static(
                    f"{item.get_icon()}   - {item.get_nome().capitalize()}", classes="item_inventario"))
            Init.inventario_aberto = True

    def action_x(self):
        if Init.cacador.inventario:
            lista_items = list(Init.cacador.inventario.keys())
            Init.cacador.equipar_item(lista_items[Init.contador])
            # self.atualizar_header()
            self.notify(
                f"Item equipado: {Init.cacador.item_equipado.get_nome()}")
            Init.contador -= 1
            if Init.contador < 0:
                Init.contador = len(lista_items) - 1
        else:
            self.notify("Inventário vazio")

    def action_c(self):
        self.abrir_inventario()

    def action_left(self):
        if Init.cacador_padding[3] > 0:
            Init.cacador_padding[3] -= 1
        else:
            Init.cacador_padding[1] += 1

        Init.lbl_cacador.styles.padding = (
            Init.cacador_padding[0], Init.cacador_padding[1], Init.cacador_padding[2], Init.cacador_padding[3])

    def action_right(self):
        if Init.cacador_padding[1] > 0:
            Init.cacador_padding[1] -= 1
        else:
            Init.cacador_padding[3] += 1
        Init.lbl_cacador.styles.padding = (
            Init.cacador_padding[0], Init.cacador_padding[1], Init.cacador_padding[2], Init.cacador_padding[3])

    def action_up(self):
        if Init.cacador_padding[0] > 0:
            Init.cacador_padding[0] -= 1
        else:
            Init.cacador_padding[2] += 1
        Init.lbl_cacador.styles.padding = (
            Init.cacador_padding[0], Init.cacador_padding[1], Init.cacador_padding[2], Init.cacador_padding[3])

    def action_down(self):
        if Init.cacador_padding[2] > 0:
            Init.cacador_padding[2] -= 1
        else:
            Init.cacador_padding[0] += 1
        Init.lbl_cacador.styles.padding = (
            Init.cacador_padding[0], Init.cacador_padding[1], Init.cacador_padding[2], Init.cacador_padding[3])
