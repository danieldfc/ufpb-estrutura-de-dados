class PilhaE():
  def __init__(self):
    self.vetor = [None, None, None, None, None]
    self.quant = 0

  def getTopo(self):
    return self.vetor[self.quant-1]

  def estaVazia(self):
    return self.quant == 0

  def estaCheia(self):
    return self.quant == 5

  def push(self, valor):
    if not self.estaCheia():
      self.vetor[self.quant] = valor
      self.quant += 1

  def pop(self):
    if not self.estaVazia():
      self.quant -= 1

  def imprimir(self):
    for i in range(self.quant):
      print(self.vetor[i], end=' ')
    print()
