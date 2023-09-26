"""
Flag (bandeira) - Marcar um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade
id = identidade)
"""

condicao = False
passou_no_if = None

if condicao:
   passou_no_if = True
   print('Faça algo')
else:
   print('Não faça algo')

print(passou_no_if, passou_no_if is None) #mesma coisa que passou_no_if == None
# Mas quano de usa None, é mais comum usar o is None
print(passou_no_if, passou_no_if is not None)

# Ou

if passou_no_if is None:
   print('Não passaou no if')
if passou_no_if is not None:
   print('Passou no if')
