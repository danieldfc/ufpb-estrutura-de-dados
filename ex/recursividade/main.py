print('--- Exercícios ---')
print('--- EX 1 ---')

def exp(num: int, expoente: int) -> int:
  if expoente == 0:
    return 1
  return num * exp(num, expoente - 1)

print('5^4=', exp(5, 5))

print('--- EX 2 ---')

def mult(firstFactor: int, secondFactor: int) -> int:
  if firstFactor == 0:
    return 0
  return secondFactor + mult(firstFactor - 1, secondFactor)

print('5x7=', mult(5, 9))

print('--- EX 3 ---')

def fib(index: int) -> int:
  if index == 0:
    return 0
  elif index == 1:
    return 1
  return fib(index - 1) + fib(index - 2)

print('f(8)=', fib(8))
