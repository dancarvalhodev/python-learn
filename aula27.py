"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Hello World'

print(variavel[4:])
print(variavel[4:9])
print(variavel[0:5])
print(variavel[:5])
print(variavel[-1:-3])
print(len(variavel))
print(variavel[0:len(variavel):1])
print(variavel[0:len(variavel):3])
print(variavel[::-1])
print(variavel[-1:-12:-1])