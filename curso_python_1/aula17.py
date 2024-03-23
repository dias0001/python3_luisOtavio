# if /    elif   / else
# se / se não se / se não

'''condicao = False

if condicao:
    print('Este é o codigo do if')
else:
    print('Este é o else do primeiro if')

if 10 ==10:
    print('Outro if')

print('Fora do if')'''

condicao1 = False
condicao2 = False
condicao3 = True # False / sera checado a condição que for primeira e não respondera outra abaixo
condicao4 = False

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1') # para mostra que pode ter mais de uma condição
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi sstisfeita.')


