import Les

lista = Les.Les()

if not (lista.estaCheia()):
    lista.inserirFim(1)
if not (lista.estaCheia()):
    lista.inserirFim(2)
if not (lista.estaCheia()):
    lista.inserirFim(3)
if not (lista.estaCheia()):
    lista.inserirFim(4)
if not (lista.estaCheia()):
    lista.inserirFim(1)
if not (lista.estaCheia()):
    lista.inserirFim(6)
print('Lista com insercao dos elementos 1, 2, 3, 4 e 5 no fim da lista e tentativa do 6')
lista.imprimir()
('\n'
 'if not (lista.estaVazia()):\n'
 '    lista.removerFim()\n'
 'if not (lista.estaVazia()):\n'
 '    lista.removerFim()\n'
 'if not (lista.estaVazia()):\n'
 '    lista.removerFim()\n'
 'print(\'Lista com remocao dos 3 ultimos elementos da lista\')\n'
 'lista.imprimir()\n'
 '\n'
 'print(\'Quantidade de elementos da lista: \', lista.getQuant())\n'
 '\n'
 'if not (lista.estaCheia()):\n'
 '    lista.inserirInicio(0)\n'
 'if not (lista.estaCheia()):\n'
 '    lista.inserirInicio(-1)\n'
 '\n'
 'print(\'Lista com insercao dos elementos -1, 0, 1, e 2\')\n'
 'lista.imprimir()\n'
 '\n'
 'if not (lista.estaVazia()):\n'
 '    lista.removerInicio()\n'
 'lista.imprimir()\n'
 'if not (lista.estaVazia()):\n'
 '    lista.removerInicio()\n'
 'lista.imprimir()\n'
 '\n'
 'print(\'Posicao do elemento 4: \', lista.consultarElemento(4))\n'
 'print(\'Posicao do elemento 6: \', lista.consultarElemento(6))\n'
 'lista.removerFim()\n'
 'print(\'Primeiro elemento da lista\', lista.getPrim())\n'
 'print(\'Ultimo elemento da lista\', lista.getUlt())\n')

print('Quantidade de elementos 1 na lista', lista.contarQtdOcorrencias(1))
print('Soma dos elementos da lista', lista.somaElementos())

lista.substituirTodasOcorrencias(1, 2)
lista.imprimir()