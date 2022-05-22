import Tree

print('--- Exercícios ---')
print('--- EX 4 ---')

print(
  '''
  Primeiro arquivo Tree.py:
  Define uma função de busca de algum valor dentro da árvore,
  caso não tenha valor na árvore, é retornado valor: 0.
  '''
)

print('--- EX 5 ---')

tree = Tree.Tree()

tree.insere(3)
tree.insere(2)
tree.insere(1)
tree.insere(4)

print(
  '''
      3
    2   4
  1
  '''
)

print('1. Implementar um método para imprimir a soma de todos os nós da árvore')
print('Somatório: 3 + 2 + 1 + 4 =>', tree.sumNoValues())

print('\n2. Implementar um método para imprimir a soma de todos os nós-folha da árvore')
print('Somatório: 1 + 4 =>', tree.sumNoLeafValues())

print('\n3. Implementar um método para buscar o elemento mais à direita na árvore')
print('Busca elemento mais a direita =>', tree.maiorElemento())

print('\n4. Implementar um método para contar a quantidade nós pares da árvore')
print('Quantidade de Nós pares =>', tree.contarNoPares())

print('\n5. Implementar um método para encontrar à altura da árvore')
print('Altura da árvore =>', tree.buscaAltura())
