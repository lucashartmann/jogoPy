import random
from models import Item


class Bau:

    def __init__(self):
        self.itens_no_bau = []
        self.capacidade = 10
        self.init()

    def init(self):
        quant_itens_no_bau = int(random.randrange(0, self.capacidade))
        for i in range(quant_itens_no_bau):
            item = Item.Item()
            quant_certo_item = int(random.randrange(1, 10))
            if item not in self.itens_no_bau:
                item.set_quant(quant_certo_item)
                self.itens_no_bau.append(item)
                i += 1

    def guardar(self, item, quant):
        if len(self.itens_no_bau) < 10:
            item.set_quant(item.get_quant() - quant)
            if item in self.itens_no_bau:
                item.set_quant(item.get_quant() + quant)
                return True
            else:
                self.itens_no_bau.append(item)
                return True
        return False

    def get_item(self, nome, quant):
        for item in self.itens_no_bau:
            if nome in item.get_nome():
                if quant > item.get_quant():
                    return None
                elif quant == item.get_quant():
                    self.itens_no_bau.remove(item)
                else:
                    item.set_quant(item.get_quant() - quant)
                return item
        return None

    def get_itens_no_bau(self):
        return self.itens_no_bau

    def __str__(self):
        return f"###ITENS NO BAÚ#### \n{"\n".join(str(item) for item in self.get_itens_no_bau())}"
