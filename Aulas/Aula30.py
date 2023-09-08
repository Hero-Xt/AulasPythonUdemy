"""
Constante = "Variaveis" que não muda
Muitas condições no mesmo if (ruim) 
    <- contagem de complexidade (ruim)

Há uma conversão em python que Variaveis nomedas com letra
maiuscula são constantes
"""
velocidade = 61 # velocidade atual do carro
local_carro = 100 #local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar q
LOCAL_1 = 100 #local onde o radar 1 esta
RADAR_RANGE = 1 #Distância onde o radar pega

#if velocidade > RADAR_1:
#    print('Velocidade carro passou do radar 1')
#if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
#    (local_carro <= LOCAL_1 + RADAR_RANGE) and \
#        velocidade > RADAR_1:
#    print('Carro passou radar 1')


#simplificação de codigo, com boas partica

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = (LOCAL_1 - RADAR_RANGE) and (local_carro <= LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = vel_carro_pass_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro oassou do rada 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')
