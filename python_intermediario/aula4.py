def par_imp(a):
  if a % 2 == 0:
    return f'{a} é par!'
  return f'{a} é impar!'

numero = input('Digite um numero: ')
numero = int(numero)
print(par_imp(numero))