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

    def on_screen_resume(self):
        Init.lbl_cacador = self.query_one("#cacador")
        Init.cacador_padding = [0, 0, 0, 0]

    def on_mount(self):
        self.app.atualizar_header()

    def compose(self):
        yield Header(show_clock=False)
        with HorizontalGroup():
            yield Label(Init.chave.get_icon(), id=f"{Init.chave.get_nome()}")
            yield Label('🧟', id="zumbi")
#             yield Label('''10
#   🧟''', id="zumbi")
            yield Label("🚪", id="porta")
            yield Label(Init.espada.get_icon(), id=f"{Init.espada.get_nome()}")
        yield Label(Init.cacador.icone, id="cacador")
        yield Footer(show_command_palette=False)

    @work
    async def acoes(self, evento):
        if evento.key == "z" and Init.objeto_iteracao != "":
            Init.pode_movimentar = False
            match Init.objeto_iteracao:
                case "zumbi":
                    if Init.cacador.item_equipado:
                        if Init.cacador.item_equipado.get_categoria() == "arma":
                            self.notify(
                                "Entrando em combate com o zumbi")
                            await sleep(1)
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
                        self.query_one(
                            f"#{Init.objeto_iteracao}").remove()
            Init.pode_movimentar = True

    @work
    async def combate(self):
        vida_zumbi = 10
        Init.cacador.set_vida(2)

        dano_arma = Init.cacador.item_equipado.get_dano()

        while vida_zumbi > 0 and Init.cacador.get_vida() > 0:
            vida_zumbi -= dano_arma
            self.notify(
                f"Dano {dano_arma} no zumbi, Vida do Zumbi = {vida_zumbi}")
            await sleep(2)
            self.notify("Dano 5 no caçador")
            self.app.atualizar_header()
            Init.cacador.set_vida(Init.cacador.get_vida() - 5)
            if vida_zumbi <= 0:
                self.notify("Zumbi morreu")
                await self.query("#zumbi").remove()
                Init.zumbi_morto = True
            if Init.cacador.get_vida() <= 0:
                self.app.tela_morte()
                Init.pode_agir = False
                Init.pode_movimentar = False

    @work
    async def _on_key(self, evento: Key):
        Init.objeto_iteracao = ""
        Init.pode_agir = False
        lbl = self.query_one("#cacador")
        self.acoes(evento)

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
