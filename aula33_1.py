"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_texto = input("Digite um número inteiro: ")

try:
    numero_inteiro = int(numero_texto)
    numero_inteiro_e_par = numero_inteiro % 2 == 0
    numero_inteiro_e_impar = numero_inteiro % 3 == 0
    
    if numero_inteiro_e_par:
        print(f"{numero_texto} é par")
    elif numero_inteiro_e_impar:
        print(f"{numero_texto} é impar")
    else:
        print(f"{numero_texto} não é par nem impar")
except:
    print(f"{numero_texto} não é um número")