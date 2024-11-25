"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Daniel', 'Maria']
lista_b = lista_a

lista_a.append('Lucas')

print(lista_a)
print(lista_b)

lista_c = ['Arroz', 'Feijão']
lista_d = lista_c.copy()

lista_c.append('Lucas')

print(lista_c)
print(lista_d)