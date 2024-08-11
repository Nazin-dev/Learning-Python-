# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
#---------------------------------------------------------
# Useful dictionary methods in Python
# len - how many keys
# keys - iterable with keys
# values ​​- iterable with values
# items - iterable with keys and values
# setdefault - adds value if key does not exist
# copy - returns a shallow copy (shallow copy)
# get - get a key
# pop - Deletes an item with the specified key (del)
# popitem - Deletes the last added item
# update - Updates one dictionary with another

person = {'name': 'Nailton', 
          'age': 17}

# print(person.__len__()) or print(len(person))

person.setdefault('street', None) # set default value for non-existent key / definir valor padrão para chave inexistente

print(person['street'])
print(list(person.keys()))
print(list(person.values()))
print(list(person.items()))

# for value in person.values():  # I'm getting the values / estou pegando os valores
#   print(value)

for keys, values in person.items(): # printing keys and values / imprimindo chaves e valores
  print(keys, values)