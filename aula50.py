"""
Listas em python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métodos ùteis: append, insert, pop, del, clear, extent, +
Create Read Update Delete
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
lista[2] = 300

# Python REORGANIZA os indices da lista 
# (REQUER MUITO PROCESSAMENTO DEPENDENDO DO TAMANHO DA LISTA)
# O interessante é adicionar e remover coisas apenas do final da lista
del lista[2] # Deleta

# Append adiciona o elemento ao final
lista.append(50)
lista.append(60)
lista.append(70)

# Pop remove o último elemento da lista
# Retorna o valor removido
removido = lista.pop()

print(f'LISTA: {lista}', f' | REMOVIDO: {removido}')


