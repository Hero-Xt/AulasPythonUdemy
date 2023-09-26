"""
Exercício
Peça ao usuario para digitar seu nome
Peça ao usuario para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é:
        Seu nome invertido é:
        Seu nome contém ou não espaços
        Seu nome tem n letras
        Aprinmeira letra do seu nome é:
        A útima letra do seu nome é:
Se nada for digitado em nome ou idade:
    exiba: "Desculpe, você deixou campos vazios"
"""
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
if nome and idade : # não precisa definir == "" 
    print(f"Seu nome é {nome}")
    print("Seu nome invertido é %s" % nome[::-1])
    if " " in nome:
        print("Seu nome contém espaços")
    else:
        print('Seu nome não contém espaços')
    print('Seu nome tem {} letras'.format(len(nome)))
    print(f"A Primeira letra do seu nome é {nome[0]}")
    print("A utima letra do seu nome é {}".format(nome[-1]))
else:
    print("Desculpe, você deixou campos vazios")
