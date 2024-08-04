"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

#Eu pensei que era as horas e minutos e não só a hora kkkkk

hora = input('Digite a hora: ')

hora_minuto = hora

hora = hora[0:2]

hora_int = int(hora)

dia = hora_int >= 0 and hora_int < 12

tarde = hora_int >= 12 and hora_int < 18

noite = hora_int >= 18 and hora_int < 24

if dia:
  print(f'Bom dia! {hora_minuto}')
  
if tarde:
  print(f'Bom tarde! {hora_minuto}')
  
if noite:
  print(f'Bom noite! {hora_minuto}')
