# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# D a n i e l
# -6-5-4-3-2-1

nome = 'Daniel'
print(nome[2])
print(nome[-4])

# Minusculo e maiusculo fazem diferença
print('dan' in nome)
print('Dan' in nome)
print('x' in nome)

print(20 * '-')

print('dan' not in nome)
print('Dan' not in nome)
print('x' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')