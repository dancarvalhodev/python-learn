"""
Flag (Bandeira) - Marcar um local (controla o fluxo do código com base 
em seu valor booleano, indicando se uma parte específica do código foi 
executada.)

None - Não valor

is e is not = 'é' ou 'não é'
"""

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')