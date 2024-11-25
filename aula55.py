"""
Exercicio
Exiba os indices da lista

0 Maria
1 Helena
2 Luiz
"""

lista = ['Daniel', 'José', 'Pedro']
lista.append('Shakira')

for indice in range(len(lista)):
    print(f'{indice} {lista[indice]}')