def criar_saudacao(saudacao):
  def saudar(nome):
    return f'{saudacao} {nome}'
  return saudar

falar_bomdia = criar_saudacao('Bom dia')
falar_boanoite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Luiz', 'Pedro']:
  print(falar_bomdia(nome))
  print(falar_boanoite(nome))