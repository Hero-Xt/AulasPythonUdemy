"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Convversion flags - !r !s !a
"""
variavel = "ABC"
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}') #sem ponto no final
print(f'{variavel: ^10}.') #preenche com espaços com ponto no final
print(f'{variavel:$>10}')
print(f'{variavel:-<10}.')
print(f'{variavel:´^10}.')
print(f'{1000.4873891879779:.1f}')
print(f'{1000.4873891879779:,.1f}') #usa a virgula para separar a centena
print(f'{1000.4873891879779:+,.1f}') #usa o + para ixibir o sinal de positivo no numero, caso seja positivo
print(f'{-1000.4873891879779:+,.1f}')
