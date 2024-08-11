palavra = 'Python.-Não sei..Sei--Lá'

def formatacao(a):
  format_p = a.split('.')
  recebe = ''
  for letra in format_p:
    recebe += letra
  recebe = recebe.split('-')
  recebe2 = ''
  for letra in recebe:
    recebe2 += letra
  print(recebe2)
  return recebe2

