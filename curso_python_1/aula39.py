"""
Iterando strings com while
"""
#       01234567891011
#nome = 'luiz gustavo'  # iteráveis
# print(nome[-12])  # para ver os índices
#tamanho_nome = len(nome)
#print(nome)         # luiz gustavo
#print(tamanho_nome) # 12
#print(nome[3])      # z

#nova_string = ''
#nova_string += '*l*u*i*z* *G*u*s*t*a*v*o'


"""
ATENÇÃO EXERCICIO COM WHILE - 
"""
"""
nome = 'Luiz Otávio'

indice = 0 
while indice <len(nome):
    print(nome[indice])
    indice += 1
    """

nome = 'Luiz Otávio'
novo_nome = ''
indice = 0 
while indice <len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)

# --------------------------------------------------- exemplo 2 -----------

nome = 'Maria Zeli'
novo_nome = ''
indice = 0 
while indice <len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
