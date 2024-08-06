"""
Lista de listas e seus índices
"""

salas = [['Frederico', 'Jaco'], ['Nailton', 'Herique', 'Pedro', (10, 20, 30, 40)]]

print(salas[1][1])

# Estou pegando a sala
for sala in salas:
  # Depois estou pegando os alunos de cada sala
  for aluno in sala:
    print(aluno)
