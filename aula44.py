"""
while: não sei quantas repetições vou executar
for: sei quantas repetições vou executar
"""

texto = "Python"
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'

print(novo_texto)