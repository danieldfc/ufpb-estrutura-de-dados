import No

class Ldse:
  def __init__(self):
    self.first = self.last = None
    self.quant = 0


  def estaVazia(self):
    return self.quant == 0


  def inserirInicio(self, valor):
    if self.quant == 0:
      self.first = self.last = No.No(valor, None)
    else:
      self.first = No.No(valor, self.first)
    self.quant += 1


  def removerInicio(self):
    if not self.estaVazia():
      if self.quant == 1:
        self.first = self.last = None
      else:
        self.first = self.first.proximo
      self.quant -= 1


  def removerFim(self):
    if not self.estaVazia():
      aux = self.first
      while aux != self.last:
        if aux.proximo == self.last:
          break
        aux = aux.proximo
      self.last = aux
      self.last.proximo = None
      self.quant -= 1


  def removerElemento(self, elemento):
    if not self.estaVazia():
      anterior = self.first
      proximo = self.first.proximo
      encontrado = False
      primeiro = False

      while not encontrado:
        if self.first == anterior and anterior.info == elemento:
          self.removerInicio()
          encontrado = True
          primeiro = True
          break

        if proximo.info == elemento:
          anterior.proximo = proximo.proximo
          encontrado = True
          break

        if proximo.proximo == None:
          break

        anterior = proximo
        proximo = proximo.proximo

      if not primeiro:
        self.quant -= 1


  def removerElementoPosicao(self, posicao):
    if not self.estaVazia() and posicao + 1 <= self.quant:
      count = 0
      aux = self.first

      for i in range(self.quant):
        if posicao == count:
          self.removerElemento(aux.info)
          break
        aux = aux.proximo
        count += 1


  def inserirFim(self, valor):
    if self.estaVazia():
      self.first = self.last = No.No(valor, None)
    else:
      novoElemento = No.No(valor, None)
      if self.quant == 1:
        self.first.proximo = novoElemento
        self.last = novoElemento
      else:
        anterior = self.first
        proximo = self.first.proximo

        ultimoElemento = False

        while not ultimoElemento:
          if proximo.proximo == None:
            ultimoElemento = True
            break
          proximo = proximo.proximo

        proximo.proximo = novoElemento
        self.last = novoElemento

    self.quant += 1


  def getQuant(self):
    return self.quant


  def getFirstElement(self):
    if not self.estaVazia():
      return self.first.info


  def getLastElement(self):
    if not self.estaVazia():
      return self.last.info


  def imprimir(self):
    aux = self.first
    while aux != None:
      print(aux.info, end=' ')
      aux = aux.proximo
    print()
