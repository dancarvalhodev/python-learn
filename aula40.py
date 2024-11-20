"""
Iterando strings com while
"""

nome = 'Daniel Carvalho'
tamanho = len(nome)

indice = 0
nome_purpurinado = ''

while indice < tamanho:
    letra_purpurinada = nome[indice]
    nome_purpurinado += f'*{letra_purpurinada}'
    indice += 1

print(f'{nome_purpurinado}*')