"""
Introdução ao try/except
try -> tentar executar o código
except - > ocorreu algum erro ao tentar ao executar
"""

#print(1234)
#print(456)
#print('a')

# numero = input('Voudobrar um número que vc digitar: ')
# nuemro_float = float(numero)
# print(f"O dobro de {numero} é {nuemro_float * 2}")

numero_str = input('Voudobrar um número que vc digitar: ')

try:
    numero_float = float(numero_str)
    print('Float:', numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2}")
except:
    print('Isso não é um número')
    
