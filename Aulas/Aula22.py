# or -> Qualquer condição verdadeira avalia toda expressão como verdadeira
#Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor

print()
entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = "123456"

#Ambas as condições tem q ser verdadeiras
if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")

# Avaliação de Curto circuito
print(True and 0 and True)
print(True or False or 0 or "abc")
senha = input("Senha: ") or "Sem senha"
print(senha)
