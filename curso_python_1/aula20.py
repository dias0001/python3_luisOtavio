# if /    elif   / else
# se / se não se / se não

'''entrada = input('você quer "entrar" ou "sair"?')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('você não digitou nem entrar e nem sair.')'''

primeiro_valor = input('Digite um valor: ')
segundo_valor  = input('Digite outro valor: ')

'''if primeiro_valor > segundo_valor:
    print('primeiro_valor=', primeiro_valor, 
    'é maior do que segundo_valor=', segundo_valor
)'''

'''else:
    print('Segundo_valor=', segundo_valor, 
    'é maior do que primeiro_valor=', primeiro_valor
)'''

if primeiro_valor >= segundo_valor:
    print(
    f'{primeiro_valor=} é maior ou igual '
    f'ao que {segundo_valor=}'
) 
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )

