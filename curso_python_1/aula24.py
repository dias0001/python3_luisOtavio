# Operadores in e not in
# Strings são iteráveis
# 0  1  2  3  4  5
# o  t  á  v  i  o
#-6 -5 -4 -3 -2 -1
#nome = 'Otávio'
#print(nome[2])
#print(nome[-4])
#print(10 * '-')
#print('vio' in nome)
#print('zero' in nome)
#print(10 * '-')
#print('vio' not in nome)  #inverte => not in == True será False
#print('zero' not in nome) #inverte => not in == False será True
#print(40 * '-')

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
