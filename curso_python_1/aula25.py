"""
Interpelação básica de strings
s - string
d e i - int
f - float
x e x - Hexadecimal (abcdef0123456789)
"""

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (15, 15))

# ver qual a melhor formatação time 6:25 ele fala de umas boas 