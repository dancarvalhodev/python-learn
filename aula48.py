"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

palavra_secreta = 'macaco'
palavra = ''
palavra_sendo_descoberta = ''
tentativas = 0

for letra in palavra_secreta:
    palavra += '*'


while True:
    try:
        tentativas += 1
        letra = input('Digite uma letra: ').lower()

        if len(letra) != 1:
            print('Digite apenas uma letra')
            continue

        if letra.isdigit():
            print('Não são permitidos números')
            continue
    except:
        print('Foi informado um digito inválido')

    for posicao in range(len(palavra_secreta)):
        if palavra_secreta[posicao] == letra:
            palavra_sendo_descoberta = palavra[:posicao] + letra + palavra[posicao + 1:]
            palavra = palavra_sendo_descoberta


    if palavra_sendo_descoberta == palavra_secreta:
        os.system('clear') 
        
        print('VOCÊ GANHOU!!!!!')
        print(f"A palavra secreta '{palavra}' foi descoberta")
        print(f"Número de tentativas: {tentativas}")

        palavra_sendo_descoberta = ''
        palavra = ''
        tentativas = ''

        break
    else:
        print(palavra)