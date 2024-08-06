"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um numero inteiro: ')

try:
  
  num = int(num)
  
  if num % 2 == 0:
    print(f'Numero {num} é Par!')
    
  elif num % 2 == 1:
    print(f'Numero {num} é impar')
    
except:
  print('Não é um numero inteiro!')
 
