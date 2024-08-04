import os

palavra_secreta = 'sec'   
letras_encontradas = ''
tentativas = 0


while True:
  
  letra = input('Digite uma letra: ')
  tentativas += 1
  
  if len(letra) > 1:
    print('Digite apenas uma letra.')
    continue
  
  if letra in palavra_secreta:
    letras_encontradas += letra

  palavra_formada = ''
  
  # Dar atenção a essa parte do codigo, tem uma logica muito boa.
  for letra_secreta in palavra_secreta:
    
    if letra_secreta in letras_encontradas:
      palavra_formada += letra_secreta
    else:
      palavra_formada += '*'
      
  print(palavra_formada)
  if palavra_formada == palavra_secreta:
    os.system('cls')
    print('Você acertou, parabêns!')    
    print('A palavra formada foi: ', palavra_formada)
    print(f'O seu numero tentativas foi {tentativas}x.')
    letras_encontradas = ''
    tentativas = 0
