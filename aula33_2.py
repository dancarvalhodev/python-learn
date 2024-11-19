"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input("Digite a hora: ")

try:
    hora_inteira = int(hora)

    hora_matutina = hora_inteira >= 0 and hora_inteira <= 11
    hora_vespertina = hora_inteira >= 12 and hora_inteira <= 17
    hora_noturna = hora_inteira >= 18 and hora_inteira <= 23

    if hora_matutina:
        print("Bom dia 0-11")
    elif hora_vespertina:
        print("Boa tarde 12-17")
    elif hora_noturna:
        print("Boa noite 18-23")
    else:
        print("A hora informada não pertence ao range (0-24)")
except:
    print("A hora digitada não é válida")