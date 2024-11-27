"""
Tipo tupla - Uma lista imutável
É mais eficiente que as listas
Se não vou modificar, é ideal usar tupla
"""

nomes = ('Maria', 'Helena', 'Luiz') # Com ou sem parenteses
# tuple(lista) converte uma lista em tupla
_,_, nome, *resto = nomes

print(nomes)