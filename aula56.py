"""
Introdução ao desempacotamento
"""

# Mesma quantidade de variáveis e valores
# nome1, nome2, nome3 = ['Daniel', 'José', 'Pedro']

# _ tem as demais variáveis, evitando o erro de unpack
# _ é uma convenção que essa variavel existe mais não será utilizada
_, nome2, *_ = ['Daniel', 'José', 'Pedro']

print(nome2)