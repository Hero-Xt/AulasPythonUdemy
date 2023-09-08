# if / elif / else
# se / se não se / se não
entrada = input(('Você quer "entrar" ou "sair" '))

# A partir da condição True, o sistema pula as outras condicionais 
if entrada == "entrar" :
    print("Você entrou no sistema")
elif entrada == "sair" :
    print("você saiu do sistema")
else:
    print("Você não digitou nem entrar nem sair!")
