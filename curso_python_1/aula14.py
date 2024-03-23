a = 'A'
b = 'B'
c = 1.1
string = 'a={0} b={1} c={2:.2f}'
formato = string.format(a, b, c) # {} seleciona a ordem
# parametro nomeado (quando se da o nome pra coisas) 
# => tudo que vir depois do paramentro tem que ser nomeado tbm

print(formato)
