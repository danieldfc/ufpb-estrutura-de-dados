class Les():
    def __init__(self):
        self.vetor = [None, None, None, None, None]
        self.quant = 0

    def getQuant(self):
        return self.quant

    def getPrim(self):
        return self.vetor[0]

    def getUlt(self):
        return self.vetor[self.quant-1]

    def estaVazia(self):
        return self.quant == 0

    def estaCheia(self):
        return self.quant == 5

    def imprimir(self):
        for i in range(self.quant):
            print(self.vetor[i], end=' ')
        print()

    def inserirFim(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1

    def inserirInicio(self, valor):
        for i in range(self.quant, 0, -1):
            self.vetor[i] = self.vetor[i-1]
        self.vetor[0] = valor
        self.quant += 1

    def removerFim(self):
       self.quant -= 1

    def removerInicio(self):
        for i in range(1, self.quant):
            self.vetor[i-1] = self.vetor[i]
        self.quant -= 1

    def removerPosicao(self, posicao):
        for i in range(posicao, self.quant - 1):
            self.vetor[i] = self.vetor[i + 1]
        self.vetor[self.quant - 1] = None
        self.quant -= 1

    def removerElemento(self, valor):
        index = self.consultarElemento(valor)
        if not (index is None):
            self.removerPosicao(index)

    def consultarElemento(self, valor):
        for i in range(self.quant):
            if self.vetor[i] == valor:
                return i


    def contarQtdOcorrencias(self, valor):
        quantElementos = 0
        for i in range(self.quant):
            if self.vetor[i] == valor:
                quantElementos += 1
        return quantElementos

    def somaElementos(self):
        soma = 0
        for i in range(self.quant):
            soma += self.vetor[i]
        return soma

    def substituirTodasOcorrencias(self, valor, novovalor):
        for i in range(self.quant):
            if self.vetor[i] == valor:
                self.vetor[i] = novovalor