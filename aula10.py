entrar = input("[E]entrar - [S]sair: ")
senha = input("Senha: ")

verificacao = '123456'

if (entrar == "E" or entrar == "e") and senha == verificacao:
  print("Entrou...")
else:
  print("Saiu...")
  
#Avaliação de curto circuito
print(False or True)

# Operador logico not inverte as expressões 
# not True = False
# not False = True