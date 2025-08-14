from textual.app import App
from textual.binding import Binding
from view import TelaLoja, TelaInicial, FaseInicial


class Jogo(App):

    SCREENS = {
        "tela_inicial": TelaInicial.TelaInicial,
        "fase_inicial": FaseInicial.FaseInicial,
        "tela_loja": TelaLoja.TelaLoja,
        "loja": TelaLoja.Loja
    }

    BINDINGS = [
        # Usar os bindings ou continuar trarando o on_key direto?
        Binding("left", "a2", "Andar para a esquerda"),
        Binding("right", "a3", "Andar para a direita"),
        Binding("up", "a4", "Andar para cima"),
        Binding("down", "a5", "Andar para baixo"),
        Binding("z", "a1", "Interagir"),
        Binding("c", "a6", "Abrir inventário"),
        Binding("x", "a7", "Equipar item"),
        Binding("q", "exit()", "Encerrar") # Fazer funcionar
    ]

    def on_mount(self):
        self.push_screen("tela_inicial")

    def movimentacao(self, evento, label, cacador_padding):
        match evento.key:
            case "left":
                if cacador_padding[3] > 0:
                    cacador_padding[3] -= 1
                else:
                    cacador_padding[1] += 1

            case "right":
                if cacador_padding[1] > 0:
                    cacador_padding[1] -= 1
                else:
                    cacador_padding[3] += 1

            case "up":
                if cacador_padding[0] > 0:
                    cacador_padding[0] -= 1
                else:
                    cacador_padding[2] += 1

            case "down":
                if cacador_padding[2] > 0:
                    cacador_padding[2] -= 1
                else:
                    cacador_padding[0] += 1
            case _:
                return

        label.styles.padding = (
            cacador_padding[0], cacador_padding[1], cacador_padding[2], cacador_padding[3])