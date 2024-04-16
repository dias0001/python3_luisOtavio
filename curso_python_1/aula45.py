'''
Iterável -> str, range, etc(etc (_iter_)
next -> me entregue o próximo valor
iter -> me entregue seu iterador
'''

'''
numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)
'''

'''
texto = iter('Luiz') # __iter__()
print(texto.__next__()) # l
print(texto.__next__()) # u
print(texto.__next__()) # i
print(texto.__next__()) # z
'''
'''
texto = iter('Luiz') # __iter__()
print(next(texto))   # L
print(next(texto))   # u
print(next(texto))   # i
print(next(texto))   # z
'''

# for letra in texto
texto = 'Luiz'  # iterável
#iteratador = iter(texto) # iterator

#while True:
#    try:
#        letra = next(iteratador)
#       print(letra)
#    except StopIteration:
#        break
for letra in texto:
    print(letra)  # igual o comando acima ^ 