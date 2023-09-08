"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutaveis que vimos: str, int, float, bool
"""
string = 'Luiz Otávio'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
# string[3] = 'ABC' -> não é possivel alterar o valor por ser imutavel
print(string)
print(outra_variavel)
print(string.capitalize)
print(string.upper)
