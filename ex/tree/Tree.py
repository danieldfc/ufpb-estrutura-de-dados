class Tree:
    def __init__(self):
        self.raiz = None

    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)

    def busca(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca(valor)

    def imprimirIn(self):
        if self.raiz != None:
            self.raiz.imprimirIn()

    def imprimirPre(self):
        if self.raiz != None:
            self.raiz.imprimirPre()

    def imprimirPos(self):
        if self.raiz != None:
            self.raiz.imprimirPos()

    def oqfaz(self, valor):
        if self.raiz == None:
            return 0
        else:
            return self.raiz.busca(valor)

    def nivelMaisCompleto(self, valor):
        if self.raiz != None:
            return self.raiz.nivelMaisCompleto(valor)

    def nivel(self, valor):
        if self.raiz != None:
            return self.raiz.nivel(valor)

    def imprimeNaoFolha(self):
        if self.raiz != None:
            self.raiz.imprimeNaoFolha()

    def imprimeNoFolha(self):
        if self.raiz != None:
            self.raiz.imprimeNoFolha()

    def estritamenteBinario(self):
        if self.raiz != None:
            return self.raiz.estritamenteBinario()

    def sumNoValues(self):
      if self.raiz == None:
        return 0
      else:
        return self.raiz.info + self.raiz.sumNoValues()

    def sumNoLeafValues(self):
      if self.raiz == None:
        return 0
      else:
        return self.raiz.sumNoLeafValues()

    def maiorElemento(self):
      if self.raiz == None:
        return 0
      else:
        return self.raiz.maiorElemento()

    def contarNoPares(self):
      if self.raiz == None:
        return 0
      else:
        return self.raiz.contarNoPares()

    def buscaAltura(self):
      if self.raiz == None:
        return 0
      else:
        return 1 + self.raiz.buscaAltura()

class No:
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None

    def insere(self, valor):
        if (valor < self.info):
            if self.esq == None:
                self.esq = No(valor)
            else:
                self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)
            else:
                self.dir.insere(valor)

    def busca(self, valor):
        if valor == self.info:
                return True
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.busca(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.busca(valor)

    def maiorElemento(self):
      if self.dir != None:
        return self.dir.maiorElemento()

      return self.info

    def buscaAltura(self):
      if self.esq == None and self.dir == None:
        return 0

      alturaElementoEsquerda = 0
      alturaElementoDireita = 0

      if self.esq != None:
        alturaElementoEsquerda += 1 + self.esq.buscaAltura()

      if self.dir != None:
        alturaElementoDireita += 1 + self.dir.buscaAltura()

      return max(alturaElementoDireita, alturaElementoEsquerda)

    def oqfaz(self, valor):
        if self.info == valor:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                aux = self.esq.oqfaz(valor)
                if aux == 0:
                    return 0
                else:
                    return aux + 1
        else:
            if self.dir == None:
                return 0
            else:
                aux = self.dir.oqfaz(valor)
                if aux == 0:
                    return 0
                else:
                    return aux + 1

    def imprimirIn(self):
        if self.esq != None:
           self.esq.imprimirIn()
        print(self.info)
        if self.dir != None:
           self.dir.imprimirIn()

    def imprimirPre(self):
        print(self.info)
        if self.esq != None:
           self.esq.imprimirPre()
        if self.dir != None:
           self.dir.imprimirPre()

    def imprimirPos(self):
        if self.esq != None:
           self.esq.imprimirPos()
        if self.dir != None:
           self.dir.imprimirPos()
        print(self.info)

    def nivelMaisCompleto(self, valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                aux = self.esq.nivelMaisCompleto(valor)
                if aux != 0:
                    return 1 + aux
                else:
                    return 0
        else:
            if self.dir == None:
                return 0
            else:
                aux = self.dir.nivelMaisCompleto(valor)
                if aux != 0:
                    return 1 + aux
                else:
                    return 0

    def nivel(self, valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                return self.esq.nivel(valor) + 1
        else:
            if self.dir == None:
                return 0
            else:
                return self.dir.nivel(valor) + 1

    def imprimeNaoFolha(self):
        if self.esq != None:
            self.esq.imprimeNaoFolha()

        if self.esq != None or self.dir != None:
            print(self.info)

        if self.dir != None:
            self.dir.imprimeNaoFolha()

    def imprimeNoFolha(self):
        if self.esq != None:
            self.esq.imprimeNoFolha()

        if self.esq == None and self.dir == None:
            print(self.info)

        if self.dir != None:
            self.dir.imprimeNoFolha()

    def estritamenteBinario(self):
        if self.esq != None and self.dir != None:
            return self.esq.estritamenteBinario() and self.dir.estritamenteBinario()
        elif self.esq == None and self.dir == None:
            return True
        else:
            return False

    def sumNoValues(self):
      soma = 0
      if self.esq != None:
        soma += self.esq.info + self.esq.sumNoValues()
      if self.dir != None:
        soma += self.dir.info + self.dir.sumNoValues()
      return soma

    def sumNoLeafValues(self):
      soma = 0
      if self.esq == None and self.dir == None:
        soma += self.info

      if self.esq != None:
        soma += self.esq.sumNoLeafValues()
      if self.dir != None:
        soma += self.dir.sumNoLeafValues()

      return soma

    def contarNoPares(self):
      count = 0

      if self.info % 2 == 0:
        count += 1

      if self.esq != None:
        count += self.esq.contarNoPares()

      if self.dir != None:
        count += self.dir.contarNoPares()

      return count
