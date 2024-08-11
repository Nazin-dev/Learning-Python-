while True:
  codigo = input('Digite o codigo aqui: ')
  codigo_format = codigo.split(' ')
  for cod in codigo_format:
    if cod != '':
      print(cod)
  print('-'*30)
  
