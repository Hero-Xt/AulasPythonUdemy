# Operadores Lógicos
# and (e) or (ou) not (não)
# verdadeiras
# Se qualquer valor for considerado falso a expresão inteira será avaliada naquele valor
# São considerados falsys ((que vc ja viu))
# 0    0.0   ""   False
# Também existe o tipo None que é usado para representar um não valor

print(True and True and True) #True
print(True and False and True) #Apos o false, não verifica os itens seguintes
print(bool("")) #False
print(bool(0)) #False
print(bool(0.0)) #False


print()
entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = "123456"

#Ambas as condições tem q ser verdadeiras
if entrada == "E" and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")

