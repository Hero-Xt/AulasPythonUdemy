"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito - > Quando um código não tem fim
"""
condição = True
while condição:
    nome = input('Qual o seu nome')
    if nome == 'sair':
        break
    print(f'Seu nome é {nome}')
    
print('acabou')
