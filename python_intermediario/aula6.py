# Closure - Python
def mult(x):
  def result(y):
    resultado = x * y
    return resultado
  return result

duplicar = mult(2)
triplicar = mult(2)
quadriplicar = mult(2)


print(duplicar(2))
print(triplicar(3))
print(quadriplicar(4))