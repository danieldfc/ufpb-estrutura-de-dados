import Ldde

lista = Ldde.Ldde()

print('lista b c d: ')
lista.inserirInicio('d')
lista.inserirInicio('c')
lista.inserirInicio('b')
lista.imprimir()


print('lista a b c d e f: ')
lista.inserirFim('e')
lista.inserirInicio('a')
lista.inserirFim('f')
lista.imprimir()

print('lista aa b c d e: ')
lista.removerInicio()
lista.inserirInicio('aa')
lista.removerFim()
lista.imprimir()

lista.imprimirReverso()
