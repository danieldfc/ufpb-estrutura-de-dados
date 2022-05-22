import Tree

t1 = Tree.Tree()

t1.insere(4)
t1.insere(2)
t1.insere(1)
t1.insere(5)
t1.insere(8)
t1.insere(6)
t1.insere(10)
t1.insere(3)
t1.insere(4.4)
t1.insere(4.6)

#print('Busca do numero 5: ', t1.busca(5))
#print('Busca do numero 3: ', t1.busca(3))
#print('Busca do numero 7: ', t1.busca(7))

#t1.imprimeNoFolha()
#print(t1.estritamenteBinario())
print('nivel de 13', t1.nivelMaisCompleto(13))
