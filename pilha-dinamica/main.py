import PilhaD

pilhaD = PilhaD.PilhaD()

pilhaD.push('a')
pilhaD.push('b')
pilhaD.push('c')

pilhaD.imprimir()

pilhaD.pop()
pilhaD.imprimir()

pilhaD.push('d')
pilhaD.imprimir()

pilhaD.push('e')
pilhaD.imprimir()

print('Pilha está vazia:', pilhaD.estaVazia())

pilhaD.push('f')
pilhaD.imprimir()

print('Topo da pilha:', pilhaD.getTopo())
