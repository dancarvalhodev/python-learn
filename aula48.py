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

palavra = '******'

while True:
    palavra_secreta = 'chaves'
    

    try:
        letra = input('Digite APENAS UMA letra: ').lower()

        if len(letra) != 1:
            print('Digite apenas uma letra')
            continue
    except:
        print('Foi informado um digito inválido')


    i = 0
    palavra_sendo_descoberta = ''
    while i < len(palavra_secreta):
        

        if palavra_secreta[i] == letra:
            palavra_sendo_descoberta += letra
        else:   
            palavra_sendo_descoberta += '*'

        i += 1

    palavra = palavra_sendo_descoberta
    print(palavra)





    sair = input('Deseja sair [s]im: ').lower().startswith('s')

    if sair is True:
        print(palavra)
        break




