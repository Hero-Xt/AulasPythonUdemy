a = "A"
b = "B"
c = 1.1
formato = 'a = {}, b = {}, c = {:.2f},'.format(a, b, c) #sem indice tem q ter ordem
string = "b = {1}, a = {0}, a = {0}, b = {1}, c = {2}" #com indeice dispensa ordem
formato2 = string.format(a, b, c)
print(formato)
print(formato2)
print()
print("a = {}, b = {}, c = {}".format(a, b, c)) 
print("a = {0}, b = {1}, c = {2}".format(a, b, b)) 
print()
# Parâmetro nomeado
# Tudo q estiver apos um apramêtro nomeado tem q ser nomeado
string3 = "b = {nome2}, a = {nome1}, a = {nome1}, b = {nome2}, c = {nome3}"
formato4 = string3.format(nome1=a, nome2=b, nome3=c)
print(formato4)
print("a = {}, b = {}, c = {}".format(a, b, c)) 
print("a = {nome1}, b = {nome2}, c = {nome3}".format(nome1=a, nome2=b, nome3=c)) 
