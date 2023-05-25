print(12, 34) #imprimir algo na tela, contem um argumento!
print(56, 78) #argumentos não nomeados

#auterar o separador
print(12, 34, sep=":") 
#Apos um print se tem uma quebra de linha
#No windows, apos o print há um \r\n(invisível)
#Outros sistemas \n
print(56, 78, sep='-_-')
print(910, 1112, sep='') #espaço entre aspas sem nada
print(1314, 1516, sep=' ') #espaço entre aspas sem com espaço

#padrão invisível
print(56, 78, sep='-_-', end="\r\n") 
print(910, 1112, sep='', end="\n") 
print(1314, 1516, sep=' ', end="\n") 

print(56, 78, sep='-_-', end="##\n") # ## e quebra de linhas
print(910, 1112, sep='', end="") #sem quebra de linha
print(1314, 1516, sep=' ', end="++\n") # ++ e quebra de linha 

