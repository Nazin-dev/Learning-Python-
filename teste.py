usuario = []
palavra = 'besta'
chances = 3
ganhou = False
 
 
while True:
 
    for letra in palavra:
 
         if letra.lower() in usuario:
 
            print(letra, end = ' ')
 
         else:
            print('*', end = ' ')
 
    print(f"Você tem {chances} chances")
 
    tentativa = input('Digite uma letra para adivinhar: ')
    usuario.append(tentativa.lower())
 
    if tentativa.lower() not in palavra.lower():
         chances -= 1
    ganhou = True
 
    for letra in palavra:
        if letra.lower() not in usuario:
          ganhou = False      
 
    if chances == 0 or ganhou:
        break 
 
if ganhou:
 
    print(f"Parabéns, você ganhou. A palavra era: {palavra}")
 
else:
 
    print(f"Você perdeu! A palavra era: {palavra}")
 