class Len():
  def __init__(self):
    self.vetor = [None, None, None, None, None]
    self.quant = 0

  def inserirFim(self, valor):
    self.vetor[self.quant] = valor
    self.quant += 1

  # def __str__(self):
  #   valores = ''

  #   for idx in range(self.quant):
  #     if self.vetor[idx] != None:
  #       if idx == 0:
  #         valores += str(self.vetor[idx])
  #       else:
  #         if idx > 0 and (idx+1) < self.quant: valores += ', '
  #         elif (idx+1) == self.quant: valores += ' e '
  #         valores += str(self.vetor[idx])

  #   return "Valores da lista: " + valores

  def __str__(self):
    return 'Minha saída em string'


lista = Len()

lista.inserirFim(4)
lista.inserirFim(6)
lista.inserirFim(7)

print(lista)