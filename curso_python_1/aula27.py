"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(len(variavel)) # quando quiser saber o tamanho da função colocar o LEN
print(variavel[4:])  # Sem nada depois dos dois pontos quer dizer pegar tudo
print(variavel[4:8]) # se quiser p. n. penultimo sempre pegar o ultimo 8
print(variavel[:5])
print(variavel[:5:-2])
print(variavel[0:9:1])
print(variavel[0:9:4])
print(variavel[0:len(variavel):1])
print(variavel[-1:-10:-1])
print(variavel[::-1])