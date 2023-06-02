"""
Faça um programa que peça ao usuário para digitar um número inteiro,
iforme se este número é par ou impar. Caso o usuário não digite um 
numero interiro, informe que não é um número inteiro
"""
numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print("O número {} é par" .format(numero))
    else:
        print('O número {} é impar'.format(numero))
else:
    print(f'{numero} não é um número inteiro')

# Ou

numero = input('Digite um número inteiro: ')

try:
    numero = int(numero)
    if numero % 2 == 0:
        print("O número {} é par" .format(numero))
    else:
        print('O número {} é impar'.format(numero))
except:
    print(f'{numero} não é um número inteiro')

    
