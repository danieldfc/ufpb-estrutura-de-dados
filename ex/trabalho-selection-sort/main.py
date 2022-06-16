import random
import SelectionSort

select = SelectionSort.SelectionSort()
elementos = random.sample(range(1, 20), 5)

print('Elementos:', elementos)
print('SelectionSort: ', select.sort(elementos))
