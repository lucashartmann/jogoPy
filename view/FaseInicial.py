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
from models import Init


class FaseInicial(Screen):
    CSS_PATH = "css/FaseInicial.tcss"

    def on_mount(self):
        Init.lbl_cacador = self.query_one("#cacador")
        self.atualizar_header()

    def atualizar_header(self):
        self.query_one(Header).icon = f"❤️: {Init.cacador.vida}"
        if Init.cacador.item_equipado:
            self.title = f"Item equipado: {Init.cacador.item_equipado.get_icon()}  {Init.cacador.item_equipado.get_nome().capitalize()}"
        else:
            self.title = f"Item equipado: Nenhum"

    def compose(self):
        yield Header(show_clock=False)
        with HorizontalGroup():
            yield Label(Init.chave.get_icon(), id=f"{Init.chave.get_nome()}")
            yield Label("🧟", id="zumbi")
            yield Label("🚪", id="porta")
            yield Label(Init.espada.get_icon(), id=f"{Init.espada.get_nome()}")
        yield Label(Init.cacador.icone, id="cacador")
        yield Footer(show_command_palette=False)


    @work
    async def acoes(self, evento):
        match evento.key:
            case "z":
                if Init.objeto_iteracao != "":
                    Init.pode_movimentar = False
                    match Init.objeto_iteracao:
                        case "zumbi":
                            if Init.cacador.item_equipado:
                                if Init.cacador.item_equipado.get_categoria() == "arma":
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
                            if Init.cacador.item_equipado:
                                if Init.cacador.item_equipado.get_nome() == "chave":
                                    self.app.switch_screen("tela_loja")
                                else:
                                    self.notify(
                                        "Você precisa da chave para abrir a porta")
                            else:
                                self.notify(
                                    "Você precisa de um item equipado para abrir a porta")

                        case "chave" | "espada":
                            if Init.pode_agir:
                                self.notify(
                                    f"{Init.objeto_iteracao.capitalize()} coletada")
                                Init.cacador.coletar_item(Init.objeto_iteracao)
                                Init.contador = len(
                                    list(Init.cacador.inventario.keys())) - 1
                                self.atualizar_header()
                                self.query_one(
                                    f"#{Init.objeto_iteracao}").remove()
                    Init.pode_movimentar = True

           

    @work
    async def combate(self):
        # Fazer a classe do personagem com vida e dano. Implementar o dano da arma equipada e etc.
        self.notify(f"Dano {Init.cacador.item_equipado.get_dano()} no zumbi")
        await sleep(2)
        self.notify("Dano 5 no caçador")
        Init.cacador.vida -= 5
        await sleep(2)
        self.notify(f"Dano {Init.cacador.item_equipado.get_dano()} no zumbi")
        await sleep(2)
        self.notify("Zumbi morreu")
        await self.query("#zumbi").remove()
        Init.pode_movimentar = True
        Init.zumbi_morto = True
        self.atualizar_header()

    @work
    async def _on_key(self, evento: Key):
        Init.objeto_iteracao = ""
        Init.pode_agir = False
        lbl = self.query_one("#cacador")
        self.acoes(evento)

        # if Init.pode_movimentar:
        #     self.screen.app.movimentacao(evento, lbl, Init.cacador_padding)

        for lbl in self.query("Label"):
            match lbl.id:
                case "zumbi":
                    if "chave" not in Init.cacador.inventario:
                        if Init.cacador_padding == [0, 0, 0, 62]:
                            self.notify("Zumbi encontrado")
                            Init.pode_agir = True
                            Init.objeto_iteracao = "zumbi"
                    else:
                        if Init.cacador_padding == [0, 0, 0, 41]:
                            self.notify("Zumbi encontrado")
                            Init.pode_agir = True
                            Init.objeto_iteracao = "zumbi"

                case "chave":
                    if Init.cacador_padding == [0, 0, 0, 20]:
                        Init.objeto_iteracao = "chave"
                        Init.pode_agir = True
                        self.notify("Chave encontrada")

                case "espada":
                    if "chave" not in Init.cacador.inventario:
                        if Init.cacador_padding == [0, 0, 0, 142]:
                            self.notify("Espada encontrada")
                            Init.pode_agir = True
                            Init.objeto_iteracao = "espada"
                    else:
                        if Init.cacador_padding == [0, 0, 0, 123]:
                            self.notify("Espada encontrada")
                            Init.pode_agir = True
                            Init.objeto_iteracao = "espada"

        if Init.zumbi_morto == False and "chave" not in Init.cacador.inventario:
            if Init.cacador_padding == [0, 0, 0, 114]:
                Init.objeto_iteracao = "porta"
                Init.pode_agir = True
                self.notify("Porta encontrada")
        elif Init.zumbi_morto == True and "chave" in Init.cacador.inventario:
            if Init.cacador_padding == [0, 0, 0, 49]:
                Init.objeto_iteracao = "porta"
                Init.pode_agir = True
                self.notify("Porta encontrada")
        elif Init.zumbi_morto == True:
            if Init.cacador_padding == [0, 0, 0, 72]:
                Init.objeto_iteracao = "porta"
                Init.pode_agir = True
                self.notify("Porta encontrada")
        elif "chave" in Init.cacador.inventario:
            if Init.cacador_padding == [0, 0, 0, 92]:
                Init.objeto_iteracao = "porta"
                Init.pode_agir = True
                self.notify("Porta encontrada")
