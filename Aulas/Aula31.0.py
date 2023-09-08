"""
Flag (bandeira) - Marcar um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade
id = identidade)
"""
#variaveis iguais, mesmo id(endereço)
v1 = "a"
v2 = "a" 
print(id(v1))
print(id(v2))

#Variaveis diferentes, id diferente
v1 = "a"
v2 = "b"
print(id(v1))
print(id(v2))
