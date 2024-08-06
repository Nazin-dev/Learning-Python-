import os
lista_de_compras = []


while True:
  # Mostra a lista de comandos e perguta qual o usuario escolhe
  print('Selecione uma opção')
  opcao = input('[i]Inserir [a]Apagar [l]Listar: ').lower()
  os.system('cls')  
  # Se digitar qualquer coisa fora de 'ial' imprimira um erro  
  if opcao in 'ial':
    
    if opcao == 'i':
      os.system('cls') # Limpa sempre o terminal
      inserir = input('O que você quer inserir na lista? ')
      lista_de_compras.append(inserir)
      for indice, nome in enumerate(lista_de_compras):
        print(indice, nome) 
      
    elif opcao == 'a':
      os.system('cls') 
      for indice, nome in enumerate(lista_de_compras):
        print(indice, nome)
         
      apagar = input('Escolha o indice de qual item quer apagar: ')
      
      try:
        apagar = int(apagar)
        del lista_de_compras[apagar]
        
      except ValueError:
        print('Digite um numero inteiro.')
        
      except IndexError:
        print('Digite um indice valido.')
        
       
    elif opcao == 'l':
      os.system('cls') 
      
      if len(lista_de_compras) > 0:
        for indice, nome in enumerate(lista_de_compras):
          print(indice, nome)
          
      else:
        print('Você não adcionou nada a sua lista!')
        
  else:
    print('Você não digitou um valor valido!') 