class Tabuleiro:
    def __init__(self, linhas, colunas):
        self.tabuleiro = Tabuleiro.gerar_tabuleiro(self, linhas, colunas)
        self.num_linhas = linhas
        self.num_colunas = colunas

    def gerar_tabuleiro(self, linhas, colunas):
        tabuleiro = []
        for numero_linha in range(linhas):
            l = ['[ ]' for i in range(colunas)]
            tabuleiro.append(l)
        return tabuleiro

    def posicionar_peca(self, peca, linha, coluna):
        self.tabuleiro[linha-1][coluna-1] = f"[{peca}]"
        return True

    def mover_peca(self, origem, destino):
        peca = self.get_peca(origem[0], origem[1])
        peca = peca[1]
        self.posicionar_peca(" ", origem[0], origem[1])
        self.posicionar_peca(peca, destino[0], destino[1])

    def get_peca(self, linha, coluna):
        posicao = self.tabuleiro[linha-1][coluna-1]
        if posicao:
            return posicao
        return None

    def imprimir_tabuleiro(self):
        print("   ", end="")
        for num_coluna in range(1, self.num_colunas+1):
            print(f" {num_coluna}  ", end="")
        print()
        for num_linha, linha in enumerate(self.tabuleiro):
            print(num_linha+1, end=": ")
            for valor in linha:
                print(valor, end=" ")
            print()
