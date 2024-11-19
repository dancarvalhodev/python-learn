"""
Repetições
while (Enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> código sem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print("Acabou")