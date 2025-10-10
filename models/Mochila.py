class Mochila:

    def __init__(self):
        self.mochila = []

    def get_mochila(self):
        return self.mochila

    def esvaziar(self):
        self.get_mochila().clear()

    def guardar(self, item):
        if len(self.mochila) < 10 and item not in self.mochila:
            self.mochila.append(item)
            return True
        return False

    def pegar(self, item, quant):
        if item in self.mochila and item.get_quant() >= quant:
            if item.get_quant() == quant:
                self.mochila.remove(item)
            else:
                item.set_quant((item.get_quant() - quant))

    def __str__(self):
        return f"Mochila [{" , ".join(str(item) for item in self.get_mochila())}"
