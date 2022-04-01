class No:
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo

class Ldde:
    def __init__(self):
          self.prim = self.ult = None
          self.quant = 0

    def estaVazia(self):
        return self.quant == 0

    def getPrimeiro(self):
         return self.prim.info

    def getUltimo(self):
        return self.ult.info

    def getQuant(self):
         return self.quant

    def inserirInicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.prim.ant = self.prim = No(None, valor, self.prim)
        self.quant += 1

    def inserirFim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, None)
        self.quant += 1

    def removerInicio(self):
        if self.quant == 1:
           self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.prim.ant = None
        self.quant -= 1

    def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.ult = self.ult.ant
            self.ult.prox = None
        self.quant -= 1

    def imprimir(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end=' ')
            aux = aux.prox
        print()
        return ' '

    def imprimirReverso(self):
        aux = self.ult
        while aux != None:
            print(aux.info, end=' ')
            aux = aux.ant
        print()
