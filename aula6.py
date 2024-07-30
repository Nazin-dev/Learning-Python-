peso = input("Digite o seu peso em KG: ")
peso = float(peso)
altura = input("Digite sua altura em Metros: ")
altura = float(altura)

imc = peso / altura ** 2

print(f"Seu peso é de {peso}, sua altura é {altura} e o seu IMC é de -> {imc:.3f}")
#Acima estou usando o f-string.

print("Seu peso é de {}, sua altura é {} e o seu IMC é de -> {}".format(peso, altura, imc))
#Acima estou usando o metodo format.

###
string = "a={}, b={}"
a = "A"
b = "B"
print(string.format(a, b))