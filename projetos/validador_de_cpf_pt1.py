"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
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