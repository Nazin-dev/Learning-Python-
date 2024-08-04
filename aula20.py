"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ')

tamanho_nome = len(nome)

curto = tamanho_nome <= 4

normal = tamanho_nome >= 5 and tamanho_nome <= 6

grande = tamanho_nome > 6

if tamanho_nome >= 1:
  if curto:
    print('Seu nome é curto')

  elif normal:
    print('Seu nome é normal')
    
  elif grande:
    print('Seu nome é grande')
else:
  print('Digite alguma coisa!')
  
 