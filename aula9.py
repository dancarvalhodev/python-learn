# Atenção aos tipos no caso se somar string com int, geraria um 
# erro diferente do PHP que poderia converter por inferência.
adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 2.2  # float
print('Divisão', divisao)

divisao_inteira = 10 // 2.2 # Ela trunca as casas decimais, mesmo a conta gerando numeros decimais
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0) # par
print(15 % 2 == 0) # impar
print(16 % 2 == 0) # par