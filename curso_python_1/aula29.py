"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('float:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

'''
numero = input('Vou dobrar o número que vc digitar:')

numero_float = float(numero)

# print(f'O dobro de {numero} é {numero * 2}')  # O dobro de 2 é 22
print(f'O dobro de {numero} é {numero_float * 2}') # O dobro de 2 é 4.0
print(f'O dobro de {numero} é {numero_float * 2:.0f}') # O dobro de 2 é 4
print(f'O dobro de {numero} é {numero_float * 2:.2f}') # O dobro de 2.2 é 4.40
'''


#   outro exemplo 

'''
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)
print(numero_str.isdigit())

numero_float = float(numero_str)
print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# respostra de cima=2    => True  O dobro de 2 é 4.00
# respostra de cima=2.3  =>  False O dobro de 2.3 é 4.60
'''

#numero_str = input(
#    'Vou dobrar o número que vc digitar: '
#)

#if numero_str.isdigit():  # isdigit = bool
#    numero_float = float(numero_str)
#    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
#else:
#    print('Isso não é um número')


    