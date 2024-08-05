"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase = 'Python é uma otima linguagem, eu gosto!'

lista_frase = frase.split(',')
lista_recebe = []

for i, frase in enumerate(lista_frase):
  lista_recebe.append(lista_frase[i].split())

print(lista_recebe)
print(lista_frase)

lista_unida = '-'.join(lista_frase)
print(lista_unida)