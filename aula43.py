# Quero verificar, em uma string, qual a letra que apareceu
# mais vezes em uma string

frase = 'aaaooo'

i = 0
quantidade_total = 0
letra_final = ''

while i < len(frase):
    letra_atual = frase[i]
    quantidade_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    quantidade_atual = frase.count(letra_atual)

    if quantidade_total <= quantidade_atual:
        quantidade_total = quantidade_atual
        letra_final = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_final}" que apareceu '
    f'{quantidade_total}x.'
)