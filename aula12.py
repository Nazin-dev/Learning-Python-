"""
Interpolação de stings basicas
s     - string
d e i - int
f     - float
x e X - Hexadecimal 
"""

nome = 'Nailton'
preco = 108.95
variavel = '%s, o preço é %.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %x' % (15, 15))
# Outra forma de fazer a mesma coisa
print(f'O hexadecimal de 1500 é {1500:04x}')

# Formatação basica de strings 

var = 'ABC'
print(var)
print(f'{var:->10}')
print(f'{var:-<10}')
print(f'{var:-^10}')