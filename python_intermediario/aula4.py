def paridade(a):
  if a % 2 == 0:
    print('Seu numero é par!')
  else:
    print('Seu numero é impar!')
  return
numero = input('Digite um numero: ')
numero = int(numero)

paridade(numero)