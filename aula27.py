""" Exercicio de qual letra apareceu mais na frase"""
frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'.lower()

frase_tamanho = len(frase)

cont = 0 # Contador
recorrencia = 0 # Numero de recorrencia das letras na frase.
maior_recorrencia = 0 # O numero de recorrencias da letra de maior recorrencia.
maior_letra = '' # A letra com maior recorrencia.


""" O while vai correr por todos os caracteres da frese"""
while cont < frase_tamanho:
  
  # a variavel letra_atual recebe a letra em que  o while está no momento.
  letra_atual = frase[cont]
  
  # A variavel recorrencia vai receber o numero de recorrecias da letra apenas se não for um espaço ' '.
  # Basicamente o while tem que estar em algum caractere diferente de ' '.
  if frase[cont] != ' ':
    recorrencia = frase.count(frase[cont])
    print(letra_atual, recorrencia)
  
  """Esse if verifica se a recorrencia atual é maior que a recorrencia anterior. Caso seja maior, a variavel  
     maior_recorrencia recebe o novo valor que agora é o maior."""  
  # A recorrencia anterior ficou salva na variavel maior_recorrencia.
  if recorrencia >= maior_recorrencia:
    maior_recorrencia = recorrencia
    maior_letra = frase[cont] # Recebe a letra que atualmente tem a maior recorrencia. 
    
  cont += 1
  
print(f'A letra de maior recorrencia foi [{maior_letra}] com {maior_recorrencia} recorrencias!')