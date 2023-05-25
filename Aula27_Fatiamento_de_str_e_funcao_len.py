"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Pbs.: a função len retornar a qtd de caracteres da str
"""

variavel = "Olá mundo"
print(variavel[0:8:2])
print(len(variavel))
print(len(variavel[2:8]))
print(variavel[0:len(variavel):1])
print(variavel[::-1])
print(variavel[-1:-10:-1])
