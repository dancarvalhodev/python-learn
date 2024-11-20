"""
Repetições
while (Enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> código sem fim
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6 fi')
        continue

    if contador >= 10 and contador <= 27:
        print(f'Não vou mostrar o {contador} fi')
        continue

    print(contador)

    if contador == 40:
        break

print("Acabou")