from textual.app import App
from textual.binding import Binding
from view import TelaLoja, TelaInicial, FaseInicial
from models import cacador_padding

class Jogo(App):

    SCREENS = {
        "tela_inicial": TelaInicial.TelaInicial,
        "fase_inicial": FaseInicial.FaseInicial,
        "tela_loja": TelaLoja.TelaLoja,
        "loja": TelaLoja.Loja
    }

    BINDINGS = [
        # Usar os bindings ou continuar trarando o on_key direto?
        Binding("left", "left", "Andar para a esquerda"),
        Binding("right", "right", "Andar para a direita"),
        Binding("up", "up", "Andar para cima"),
        Binding("down", "down", "Andar para baixo"),
        Binding("z", "a1", "Interagir"),
        Binding("c", "a6", "Abrir inventário"),
        Binding("x", "a7", "Equipar item"),
        Binding("q", "exit()", "Encerrar") # Fazer funcionar
    ]

    def on_mount(self):
        self.push_screen("tela_loja")

    def action_left(self):
        if cacador_padding[3] > 0:
                    cacador_padding[3] -= 1
        else:
                    cacador_padding[1] += 1

        label.styles.padding = (
            cacador_padding[0], cacador_padding[1], cacador_padding[2], cacador_padding[3])
    def action_right(self):
        if cacador_padding[1] > 0:
                    cacador_padding[1] -= 1
        else:
                    cacador_padding[3] += 1
        label.styles.padding = (
            cacador_padding[0], cacador_padding[1], cacador_padding[2], cacador_padding[3])
    def action_up(self):
        if cacador_padding[0] > 0:
                    cacador_padding[0] -= 1
        else:
                    cacador_padding[2] += 1
        label.styles.padding = (
            cacador_padding[0], cacador_padding[1], cacador_padding[2], cacador_padding[3])
    def action_down(self):
        if cacador_padding[2] > 0:
                    cacador_padding[2] -= 1
        else:
                    cacador_padding[0] += 1
        label.styles.padding = (
            cacador_padding[0], cacador_padding[1], cacador_padding[2], cacador_padding[3])

    

        