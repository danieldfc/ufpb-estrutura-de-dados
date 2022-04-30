def fatorial(num: int) -> int:
  if num == 0 or num == 1:
    return 1
  return num * fatorial(num - 1)

print("Fatorial do número 10 é: ", fatorial(10))
