""" Calculadora com while """
import operator

while True:
    sair = input('Deseja sair [s]im: ').lower().startswith('s')

    if sair is True:
        break

    primeiro_numero = input("Digite o primeiro número: ")
    segundo_numero = input("Digite o segundo número: ")
    operador = input("Digite o operador (+, -, * e /) para (adição, subtração, multiplicação e divisão): ")
    
    try:
        primeiro_numero_float = float(primeiro_numero)
        segundo_numero_float = float(segundo_numero)

        if operador == '+':
            print(operator.add(primeiro_numero_float, segundo_numero_float))
        elif operador == '-':
            print(operator.sub(primeiro_numero_float, segundo_numero_float))
        elif operador == '*':
            print(operator.mul(primeiro_numero_float, segundo_numero_float))
        elif operador == '/':
            print(f'{operator.truediv(primeiro_numero_float, segundo_numero_float):.2f}')
        else:
            print('O operador digitado é inválido')
    except:
        print('Os dados informados são inválidos')