class No:
  def __init__(self, info, proximo):
    self.info = info
    self.prox = proximo


class PilhaD:
  def __init__(self):
    self.prim = self.ult = None
    self.quant = 0

  def getTopo(self):
    if not self.estaVazia():
      return self.prim.info

  def estaVazia(self):
    return self.quant == 0

  def push(self, valor):
    if self.quant == 0:
      self.prim = self.ult = No(valor, None)
    else:
      self.prim = No(valor, self.prim)
    self.quant += 1

  def pop(self):
    if self.quant == 1:
      self.prim = self.ult = None
    else:
      self.prim = self.prim.prox
    self.quant -= 1

  def imprimir(self):
    aux = self.prim
    while aux!= None:
      print(aux.info, end=' ')
      aux = aux.prox
    print()
