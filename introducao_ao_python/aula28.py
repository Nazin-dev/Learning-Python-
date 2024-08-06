""" Estudando for """

texto = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'
recorrencia = 0
letra_atual = ''
maior = 0

for letra in texto:
  
  if letra != ' ':
    recorrencia = texto.count(letra)
  
  if recorrencia >= maior:
    maior = recorrencia
    letra_atual = letra
    
print(f'A letra {letra_atual} aparece {maior}x.')