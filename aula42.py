string = "Valor qualquer"

i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)

    i += 1
else:
    # Se tiver break, o print abaixo não será exibido
    # Será executado após o while ser executado por completo
    print('Não encontrei um espaço na string.')
print('Fora do while')