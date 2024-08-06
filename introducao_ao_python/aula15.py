"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
  'Digite um numero que eu irei dobrar: '
  )

try:
  numero_float = float(numero_str)
  print('FLOAT:', numero_float)
  print(f'O dobro do numero {numero_str} é {numero_float * 2}! ')
except:
  print('Isso não é um numero!')
  
  """_Irei tentar explicar aqui_
    Basicamente, estou pegando um input e multiplicando por 2. O problema é que, se 
    o usuário digitar uma letra, isso geraria um erro. Se eu usar um if e testar com 
    isdigit(), ele me retornaria True caso fosse um número inteiro e False se fosse 
    uma letra. Entretanto, ele retorna False para números do tipo float, por isso, 
    se eu usar ele na condição, vai retornar "isso não é um número".

   Por isso, estou usando try e except. Em resumo, o try tenta executar um código e, 
   caso ocorra um erro, ele direciona para o except, onde você pode colocar o código 
   que quiser para tratar o erro.
  """
  
#Codigo antigo, que geraria o resultado indesejado .
# if numero_str.isdigit() == True:
#   print(numero_str.isdigit())
#   print(f'O dobro do numero {numero_str} é {numero_float * 2}! ')
# else:
#   print('Isso não é um numero!')