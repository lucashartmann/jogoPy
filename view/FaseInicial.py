from textual.app import App
from textual.widgets import Label, Static, Footer, Header
from textual.containers import HorizontalGroup, Container
from textual.events import Key
from asyncio import sleep
from textual import work
from models.Personagem import Personagem
from textual.screen import Screen
from textual.binding import Binding
from view.TelaLoja import TelaLoja, Loja
from models.Item import Item
from models.Cena import Cena


class FaseInicial(Screen):
    CSS_PATH = "css/FaseInicial.tcss"

    sala_inicial = Cena("Sala Inicial")

    cacador = Personagem()
    cacador.sala = sala_inicial

    chave = Item()
    chave.set_nome("chave")
    chave.set_categoria("item_comum")
    chave.set_icon("🗝️")
    chave.set_dano(0)
    chave.set_protecao(0)
    chave.set_genero_objeto("feminino")
    chave.set_quant(1)

    sala_inicial.colocar_item(chave)

    espada = Item()
    espada.set_nome("espada")
    espada.set_categoria("arma")
    espada.set_icon("🗡️")
    espada.set_dano(5)
    espada.set_protecao(0)
    espada.set_genero_objeto("feminino")
    espada.set_quant(1)

    sala_inicial.colocar_item(espada)

    cacador_padding = [0, 0, 0, 0]

    zumbi_morto = False
    pode_movimentar = True
    pode_agir = False
    objeto_iteracao = ""
    inventario_aberto = False
    contador = len(list(cacador.inventario.keys())) - 1

    def on_mount(self):
        self.atualizar_header()

    def atualizar_header(self):
        self.query_one(Header).icon = f"❤️: {self.cacador.vida}"
        if self.cacador.item_equipado:
            self.title = f"Item equipado: {self.cacador.item_equipado.get_icon()}  {self.cacador.item_equipado.get_nome().capitalize()}"
        else:
            self.title = f"Item equipado: Nenhum"

    def compose(self):
        yield Header(show_clock=False)
        with HorizontalGroup():
            yield Label(self.chave.get_icon(), id=f"{self.chave.get_nome()}")
            yield Label("🧟", id="zumbi")
            yield Label("🚪", id="porta")
            yield Label(self.espada.get_icon(), id=f"{self.espada.get_nome()}")
        yield Label("👮", id="cacador")
        yield Footer(show_command_palette=False)

    def abrir_inventario(self):
        if self.inventario_aberto:
            self.query_one("#inventario", Container).remove()
            self.inventario_aberto = False
        else:
            self.mount(Container(id="inventario"))
            for item in self.cacador.inventario.values():
                self.query_one("#inventario").mount(Static(
                    f"{item.get_icon()}   - {item.get_nome().capitalize()}", classes="item_inventario"))
            self.inventario_aberto = True

    @work
    async def acoes(self, evento):
        match evento.key:
            case "z":
                if self.objeto_iteracao != "":
                    self.pode_movimentar = False
                    match self.objeto_iteracao:
                        case "zumbi":
                            if self.cacador.item_equipado:
                                if self.cacador.item_equipado.get_categoria() == "arma":
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
                            if self.cacador.item_equipado:
                                if self.cacador.item_equipado.get_nome() == "chave":
                                    self.app.switch_screen("tela_loja")
                                else:
                                    self.notify(
                                        "Você precisa da chave para abrir a porta")
                            else:
                                self.notify(
                                    "Você precisa de um item equipado para abrir a porta")

                        case "chave" | "espada":
                            if self.pode_agir:
                                self.notify(
                                    f"{self.objeto_iteracao.capitalize()} coletada")
                                self.cacador.coletar_item(self.objeto_iteracao)
                                self.contador = len(list(self.cacador.inventario.keys())) - 1
                                self.atualizar_header()
                                self.query_one(
                                    f"#{self.objeto_iteracao}").remove()
                    self.pode_movimentar = True

            case "x":
                if self.cacador.inventario:
                    lista_items = list(self.cacador.inventario.keys())
                    self.cacador.equipar_item(lista_items[self.contador])
                    self.atualizar_header()
                    self.notify(
                        f"Item equipado: {self.cacador.item_equipado.get_nome()}")
                    self.contador -= 1
                    if self.contador < 0:
                        self.contador = len(lista_items) - 1
                else:
                    self.notify("Inventário vazio")

            case "c":
                self.abrir_inventario()

    @work
    async def combate(self):
        # Fazer a classe do personagem com vida e dano. Implementar o dano da arma equipada e etc.
        self.notify(f"Dano {self.cacador.item_equipado.get_dano()} no zumbi")
        await sleep(2)
        self.notify("Dano 5 no caçador")
        self.cacador.vida -= 5
        await sleep(2)
        self.notify(f"Dano {self.cacador.item_equipado.get_dano()} no zumbi")
        await sleep(2)
        self.notify("Zumbi morreu")
        await self.query("#zumbi").remove()
        self.pode_movimentar = True
        self.zumbi_morto = True
        self.atualizar_header()

    @work
    async def _on_key(self, evento: Key):
        self.objeto_iteracao = ""
        self.pode_agir = False
        lbl = self.query_one("#cacador")
        self.acoes(evento)

        if self.pode_movimentar:
            self.screen.app.movimentacao(evento, lbl, self.cacador_padding)

        for lbl in self.query("Label"):
            match lbl.id:
                case "zumbi":
                    if "chave" not in self.cacador.inventario:
                        if self.cacador_padding == [0, 0, 0, 62]:
                            self.notify("Zumbi encontrado")
                            self.pode_agir = True
                            self.objeto_iteracao = "zumbi"
                    else:
                        if self.cacador_padding == [0, 0, 0, 41]:
                            self.notify("Zumbi encontrado")
                            self.pode_agir = True
                            self.objeto_iteracao = "zumbi"

                case "chave":
                    if self.cacador_padding == [0, 0, 0, 20]:
                        self.objeto_iteracao = "chave"
                        self.pode_agir = True
                        self.notify("Chave encontrada")

                case "espada":
                    if "chave" not in self.cacador.inventario:
                        if self.cacador_padding == [0, 0, 0, 142]:
                            self.notify("Espada encontrada")
                            self.pode_agir = True
                            self.objeto_iteracao = "espada"
                    else:
                        if self.cacador_padding == [0, 0, 0, 123]:
                            self.notify("Espada encontrada")
                            self.pode_agir = True
                            self.objeto_iteracao = "espada"

        if self.zumbi_morto == False and "chave" not in self.cacador.inventario:
            if self.cacador_padding == [0, 0, 0, 114]:
                self.objeto_iteracao = "porta"
                self.pode_agir = True
                self.notify("Porta encontrada")
        elif self.zumbi_morto == True and "chave" in self.cacador.inventario:
            if self.cacador_padding == [0, 0, 0, 49]:
                self.objeto_iteracao = "porta"
                self.pode_agir = True
                self.notify("Porta encontrada")
        elif self.zumbi_morto == True:
            if self.cacador_padding == [0, 0, 0, 72]:
                self.objeto_iteracao = "porta"
                self.pode_agir = True
                self.notify("Porta encontrada")
        elif "chave" in self.cacador.inventario:
            if self.cacador_padding == [0, 0, 0, 92]:
                self.objeto_iteracao = "porta"
                self.pode_agir = True
                self.notify("Porta encontrada")
