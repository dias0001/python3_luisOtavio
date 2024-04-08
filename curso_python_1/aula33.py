"""
https://docs.python.org/pt-br/3/library/stdtypes.html
imutáveis que vimos: str, int, float e bool
"""

"""
string = 'Luiz Gustavo'
outra_variavel = f'{string[:3]}abc' # add abc depois da 3° string 
print(outra_variavel)  # resposta => Luiabc
"""
"""
string = 'Luiz Gustavo'
outra_variavel = f'{string[:3]}abc{string[4:]}' # add abc depois completa espaço e Gustavo 
print(string)          # resposta Luiz Gustavo => imutável
print(outra_variavel)  # resposta => Luiabc Gustavo
"""
"""
string = 'luiz Gustavo'
print(string.capitalize()) # método capitalize => pega a string com a 1° letra minus. p/ maiusc.
"""
string = 'luiz Gustavo'
print(string.zfill(25))    # método zfill => 0000000000000luiz Gustavo =>Tem 25 caracter

