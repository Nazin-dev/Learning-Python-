""" 
Calculadora com while
Pedir o primeiro e segundo numero para o usuario.
Pedir um operador: +, -, *
E mostrar resultado na tela, no final perguntar se quer continuar
"""

while True:
  
  # Se digitar algo que não seja um  nuemro redireciona para o except.
  try:
    primeiro_numero = input('Digite o primeiro  numero: ') 
    primeiro_numero = float(primeiro_numero) # Converte a str para float
    segundo_numero = input('Digite o segundo numero: ')
    segundo_numero = float(segundo_numero) # Converte a str para float
  except:
    print('Você não digitou um numero!') # Informa que digitou algo errado
    continue # Começa o loop novamente
  
  print('Digite um operador: ') # Escolha o operador 
  print('[1] +')
  print('[2] -')
  print('[3] *')
  operador = input()
  
  resultado = 0
  
  if operador == '1':
    resultado = primeiro_numero + segundo_numero
    print(f'O resultado do calculo é [{resultado:.2f}]!')
  elif operador == '2':
    resultado = primeiro_numero - segundo_numero
    print(f'O resultado do calculo é [{resultado:.2f}]!')
  elif operador == '3':
    resultado = primeiro_numero * segundo_numero
    print(f'O resultado do calculo é [{resultado:.2f}]!')
  else:
    print('Você não digitou um numero correspodente!')
    # Digitar qualquer coisa que não seja 1, 2 e 3 traz para cá!
    
  sair = input('Quer sair? [s]im: ').lower().startswith('s')
  
  if sair is True:
    break