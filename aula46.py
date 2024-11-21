"""
For debaixo dos panos

Iterável -> str, range, etc (tem o método __iter__) É O ENTREGADOR
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# Se esgotar os valores, gera o erro StopIteration
texto = 'Dan' #iterável
iterador = iter(texto) # iterator

while True:
    try:
        print(next(iterador)) # next == __next__() e as __ chama dander
    except StopIteration:
        break