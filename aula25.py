"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Dan'
preco = 1000.9563258
variavel = '%s, o preço total foi R$ %.2f' % (nome, preco) # Tipo o sprintf/printf

print(variavel)
print('O hexadecimal de %d é %08X' % (6963, 6963))