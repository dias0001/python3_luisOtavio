"""
CONSTANTE = 'Variáveis' que não vão mudar
Muitas condoções no mesmo if (ruim)
....<- Contagem de complexidade (ruim)
"""

# VALOR CONSTANTE NÃO IRÁ MUDAR => COLOCA EM MAIÙSCULO (RADAR_1 - RADAR_1 - RADAR_RANGE )

"""
velocidade = 61 # velocidade do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega 

if velocidade > RADAR_1:
    print('Velocidade carro passou no radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
    print('carro multado em radar 1')
    """
velocidade = 61 # velocidade do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega 

vel_carro_passou_radar_1 = velocidade > RADAR_1 #foi melhorado  aqui a repetição

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) #foi melhorado  aqui a repetição

carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_passou_radar_1

if vel_carro_passou_radar_1:
    print('Velocidade carro passou no radar 1')

if carro_passou_radar_1:
    print('Carro passou no radar 1')

if  carro_multado_radar_1:
    print('carro multado em radar 1')

    '''
    quando quiser trocar a variável => f2 ela muda as duas variáveis '''


