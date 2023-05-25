"""
Faça um programa que pergunte a hora ao usuário e baseando-se no horário 
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, boa tarde 12-17 e boa noite 18-23
"""
hora = input("Digite a hora: ")
try:
    n = int(hora[0:2])
    if 0 < n <= 11:
        print('Bom dia')
    elif n <= 17:
        print('Boa tarde')
    elif n <= 23:
        print('Boa noite')
    else:
        print('Não conheço esse número')
except:
    print('Você não digitou um horario valido')
