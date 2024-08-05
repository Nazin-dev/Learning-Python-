"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create | Read| Update  | Delete
Criar  | ler | alterar | apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]

del lista[2]

lista.append(50) # Adicionou 50
lista.pop() # Tirou o ultimo elemento da lista, que no caso é o 50
lista.append(60) # Adicionou 60

lista.insert(0, 5.5)

print(lista)