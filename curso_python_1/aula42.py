frase = 'ooooaaa.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

    print(
        'A letra que apareceu mais vezes foi '
        f'{letra_apareceu_mais_vezes} que apareceu '
        f'{qtd_apareceu_mais_vezes}x'
    )
    




'''
frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criador por Guido van Rossum.'

print(frase.count('a')) # 9 vezes
print(frase.count('o')) # 9 vezes
print(frase.count('n')) # 4 vezes



frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criador por Guido van Rossum.'
print(frase)
print(frase.count('Python')) # count => quantas vezes a palavra na variável frase
print(frase.lower().count('Python'))

# ---------------------

frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criador por Guido van Rossum.'.lower()

print(frase.lower().count('python'))

#------------------------

frase = 'O PYTHON é uma linguagem de programação ' \
    'multiparadigma. PYTHON ' \
    'PYTHON foi criador por Guido van Rossum.'  

print(frase)
print(frase.upper().count('PYTHON')) #  upper => toda maiúscula
'''

