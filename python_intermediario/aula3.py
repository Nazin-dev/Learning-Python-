def mult(*args):
  resultado = 1
  for i in args:
    resultado = resultado * i
  return resultado

print(mult(9, 2, 3))