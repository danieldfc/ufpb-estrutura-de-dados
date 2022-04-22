import PilhaE

pilhaE = PilhaE.PilhaE()

pilhaE.push('a')
pilhaE.push('b')
pilhaE.push('c')

print('Pilha com inserção dos elementos a, b, c')
pilhaE.imprimir()

pilhaE.pop()

print('Pilha com remoção do elemento c')
pilhaE.imprimir()

pilhaE.push('c')
pilhaE.push('d')

print('Pilha com inserção dos elementos c, d')
pilhaE.imprimir()

print('Topo da Pilha, deve ser o d')
print(pilhaE.getTopo())

pilhaE.pop()
pilhaE.pop()
pilhaE.pop()
pilhaE.pop()
pilhaE.pop()
pilhaE.pop()
pilhaE.pop()

print('Topo da Pilha, deve ser o d')
print(pilhaE.getTopo())

