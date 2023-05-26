"""
Operadores de atrinuição
= += -= *= /= //= **= %=
"""

contador = 0

###
contador += 1 #adiciona 1 ao contador                   contador= 1
print(contador)
contador *= 10 #mutiplica 10 ao contador                contador= 10
print(contador)
contador -= 1 #diminue 1 ao contador                    contador= 9
print(contador)
contador /= 3 #divide o contador por 3                  contador= 3
print(contador)
contador **= 4 #eleva o valor q está no contador a 4    contador= 81
print(contador)
contador //= 2 # faz a divisão inteira por 2            contador= 40
print(contador)
contador %= 3 #tia o modulo do contador por 2           contador= 1
print(contador)


contador = 0
while contador < 10:
    contador += 1
    print(contador)

print('Acabou')
