"""
CONSTANTE = Variaveis que não irão mudar
Muita condição no mesmo if (ruim - evite)
    <- Contagem de complexidade (quando mais bloco de código dentro do outro) (ruim - evite)
"""
velocidade_atual = 61 # pode mudar
local_carro = 100 # pode mudar

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde está o radar 1
RADAR_RANGE = 1 # a distancia onde a radar pega

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_1) and local_carro <= (LOCAL_1 + RADAR_1)
velocidade_carro_passou_radar_1 = velocidade_atual > RADAR_1
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print("Velocidade carro passou do radar 1: ")

if carro_passou_radar_1:
    print("Carro passou no radar 1")

if  carro_multado_radar_1:
    print("Carro multado em radar 1")