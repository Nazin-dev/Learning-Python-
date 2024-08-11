# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Quanto é 100/10?',
        'Opções': ['4', '5', '2', '10'],
        'Resposta': '10',
    },
]

cont = 0
seletion = 0
resposta = ''
roleta = 0

while True:
  print(f'Pergunta: {perguntas[roleta]['Pergunta']}')

  for op in perguntas[roleta]['Opções']:
    print(f'{cont}) {op}')
    cont += 1
  opcao_escolhida = input('Escolha uma opção: ')
  try:
    opcao_escolhida =  int(opcao_escolhida)
  except ValueError:
    cont = 0
    print('Digite um valor congruente!')
    continue
  
  lista = list(perguntas[roleta]['Opções'])

  for comparacao in lista:
    if seletion == opcao_escolhida:
      resposta = lista[seletion]
    seletion += 1
    
  # checking if the answer is correct / verificando se resposta está correta 
  if resposta == perguntas[roleta]['Resposta']:
    print('Parabéns! Você acertou!')
  else:
    print('Que pena! Você errou!')
    
  if len(perguntas) - 1 == roleta:
    break
  
  # reset variables 
  seletion = 0
  roleta += 1
  cont = 0