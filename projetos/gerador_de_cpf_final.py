"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf = input('Digite o seu cpf: ')

# Aqui estou tratando a informação, tirando os pontos e traços

cpf_ponto = cpf.split('.') # Tiro os pontos


cpf_formatado_ponto = ''

for digito in cpf_ponto:
  cpf_formatado_ponto += digito # Jogo os digitos para a variavel 
  # Estou pegando os valores da lista e jogando para um string

cpf_traco = cpf_formatado_ponto.split('-') # Tiro o traço

cpf_formatado_traco = ''

for numero in cpf_traco:
  cpf_formatado_traco += numero # Jogo os digitos para a variavel 

#--------------------------Soma dos 9 primeiros digitos----------------------------------#

primeiros_digitos = cpf_traco[0] # Peguei os 9 primeiros digitos

lista_de_mult = [10, 9, 8, 7, 6, 5, 4, 3, 2] # Lista de numeros que os digitos serão multiplicados
indice = 0 # Indice da lista de multiplicados 

soma_dos_primeiros_digitos = 0

for i in primeiros_digitos:
  i = int(i)
  soma_dos_primeiros_digitos += i * lista_de_mult[indice] # Multiplica os 9 primeios digitos por os numeros da lista_de_mult
  indice += 1

#--------------------------Multiplicando por 10 e verificando----------------------------------#

resultado_da_mult = soma_dos_primeiros_digitos * 10

resultado_do_resto = resultado_da_mult % 11

digito1 = 0

if resultado_do_resto > 9:
  print('Cpf invalido!')
  
elif resultado_do_resto <= 9:
  digito1 = resultado_do_resto
  print(f'O primeiro digito do cpf é [{digito1}].')
  
#--------------------------Somando o Ultimo Digito----------------------------------#

segunda_lista_de_mult = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

primeiros_digitos_mais_um = cpf_traco[0] + str(digito1) # São os 10 primeiros digitos

soma_dos_dez_primeiros = 0

indice2 = 0
for j in primeiros_digitos_mais_um:
  j = int(j)
  soma_dos_dez_primeiros += j * segunda_lista_de_mult[indice2] # Multiplicando e Somando os 10 primeiros digitos
  indice2 += 1 

#----------------------Multiplicando por 10 e verificando o ultimo digito-------------------------------#

resto_da_mult_por_dez = (soma_dos_dez_primeiros * 10) % 11

digito2 = 0
if resto_da_mult_por_dez > 9:
  print('Cpf invalido!')
  
elif resto_da_mult_por_dez <= 9:
  digito2 = resto_da_mult_por_dez
  print(f'O segundo digito do cpf é [{digito2}].')
print(resto_da_mult_por_dez)