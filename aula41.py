""" Calculadora com while """
while True:
    primeiro_numero = input("Digite o primeiro número: ")
    segundo_numero = input("Digite o segundo número: ")
    operador = input("Digite o operador (+, -, * e /) para (adição, subtração, multiplicação e divisão): ")
    
    try:
        primeiro_numero_float = float(primeiro_numero)
        segundo_numero_float = float(segundo_numero)
    except:
        print("Um ou ambos números estão inválidos")
        continue

    operadores_permitidos = '+-/*'

    if len(operador) > 1:
        print("Operador inválido")
        continue

    if(operador not in operadores_permitidos):
        print("O operador informado não é permitido")
        continue

    print("Realizando operação ...")

    try:
        if operador == '+':
            print(f"{primeiro_numero_float} + {segundo_numero_float} = {(primeiro_numero_float + segundo_numero_float):.2f}")
        elif operador == '-':
            print(f"{primeiro_numero_float} - {segundo_numero_float} = {(primeiro_numero_float - segundo_numero_float):.2f}")
        elif operador == '*':
            print(f"{primeiro_numero_float} X {segundo_numero_float} = {(primeiro_numero_float * segundo_numero_float):.2f}")
        elif operador == '/':
            print(f"{primeiro_numero_float} / {segundo_numero_float} = {(primeiro_numero_float / segundo_numero_float):.2f}")
        else:
            print("Ocorreu um erro desconhecido")
    except:
        print('Ocorreu um problema ao realizar a operação')
    
    sair = input('Deseja sair [s]im: ').lower().startswith('s')

    if sair is True:
        break