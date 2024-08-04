"""
CONSTANTE = "Variáveis" que não vão mudar
            Muitas condições no mesmo if (ruim)
            <- Contagem de complexidade (ruim)
            - Manter o codigo limpo e facil de ser lido. 
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_carro_radar1 = velocidade > RADAR_1

carro_passou_no_local1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado = velocidade_carro_radar1 and carro_passou_no_local1

if velocidade_carro_radar1:
  print('- Passou da velocidade maxima permitida!')

if carro_passou_no_local1:
  print('- Carro passou no radar 1!')
  
if carro_multado:
  print('- Carro pego no radar 1 e multado por excesso de velocidade')

  """
  Essa aula foi sobre complexidade de codigo!
  
  É necessario fazer um codigo que os outros entendam, para isso temos que ter cuidado com a quantidade de ifs e usar algumas convenções como variaveis em MAIUSCULO, não existe variaveis constantes no Python, mas é uma convensão usar variaveis maiusculas como constantes. 
  """