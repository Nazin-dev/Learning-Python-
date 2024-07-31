entrar = input("[E]entrar - [S]sair: ")
senha = input("Senha: ")

verificacao = '123456'

if entrar == "E" and senha == verificacao:
  print("Entrou...")
else:
  print("Saiu...")
  
#Avaliação de curto circuito
print(True and True and False)