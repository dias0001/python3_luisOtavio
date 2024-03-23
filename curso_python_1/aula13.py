#Luiz Gustavo tem 1.80 de altura, 
# pesa 95 quilos e seu IMC é
# 29.3200987654320987

# imc = peso / (altura x altura)
# peso (em Kg), altura ao quadrado (em m)
# o resultado de IMC é dado eM kg/m 2

nome = 'Luiz Gustavo'
# altura = 100050.4  # poderia ser 1.80 => {altura:,.2f} 1.80 resposta
altura1 = 1.80
peso = 95
imc = ...

# imc = peso / (altura * altura)
imc = peso / (altura1 ** 2)

"f-strings"
linha_1 = f'{nome} tem {altura1:,.2f} de altura' # .2f => casa decimais (2)
# ,2f  => 100,050.40
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
