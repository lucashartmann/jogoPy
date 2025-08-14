from textual.app import App
from textual.widgets import Label, Static, Footer, Header
from textual.containers import HorizontalGroup, Container
from textual.events import Key
from asyncio import sleep
from textual import work
from models.Personagem import Personagem
from textual.screen import Screen
from textual.binding import Binding
from view import TelaLoja, Loja
from models import cacador, cacador_padding, chave, espada, inventario_aberto, pode_agir, pode_movimentar, zumbi_morto, objeto_iteracao, contador

class FaseInicial(Screen):
    CSS_PATH = "css/FaseInicial.tcss"

    def on_mount(self):
        self.atualizar_header()

    def atualizar_header(self):
        self.query_one(Header).icon = f"❤️: {cacador.vida}"
        if cacador.item_equipado:
            self.title = f"Item equipado: {cacador.item_equipado.get_icon()}  {cacador.item_equipado.get_nome().capitalize()}"
        else:
            self.title = f"Item equipado: Nenhum"

    def compose(self):
        yield Header(show_clock=False)
        with HorizontalGroup():
            yield Label(chave.get_icon(), id=f"{chave.get_nome()}")
            yield Label("🧟", id="zumbi")
            yield Label("🚪", id="porta")
            yield Label(espada.get_icon(), id=f"{espada.get_nome()}")
        yield Label(cacador.icone, id="cacador")
        yield Footer(show_command_palette=False)

    def abrir_inventario(self):
        if inventario_aberto:
            self.query_one("#inventario", Container).remove()
            inventario_aberto = False
        else:
            self.mount(Container(id="inventario"))
            for item in cacador.inventario.values():
                self.query_one("#inventario").mount(Static(
                    f"{item.get_icon()}   - {item.get_nome().capitalize()}", classes="item_inventario"))
            inventario_aberto = True

    @work
    async def acoes(self, evento):
        match evento.key:
            case "z":
                if objeto_iteracao != "":
                    pode_movimentar = False
                    match objeto_iteracao:
                        case "zumbi":
                            if cacador.item_equipado:
                                if cacador.item_equipado.get_categoria() == "arma":
                                    await sleep(2)
                                    self.notify(
                                        "Entrando em combate com o zumbi")
                                    self.combate()
                                else:
                                    self.notify(
                                        "Você precisa de uma arma para iniciar o combate")
                            else:
                                self.notify(
                                    "Você precisa de um item equipado para iniciar o combate")

                        case "porta":
                            if cacador.item_equipado:
                                if cacador.item_equipado.get_nome() == "chave":
                                    self.app.switch_screen("tela_loja")
                                else:
                                    self.notify(
                                        "Você precisa da chave para abrir a porta")
                            else:
                                self.notify(
                                    "Você precisa de um item equipado para abrir a porta")

                        case "chave" | "espada":
                            if pode_agir:
                                self.notify(
                                    f"{objeto_iteracao.capitalize()} coletada")
                                cacador.coletar_item(objeto_iteracao)
                                contador = len(list(cacador.inventario.keys())) - 1
                                self.atualizar_header()
                                self.query_one(
                                    f"#{objeto_iteracao}").remove()
                    pode_movimentar = True

            case "x":
                if cacador.inventario:
                    lista_items = list(cacador.inventario.keys())
                    cacador.equipar_item(lista_items[contador])
                    self.atualizar_header()
                    self.notify(
                        f"Item equipado: {cacador.item_equipado.get_nome()}")
                    contador -= 1
                    if contador < 0:
                        contador = len(lista_items) - 1
                else:
                    self.notify("Inventário vazio")

            case "c":
                self.abrir_inventario()

    @work
    async def combate(self):
        # Fazer a classe do personagem com vida e dano. Implementar o dano da arma equipada e etc.
        self.notify(f"Dano {cacador.item_equipado.get_dano()} no zumbi")
        await sleep(2)
        self.notify("Dano 5 no caçador")
        cacador.vida -= 5
        await sleep(2)
        self.notify(f"Dano {cacador.item_equipado.get_dano()} no zumbi")
        await sleep(2)
        self.notify("Zumbi morreu")
        await self.query("#zumbi").remove()
        pode_movimentar = True
        zumbi_morto = True
        self.atualizar_header()

    @work
    async def _on_key(self, evento: Key):
        objeto_iteracao = ""
        pode_agir = False
        lbl = self.query_one("#cacador")
        self.acoes(evento)

        if pode_movimentar:
            self.screen.app.movimentacao(evento, lbl, cacador_padding)

        for lbl in self.query("Label"):
            match lbl.id:
                case "zumbi":
                    if "chave" not in cacador.inventario:
                        if cacador_padding == [0, 0, 0, 62]:
                            self.notify("Zumbi encontrado")
                            pode_agir = True
                            objeto_iteracao = "zumbi"
                    else:
                        if cacador_padding == [0, 0, 0, 41]:
                            self.notify("Zumbi encontrado")
                            pode_agir = True
                            objeto_iteracao = "zumbi"

                case "chave":
                    if cacador_padding == [0, 0, 0, 20]:
                        objeto_iteracao = "chave"
                        pode_agir = True
                        self.notify("Chave encontrada")

                case "espada":
                    if "chave" not in cacador.inventario:
                        if cacador_padding == [0, 0, 0, 142]:
                            self.notify("Espada encontrada")
                            pode_agir = True
                            objeto_iteracao = "espada"
                    else:
                        if cacador_padding == [0, 0, 0, 123]:
                            self.notify("Espada encontrada")
                            pode_agir = True
                            objeto_iteracao = "espada"

        if zumbi_morto == False and "chave" not in cacador.inventario:
            if cacador_padding == [0, 0, 0, 114]:
                objeto_iteracao = "porta"
                pode_agir = True
                self.notify("Porta encontrada")
        elif zumbi_morto == True and "chave" in cacador.inventario:
            if cacador_padding == [0, 0, 0, 49]:
                objeto_iteracao = "porta"
                pode_agir = True
                self.notify("Porta encontrada")
        elif zumbi_morto == True:
            if cacador_padding == [0, 0, 0, 72]:
                objeto_iteracao = "porta"
                pode_agir = True
                self.notify("Porta encontrada")
        elif "chave" in cacador.inventario:
            if cacador_padding == [0, 0, 0, 92]:
                objeto_iteracao = "porta"
                pode_agir = True
                self.notify("Porta encontrada")
