lista = ['Maria', 'João', 'Pedro']

# enumerate serve para numerar a lista, colocando indices 
enumerate(lista)

for item in enumerate(lista):
  a, b = item # Estou usando o desempacotamento para pegar o indice do enumerate e o nome. 
  print(a, b)
  
# Forma simplificada de fazer a mesma coisa
for indice, nome in enumerate(lista):
  print(indice, nome)