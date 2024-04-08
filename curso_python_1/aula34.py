"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}') # loop infinit -> Seu nome é gustavo

    if nome == 'Sair':  # uma condição para sair do loop infinito, quando dig=>Sair
        break

print('Acabou')
    
