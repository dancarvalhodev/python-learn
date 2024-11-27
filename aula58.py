"""
enumerate - enumera iterareis (indices)
"""

# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'Daniel')]
# O python não tem acesso direto aos indices, então o dev não consegue
# simplismente utiliza-los como PHP dando um echo ... ao enumerar e
# converter pra lista ele cria uma tupla em cada elemento com o indice e o elemento
# ai consigo acessar

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Daniel')

# lista_enumerada = list(enumerate(lista))

# print(lista_enumerada)

for item in enumerate(lista):
    indice, nome = item # desempacotamento
    print(indice, nome)
